import pygame
import sys
import math #imported this for scroll effect because we need math
import random #this for the random generation in the hright of the tubes

pygame.init()
pygame.font.init()  #import this for font

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 630
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

#GAME STATE --------------------------------------------------------------------------------------------------------------------------------------------------------------

MENU = 0
PLAYING = 1
GAME_OVER = 2
 
game_state = MENU

#MAIN MENU +  IMAGES -----------------------------------------------------------------------------------------------------------------------------------------------------

menu_background = pygame.image.load("blueFlappyBG.jpg").convert()
menu_background_width = menu_background.get_width()

#THE BIRD + Ground collision ---------------------------------------------------------------------------------------------------------------------------------------------
bird_image_file = pygame.image.load("thebird.png").convert_alpha()  #create the bird here with image and put rectangle ---- convert_alpha takes away the background
bird_image = pygame.transform.scale(bird_image_file, (70,50))
bird_rect = bird_image.get_rect()   #rectangle to the bird

bird_x = 300   
bird_y = 300

bird_gravity = 1
bird_jump =-10
bird_speed_downwards = 0

ground_barrier = 520  #variable for collision on the ground
sky_barrier = -75   #variable for sky cap

#GAME FUNCTIONS ----------------------------------------------------------------------------------------------------------------------------------------------------------

def draw_text(screen, text, font, color, x, y):   #function for the title and instructions (YOU CAN SEE ALL THOSE LINES UNDER WERE THERE BEFORE BUT NOW WE JUST PUT THEM INTO A FUNCTION!)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)
    
def top_tube(image_path, width, height):            #function to create top tube
    base_image = pygame.image.load(image_path).convert_alpha()
    scaled_image = pygame.transform.scale(base_image, (width, height))
    flipped_image = pygame.transform.flip(scaled_image, False, True)
    image_rect = flipped_image.get_rect()
    return flipped_image, image_rect

def bottom_tube(image_path, width, height):             #function to create bottom tube
    base_image = pygame.image.load(image_path).convert_alpha()
    scaled_image = pygame.transform.scale(base_image, (width, height))
    image_rect = scaled_image.get_rect()
    return scaled_image, image_rect

def reset_tubes():             #THIS IS A FUNCTION TO RESET ALL THE PIPES WHEN GAME IS OVER
    global bottom_tube_x, bottom_tube_y, top_tube_x, top_tube_y
    bottom_tube_x = 1300
    bottom_tube_y = random.randint(160, 600)
    top_tube_x = 1300
    top_tube_y = bottom_tube_y - tube_spacing - tube_height
    
    global bottom_tube_x2, bottom_tube_y2, top_tube_x2, top_tube_y2
    bottom_tube_x2 = 1675
    bottom_tube_y2 = random.randint(160, 600)
    top_tube_x2 = 1675
    top_tube_y2 = bottom_tube_y2 - tube_spacing - tube_height
    
    global bottom_tube_x3, bottom_tube_y3, top_tube_x3, top_tube_y3
    bottom_tube_x3 = 2050
    bottom_tube_y3 = random.randint(160, 600)
    top_tube_x3 = 2050
    top_tube_y3 = bottom_tube_y3 - tube_spacing - tube_height
    
    global bottom_tube_x4, bottom_tube_y4, top_tube_x4, top_tube_y4
    bottom_tube_x4 = 2425
    bottom_tube_y4 = random.randint(160, 600)
    top_tube_x4 = 2425
    top_tube_y4 = bottom_tube_y4 - tube_spacing - tube_height
    
def reset_bird():     #RESET THE BIRD WHEN GAME IS over
    global bird_y
    bird_y = 220
    
#THE TUBES --------------------------------------------------------------------------------------------------------------------------------------------------------------

tube_image_file = pygame.image.load("tube.png").convert_alpha()

tube_height = 200
tube_spacing = 560

            #TUBE SET 1
bottom_tube_image, bottom_tube_rect = bottom_tube("tube.png", 150, 555)
top_tube_image, top_tube_rect = top_tube("tube.png", 150, 555)

bottom_tube_x = 1300
bottom_tube_y = random.randint(160, 600)  # Adjust the range for random height
top_tube_x = 1300
top_tube_y = bottom_tube_y - tube_spacing - tube_height

            #TUBE SET 2
bottom_tube_image2, bottom_tube_rect2 = bottom_tube("tube.png", 150, 555)
top_tube_image2, top_tube_rect2 = top_tube("tube.png", 150, 555)

bottom_tube_x2 = 1675
bottom_tube_y2 = random.randint(160, 600)
top_tube_x2 = 1675
top_tube_y2 = bottom_tube_y2 - tube_spacing - tube_height

            #TUBE SET 3
bottom_tube_image3, bottom_tube_rect3 = bottom_tube("tube.png", 150, 555)
top_tube_image3, top_tube_rect3 = top_tube("tube.png", 150, 555)

bottom_tube_x3 = 2050
bottom_tube_y3 = random.randint(160, 600)
top_tube_x3 = 2050
top_tube_y3 = bottom_tube_y3 - tube_spacing - tube_height

            #TUBE SET 4
bottom_tube_image4, bottom_tube_rect4 = bottom_tube("tube.png", 150, 555)
top_tube_image4, top_tube_rect4 = top_tube("tube.png", 150, 555)

bottom_tube_x4 = 2425
bottom_tube_y4 = random.randint(160, 600)
top_tube_x4 = 2425
top_tube_y4 = bottom_tube_y4 - tube_spacing - tube_height

#DEFINE GAME VARIABLES --------------------------------------------------------------------------------------------------------------------------------------------------

scroll = 0
tiles = math.ceil(SCREEN_WIDTH / menu_background_width) + 1  #we add one at the end to fill the little space for scrolling menu 

font_path = "Minecraft.ttf"
font = pygame.font.Font(font_path, 30)  #the font we have saved in our file
font_large =pygame.font.Font(font_path, 110)  #this is for the title

score = 0 
high_score = 0 

score_interval = 860  # 1 second in milliseconds
next_score_time = pygame.time.get_ticks() + 2600 #this is the begining delay

#GAME LOOP WHERE GAME BEGINS -----------------------------------------------------------------------------------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                                #-------------------------- (  MENU SCREEN  ) -------------------------------
    if game_state == MENU:      
        
        for i in range (0, tiles):
            screen.blit(menu_background, (i * menu_background_width + scroll, 0))
        #scroll background
        scroll -= 5 #make sure the background is going left at -5
        #reset scroll
        if abs(scroll) > menu_background_width:
            scroll = 0
        
        draw_text(screen, "Flappy Bird", font_large, "yellow", 600, 130)   #the title has the large font variable
        draw_text(screen, "Press Space to Start the Game!", font, "White", 600, 300)  
        draw_text(screen, "Created By Diljot Sahota", font, "white",600, 240)
        
        keys = pygame.key.get_pressed()  #when we click keyboard space the in_menu variable turns false turning the game on 
        if keys[pygame.K_SPACE]:
            game_state = PLAYING
        
                            # ----------------------- (  ACTUAL GAMEPLAY  ) ---------------------------------
    elif game_state == PLAYING:  
          #This code is being copied from above for scroll effect
        for i in range (0, tiles):
            screen.blit(menu_background, (i * menu_background_width + scroll, 0))
        scroll -= 5 
        if abs(scroll) > menu_background_width:
            scroll = 0
            
        screen.blit(bird_image, (bird_x, bird_y))           #THE BIRD  - Screen blit
        
        #----------------- TUBE mechanics ---------------
        
        #tube WEST movment
        
        bottom_tube_x -= 7
        top_tube_x -=7
        
        bottom_tube_x2 -= 7
        top_tube_x2 -= 7
        
        bottom_tube_x3 -= 7
        top_tube_x3 -= 7
        
        bottom_tube_x4 -= 7
        top_tube_x4 -= 7
           
#--------------------     TUBE 1           ----------------------------------------
        #----- bottom 1 tube -----
        if bottom_tube_x < -200:
            bottom_tube_x = 1250

        # Generate a random height for the bottom tube within a range
            min_bottom_tube_y = 160
            max_bottom_tube_y = 600
            bottom_tube_y = random.randint(min_bottom_tube_y, max_bottom_tube_y)
            top_tube_y = bottom_tube_y - tube_spacing - tube_height
            
        #---- top 1 tube -------
        if top_tube_x < -200:
            top_tube_x = 1250

        # Generate a random height for the bottom tube within a range
            min_top_tube_y = 160
            max_top_tube_y = 600
            top_tube_y = random.randint(min_bottom_tube_y, max_bottom_tube_y)
            bottom_tube_y = top_tube_y - tube_spacing - tube_height
        
#--------------------     TUBE 2       ----------------------------------------
        if bottom_tube_x2 < -200:
            bottom_tube_x2 = 1250

            min_bottom_tube_y = 160
            max_bottom_tube_y = 600
            bottom_tube_y2 = random.randint(min_bottom_tube_y, max_bottom_tube_y)
            top_tube_y2 = bottom_tube_y2 - tube_spacing - tube_height
            
        if top_tube_x2 < -200:
            top_tube_x2 = 1250

            min_top_tube_y = 160
            max_top_tube_y = 600
            top_tube_y2 = random.randint(min_bottom_tube_y, max_bottom_tube_y)
            bottom_tube_y2 = top_tube_y2 - tube_spacing - tube_height
            
#--------------------     TUBE 3       ----------------------------------------
        if bottom_tube_x3 < -200:
            bottom_tube_x3 = 1250

            min_bottom_tube_y = 160
            max_bottom_tube_y = 600
            bottom_tube_y3 = random.randint(min_bottom_tube_y, max_bottom_tube_y)
            top_tube_y3 = bottom_tube_y2 - tube_spacing - tube_height
            
        if top_tube_x3 < -200:
            top_tube_x3 = 1250

            min_top_tube_y = 160
            max_top_tube_y = 600
            top_tube_y3 = random.randint(min_bottom_tube_y, max_bottom_tube_y)
            bottom_tube_y3 = top_tube_y3 - tube_spacing - tube_height
            
#--------------------     TUBE 4       ----------------------------------------
        if bottom_tube_x4 < -200:
            bottom_tube_x4 = 1250

            min_bottom_tube_y = 160
            max_bottom_tube_y = 600
            bottom_tube_y4 = random.randint(min_bottom_tube_y, max_bottom_tube_y)
            top_tube_y4 = bottom_tube_y4 - tube_spacing - tube_height
            
        if top_tube_x4 < -200:
            top_tube_x4 = 1250

            min_top_tube_y = 160
            max_top_tube_y = 600
            top_tube_y4 = random.randint(min_bottom_tube_y, max_bottom_tube_y)
            bottom_tube_y4 = top_tube_y4 - tube_spacing - tube_height
            

#---TUBE code to make it actually appear with tube spawn function and appear on the screen----

        screen.blit(bottom_tube_image, (bottom_tube_x, bottom_tube_y))  #set 1
        screen.blit(top_tube_image, (top_tube_x, top_tube_y))
        
        screen.blit(bottom_tube_image2, (bottom_tube_x2, bottom_tube_y2))   #set 2
        screen.blit(top_tube_image2, (top_tube_x2, top_tube_y2))
        
        screen.blit(bottom_tube_image3, (bottom_tube_x3, bottom_tube_y3))   #set 3
        screen.blit(top_tube_image3, (top_tube_x3, top_tube_y3))
        
        screen.blit(bottom_tube_image4, (bottom_tube_x4, bottom_tube_y4))   #set 4
        screen.blit(top_tube_image4, (top_tube_x4, top_tube_y4))
        
        
#Score mechanic -------------------------------------------------------------------------
        current_time = pygame.time.get_ticks()
        if current_time >= next_score_time:
            score += 1
            next_score_time = current_time + score_interval
            print("Score: ", score)
            
        draw_text(screen, f"Score: {score}", font, "yellow", 600, 130)
        
#BIRD v. TUBE COLLISIONS ----------------------------------------------------------------
        
        bird_rect.x = bird_x
        bird_rect.y = bird_y
        bottom_tube_rect.x = bottom_tube_x
        bottom_tube_rect.y = bottom_tube_y
        top_tube_rect.x = top_tube_x
        top_tube_rect.y = top_tube_y
        bottom_tube_rect2.x = bottom_tube_x2
        bottom_tube_rect2.y = bottom_tube_y2
        top_tube_rect2.x = top_tube_x2
        top_tube_rect2.y = top_tube_y2
        bottom_tube_rect3.x = bottom_tube_x3
        bottom_tube_rect3.y = bottom_tube_y3
        top_tube_rect3.x = top_tube_x3
        top_tube_rect3.y = top_tube_y3
        bottom_tube_rect4.x = bottom_tube_x4
        bottom_tube_rect4.y = bottom_tube_y4
        top_tube_rect4.x = top_tube_x4
        top_tube_rect4.y = top_tube_y4

    # Check for collisions with tubes               #we use rectangle of the bird and tubes for collision 
        if (bird_rect.colliderect(bottom_tube_rect) or bird_rect.colliderect(top_tube_rect) or
            bird_rect.colliderect(bottom_tube_rect2) or bird_rect.colliderect(top_tube_rect2) or
            bird_rect.colliderect(bottom_tube_rect3) or bird_rect.colliderect(top_tube_rect3) or
            bird_rect.colliderect(bottom_tube_rect4) or bird_rect.colliderect(top_tube_rect4)):
            game_state = GAME_OVER    

        
        #--------------- CONTROLS FOR THE BIRD ------------------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bird_speed_downwards = bird_jump

        # Update bird's vertical position and velocity
        bird_speed_downwards += bird_gravity
        bird_y += bird_speed_downwards 
        
        #sky cap (so the bird does not jumo over all the tubes because they are not infinite)
        if bird_y < sky_barrier:
            bird_y = sky_barrier
            
        # FOR GROUND COLLISIONS
        if bird_y >= ground_barrier:
            bird_y = ground_barrier
        

            
            game_state = GAME_OVER
            
                                # ----------------------- (   GAME OVER SCREEN  ) ---------------------------------
    elif game_state == GAME_OVER:         
        # Display the game over screen
        for i in range (0, tiles):
            screen.blit(menu_background, (i * menu_background_width + scroll, 0))
        scroll -= 5
        if abs(scroll) > menu_background_width:
            scroll = 0
        draw_text(screen, "Game Over", font_large, "red", 600, 130)
        draw_text(screen, f"Score: {score}", font, "yellow", 600, 250)
        
        draw_text(screen, "Game Over", font_large, "red", 600, 130)
        draw_text(screen, "Press [1] to Restart the Game", font, "White", 600, 400)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:    #we click [1] to restart the game
            game_state = PLAYING
            reset_bird()  # We are calling the functions in the function section to rest the pipes and bird 
            reset_tubes() 
            score = 0 
            next_score_time = pygame.time.get_ticks() + 2400
        #if keys[pygame.K_0]:   
        #     game_state = MENU
        #     reset_bird()  # We are calling the functions in the function section to rest the pipes and bird 
        #     reset_tubes() 
        #     score = 0 
        #     next_score_time = pygame.time.get_ticks() + 2400
            
        
    pygame.display.update()
    clock.tick(FPS)
    
#my high score is 24:) - DJ
    
