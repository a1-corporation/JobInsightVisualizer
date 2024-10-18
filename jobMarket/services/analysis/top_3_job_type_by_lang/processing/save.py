from jobMarket.models.shared import *
from jobMarket.models.chart4model import *
from .process import *

def save_aggregation(n_types=3):
    """Save queired data for the chart to a hard view
    Parameters:
    n_types (The number of subtypes per skill ,default=3)
    """
    data = query_from_primaries(n_types=n_types)

    # is new로 조회 해왔으니까 update 안하고 그냥 쭉 추가하면 될덧
    for item in data:
        for lang, roles in item.items():
            for role, percentage in roles.items():
                ChartFour.objects.create(
                    language=lang,
                    role=role,
                    percentage=percentage
                )