import pygame
import draw
import const
import singleplayergame

number = 4


def singleplayer_screen():
    running = True
    novo_dugme = False
    button_clicked = False
    novo_dugme2 = False
    button_clicked2 = False
    clicked_up = False
    clicked_down = False
    global number  # Velicina table
    selected = False
    player = False  # Ako je false, igra komp, ako je true, igra igrac prvi

    image = pygame.image.load("Tes.png").convert()
    scaled_image = pygame.transform.scale(image, (const.screen.get_width(), const.screen.get_height()))

    while running:

        const.screen.blit(scaled_image, (0, 0))

        font = pygame.font.Font(None, 36)

        draw.draw_title(const.screen, const.black, "SINGLEPLAYER")

        back_button = pygame.Rect(const.button_x, const.button_y + 300, const.button_width, const.button_height)
        draw.draw_button(const.screen, const.blue, back_button, "Back to Main Menu", font, const.black)

        who_plays_first_button = pygame.Rect(const.button_x - 230, const.button_y + 40, const.button_width,
                                             const.button_height)
        draw.draw_button(const.screen, const.blue, who_plays_first_button, "Who plays first", font, const.black)

        pick_the_board_button = pygame.Rect(const.button_x + 230, const.button_y + 40, const.button_width,
                                            const.button_height)
        draw.draw_button(const.screen, const.blue, pick_the_board_button, "Pick the Board", font, const.black)

        start_game_button = pygame.Rect(const.button_x, const.button_y - 80, const.button_width, const.button_height)
        draw.draw_button(const.screen, const.blue, start_game_button, "Start Game", font, const.black)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if who_plays_first_button.collidepoint(mouse_pos):
            draw.draw_button(const.screen, const.hover_blue, who_plays_first_button, "Who plays first???", font,
                             const.black)
            if pygame.mouse.get_pressed()[0] and not button_clicked:
                novo_dugme = not novo_dugme
                button_clicked = True

        elif back_button.collidepoint(mouse_pos):
            draw.draw_button(const.screen, const.hover_blue, back_button, "Back to Main Menu", font, const.black)
            if pygame.mouse.get_pressed()[0]:
                return

        elif pick_the_board_button.collidepoint(mouse_pos):
            draw.draw_button(const.screen, const.hover_blue, pick_the_board_button, "Pick the Board???", font,
                             const.black)
            if pygame.mouse.get_pressed()[0] and not button_clicked2:
                novo_dugme2 = not novo_dugme2
                button_clicked2 = True

        elif start_game_button.collidepoint(mouse_pos):
            draw.draw_button(const.screen, const.hover_blue, start_game_button, "Start Game", font, const.black)
            if mouse_click[0]:
                singleplayergame.game(player)

        if novo_dugme:
            player_1_button = pygame.Rect(const.button_x - 230, const.button_y + 125, const.button_width,
                                          const.button_height)
            draw.draw_button(const.screen, const.blue, player_1_button, "Player", font, const.black)
            if player_1_button.collidepoint(mouse_pos):
                draw.draw_button(const.screen, const.hover_blue, player_1_button, "Player", font, const.black)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not player:
                        player = True
                        print(player)

            player_2_button = pygame.Rect(const.button_x - 230, const.button_y + 210, const.button_width,
                                          const.button_height)
            draw.draw_button(const.screen, const.blue, player_2_button, "Computer", font, const.black)
            if player_2_button.collidepoint(mouse_pos):
                draw.draw_button(const.screen, const.hover_blue, player_2_button, "Computer", font, const.black)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player:
                        player = False
                        draw.ret_player(player)

        if novo_dugme2:
            board_increment_button = pygame.Rect(const.button_x + 480, const.button_y + 125, const.button_width - 250,
                                                 const.button_height)
            draw.draw_button(const.screen, const.blue, board_increment_button, "+", font, const.black)
            if board_increment_button.collidepoint(mouse_pos):
                draw.draw_button(const.screen, const.hover_blue, board_increment_button, "+", font, const.black)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if number < 8 and not clicked_up:
                            number += 1
                            clicked_up = True

            board_decrement_button = pygame.Rect(const.button_x + 230, const.button_y + 125, const.button_width - 250,
                                                 const.button_height)
            draw.draw_button(const.screen, const.blue, board_decrement_button, "-", font, const.black)
            if board_decrement_button.collidepoint(mouse_pos):
                draw.draw_button(const.screen, const.hover_blue, board_decrement_button, "-", font, const.black)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if number > 4 and not clicked_down:
                            number -= 1
                            clicked_down = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked_up = False
                    clicked_down = False
                    selected = False

            board_dimension_button = pygame.Rect(const.button_x + 290, const.button_y + 125, const.button_width - 120,
                                                 const.button_height)
            draw.draw_button(const.screen, const.blue, board_dimension_button, str(number), font, const.black)
            if board_dimension_button.collidepoint(mouse_pos):
                draw.draw_button(const.screen, const.hover_blue, board_dimension_button, str(number), font, const.black)

            select_button = pygame.Rect(const.button_x + 230, const.button_y + 210, const.button_width,
                                        const.button_height)
            draw.draw_button(const.screen, const.blue, select_button, "Select", font, const.black)
            if select_button.collidepoint(mouse_pos):
                draw.draw_button(const.screen, const.hover_blue, select_button, "Select???", font, const.black)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not selected:
                            print(number)
                            selected = True

        if not pygame.mouse.get_pressed()[0]:
            button_clicked = False
            button_clicked2 = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
        pygame.display.flip()
