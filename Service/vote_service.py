from typing import List

from Domain.vote import Vote
from Repository.vote_repository import VoteRepository


class VoteService:

    def __init__(self, vote_repository: VoteRepository):
        """
        TODO
        :param vote_repository:
        """
        self.vote_repository = vote_repository

    def add_vote(self, id_vote, location_black, location_white):
        """
        TODO
        :param id_vote:
        :param location_black:
        :param location_white:
        :return:
        """
        vote = Vote(id_vote, location_black, location_white)
        # TODO: validate the vote
        self.vote_repository.create(vote)

    def get_all(self) -> List[Vote]:
        """
        TODO
        :return:
        """
        return self.vote_repository.read()
