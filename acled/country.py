import pandas as pd
import numpy as np
import requests
from datetime import datetime


def country(
        terms: str = "accept",
        country: str = None,
        iso: int = None,
        iso3: str = None,
        first_event_date: int = None,
        last_event_date: datetime = None,
        event_count: int = None) -> pd.DataFrame:
    """
    Returns the countries

    :param terms: licence term, must be accepted to return query results.
    :param country: The name of the country
    :param iso: The iso number of the country
    :param iso3: The iso3 representation of the country
    :param first_event_date: The date the first event for this actor type occurred in the format: yyyy-mm-dd
    :param last_event_date: The date the last event for this actor type occurred in the format: yyyy-mm-dd
    :param event_count: The	number of events that have occurred with this actor type
    :return: The pandas dataset
    """

    url = "https://api.acleddata.com/country/read"

    data = dict()
    if terms is not None:
        data["terms"] = terms

    if country is not None:
        data["country"] = country

    if iso is not None:
        data["iso"] = iso

    if iso3 is not None:
        data["iso3"] = iso3

    if first_event_date is not None:
        data["first_event_date"] = first_event_date

    if last_event_date is not None:
        data["last_event_date"] = last_event_date

    if event_count is not None:
        data["event_count"] = event_count

    ret = requests.get(url, params=data, verify=True).json()

    dtypes = np.dtype([
        ('event_count', int),
        ('iso', int),
        ('iso3', str),
        ('country', str),
        ('first_event_date', datetime),
        ('last_event_date', datetime)
    ])
    columns = [
        'event_count',
        'iso',
        'iso3',
        'country',
        'first_event_date',
        'last_event_date'
    ]
    df = pd.DataFrame(columns=columns)
    df.astype(dtype=dtypes)
    if ret["success"]:
        df = pd.DataFrame(ret["data"])

    return df

