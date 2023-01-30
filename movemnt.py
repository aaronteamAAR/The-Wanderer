import pygame, imageio

# Initialize the player's starting position
player_x = 100
player_y = 100

# Load the gif image using `pygame.image.load()`
player_image = pygame.image.load("preview_idle.gif")


screen = pygame.display.set_mode((800, 600))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # L, R, T, B Movements 
    if keys[pygame.K_LEFT]:
        player_x -= 3
    if keys[pygame.K_RIGHT]:
        player_x += 3
          
    if keys[pygame.K_UP]:
        player_y -= 3
        player_image = pygame.transform.rotate(player_image,-90)
    if keys[pygame.K_DOWN]:
        player_y += 3
        player_image = pygame.transform.rotate(player_image,-90)

    screen.fill((0, 0, 0))
    
    screen.blit(player_image, (player_x, player_y))

    # Update the screen
    pygame.display.flip()

# Clean up
pygame.quit()
