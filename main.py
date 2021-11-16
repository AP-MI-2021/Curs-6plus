from Domain.vote import Vote
from Domain.vote_validator import VoteValidator
from Repository.repository_inmemory import RepositoryInMemory
from Repository.repository_json import RepositoryJson
from Service.vote_service import VoteService
from UserInterface.console import Console


def main():
    vote_repository = RepositoryJson('votes.json')

    vote_validator = VoteValidator()
    vote_service = VoteService(vote_repository, vote_validator)

    console = Console(vote_service)

    console.run_console()


if __name__ == '__main__':
    main()
