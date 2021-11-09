from typing import List, Tuple

from Domain.vote import Vote
from Domain.vote_validator import VoteValidator
from Repository.vote_repository_json import VoteRepositoryJson


class VoteService:

    def __init__(self, vote_repository: VoteRepositoryJson, vote_validator: VoteValidator):
        """
        TODO
        :param vote_repository:
        """
        self.vote_repository = vote_repository
        self.vote_validator = vote_validator

    def add_vote(self, id_vote, location_black, location_white):
        """
        TODO
        :param id_vote:
        :param location_black:
        :param location_white:
        :return:
        """
        vote = Vote(id_vote, location_black, location_white)
        self.vote_validator.validate(vote)
        self.vote_repository.create(vote)

    def get_tally(self) -> Tuple[int, ...]:
        """

        :return: tuplu (nr voturi pro, nr voturi contra, nr voturi nule)
        """
        tally = [0, 0, 0]
        for vote in self.vote_repository.read():
            vote_result = vote.get_result()
            if vote_result == 1:
                tally[0] += 1
            elif vote_result == 0:
                tally[1] += 1
            else:
                tally[2] += 1

        return tuple(tally)

    def get_all(self) -> List[Vote]:
        """
        TODO
        :return:
        """
        return self.vote_repository.read()
