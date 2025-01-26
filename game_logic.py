def generate_empty_table(table_length):
    table_min_length = 4
    table_max_length = 8
    if table_length < table_min_length or table_length > table_max_length:
        print('Table size is not valid')
        return
    max_row_elements = (table_length-1)*2+1
    table = {}
    dynamic_column = table_length
    for i in range(max_row_elements):
        for j in range(dynamic_column):
            if i < table_length - 1 and j==dynamic_column-1:
                table[(i,j)] = {"right_flag" : False , "down_left_flag" : False , "down_right_flag" : False
                                , "right" : None , "down_left" : (i+1 , j) , "down_right" : (i+1,j+1)}

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
    return table

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
        return all_possible_moves
    if start_move[0] == end_move[0]:
        current_pillar = start_move
        for i in range(3):
            table[current_pillar]["right_flag"] = True
            current_pillar = table[current_pillar]["right"]
    else:
        current_pillar = start_move
        for i in range(3):
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
    return all_possible_moves


def minimum_triangles_for_win(table_length):
        minimum_triangles = 0
        triangle_row = (table_length - 1) * 2 + 1
        for i in range(table_length-1):
            minimum_triangles+=triangle_row
            triangle_row+=2
        return minimum_triangles

def end_game(table_length, blue_triangles, red_triangles, all_possible_moves):
    minimum_triangles = minimum_triangles_for_win(table_length)
    if blue_triangles >= minimum_triangles:
        print('Blue wins!')
        message = "Blue wins!"
    elif red_triangles >= minimum_triangles:
        print('Red wins!')
        message = "Red wins!"
    elif not all_possible_moves and blue_triangles > red_triangles:
        print('Blue wins!')
        message = "Blue wins!"
    elif not all_possible_moves and red_triangles > blue_triangles:
        print('Red wins!')
        message = "Red wins!"
    elif not all_possible_moves and red_triangles == blue_triangles:
        print('It is a tie!')
        message = "It is a tie!"
    else:
        print('Continue the game!')
        message = "Continue the game!"
    return message


def main() :
    table_length = 5
    table = generate_empty_table(table_length)
    all_possible_moves = find_all_possible_moves(table , table_length)
    all_possible_moves = play_move(table, table_length, all_possible_moves, (0, 3), (3, 3))
    all_possible_moves = play_move(table, table_length, all_possible_moves, (3, 3), (6, 0))
    for key, value in table.items():
        print(f"{key}: {value}")

    print(all_possible_moves)
    minimum_triangles = minimum_triangles_for_win(table_length)
    print(minimum_triangles)
    message = end_game(table_length , 23,48, all_possible_moves)

main()