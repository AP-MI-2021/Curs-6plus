from Service.vote_service import VoteService


class Console:

    def __init__(self, vote_service: VoteService):
        """
        TODO
        :param vote_service:
        """
        self.vote_service = vote_service

    def run_console(self):

        while True:
            self.show_menu()
            option = input('Optiunea aleasa:')

            if option == '1':
                self.handle_add_vote()
            elif option == '2':
                self.handle_count_votes()
            elif option == '3':
                pass
            elif option == 'a':
                self.handle_show_votes()
            elif option == 'x':
                break
            else:
                print('Optiune invalida, reincercati.')

    def show_menu(self):
        print('1. Adauga vot')
        print('2. Numara voturi')
        print('3. Resetare voturi')
        print('a. Afisare voturi')
        print('x. Exit')

    def handle_add_vote(self):
        try:
            id_vote = input('Dati id-ul votului: ')
            location_black = input('Dati locatia bilei negre (white / black): ')
            location_white = input('Dati locatia bilei albe (white / black): ')

            self.vote_service.add_vote(id_vote, location_black, location_white)
        except KeyError as ke:
            print('Eroare de id:', ke)
        except ValueError as ve:
            print('Probleme cu valorile introduse:', ve)
        except Exception as ex:
            print('Eroare:', ex)


    def handle_show_votes(self):
        print('Avem urmatoarele voturi:')
        for vote in self.vote_service.get_all():
            print(vote)

    def handle_count_votes(self):
        print('Rezultatul votului este:')
        result = self.vote_service.get_tally()
        print(f'Pentru: {result[0]}')
        print(f'Impotriva: {result[1]}')
        print(f'Voturi nule: {result[2]}')
