# the "app/rps.py" file (v2) ...

from random import choice


VALID_OPTIONS = ["rock", "paper", "scissors"]

USER_WINS_MESSAGE = "USER WINS"
COMPUTER_WINS_MESSAGE = "COMPUTER WINS"
TIE_GAME_MESSAGE = "TIE GAME"


def generate_computer_choice():
    return choice(VALID_OPTIONS)


def determine_outcome(u, c):
    """
    Determines the outcome of a Rock-Paper-Scissors game between a user and the computer.

    Args:
        u (str): The user's choice. Must be one of 'rock', 'paper', or 'scissors'.
        c (str): The computer's choice. Must be one of 'rock', 'paper', or 'scissors'.

    Returns:
        str: The outcome of the game. Returns one of the following:
             - "USER WINS" if the user wins.
             - "COMPUTER WINS" if the computer wins.
             - "TIE GAME" if both selections are the same.

    Raises:
        KeyError: If either `u` or `c` is not one of 'rock', 'paper', or 'scissors'.
    """
    winners = {
        "rock":{
            "rock": TIE_GAME_MESSAGE,
            "paper": COMPUTER_WINS_MESSAGE,
            "scissors": USER_WINS_MESSAGE,
        },
        "paper":{
            "rock": USER_WINS_MESSAGE,
            "paper": TIE_GAME_MESSAGE,
            "scissors": COMPUTER_WINS_MESSAGE,
        },
        "scissors":{
            "rock": COMPUTER_WINS_MESSAGE,
            "paper": USER_WINS_MESSAGE,
            "scissors": TIE_GAME_MESSAGE,
        },
    }
    outcome = winners[u][c]
    return outcome



if __name__ == "__main__": 
    # NEED NAME CONDITIONAL IF IMPORTING FROM ONE FILE TO ANOTHER PYTHON FILE
    # WHEN YOU RUN THIS CODE FROM THE COMMAND LINE IT WILL BE EXECUTED, BUT IT WILL NOT BE EXECUTED WHEN YOU IMPORT FROM THIS FILE
    # ANY USER INPUTS SHOULD BE WITHIN THE NAME CONDITIONAL
    # THERE CAN ONLY BE ONE NAME CONDITIONAL PER FILE, IT GOES AT THE BOTTOM

    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = generate_computer_choice()
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    outcome = determine_outcome(u, c)
    print(outcome)