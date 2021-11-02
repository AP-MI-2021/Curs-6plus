from Repository.vote_repository import VoteRepository
from Service.vote_service import VoteService
from UserInterface.console import Console


def main():
    vote_repository = VoteRepository()
    vote_service = VoteService(vote_repository)
    console = Console(vote_service)

    console.run_console()


if __name__ == '__main__':
    main()
