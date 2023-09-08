pl = {"tl": " ", "t":" ", "tr":" ", "cl":" ", "c":" ", "cr":" ", "bl":" ", "b":" ", "br":" "}
empty_count = 0
board_full = False

def draw_board(caller):
    print("---------")
    print(f"{pl['tl']} | {pl['t']} | {pl['tr']}\n---------\n{pl['cl']} | {pl['c']} | {pl['cr']}\n---------\n{pl['bl']} | {pl['b']} | {pl['br']}")
    print("---------")

    if board_full == False:

        if caller == "X":
            start_turn("O")
        else:
            start_turn("X")

def start_turn(player):
        answer = input(f"Please name an empty direction to mark with '{player}' (tl / br / c...): ")
        try:
            if pl[answer.lower()] == " ":
                pl[answer.lower()] = player
            else:
                print("This position is not empty. Please mark an empty position.")
                start_turn(player)
        except KeyError:
            print("Not a valid position!")
            start_turn(player)
            
        check_win(player)


def check_win(caller):
    global empty_count
    if (pl['tl'] == pl['t'] == pl['tr'] != " " or
        pl['cl'] == pl['c'] == pl['cr'] != " " or
        pl['bl'] == pl['b'] == pl['br'] != " " or
        pl['tl'] == pl['cl'] == pl['bl'] != " " or
        pl['t'] == pl['c'] == pl['b'] != " " or
        pl['tr'] == pl['cr'] == pl['br'] != " " or
        pl['tl'] == pl['c'] == pl['br'] != " " or
        pl['tr'] == pl['c'] == pl['bl']!= " "): 
        print(f"PLAYER {caller} WINS!")
        play_again()

    else:
        check_tie(caller)
    
def check_tie(caller):
    global board_full, empty_count
    for key, value in pl.items():
        if value == " ":
            empty_count += 1

    if empty_count == 0:
        board_full = True
        draw_board(caller)
        print("IT'S A TIE!")
        play_again()

    else:
        empty_count = 0
        draw_board(caller)

def play_again():
    global pl, board_full, empty_count
    answer = input("Play again? (y/n): ")
    if answer.lower() == "y":
        board_full = False
        empty_count = 0
        pl = {"tl": " ", "t":" ", "tr":" ", "cl":" ", "c":" ", "cr":" ", "bl":" ", "b":" ", "br":" "}
        draw_board("O")


draw_board(caller="O")