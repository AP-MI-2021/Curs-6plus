from Domain.vote import Vote


class VoteValidator:

    def validate(self, vote: Vote) -> None:
        """
        TODO
        :param vote:
        :return:
        """
        errors = []
        valid_locations = ['white', 'black']
        if vote.location_black not in valid_locations:
            errors.append('Locatiile valide pentru bila neaga'
                          ' sunt white si black.')
        if vote.location_white not in valid_locations:
            errors.append('Locatiile valide pentru bila alba'
                          ' sunt white si black.')

        if errors:
            raise ValueError(errors)
