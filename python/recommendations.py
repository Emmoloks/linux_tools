###A recomendation based on user input
def main():
    difficulty = input("Lets play a game Difficult or Easy: ")
    players = input("Multiplayer or Single-player: ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
            print("Enter a valid player")

    elif difficulty == "Easy":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single=player":
                recommend("Clock")
        else:
            print("Enter a valid player")

    else:
        print("Enter a valid choice")


def recommend(game):
   return print(f"You would like {game}")


main()
