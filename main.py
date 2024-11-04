import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Inicio del Juego')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Fuentes
font = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 36)

# Dimensiones del laberinto y posición inicial
maze = [
    "##########",
    "#        #",
    "# ## ### #",
    "# #      #",
    "# # ######",
    "#        #",
    "##########",
]

cell_size = 60
player_pos = [1, 1]  # Posición inicial del jugador

# Función para dibujar el laberinto
def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                pygame.draw.rect(screen, WHITE, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif cell == " ":
                pygame.draw.rect(screen, BLACK, (x * cell_size, y * cell_size, cell_size, cell_size))

# Función para dibujar el jugador
def draw_player():
    pygame.draw.rect(screen, GREEN, (player_pos[0] * cell_size, player_pos[1] * cell_size, cell_size, cell_size))

# Función para mostrar el menú de inicio
def show_start_menu():
    while True:
        screen.fill(BLACK)

        title_text = font.render('Mi Juego', True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        # Definición de los botones
        start_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
        exit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 40, 200, 50)

        # Dibuja los botones
        mouse_pos = pygame.mouse.get_pos()
        draw_button('Comenzar', start_button_rect.x, start_button_rect.y, start_button_rect.width, start_button_rect.height, start_button_rect.collidepoint(mouse_pos))
        draw_button('Salir', exit_button_rect.x, exit_button_rect.y, exit_button_rect.width, exit_button_rect.height, exit_button_rect.collidepoint(mouse_pos))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botón izquierdo del mouse
                    if start_button_rect.collidepoint(event.pos):
                        start_game()  # Inicia el juego
                    elif exit_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

# Función para iniciar el juego
def start_game():
    global player_pos
    player_pos = [1, 1]  # Reinicia la posición del jugador
    while True:
        screen.fill(BLACK)

        draw_maze()  # Dibuja el laberinto
        draw_player()  # Dibuja al jugador

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        move_player(keys)

        pygame.display.flip()
        pygame.time.delay(100)

# Función para mover al jugador
def move_player(keys):
    new_x, new_y = player_pos

    if keys[pygame.K_w]:
        new_y -= 1
    if keys[pygame.K_s]:
        new_y += 1
    if keys[pygame.K_a]:
        new_x -= 1
    if keys[pygame.K_d]:
        new_x += 1

    # Verificar colisión con las paredes del laberinto
    if maze[new_y][new_x] == " ":
        player_pos[0] = new_x
        player_pos[1] = new_y

# Función para dibujar un botón
def draw_button(text, x, y, width, height, is_hovered):
    color = GRAY if is_hovered else WHITE
    pygame.draw.rect(screen, color, (x, y, width, height))
    label = font_small.render(text, True, BLACK)
    screen.blit(label, (x + (width - label.get_width()) // 2, y + (height - label.get_height()) // 2))

# Ejecuta el menú de inicio
show_start_menu()
