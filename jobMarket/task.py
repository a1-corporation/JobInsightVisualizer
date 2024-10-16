from jobMarket.services.processing import (
    posting_by_job_location,
    posting_by_job_type,
)
from jobMarket.services.common import pipeline

posting_by_job_location_pipeline = [
    posting_by_job_location.extract_from_primary(),
    posting_by_job_location.transform_for_secondary(),
    posting_by_job_location.load_to_secondary(),
]

posting_by_job_type_pipeline = [
    posting_by_job_type.extract_from_primary(),
    posting_by_job_type.transform_for_secondary(),
    posting_by_job_type.load_to_secondary(),
]

pipeline.run(posting_by_job_location_pipeline)
pipeline.run(posting_by_job_type_pipeline)
