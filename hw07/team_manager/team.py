from player import Player


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.
    def __init__(self):
        self.name = "Anonymous Team"
        # self.player = Player()
        self.players = []
    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.

    def set_team_name(self, name):
        # TODO: set the team name
        self.name = name

    def add_player(self, player_name, player_number, player_position):
        player = Player(player_name, player_number, player_position)
        self.players.append(player)

    def cut_player(self, player_name):
        self.players = [player for player in self.players
                        if player.name != player_name]

    def is_position_filled(self, position):
        for player in self.players:
            if player.pos == position:
                return True
        return False

    def display(self):
        # Printing the team roster in the desired format
        print(f"The lineup for {self.name} is:")
        for player in self.players:
            print(f"{player.num:<10}{player.name:<20}{player.pos}")

    def is_player_in_team(self, name):
        return any(player.name == name for player in self.players)

    #    The lineup for Seattle Scorpions is:
    #    15       Garcia          catcher
    #    55       Wiggins         corner
    #    99       McCann          sniper
