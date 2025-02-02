import pygame
import const


def draw_button(surface, color, rect, text, font, text_color):
    pygame.draw.rect(surface, color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    surface.blit(text_surface, text_rect)


def draw_title(screen, color, text="TRIGGLE"):
    font_size = 100

    title_font = pygame.font.Font(None, font_size)

    title_text = text
    title_surface = title_font.render(title_text, True, color)
    title_rect = title_surface.get_rect(center=((screen.get_width() - 50) // 2, screen.get_height() // 6))

    screen.blit(title_surface, title_rect)

def drawPlayerText(screen, player1_score, player2_score, player):
    font_size = 70
    font = pygame.font.Font(None, font_size)


    player1_color = (0, 255, 0) if player else (0, 0, 0)
    player2_color = (0, 255, 0) if not player else (0, 0, 0)


    text_surface1 = font.render(f"Player 1: {player1_score}", True, player1_color)
    text_rect1 = text_surface1.get_rect(topleft=(20, 20))
    pygame.draw.rect(screen, (255, 255, 255), text_rect1)
    screen.blit(text_surface1, text_rect1)


    text_surface2 = font.render(f"Player 2: {player2_score}", True, player2_color)
    text_rect2 = text_surface2.get_rect(bottomright=(screen.get_width() - 20, screen.get_height() - 20))
    pygame.draw.rect(screen, (255, 255, 255), text_rect2)
    screen.blit(text_surface2, text_rect2)

def drawPlayerComputerText(screen, player1_score, player2_score, player):
    font_size = 70
    font = pygame.font.Font(None, font_size)


    player1_color = (0, 255, 0) if player else (0, 0, 0)
    player2_color = (0, 255, 0) if not player else (0, 0, 0)


    text_surface1 = font.render(f"Player: {player1_score}", True, player1_color)
    text_rect1 = text_surface1.get_rect(topleft=(20, 20))
    pygame.draw.rect(screen, (255, 255, 255), text_rect1)
    screen.blit(text_surface1, text_rect1)


    text_surface2 = font.render(f"Computer: {player2_score}", True, player2_color)
    text_rect2 = text_surface2.get_rect(bottomright=(screen.get_width() - 20, screen.get_height() - 20))
    pygame.draw.rect(screen, (255, 255, 255), text_rect2)
    screen.blit(text_surface2, text_rect2)







def draw_circle_pattern(screen, circle_radius, circle_color, rows):
    horizontal_spacing = circle_radius * 4
    vertical_spacing = circle_radius * 3
    circles = []

    for i, num_circles in enumerate(rows):
        x_offset = (screen.get_width() - num_circles * horizontal_spacing) // 2
        for j in range(num_circles):
            circle_center = (int(x_offset + j * horizontal_spacing), int(i * vertical_spacing + circle_radius))
            pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

            circle_coordinates = (i, j)
            circles.append((circle_center, circle_coordinates))  # (pozicija,  koordinata tuple)




    return circles


def handle_mouse_click(circles, mouse_pos, selected_points):

    for circle_center, label in circles:
        cx, cy = circle_center
        if (mouse_pos[0] - cx) ** 2 + (mouse_pos[1] - cy) ** 2 <= const.circle_radius ** 2:
            # Ako je tačka kliknuta, dodaj je u listu selektovanih
            if len(selected_points) < 2:
                selected_points.append((circle_center, label))
            elif len(selected_points) == 2:
                # Ako su već selektovane dve tačke, resetuj selekciju
                selected_points = [(circle_center, label)]
            break
    return selected_points


def draw_lines(screen, lines, line_color, line_thickness):

    for line in lines:
        pygame.draw.line(screen, line_color, line[0], line[1], line_thickness)




def draw_triangles_from_difference(screen, difference, circles, player):
    for triangle_set in difference:

        triangle_points = []
        for item in triangle_set:
            # Tražimo fizičku lokaciju tačke u 'circles' na osnovu indeksa
            for circle_center, label in circles:
                if label == item:
                    triangle_points.append(circle_center)  # Dodajemo fizičku lokaciju tačke
                    break


        if len(triangle_points) == 3:
            smaller_triangle_points = get_smaller_triangle(triangle_points)
            draw_triangle(screen, smaller_triangle_points, player)



def get_smaller_triangle(points):
    # Uzmi sredinu između tačaka da bi se smanjio trougao
    midpoints = []
    for i in range(3):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 3]
        # Sredina između svake dve tačke
        midpoints.append(((x1 + x2) / 2, (y1 + y2) / 2))


    x1, y1 = midpoints[0]
    x2, y2 = midpoints[1]
    x3, y3 = midpoints[2]


    return [(x1, y1), (x2, y2), (x3, y3)]



def draw_triangle(screen, points, player):

    if player:
        pygame.draw.polygon(screen, (255, 0, 0), points)
    else:
        pygame.draw.polygon(screen, (0, 0, 255), points)

def draw_winning_message(message):
    font = pygame.font.Font(None, 48)
    text_surface = font.render(message, True, (255, 0, 0))
    text_rect = text_surface.get_rect(
        topleft=(10, const.screen.get_height() - text_surface.get_height()-20))
    const.screen.blit(text_surface, text_rect)

