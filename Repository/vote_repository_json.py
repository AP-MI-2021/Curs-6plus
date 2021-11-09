
import jsonpickle
from typing import Dict, Union, Optional, List

from Domain.vote import Vote
from Repository.vote_repository_inmemory import VoteRepositoryInMemory


class VoteRepositoryJson(VoteRepositoryInMemory):

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __read_file(self):
        try:
            with open(self.filename, 'r') as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __write_file(self, objects: Dict[str, Vote]):
        with open(self.filename, 'w') as f:
            f.write(jsonpickle.dumps(objects))

    def create(self, vote: Vote) -> None:
        """
        TODO
        :param vote:
        :return:
        """

        self.storage = self.__read_file()
        super().create(vote)
        self.__write_file(self.storage)

        # votes = self.__read_file()
        # if self.read(vote.id_vote) is not None:
        #     raise KeyError(f'Exista deja un vot cu id-ul {vote.id_vote}.')
        #
        # votes[vote.id_vote] = vote
        # self.__write_file(votes)

    def read(self, id_vote=None) -> Union[Optional[Vote], List[Vote]]:
        """
        TODO
        :param id_vote: id-ul votului
        :return:
            - votul cu id=id_vote sau None daca id_vote nu e None
            - lista cu toate voturile daca id_vote e None
        """

        votes = self.__read_file()
        if id_vote:
            if id_vote in votes:
                return votes[id_vote]
            else:
                return None

        return list(votes.values())

    def update(self, vote: Vote) -> None:
        """
        TODO
        :param vote:
        :return:
        """

        votes = self.__read_file()
        if self.read(vote.id_vote) is None:
            msg = f'Nu exista un vot cu id-ul {vote.id_vote} de actualizat.'
            raise KeyError(msg)

        votes[vote.id_vote] = vote
        self.__write_file(votes)

    def delete(self, id_vote: int) -> None:
        """
        TODO
        :param id_vote:
        :return:
        """
        votes = self.__read_file()
        if self.read(id_vote) is None:
            raise KeyError(
                f'Nu exista un vot cu id-ul {id_vote} pe care sa-l stergem.')

        del votes[id_vote]
        self.__write_file(votes)
