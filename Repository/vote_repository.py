from typing import Optional, Union, List

from Domain.vote import Vote


class VoteRepository:

    def __init__(self):
        self.storage = {}  # storage[x] = votul cu id-ul x

    def create(self, vote: Vote) -> None:
        """
        TODO
        :param vote:
        :return:
        """
        if self.read(vote.id_vote) is not None:
            raise KeyError(f'Exista deja un vot cu id-ul {vote.id_vote}.')

        self.storage[vote.id_vote] = vote

    def read(self, id_vote=None) -> Union[Optional[Vote], List[Vote]]:
        """
        TODO
        :param id_vote: id-ul votului
        :return:
            - votul cu id=id_vote sau None daca id_vote nu e None
            - lista cu toate voturile daca id_vote e None
        """
        if id_vote:
            if id_vote in self.storage:
                return self.storage[id_vote]
            else:
                return None

        return list(self.storage.values())

    def update(self, vote: Vote) -> None:
        """
        TODO
        :param vote:
        :return:
        """

        if self.read(vote.id_vote) is None:
            msg = f'Nu exista un vot cu id-ul {vote.id_vote} pe care sa-l actualizam.'
            raise KeyError(msg)

        self.storage[vote.id_vote] = vote

    def delete(self, id_vote: int) -> None:
        """
        TODO
        :param id_vote:
        :return:
        """
        if self.read(id_vote) is None:
            raise KeyError(
                f'Nu exista un vot cu id-ul {id_vote} pe care sa-l stergem.')

        del self.storage[id_vote]
