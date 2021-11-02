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

    def get_result(self):
        """
        TODO
        :return: 1 if this is a for vote and
                 0 if it is an against vote and
                 None if it is a null vote
        """
        if self.location_white == 'white' and \
                self.location_black == 'black':
            return 1
        elif self.location_black == 'white' and \
                self.location_white == 'black':
            return 0
        return None
