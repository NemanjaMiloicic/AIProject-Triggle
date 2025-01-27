import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('Triggle')


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
circle_color = (255, 0, 0)
line_color = (0, 255, 40)
line_thickness = 3