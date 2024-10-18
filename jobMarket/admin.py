from django.contrib import admin
from jobMarket.models.shared import *
from jobMarket.models.all_models import *
from jobMarket.models.misc import *
from jobMarket.models.chart4model import *

# Register your models here.

class PlatformAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ID', {'fields': ['id']}),
        ('Name', {'fields': ['name']}),
        ('Created', {'fields': ['created_on']}),
        ('Edited', {'fields': ['last_edit']}),
    ]
    list_display = ('name', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ID', {'fields': ['id']}),
        ('Name', {'fields': ['name']}),
        ('Created', {'fields': ['created_on']}),
        ('Edited', {'fields': ['last_edit']}),
    ]
    list_display = ('name', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class JobPostingAdmin(admin.ModelAdmin):    
    list_display = ('title', 'company', 'platform', 'experience_level', 'is_new', 'deadline', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class LocationAdmin(admin.ModelAdmin):    
    list_display = ('job_posting', 'name', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class SkillCategoryAdmin(admin.ModelAdmin):    
    list_display = ('name', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class SkillAdmin(admin.ModelAdmin):    
    list_display = ('name', 'skill_cat', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class RequirementAdmin(admin.ModelAdmin):    
    list_display = ('job_posting', 'skill', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class JobSuperTypeAdmin(admin.ModelAdmin):    
    list_display = ('name', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class JobSubTypeAdmin(admin.ModelAdmin):    
    list_display = ('name', 'super_type', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class JobSuperSubAssociationAdmin(admin.ModelAdmin):    
    list_display = ('job_posting', 'super_type', 'sub_type', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class RawFileAdmin(admin.ModelAdmin):    
    list_display = ('filename', 'collected_on', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']

class Chart4Admin(admin.ModelAdmin):
    list_display = ('language', 'role', 'percentage', 'created_on', 'last_edit', 'id')
    readonly_fields = ['id', 'created_on', 'last_edit']


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(JobSuperType, JobSuperTypeAdmin)
admin.site.register(JobSubType, JobSubTypeAdmin)
admin.site.register(JobSuperSubAssociation, JobSuperSubAssociationAdmin)
admin.site.register(RawFile, RawFileAdmin)
admin.site.register(ChartFour, Chart4Admin)