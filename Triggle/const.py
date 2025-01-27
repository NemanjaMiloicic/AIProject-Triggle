import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('Triggle')

# Boje
white = (255, 255, 255)
blue = (0, 0, 200)
red = (255, 0, 0)
hover_blue = (0, 0, 255)
black = (0, 0, 0)

button_width = 300
button_height = 80
button_x = (screen.get_width()-350)//2
button_y = (screen.get_height()-70)//2.5

circle_radius = 17
circle_color = (255, 0, 0)  # Crvena boja
line_color = (0, 0, 255)  # Plava boja linije
line_thickness = 3  # Debljina linije