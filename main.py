from Domain.vote_validator import VoteValidator
from Repository.vote_repository_inmemory import VoteRepositoryInMemory
from Repository.vote_repository_json import VoteRepositoryJson
from Service.vote_service import VoteService
from UserInterface.console import Console


def main():
    vote_repository = VoteRepositoryJson('votes.json')
    vote_validator = VoteValidator()
    vote_service = VoteService(vote_repository, vote_validator)

    console = Console(vote_service)

    console.run_console()


if __name__ == '__main__':
    main()
