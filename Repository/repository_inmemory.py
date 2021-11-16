from typing import Optional, Union, List
from Domain.entity import Entity
from Repository.repository import Repository


class RepositoryInMemory(Repository):

    def __init__(self):
        self.storage = {}  # storage[x] = votul cu id-ul x

    def create(self, Entity: Entity) -> None:
        """
        TODO
        :param Entity:
        :return:
        """
        if self.read(Entity.id_entity) is not None:
            raise KeyError(f'Exista deja un vot cu id-ul {Entity.id_entity}.')

        self.storage[Entity.id_entity] = Entity

    def read(self, id_entity=None) -> Union[Optional[Entity], List[Entity]]:
        """
        TODO
        :param id_entity: id-ul votului
        :return:
            - votul cu id=id_entity sau None daca id_entity nu e None
            - lista cu toate voturile daca id_entity e None
        """
        if id_entity:
            if id_entity in self.storage:
                return self.storage[id_entity]
            else:
                return None

        return list(self.storage.values())

    def update(self, Entity: Entity) -> None:
        """
        TODO
        :param Entity:
        :return:
        """

        if self.read(Entity.id_entity) is None:
            msg = f'Nu exista un vot cu id-ul {Entity.id_entity} de actualizat.'
            raise KeyError(msg)

        self.storage[Entity.id_entity] = Entity

    def delete(self, id_entity: str) -> None:
        """
        TODO
        :param id_entity:
        :return:
        """
        if self.read(id_entity) is None:
            raise KeyError(
                f'Nu exista un vot cu id-ul {id_entity} pe care sa-l stergem.')

        del self.storage[id_entity]
