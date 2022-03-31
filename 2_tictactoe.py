game = [
    ".", ".", ".",
    ".", ".", ".",
    ".", ".", "."
]

def game_print():
    print(game[0] + game[1] + game[2])
    print(game[3] + game[4] + game[5])
    print(game[6] + game[7] + game[8])
    print()


# next_position = int(input("next pos: "))

# line 14 and 17 are same. Please make "1" and "2" to int (using int() function and -1)


while True:
    
    next_position = int(input("X next pos: "))

    if next_position <= 9 and next_position >= 0:
        game[next_position-1] = "X"
    
    game_print()
    
    if game[0] != "." and game[1] != "." and game[2] != "." and game[3] != "." and game[4] != "." and game[5] != "." and game[6] != "." and game[7] != "." and game[8] != ".":
        print("game ended")
        break
    
    
    next_position = int(input("O next pos: "))
    
    if next_position <= 9 and next_position >= 0:
        game[next_position-1] = "O"
    
    game_print()
    
    if game[0] != "." and game[1] != "." and game[2] != "." and game[3] != "." and game[4] != "." and game[5] != "." and game[6] != "." and game[7] != "." and game[8] != ".":
        print("game ended")
        break
    
    


# this is same as on line 7. make this a function