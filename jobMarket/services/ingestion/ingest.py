import os, json, shutil
from datetime import datetime
from django.db import transaction
from django.utils.timezone import make_aware
from django.conf import settings
from jobMarket.models.shared import *
from jobMarket.models.all_models import *
from jobMarket.models.misc import *

def ingest(fpath):
    """ Sorts and inserts raw json into tables.
    Parameters:
    filepath (file path including its extension.)
    """
    ARCHIVE_PATH = 'data/archived'
    basename = os.path.basename(fpath)
    apath = os.path.join(settings.BASE_DIR, ARCHIVE_PATH)
    collection_date_str, platform_name = basename.split('_', 2)[:2]
    collected_on = make_aware(datetime.strptime(collection_date_str, '%Y-%m-%d'))

    # load up json
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # if one fails, all will fail as well
    with transaction.atomic():
        # json file meta data archiving
        RawFile.objects.get_or_create(filename=filename, collected_on=collected_on)

        # collected platform info
        platform, _ = Platform.objects.get_or_create(name=platform_name)
        
        # for each record in the json
        for post in data:
            # create company
            company, _ = Company.objects.get_or_create(name=post['company_name'])
            
            # create super type: 일단 0번 조회 하는걸루
            super_type, _ = JobSuperType.objects.get_or_create(name=post['job_type'][0])

            ## create job posting
            # check existing post: 아마 비효율적.
            # TODO: update_or_create을 오버라이드 하는게 나을 것 같다
            job_posting = JobPosting.objects.filter(title=post['title'], company=company, is_new=True).first()
            if job_posting:
                job_posting.is_new = False
                job_posting.save()
            # and then create
            job_posting = JobPosting.objects.create(
                title=post['title'],
                company=company,
                link=post['url'],
                platform=platform,
                experience_level=post['career'],
                is_new=True,
                deadline=make_aware(datetime.strptime(post['deadline'], '%Y-%m-%d')),
                collected_on=collected_on
            )

            # create subtype
            for sub_type_name in post['sub_types']:
                sub_type, _ = JobSubType.objects.get_or_create(
                    name=sub_type_name, super_type=super_type
                )

                # create association for each subtype
                JobSuperSubAssociation.objects.get_or_create(
                    job_posting=job_posting,
                    super_type=super_type,
                    sub_type=sub_type
                )

            # handle skills entry
            for entry in post['skills']:
                split_entry = entry.split('-', 1)
                category_name, skill_name = split_entry if len(split_entry) > 1 else ['Undefined'] + split_entry
                skill_cat, _ = SkillCategory.objects.get_or_create(name=category_name)
                skill, _ = Skill.objects.get_or_create(name=skill_name, skill_cat=skill_cat)
                # create assoc for each skill
                Requirement.objects.get_or_create(job_posting=job_posting, skill=skill)

            # create location
            for loc_name in post['location']:
                Location.objects.get_or_create(name=loc_name, job_posting=job_posting)

        # move file to the archived dir
        shutil.move(fpath, apath)