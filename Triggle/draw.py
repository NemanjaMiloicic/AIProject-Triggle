import pygame
import const


def draw_button(surface, color, rect, text, font, text_color):
    pygame.draw.rect(surface, color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    surface.blit(text_surface, text_rect)


def draw_title(screen, color, text="TRIGGLE"):
    font_size = 100
    # Kreiraj font objekat
    title_font = pygame.font.Font(None, font_size)

    title_text = text
    title_surface = title_font.render(title_text, True, color)
    title_rect = title_surface.get_rect(center=((screen.get_width() - 50) // 2, screen.get_height() // 6))

    screen.blit(title_surface, title_rect)


def drawPlayerText(screen, color, text, player):
    font_size = 70
    font = pygame.font.Font(None, font_size)

    if player:  # Igrac 1
        # Tekst u gornjem levom uglu
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(topleft=(20, 20))  # Gornji levi ugao
    else:  # Igrac 2
        # Tekst u donjem desnom uglu
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(
            bottomright=(screen.get_width() - 20, screen.get_height() - 60))  # Donji desni ugao

    # Prikazivanje teksta na ekranu
    screen.blit(text_surface, text_rect)


# def draw_circle_pattern(screen, circle_radius, circle_color, rows):
#     # Definisemo razmak izmedju krugova
#     horizontal_spacing = circle_radius * 4
#     vertical_spacing = circle_radius * 3

#     # Pocetni Y offset (od gornje strane ekrana)
#     y_offset = circle_radius
#     circles = []  # Cuvanje pozicija krugova

#     for i, num_circles in enumerate(rows):
#         # Početni X offset za centriranje horizontalno
#         x_offset = (screen.get_width() - num_circles * horizontal_spacing) // 2
#         row_label = 0
#         for j in range(num_circles):
#             circle_center = (int(x_offset + j * horizontal_spacing), int(y_offset + i * vertical_spacing))
#             pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
#             # Dodaj poziciju kruga i indeks
#             circle_label = f"{i}{j}"  # Kombinacija reda i kolone
#             circles.append((circle_center, circle_label))  # (pozicija, labela)
#             # Ispis labele pored kruga
#             font = pygame.font.SysFont(None, 24)
#             label_text = font.render(circle_label, True, (0, 0, 0))  # Labela u crnoj boji
#             screen.blit(label_text, (circle_center[0] + circle_radius + 5, circle_center[1] - 10))
#     return circles

def draw_circle_pattern(screen, circle_radius, circle_color, rows):
    # Definišemo razmak između krugova
    horizontal_spacing = circle_radius * 4
    vertical_spacing = circle_radius * 3
    circles = []  # Čuvanje pozicija krugova

    for i, num_circles in enumerate(rows):
        # Početni X offset za centriranje horizontalno
        x_offset = (screen.get_width() - num_circles * horizontal_spacing) // 2
        row_label = 0  # Početno slovo za označavanje redova
        for j in range(num_circles):
            circle_center = (int(x_offset + j * horizontal_spacing), int(i * vertical_spacing + circle_radius))
            pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
            # Dodaj poziciju kruga i indeks
            circle_label = f"{i}{j}"  # Kombinacija reda i kolone
            circle_coordinates = (i, j)
            circles.append((circle_center, circle_coordinates))  # (pozicija, labela , koordinata tuple)

            # Ispis labele pored kruga
            font = pygame.font.SysFont(None, 24)
            label_text = font.render(circle_label, True, (0, 0, 0))  # Labela u crnoj boji
            screen.blit(label_text, (circle_center[0] + circle_radius + 5, circle_center[1] - 10))

    return circles


def handle_mouse_click(circles, mouse_pos, selected_points):
    """Prolazimo kroz sve krugove i proveravamo da li je kliknuta tačka."""
    for circle_center, label in circles:
        cx, cy = circle_center
        if (mouse_pos[0] - cx) ** 2 + (mouse_pos[1] - cy) ** 2 <= const.circle_radius ** 2:
            # Ako je tačka kliknuta, dodaj je u listu selektovanih
            if len(selected_points) < 2:
                selected_points.append((circle_center, label))
            elif len(selected_points) == 2:
                # Ako su već selektovane dve tačke, resetuj selekciju
                selected_points = [(circle_center, label)]
            break  # Prekidamo petlju nakon što nađemo prvu selektovanu tačku
    return selected_points


def draw_lines(screen, lines, line_color, line_thickness):
    """Crtanje svih linija na ekranu."""
    for line in lines:
        pygame.draw.line(screen, line_color, line[0], line[1], line_thickness)


def ret_player(player):
    print(player)
    return player


def draw_triangle(screen, player, points=[]):
    if player:
        pygame.draw.polygon(screen, const.blue, points)
    else:
        pygame.draw.polygon(screen, const.red, points)
