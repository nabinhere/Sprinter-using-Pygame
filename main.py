import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Snail Sprint")

#clock
time = pygame.time.Clock()

#setup font
font = pygame.font.Font("font/Pixeltype.ttf", 50)

#background
sky_surf = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surf = pygame.image.load("graphics/ground.png").convert_alpha()

#Player
player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (100, 300))
player_gravity = 0

player_stand_surf = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand_surf = pygame.transform.rotozoom(player_stand_surf, 0, 2.5)
player_stand_rect = player_stand_surf.get_rect(center = (400,200))

jump_sound = pygame.mixer.Sound("audio/jump.mp3")
jump_sound.set_volume(0.5)
bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.set_volume(0.5)
bg_music.play()

#Snail
snail_frame1 = pygame.image.load("graphics/snail/snail1.png")
snail_frame2 = pygame.image.load("graphics/snail/snail2.png")
snail_frames = [snail_frame1, snail_frame2]
snail_index = 0
snail_surf = [snail_index]

#Fly
fly_frame1 = pygame.image.load("graphics/Fly/Fly1.png")
fly_frame2 = pygame.image.load("graphics/Fly/Fly2.png")
fly_frames = [fly_frame1, fly_frame2]
fly_index = 0
fly_surf = fly_frames[fly_index]

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

#snail_timer
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

#fly_timer
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 6
            if obstacle_rect.bottom == 300: screen.blit(snail_surf, obstacle_rect)
            else: screen.blit(fly_surf, obstacle_rect)
            
def delete_old_obstacles(obstacle_list):
    new_obstacle_list = []
    if obstacle_list:
        for obstacle in obstacle_list:
            if obstacle.x > -100: new_obstacle_list.append(obstacle)
    
    return new_obstacle_list
    
def check_collisions(player, obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            if player.colliderect(obstacle): return False
        else: return True
    else: return True

def display_score(start_time):
        current_time = pygame.time.get_ticks() - start_time
        score_surf = font.render(f"Score: {int(current_time/1000)}", False, (64,64,64))
        score_rect = score_surf.get_rect(center = (400, 50))
        screen.blit(score_surf, score_rect)
        return current_time

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300: player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

obstacle_rect_list = []

start_time = 0

game_active = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900, 1100), 200)))

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE) and (player_rect.bottom == 300): 
                    player_gravity = -20
                jump_sound.play()
            
            if event.type == snail_animation_timer:
                if snail_index == 0: snail_index = 1
                else: snail_index = 0
                snail_surf = snail_frames[snail_index]

            if event.type == fly_animation_timer:
                if fly_index == 0: fly_index = 1
                else: fly_index = 0
                fly_surf = fly_frames[fly_index]

        else:
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE): 
                game_active = True
                start_time = pygame.time.get_ticks()
                    

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))

        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom > 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        obstacle_movement(obstacle_rect_list)
        obstacle_rect_list = delete_old_obstacles(obstacle_rect_list)

        score = display_score(start_time)

        game_active = check_collisions(player_rect, obstacle_rect_list)


    else:
        screen.fill("#4281bd")
        obstacle_rect_list.clear()
        screen.blit(player_stand_surf, player_stand_rect)

        #display score after game over 
        score_surf = font.render(f"Score: {int(score/1000)}", False, (64,64,64))
        score_rect = score_surf.get_rect(center = (400, 50))
        screen.blit(score_surf, score_rect)

        #instruction after game over
        instruction_surf = font.render("Press Space Key to restart", False, (64,64,64))
        instruction_rect = instruction_surf.get_rect(center = (400, 350))
        screen.blit(instruction_surf, instruction_rect)

    pygame.display.update()
    time.tick(60)

pygame.quit()