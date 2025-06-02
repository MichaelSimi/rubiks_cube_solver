import pygame
import kociemba


pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rubik's Cube Solver")
font = pygame.font.Font(None, 36)
fontmedium = pygame.font.Font(None, 60)
fontbig = pygame.font.Font(None, 72)
clock = pygame.time.Clock()


# colors
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
BLUE    = (0, 0, 255)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
ORANGE  = (255, 140, 0)
YELLOW  = (255, 255, 0)
GREY = (128 ,128, 128)


def white_center():
    # (width position,  height position, width of rectangle, height of rectangle)
    squares[4]['color'] = WHITE


square_size = 150
grid_start_x = (WIDTH - square_size * 3) // 2
grid_start_y = (HEIGHT - square_size * 3) // 2
squares = []
for row in range(3):
    for col in range(3):
        rect = pygame.Rect(
            grid_start_x + col * square_size,
            grid_start_y + row * square_size,
            square_size,
            square_size
        )
        squares.append({'rect': rect, 'color': GREY})
white_center()


def clear_grid():
    for sq in squares:
        sq['color'] = GREY


# color palette
palette = [
    {'rect': pygame.Rect(10, 10, 50, 50),   'color': WHITE},
    {'rect': pygame.Rect(70, 10, 50, 50),   'color': RED},
    {'rect': pygame.Rect(130, 10, 50, 50),  'color': GREEN},
    {'rect': pygame.Rect(190, 10, 50, 50),  'color': YELLOW},
    {'rect': pygame.Rect(250, 10, 50, 50),  'color': ORANGE},
    {'rect': pygame.Rect(310, 10, 50, 50),  'color': BLUE},
]


selected_square_index = None
show_palette = False
running = True


colors = "U", "R", "F", "D", "L", "B"


button_rect = pygame.Rect(WIDTH - 140, HEIGHT // 2 - 30, 120, 60)
button_visible = False


def get_color_name(rgb):
    if rgb == WHITE:
        return "U"
    if rgb == RED:
        return "R"
    if rgb == GREEN:
        return "F"
    if rgb == YELLOW:
        return "D"
    if rgb == ORANGE:
        return "L"
    if rgb == BLUE:
        return "B"
    return str(rgb)




center_colors = [RED, GREEN, YELLOW, ORANGE, BLUE]
center_color = 0
finished = False


all_faces = []


def next_center():
    global center_color
    if center_color < len(center_colors):
        squares[4]['color'] = center_colors[center_color]
        center_color += 1


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button_visible and button_rect.collidepoint(mouse_pos):
                color_names = [get_color_name(sq['color']) for sq in squares]
                print(", ".join(color_names))
                all_faces.append("".join(color_names))
                clear_grid()
                if center_color < len(center_colors):
                    next_center()
                else:
                    finished = True
            elif show_palette:
                for pal in palette:
                    if pal['rect'].collidepoint(mouse_pos):
                        if selected_square_index is not None:
                            squares[selected_square_index]['color'] = pal['color']
                        show_palette = False
                        selected_square_index = None
                        break
            else:
                for i, sq in enumerate(squares):
                    if i == 4:
                        continue
                    if sq['rect'].collidepoint(mouse_pos):
                        selected_square_index = i
                        show_palette = True
                        break


    if finished:
        screen.fill(BLACK)
        try:
            cube_string = "".join(all_faces)
            if cube_string:
                solution = kociemba.solve(cube_string)
                solution_text = font.render(solution, True, GREEN)
                screen.blit(solution_text, (20, HEIGHT // 2))
        except Exception as e:
            error_text = fontmedium.render(str(e), True, RED)
            screen.blit(error_text, (1.5, HEIGHT // 2))
        cube_position = font.render("Hold the cube so that the front color is green", True, GREEN)
        cube_position2 = font.render("and the top color is white", True, WHITE)
        shown_below = fontbig.render("Then do the algorithm below.", True, BLUE)
        screen.blit(cube_position, (WIDTH // 2 - 250, HEIGHT // 10 -50))
        screen.blit(cube_position2, (WIDTH // 1.65 - 250, HEIGHT // 6 -50))
        screen.blit(shown_below, (WIDTH // 4 - 150, HEIGHT // 4 -50))
    else:
        screen.fill(BLACK)
        # check if all squares are filled except the center square
        all_filled = all(sq['color'] != GREY for i, sq in enumerate(squares) if i != 4)
        button_visible = all_filled


        # draw guide
        if squares[4]['color'] == WHITE:
            #  (width position, height position, width, height)
            pygame.draw.rect(screen, RED, [625, 225, 30, 150])
            pygame.draw.rect(screen, BLUE, [325, 45, 150, 30])
            pygame.draw.rect(screen, ORANGE, [145, 225, 30, 150])
            pygame.draw.rect(screen, GREEN, [325, 525, 150, 30])
        if squares[4]['color'] == RED:
            pygame.draw.rect(screen, BLUE, [625, 225, 30, 150])
            pygame.draw.rect(screen, WHITE, [325, 45, 150, 30])
            pygame.draw.rect(screen, GREEN, [145, 225, 30, 150])
            pygame.draw.rect(screen, YELLOW, [325, 525, 150, 30])
        if squares[4]['color'] == GREEN:
            pygame.draw.rect(screen, RED, [625, 225, 30, 150])
            pygame.draw.rect(screen, WHITE, [325, 45, 150, 30])
            pygame.draw.rect(screen, ORANGE, [145, 225, 30, 150])
            pygame.draw.rect(screen, YELLOW, [325, 525, 150, 30])
        if squares[4]['color'] == YELLOW:
            pygame.draw.rect(screen, RED, [625, 225, 30, 150])
            pygame.draw.rect(screen, GREEN, [325, 45, 150, 30])
            pygame.draw.rect(screen, ORANGE, [145, 225, 30, 150])
            pygame.draw.rect(screen, BLUE, [325, 525, 150, 30])
        if squares[4]['color'] == ORANGE:
            pygame.draw.rect(screen, GREEN, [625, 225, 30, 150])
            pygame.draw.rect(screen, WHITE, [325, 45, 150, 30])
            pygame.draw.rect(screen, BLUE, [145, 225, 30, 150])
            pygame.draw.rect(screen, YELLOW, [325, 525, 150, 30])
        if squares[4]['color'] == BLUE:
            pygame.draw.rect(screen, ORANGE, [625, 225, 30, 150])
            pygame.draw.rect(screen, WHITE, [325, 45, 150, 30])
            pygame.draw.rect(screen, RED, [145, 225, 30, 150])
            pygame.draw.rect(screen, YELLOW, [325, 525, 150, 30])


        # draw squares
        for sq in squares:
            pygame.draw.rect(screen, sq['color'], sq['rect'])
            pygame.draw.rect(screen, BLACK, sq['rect'], 4)


        # draw button if all squares are filled
        if button_visible:
            pygame.draw.rect(screen, BLUE, button_rect)
            font = pygame.font.Font(None, 36)
            text = font.render("Next", True, WHITE)
            text_rect = text.get_rect(center=button_rect.center)
            screen.blit(text, text_rect)


        if show_palette:
            for pal in palette:
                pygame.draw.rect(screen, pal['color'], pal['rect'])
                pygame.draw.rect(screen, WHITE, pal['rect'], 2)


    pygame.display.flip()
    clock.tick(60)
pygame.quit()



