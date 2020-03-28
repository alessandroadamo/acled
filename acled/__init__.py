import aenum

from acled.acled import acled
from acled.actor import actor
from acled.actortype import actortype
from acled.country import country
from acled.region import region


class ActorType(aenum.Enum):
    _init_ = "value string"

    STATE_FORCES = 1, "State Forces"
    REBEL_FORCES = 2, "Rebel Forces"
    MILITIA_GROUPS = 3, "Militia Groups"
    COMMUNAL___IDENTITY_GROUPS = 4, "Communal / Identity Groups"
    RIOTERS = 5, "Rioters"
    PROTESTERS = 6, "Protesters"
    CIVILIANS = 7, "Civilians"
    FOREIGN__OTHERS = 8, "Foreign / Others"

    def __str__(self):
        return self.string

    @classmethod
    def _missing_value_(cls, value):
        for member in cls:
            if member.string == value:
                return member


class Region(aenum.Enum):
    _init_ = "value string"

    WESTERN_AFRICA = 1, "Western Africa"
    MIDDLE_AFRICA = 2, "Middle Africa"
    EASTERN_AFRICA = 3, "Eastern Africa"
    SOUTHERN_AFRICA = 4, "Southern Africa"
    NORTHERN_AFRICA = 5, "Northern Africa"
    SOUTHERN_ASIA = 6, "Southern Asia"
    WESTERN_ASIA = 7, "Western Asia"
    SOUTH_EASTERN_ASIA = 8, "South - Eastern Asia"
    SOUTH_ASIA = 10, "South Asia"
    MIDDLE_EAST = 11, "Middle East"
    EUROPE = 12, "Europe"

    def __str__(self):
        return self.string

    @classmethod
    def _missing_value_(cls, value):
        for member in cls:
            if member.string == value:
                return member


