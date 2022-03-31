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

def next_pos_true(current_posY, current_posX):
    if current_posX+1 < x_collumn and map [current_posY][current_posX+1] == 1:
        print('can go right')
        return [current_posY, current_posX+1]
    
    if current_posX-1 > 0 and map [current_posY][current_posX-1] == 1:
        print('can go left')
        return [current_posY, current_posX-1]

    if current_posY+1 < y_row and map [current_posY+1][current_posX] == 1:
        print('can go down')
        return [current_posY+1, current_posX]
    
    if current_posY-1 > 0 and map [current_posY-1][current_posX] == 1:
        print('can go up')
        return [current_posY-1, current_posX]



next_free_pos = next_pos_true(start_posY, start_posX)
print("free pos : ", next_free_pos)

while next_free_pos:
    next_free_pos = next_pos_true(next_free_pos[0], next_free_pos[1])
    print("free pos : ", next_free_pos)
