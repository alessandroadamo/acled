import pandas as pd
import numpy as np
import requests
from datetime import datetime


def region(
        key: str,
        email: str,
        terms: str = "accept",
        region: int = None,
        region_name: str = None,
        first_event_date: datetime = None,
        last_event_date: datetime = None,
        event_count: int = None) -> pd.DataFrame:
    """
    Return the regions

    :param key: API key.
    :param email: email address.
    :param terms: licence term, must be accepted to return query results.
    :param region: The id of the region
    :param region_name: The name of the region
    :param first_event_date: The date the first event for this actor type occurred in the format: yyyy-mm-dd
    :param last_event_date: The date the last event for this actor type occurred in the format: yyyy-mm-dd
    :param event_count: The	number of events that have occurred with this actor type
    :return: The pandas dataset
    """

    url = "https://api.acleddata.com/region/read"

    data = dict()
    data["key"] = key
    data["email"] = email

    if terms is not None:
        data["terms"] = terms

    if region is not None:
        data["region"] = region

    if region_name is not None:
        data["region_name"] = region_name

    if first_event_date is not None:
        data["first_event_date"] = first_event_date

    if last_event_date is not None:
        data["last_event_date"] = last_event_date

    if event_count is not None:
        data["event_count"] = event_count

    ret = requests.get(url, params=data, verify=True).json()
    if ~ret["success"]:
        raise Exception("\n    status: " + str(ret["error"]["status"]) +
                        "\n    error: " + str(ret["error"]["message"]))

    dtypes = np.dtype([
        ('event_count', int),
        ('region', int),
        ('region_name', str),
        ('first_event_date', datetime),
        ('last_event_date', datetime)
    ])
    columns = [
        'event_count',
        'region',
        'region_name',
        'first_event_date',
        'last_event_date'
    ]
    df = pd.DataFrame(columns=columns)
    df.astype(dtype=dtypes)

    df = pd.DataFrame(ret["data"])

    return df
