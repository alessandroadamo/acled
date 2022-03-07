import pandas as pd
import numpy as np
import requests
from datetime import datetime


def acled(
        key: str,
        email: str,
        terms: str = "accept",
        limit: int = 500,
        page: int = None,
        data_id: int = None,
        iso: int = None,
        event_id_cnty: str = None,
        event_id_no_cnty: str = None,
        event_date: datetime = None,
        year: int = None,
        time_precision: int = None,
        event_type: str = None,
        sub_event_type: str = None,
        actor1: str = None,
        assoc_actor_1: str = None,
        inter1: int = None,
        actor2: str = None,
        assoc_actor_2: str = None,
        inter2: int = None,
        interaction: int = None,
        region: int = None,
        country: str = None,
        admin1: str = None,
        admin2: str = None,
        admin3: str = None,
        location: str = None,
        latitude: float = None,
        longitude: float = None,
        geo_precision: int = None,
        source: str = None,
        source_scale: str = None,
        notes: str = None,
        fatalities: int = None,
        timestamp: datetime = None,
        iso3: str = None) -> pd.DataFrame:
    """
    Returns the main ACLED dataset.

    :param key: API key.
    :param email: email address.
    :param terms: licence term, must be accepted to return query results.
    :param limit: By default there is a limit of 500 rows of data returned. You can use the limit query name to change
    the default number. Setting limit as 0 will return all relevant data.
    :param page: Result page. Each page will return 500 rows of data.
    :param data_id: A unique id for the row of data
    :param iso: A numeric code for each individual country
    :param event_id_cnty: An individual identifier by number and country acronym
    :param event_id_no_cnty: An individual numeric identifier
    :param event_date: The date the event occurred in the format: yyyy-mm-dd
    :param year: The year the event occurred.
    :param time_precision:
    :param event_type: The type of conflict event
    :param sub_event_type: The type of conflict sub event
    :param actor1: The	named	actor	involved	in	the	event
    :param assoc_actor_1: The named actor allied with or identifying ACTOR1
    :param inter1: A numeric code indicating the type of	ACTOR1.
    :param actor2: The named actor involved in the event
    :param assoc_actor_2: The named actor allied with or identifying ACTOR2
    :param inter2: A numeric code indicating the type of ACTOR2
    :param interaction: A numeric code indicating the interaction between types of ACTOR1 and ACTOR2
    :param region: The region in which the event took place
    :param country: The name of the country the event occurred in
    :param admin1: The largest sub-national administrative region in which the event took place
    :param admin2: The second largest sub-national administrative region in which the event took place
    :param admin3: The second largest sub-national administrative region in which the event took place
    :param location: The location in which the event took place
    :param latitude: The latitude of the location
    :param longitude: The longitude of the location
    :param geo_precision: A	numeric	code indicating the level of certainty of the location coded for the event
    :param source: The source of the event report
    :param source_scale: The scale of the source
    :param notes: A short description of the event
    :param fatalities: The number of reported fatalities which occurred during the event
    :param timestamp: The unix timestamp this data entry was last updated
    :param iso3: A 3 character code representation of each country
    :return: The pandas dataset
    """

    url = "https://api.acleddata.com/acled/read"

    data = dict()
    data["key"] = key
    data["email"] = email

    data["export_type"] = "json"

    if terms is not None:
        data["terms"] = terms

    if limit is not None:
        data["limit"] = limit

    if page is not None:
        data["page"] = page

    if data_id is not None:
        data["data_id"] = data_id

    if iso is not None:
        data["iso"] = iso

    if event_id_cnty is not None:
        data["event_id_cnty"] = event_id_cnty

    if event_id_no_cnty is not None:
        data["event_id_no_cnty"] = event_id_no_cnty

    if event_date is not None:
        data["event_date"] = event_date

    if year is not None:
        data["year"] = year

    if time_precision is not None:
        data["time_precision"] = time_precision

    if event_type is not None:
        data["event_type"] = event_type

    if sub_event_type is not None:
        data["sub_event_type"] = sub_event_type

    if actor1 is not None:
        data["actor1"] = actor1

    if assoc_actor_1 is not None:
        data["assoc_actor_1"] = assoc_actor_1

    if inter1 is not None:
        data["inter1"] = inter1

    if actor2 is not None:
        data["actor2"] = actor2

    if assoc_actor_2 is not None:
        data["assoc_actor_2"] = assoc_actor_2

    if inter2 is not None:
        data["inter2"] = inter2

    if interaction is not None:
        data["interaction"] = interaction

    if region is not None:
        data["region"] = region

    if country is not None:
        data["country"] = country

    if admin1 is not None:
        data["admin1"] = admin1

    if admin2 is not None:
        data["admin2"] = admin2

    if admin3 is not None:
        data["admin3"] = admin3

    if location is not None:
        data["location"] = location

    if latitude is not None:
        data["latitude"] = latitude

    if longitude is not None:
        data["longitude"] = longitude

    if geo_precision is not None:
        data["geo_precision"] = geo_precision

    if source is not None:
        data["source"] = source

    if source_scale is not None:
        data["source_scale"] = source_scale

    if notes is not None:
        data["notes"] = notes

    if fatalities is not None:
        data["fatalities"] = fatalities

    if timestamp is not None:
        data["timestamp"] = timestamp

    if iso3 is not None:
        data["iso3"] = iso3

    ret = requests.get(url, params=data, verify=True).json()
    if ~ret["success"]:
        raise Exception("\n    status: " + str(ret["error"]["status"]) +
                        "\n    error: " + str(ret["error"]["message"]))

    dtypes = np.dtype([
        ("data_id", int),
        ("iso", int),
        ("event_id_cnty", str),
        ("event_id_no_cnty", str),
        ("event_date", datetime),
        ("year", int),
        ("time_precision", int),
        ("event_type", str),
        ("sub_event_type", str),
        ("actor1", str),
        ("assoc_actor_1", str),
        ("inter1", int),
        ("actor2", str),
        ("assoc_actor_2", str),
        ("inter2", int),
        ("interaction", int),
        ("region", str),
        ("country", str),
        ("admin1", str),
        ("admin2", str),
        ("admin3", str),
        ("location", str),
        ("latitude", float),
        ("longitude", float),
        ("geo_precision", int),
        ("source", str),
        ("source_scale", str),
        ("notes", str),
        ("fatalities", int),
        ("timestamp", int),
        ("iso3", str)
    ])
    columns = [
        "data_id",
        "iso",
        "event_id_cnty",
        "event_id_no_cnty",
        "event_date",
        "year",
        "time_precision",
        "event_type",
        "sub_event_type",
        "actor1",
        "assoc_actor_1",
        "inter1",
        "actor2",
        "assoc_actor_2",
        "inter2",
        "interaction",
        "region",
        "country",
        "admin1",
        "admin2",
        "admin3",
        "location",
        "latitude",
        "longitude",
        "geo_precision",
        "source",
        "source_scale",
        "notes",
        "fatalities",
        "timestamp",
        "iso3"
    ]
    df = pd.DataFrame(columns=columns)
    df.astype(dtype=dtypes)

    df = pd.DataFrame(ret["data"])

    return df

