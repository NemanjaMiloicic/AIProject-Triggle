import pygame
import const
import multiplayer
import draw
import singleplayer

def main_screen():
    running = True

    image = pygame.image.load("Pozadina.png").convert()
    scaled_image = pygame.transform.scale(image, (const.screen.get_width(), const.screen.get_height()))

    # Kreiraj font objekat
    font = pygame.font.Font(None, 36)

    while running:
        const.screen.blit(scaled_image, (0, 0))  # Ponovo pozivamo da popunimo pozadinu

        # Crtanje naslova
        draw.draw_title(const.screen, const.black, "TRIGGLE")

        # Crtanje dugmadi
        single_player_button = pygame.Rect(const.button_x, const.button_y, const.button_width, const.button_height)
        draw.draw_button(const.screen, const.blue, single_player_button, "Single-player", font, const.black)

        multiplayer_button = pygame.Rect(const.button_x, const.button_y + 150, const.button_width, const.button_height)
        draw.draw_button(const.screen, const.blue, multiplayer_button, "Multiplayer", font, const.black)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if single_player_button.collidepoint(mouse_pos):
            draw.draw_button(const.screen, const.hover_blue, single_player_button, "Single-player", font, const.black)
            if mouse_click[0]:
                singleplayer.singleplayer_screen()
        elif multiplayer_button.collidepoint(mouse_pos):
            draw.draw_button(const.screen, const.hover_blue, multiplayer_button, "Multiplayer", font, const.black)
            if mouse_click[0]:
                multiplayer.multiplayer_screen()

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
    exit()

main_screen()
