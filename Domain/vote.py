from dataclasses import dataclass

@dataclass
class Vote:
    """
    Creeaza un vot.
    - id_vote: id-ul votului, trebuie sa fie unic.
    - location_black: locatia bilei negre: black sau white
    - location_white: locatia bilei negre: black sau white
    """
    id_vote: str
    location_black: str
    location_white: str
