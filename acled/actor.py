import pandas as pd
import numpy as np
import requests
from datetime import datetime


def actor(
        key: str,
        email: str,
        terms: str = "accept",
        actor_name: str = None,
        first_event_date: datetime = None,
        last_event_date: datetime = None,
        event_count: int = None) -> pd.DataFrame:
    """
    Return the actors

    :param key: API key.
    :param email: email address.
    :param terms: licence term, must be accepted to return query results.
    :param actor_name: The name of the actor
    :param first_event_date: The date the first event for this actor occurred in the format: yyyy-mm-dd
    :param last_event_date: The date the last event for this actor occurred in the format: yyyy-mm-dd
    :param event_count: The	number of events that have occurred with this actor
    :return: The pandas dataset
    """

    url = "https://api.acleddata.com/actor/read"

    data = dict()
    data["key"] = key
    data["email"] = email

    if terms is not None:
        data["terms"] = terms

    if actor_name is not None:
        data["actor_name"] = actor_name

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
        ('actor_name', str),
        ('first_event_date', datetime),
        ('last_event_date', datetime)
    ])
    columns = [
        'event_count',
        'actor_name',
        'first_event_date',
        'last_event_date'
    ]
    df = pd.DataFrame(columns=columns)
    df.astype(dtype=dtypes)

    df = pd.DataFrame(ret["data"])

    return df

