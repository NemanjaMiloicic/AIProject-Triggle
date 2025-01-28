
def generate_empty_table(table_length):
    table_min_length = 4
    table_max_length = 8
    if table_length < table_min_length or table_length > table_max_length:
        table_length = 4
    max_row_elements = (table_length-1)*2+1
    table = {}
    dynamic_column = table_length
    for i in range(max_row_elements):
        for j in range(dynamic_column):
            if i < table_length - 1 and j==dynamic_column-1:
                table[(i,j)] = {"right_flag" : False , "down_left_flag" : False , "down_right_flag" : False
                                , "right" : None , "down_left" : (i+1 , j) , "down_right" : (i+1,j+1) }

            elif i < table_length -1 and j!=dynamic_column-1:
                table[(i, j)] = {"right_flag": False, "down_left_flag": False, "down_right_flag": False
                    , "right": (i, j + 1), "down_left": (i + 1, j), "down_right": (i + 1, j + 1)}

            elif i== max_row_elements-1 and j!= dynamic_column -1:
                table[(i, j)] = {"right_flag": False, "down_left_flag": False, "down_right_flag": False
                    , "right": (i, j + 1), "down_left": None, "down_right": None}

            elif i==max_row_elements-1 and j == dynamic_column -1:
                table[(i, j)] = {"right_flag": False, "down_left_flag": False, "down_right_flag": False
                    , "right": None, "down_left": None, "down_right": None}


            elif i >= table_length-1 and j==0:
                table[(i, j)] = {"right_flag": False, "down_left_flag": False, "down_right_flag": False
                    , "right": (i, j + 1), "down_left": None, "down_right": (i + 1, j)}

            elif i>= table_length-1 and j!=0 and j!= dynamic_column-1:
                table[(i, j)] = {"right_flag": False, "down_left_flag": False, "down_right_flag": False
                    , "right": (i, j + 1), "down_left": (i+1 , j-1), "down_right": (i + 1, j)}

            else:
                table[(i, j)] = {"right_flag": False, "down_left_flag": False, "down_right_flag": False
                    , "right": None, "down_left": (i + 1, j - 1), "down_right": None}

        if i >= table_length - 1:
            dynamic_column -= 1
        else:
            dynamic_column += 1
    return table, table_length

def find_all_possible_moves(table , table_length ):
    all_possible_moves = []
    table_min_length = 4
    table_max_length = 8

    if table_length < table_min_length or table_length > table_max_length:
        print('Table size is not valid')
        return

    max_row_elements = (table_length - 1) * 2 + 1
    dynamic_column = table_length
    for i in range(max_row_elements):
        for j in range(dynamic_column):
            already_connected_right = 0
            already_connected_down_left = 0
            already_connected_down_right = 0
            current_pillar_right = current_pillar_down_left = current_pillar_down_right = (i,j)
            invalid_right = invalid_down_left = invalid_down_right =  False

            for k in range(3):
                if table[current_pillar_right]["right_flag"]:
                    already_connected_right += 1
                current_pillar_right = table[current_pillar_right]["right"]
                if current_pillar_right is None:
                    invalid_right = True
                    break
            if not invalid_right and already_connected_right != 3:
                all_possible_moves.append([(i,j) , current_pillar_right])

            for k in range(3):
                if table[current_pillar_down_left]["down_left_flag"]:
                    already_connected_down_left += 1
                current_pillar_down_left = table[current_pillar_down_left]["down_left"]
                if current_pillar_down_left is None:
                    invalid_down_left = True
                    break
            if not invalid_down_left and already_connected_down_left != 3:
                all_possible_moves.append([(i,j) , current_pillar_down_left])

            for k in range(3):
                if table[current_pillar_down_right]["down_right_flag"]:
                    already_connected_down_right += 1
                current_pillar_down_right = table[current_pillar_down_right]["down_right"]
                if current_pillar_down_right is None:
                    invalid_down_right = True
                    break
            if not invalid_down_right and already_connected_down_right!= 3:
                all_possible_moves.append([(i,j) , current_pillar_down_right])

        if i >= table_length - 1:
            dynamic_column -= 1
        else:
            dynamic_column += 1
    return all_possible_moves

def play_move(table , table_length,  all_possible_moves , start_move , end_move):
    move = [start_move , end_move]
    if move not in all_possible_moves:
        print('Invalid move')
        return all_possible_moves , False
    if start_move[0] == end_move[0]:
        current_pillar = start_move
        for i in range(3):
            table[current_pillar]["right_flag"] = True
            current_pillar = table[current_pillar]["right"]
    else:
        current_pillar = start_move
        for i in range(3):
            if table[current_pillar]["down_left"] is None:
                break
            current_pillar = table[current_pillar]["down_left"]

        if current_pillar == end_move:
            current_pillar = start_move
            for i in range(3):
                table[current_pillar]["down_left_flag"] = True
                current_pillar = table[current_pillar]["down_left"]
        else:
            current_pillar = start_move
            for i in range(3):
                table[current_pillar]["down_right_flag"] = True
                current_pillar = table[current_pillar]["down_right"]

    all_possible_moves = []
    all_possible_moves = find_all_possible_moves(table, table_length)
    return all_possible_moves , True


def minimum_triangles_for_win(table_length):
        minimum_triangles = 0
        triangle_row = (table_length - 1) * 2 + 1
        for i in range(table_length-1):
            minimum_triangles+=triangle_row
            triangle_row+=2
        return minimum_triangles

def end_game(blue_triangles, red_triangles, all_possible_moves , minimum_triangles):

    if blue_triangles > minimum_triangles:

        message = "Blue wins!"
    elif red_triangles > minimum_triangles:

        message = "Red wins!"
    elif not all_possible_moves and blue_triangles > red_triangles:

        message = "Blue wins!"
    elif not all_possible_moves and red_triangles > blue_triangles:

        message = "Red wins!"
    elif not all_possible_moves and red_triangles == blue_triangles:
        message = "It is a tie!"
    else:
        message = "Continue the game!"
    return message


def check_triangles(table,  formed_triangles):
    new_triangles = 0
    for key, value in table.items():
            # Kombinacija 1: current -> down_left, current -> down_right, down_left -> right
            triangle_1 = {key, value["down_left"], value["down_right"]}
            if (
                table[key]["down_right_flag"]
                and table[key]["down_left_flag"]
                and table[value["down_left"]]["right_flag"]
            ):

                if triangle_1 not in formed_triangles:
                    formed_triangles.append(triangle_1)
                    new_triangles+=1

            # Kombinacija 2: current -> down_right, current -> right, right -> down_left
            triangle_2 = {key, value["down_right"], value["right"]}
            if (
                table[key]["down_right_flag"]
                and table[key]["right_flag"]
                and table[value["right"]]["down_left_flag"]
            ):
                if triangle_2 not in formed_triangles:
                    formed_triangles.append(triangle_2)
                    new_triangles += 1

    return formed_triangles, new_triangles

def columns(table_length):
    table_min_length = 4
    table_max_length = 8
    if table_length < table_min_length or table_length > table_max_length:
        return []
    max_row_elements = (table_length-1)*2+1
    start_row = table_length
    row = start_row
    columns_list = []
    reached_max = False
    reached_end = False
    while not reached_end:
        columns_list.append(row)
        if row < max_row_elements and reached_max == False:
            row+=1
        elif row == max_row_elements and reached_max == False:
            row-=1
            reached_max = True
        elif row < max_row_elements and row != start_row and reached_max == True:
            row-=1
        else:
            reached_end = True
    return columns_list



def main() :
    table_length = 4
    table , table_length = generate_empty_table(table_length)
    formed_triangles = []
    all_possible_moves = find_all_possible_moves(table, table_length)
    for i in range(len(all_possible_moves)):
        all_possible_moves = play_move(table, table_length, all_possible_moves, all_possible_moves[0][0], all_possible_moves[0][1])
        formed_triangles , new_triangles = check_triangles(table , formed_triangles)
        print(f'triangles:{formed_triangles} , number of newly formed triangles:{new_triangles}')
    print(len(formed_triangles))
    print(minimum_triangles_for_win(table_length))


