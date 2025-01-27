import pygame
import const
import draw
import main_screen
import game_logic
import multiplayer
import copy

# Postavke redova
rows = []  # Možete menjati ovu vrednost
# running = True
selected_points = []  # Lista za trenutno odabrane tačke
lines = []  # Lista za sve nacrtane linije


def game(player):
    global selected_points, lines
    const.screen = pygame.display.set_mode((1300, 800))
    running = True
    pause_button_clicked = False
    new_button = False
    paused = False
    table_length = multiplayer.number
    table, table_length = game_logic.generate_empty_table(table_length)
    rows = game_logic.columns(table_length)
    formed_triangles = []
    previously_formed_triangles = []
    all_possible_moves = game_logic.find_all_possible_moves(table, table_length)
    first_paint = True
    blue_triangles = 0
    red_triangles = 0
    while running:
        if first_paint:
            const.screen.fill((255, 255, 255))
            circles = draw.draw_circle_pattern(const.screen, const.circle_radius, const.circle_color, rows)

            first_paint = False
        draw.draw_lines(const.screen, lines, const.line_color, const.line_thickness)

        draw.drawPlayerText(const.screen,  red_triangles, blue_triangles,  player)


        if len(selected_points) == 2:

            all_possible_moves, played = game_logic.play_move(table, table_length, all_possible_moves,
                                                              selected_points[0][1], selected_points[1][1])
            if played:
                formed_triangles, new_triangles = game_logic.check_triangles(table, formed_triangles)
                lines.append((selected_points[0][0], selected_points[1][0]))  # Koristimo samo koordinate
                print(f"Linija nacrtana izmedju: {selected_points[0][1]} i {selected_points[1][1]}")  # Ispis labele

                if player :
                    red_triangles+= new_triangles
                else:
                    blue_triangles+= new_triangles
                print(f'blue:{blue_triangles}')
                print(f'red:{red_triangles}')


                if new_triangles > 0:

                    difference = [item for item in formed_triangles if item not in previously_formed_triangles]

                    previously_formed_triangles = copy.copy(formed_triangles)
                    print(difference)
                    for i in difference:
                        draw.draw_triangles_from_difference(const.screen, difference , circles , player)

                        previously_formed_triangles = copy.copy(formed_triangles)


                player = not player
                message = game_logic.end_game(table_length, blue_triangles, red_triangles, all_possible_moves)
                if message != 'Continue the game!':
                    running = False


            selected_points = []

        font = pygame.font.Font(None, 36)

        pause_button = pygame.Rect(const.button_x + 750, const.button_y - 250, const.button_width - 260,
                                   const.button_width - 260)
        draw.draw_button(const.screen, const.blue, pause_button, "||", font, const.black)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if pause_button.collidepoint(mouse_pos):
            draw.draw_button(const.screen, const.hover_blue, pause_button, "||", font, const.black)
            if mouse_click[0] and not pause_button_clicked:
                new_button = not new_button
                pause_button_clicked = True
                paused = True

        if new_button and paused:
            continue_game_button = pygame.Rect(const.button_x, const.button_y - 80, const.button_width,
                                               const.button_height)
            draw.draw_button(const.screen, const.blue, continue_game_button, "Continue", font, const.black)
            if continue_game_button.collidepoint(mouse_pos):
                draw.draw_button(const.screen, const.hover_blue, continue_game_button, "Continue???", font, const.black)
                if mouse_click[0] and not pause_button_clicked:
                    paused = False
                    pause_button_clicked = True
                    new_button = False

            quit_game_button = pygame.Rect(const.button_x, const.button_y + 80, const.button_width, const.button_height)
            draw.draw_button(const.screen, const.blue, quit_game_button, "Quit", font, const.black)
            if quit_game_button.collidepoint(mouse_pos):
                draw.draw_button(const.screen, const.hover_blue, quit_game_button, "Quit???", font, const.black)
                if mouse_click[0]:
                    running = False
                    pause_button_clicked = False
                    lines = []
                    selected_points = []
                    new_button = False
                    paused = False
                    const.screen = pygame.display.set_mode((1280, 720))
                    main_screen.main_screen()

        if not mouse_click[0]:
            pause_button_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                selected_points = draw.handle_mouse_click(circles, mouse_pos, selected_points)
        pygame.display.flip()
    pygame.quit()
    exit()
