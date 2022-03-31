import random

map = [
    [12, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [24, 0, 1, 0, 0],
    [1, 1, 1, 1, 1]
]

start_posX = 0
start_posY = 0

y_row = 5
x_collumn = 5

stop = 0

def next_pos_true(current_posY, current_posX):
    # while True:
    #     try:
    #         if map [current_posY][current_posX+1] == 24:
    #             finish = 1
            
    #         if map [current_posY][current_posX-1] == 24:
    #             finish = 1

    #         if map [current_posY+1][current_posX] == 24:
    #             finish = 1
            
    #         if map [current_posY-1][current_posX] == 24:
    #             finish = 1

    #         if finish == 1:
    #             print('u reacher the finish')
    #             break
                
    #     except:
    #         continue
    
    
    win_right = current_posX+1 < x_collumn and map [current_posY][current_posX+1] == 24
    win_left = current_posX-1 < x_collumn and map [current_posY][current_posX-1] == 24
    win_up = current_posY+1 < y_row and map [current_posY+1][current_posX] == 24
    win_down = current_posY-1 < y_row and map [current_posY-1][current_posX] == 24
    
    if win_right:
        print('u found the finish')
        stop += 1
    
    if win_left:
        print('u found the finish')
        stop += 1
    
    if win_up:
        print('u found the finish')
        stop += 1
    
    if win_down:
        print('u found the finish')
        stop += 1
    
    rand = random.randrange(1, 5)
    
    finish = map [current_posY][current_posX] == 24
    
    if rand == 1:
        go_right = current_posX+1 < x_collumn and map [current_posY][current_posX+1] == 1
    else:
        go_right = False
    
    if rand == 2:
        go_left = current_posX-1 > 0 and map [current_posY][current_posX-1] == 1
    else:
        go_left = False
    
    if rand == 3:
        go_down = current_posY+1 < y_row and map [current_posY+1][current_posX] == 1
    else:
        go_down = False
    
    if rand == 4:
        go_up = current_posY-1 > 0 and map [current_posY-1][current_posX] == 1
    else:
        go_up = False

    if go_right:
        print('can go right')
        return [current_posY, current_posX+1]

    if go_left:
        print('can go left')
        return [current_posY, current_posX-1]

    if go_down:
        print('can go down')
        return [current_posY+1, current_posX]

    if go_up:
        print('can go up')
        return [current_posY-1, current_posX]
    
    else:
        print('cant do anything')
        return [current_posY, current_posX]

next_free_pos = next_pos_true(start_posY, start_posX)
print("free pos : ", next_free_pos)

while next_free_pos and stop == 0:
    next_free_pos = next_pos_true(next_free_pos[0], next_free_pos[1])
    print("free pos : ", next_free_pos)

# else:
#     next_free_pos = next_pos_true(start_posY, start_posX)
