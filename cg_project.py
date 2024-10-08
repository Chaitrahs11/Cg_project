import pygame 
import math
# Initialize Pygame
pygame.init()
# Constants

SCREEN_WIDTH = 1100

SCREEN_HEIGHT = 700
# Colors (RGB format)

SKY_COLOR = (102, 178, 255)  # Light blue 

sun_color= (255,255,0)

SUN_COLOR = (253, 184, 19)   # Yellowish

GRASS_COLOR1 = (0, 153, 76)  # Dark green

GRASS_COLOR2 = (153, 204, 0) # Light green

CLOUD_COLOR = (225, 246, 255)  # Cloud color

NATURE_COLOR = (51, 102, 204)  # Blue

LIGHT_BLACK = (50,50,50)

YELLOW = (255, 255, 0)

FOREST_GREEN = (34,139,34)

BACKGROUND_COLOR = (128, 128, 128)



# Flower parameters

FLOWER_RADIUS = 18

NUM_PETALS = 17

PETAL_LENGTH = 50

PETAL_WIDTH = 20



# Animation parameters

BLOOM_SPEED = 0.0047

bloom_progress = 0.0


bloomspd=BLOOM_SPEED


skycolor=SKY_COLOR

inc = 40

# Variables

sun = (900, 350)

xs = 0

ys = 0

angle_inc = 0.007

angle_offset = 0

# Initialize the screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Sunflower Simulation")



# Function to draw sky

def draw_sky():

    screen.fill(skycolor)



# Function to handle keyboard events

def handle_events():  

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            quit()

# Function to draw clouds

def draw_clouds():

    

        # Draw clouds

     pygame.draw.circle(screen, CLOUD_COLOR, (100, 600), 30)

     pygame.draw.circle(screen, CLOUD_COLOR, (150, 600), 50)

     pygame.draw.circle(screen, CLOUD_COLOR, (200, 600), 45)



     pygame.draw.circle(screen, CLOUD_COLOR, (900, 600), 30)

     pygame.draw.circle(screen, CLOUD_COLOR, (950, 600), 50)

     pygame.draw.circle(screen, CLOUD_COLOR, (1000, 600), 45)



     pygame.draw.circle(screen, CLOUD_COLOR, (400, 500), 45)

     pygame.draw.circle(screen, CLOUD_COLOR, (450, 500), 57)

     pygame.draw.circle(screen, CLOUD_COLOR, (500, 500), 40)



# Function to draw sun 

def draw_sun():

    global xs, ys,skycolor

    if xs +sun[0] >400 and ys + sun[1] <= 600:

        pygame.draw.circle(screen, SUN_COLOR, (xs + sun[0], ys + sun[1]), 50)

        skycolor = (165, 229, 255)

        xs -= 2

        ys += 1

    elif ys + sun[1] <440:

        pygame.draw.circle(screen,sun_color, (70, 440), 50)

        #xs = 0

        #ys = 0

    else:

        # pygame.draw.circle(screen,sun_color, (400, 600), 50)

        pygame.draw.circle(screen, sun_color, (xs + sun[0], ys + sun[1]), 50)

        xs -= 2

        ys -= 1

        skycolor = (255,165,0)



# Function to draw ship

def draw_scene():

    pygame.draw.circle(screen, NATURE_COLOR, (315, 325), 50)

    pygame.draw.polygon(screen, NATURE_COLOR, [(300, 230), (300, 325), (330, 325), (330, 230)])



    pygame.draw.circle(screen, NATURE_COLOR, (280, 330), 42)

    pygame.draw.circle(screen, NATURE_COLOR, (350, 330), 42)

    pygame.draw.circle(screen, NATURE_COLOR, (300, 363), 39)

    pygame.draw.circle(screen, NATURE_COLOR, (330, 363), 39)

    pygame.draw.circle(screen, NATURE_COLOR, (320, 400), 28)



    pygame.draw.circle(screen, NATURE_COLOR, (550, -635), 900)



    pygame.draw.circle(screen, NATURE_COLOR, (1050, 70), 80)

    pygame.draw.circle(screen, NATURE_COLOR, (1100, 205), 30)

    pygame.draw.circle(screen, NATURE_COLOR, (1070, 150), 45)



    

    

def draw_stem(center_x, center_y):

    global inc

    # stem_width = 10

    # stem_height = 120

    # stem_rect = pygame.line

    # stem_rect = pygame.Rect(center_x - stem_width // 2, center_y-135, stem_width, stem_height)

    pygame.draw.line(screen,FOREST_GREEN, (center_x+inc,center_y),(SCREEN_WIDTH//2,center_y-120),8)



def draw_flower(center_x, center_y, bloom_progress):

    global inc

    # Draw flower center

    pygame.draw.circle(screen, LIGHT_BLACK, (center_x + inc, center_y), int(FLOWER_RADIUS))



    # Draw petals 

    for i in range(NUM_PETALS):

        angle = 2 * math.pi * i / NUM_PETALS + angle_offset

        x1 = center_x + inc + math.cos(angle) * FLOWER_RADIUS

        y1 = center_y + math.sin(angle) * FLOWER_RADIUS

        x2 = x1 + math.cos(angle) * PETAL_LENGTH * bloom_progress

        y2 = y1 + math.sin(angle) * PETAL_LENGTH * bloom_progress

        x3 = x1 + math.cos(angle + math.pi / 12) * PETAL_WIDTH * bloom_progress

        y3 = y1 + math.sin(angle + math.pi / 12) * PETAL_WIDTH * bloom_progress

        x4 = x1 + math.cos(angle - math.pi / 12) * PETAL_WIDTH * bloom_progress

        y4 = y1 + math.sin(angle - math.pi / 12) * PETAL_WIDTH * bloom_progress

        pygame.draw.polygon(screen, YELLOW, [(x1, y1), (x3, y3), (x2, y2), (x4, y4)])



def update():

    global bloom_progress, bloomspd, angle_offset, angle_inc, inc

    if bloom_progress >= 0.0:  

        inc -= 0.15
       
        angle_offset += angle_inc

        bloom_progress += bloomspd

    if bloom_progress > 1.1:

        inc -= 0.15

        angle_inc = -0.007

        bloomspd = -BLOOM_SPEED

    elif bloom_progress < 0.0:

        bloomspd = BLOOM_SPEED


def rotate_screen_180():

    rotated_screen = pygame.transform.rotate(screen, 180)

    screen.blit(rotated_screen, (0, 0))

# Main game loop

def main():

    # global inc

    clock = pygame.time.Clock()

    center_x = SCREEN_WIDTH // 2

    center_y = SCREEN_HEIGHT // 2

    while True:

        handle_events()

        update()

        draw_sky()

        draw_sun()

        draw_scene()

        draw_clouds()

        draw_stem(center_x, center_y)

        draw_flower(center_x, center_y, bloom_progress)
        
        rotate_screen_180()

        pygame.display.flip()

        clock.tick(60)  # Cap the frame rate at 60 FPS



if __name__ == "__main__":

    main()