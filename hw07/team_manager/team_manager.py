from team import Team
from bench import Bench


def main():
    print("Welcome to the team manager.")
    # Here's where we create objects for the team and the bench. These
    # objects will be able to call the methods we've defined in their
    # respective classes. When the constructor functions are called here,
    # the classes' __init__() method is called with these values
    # passed to it. In both of these cases no arguments are passed, here.
    # However, the `self` argument is always implicitly passed with any
    # method call.
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(team):
    name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def do_show_team_roster(team):
    team.display()


def do_check_position_filled(team):
    position = input("What position are you checking for?\n")
    if team.is_position_filled(position):
        print(f"Yes, the {position} position is filled")
    else:
        print(f"No, the {position} position is not filled.")


def do_add_player_to_team(team):
    player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    player_position = input("What's " + player_name + "'s position?\n")
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_send_player_to_bench(team, bench):
    name = input("Who do you want to send to the bench?\n")
    if team.is_player_in_team(name):
        bench.send_to_bench(name)
        print(f"Sent {name} to bench.")
    else:
        print(f"{name} isn't on the team.")


def do_get_player_from_bench(bench):
    if bench.is_bench_empty():
        print("The bench is empty.")
    else:
        print(f"Got {bench.get_from_bench()} from bench")
    # TODO: get the best-rested player by name from the bench
    # (i.e. the player who has been on the bench longest). Print to
    # the screen the name of the player who was retrieved from the
    # bench. If the bench is empty, print to the screen that the
    # bench is empty.


def do_cut_player(team, bench):
    player_name = input("Who do you want to cut?\n")
    if ((team.is_player_in_team) and bench.is_on_bench(player_name)):
        team.cut_player(player_name)
        print(f"{player_name} has been cut from the team.")
    else:
        print(f"{player_name} is not on the team or couldn't be cut.")


def do_show_bench(bench):
    bench.display()


def do_not_understand():
    print("I didn't understand that command")


main()
