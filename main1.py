import pygame
import join
import random

#initialisation
pygame.init()

#Caption and display
screen=pygame.display.set_mode((1200,700))
pygame.display.set_caption("Sprites")

#tower
tower_img=pygame.image.load('Asset 24.png')
tower_img=pygame.transform.scale(tower_img,(265*1.1,472*1.1))

#tower part
overlay_img=pygame.image.load('part.png')
overlay_img=pygame.transform.scale(overlay_img,(265*1.1,472*1.1))

#screen 
black=(0,0,0)
bg=(0,100,50)
back=pygame.image.load('1.jpg')
back=pygame.transform.scale(back,(1200,700))

#cannon animation
cannon1_list=[]
cannon_steps=5
animation_cooldown=200
frame_cannon=0

cannon1_image=pygame.image.load('cannon.png').convert_alpha()
cannon1_sheet=join.formed(cannon1_image)

for x in range(cannon_steps):
    cannon1_list.append(cannon1_sheet.get_image(x,128,652,1.7,black))
#cannon2
cannon2_list=[]
cannon_steps=5
animation_cooldown=200
frame_cannon=0

cannon2_image=pygame.image.load('cannon.png').convert_alpha()
cannon2_sheet=join.formed(cannon2_image)

for x in range(cannon_steps):
    cannon2_list.append(cannon2_sheet.get_image(x,128,652,1.7,black))
#cannon3
cannon3_list=[]
cannon_steps=5
animation_cooldown=200
frame_cannon=0

cannon3_image=pygame.image.load('cannon.png').convert_alpha()
cannon3_sheet=join.formed(cannon3_image)

for x in range(cannon_steps):
    cannon3_list.append(cannon3_sheet.get_image(x,128,652,1.7,black))

#cannon ball
cannonballImg = pygame.image.load('cannon-ball.png')
cannonballX = 210
cannonballY = 575
cannonballX_change = 10
cannonballY_change = 0
cannonball_state = "ready"
def fire_cannonball(x,y):
    global cannonball_state
    cannonball_state = "fire"
    screen.blit(cannonballImg, (x , y))
#cannon ball2
cannonball2Img = pygame.image.load('cannon-ball.png')
cannonball2X = 210
cannonball2Y = 500
cannonball2X_change = 10
cannonball2Y_change = 0
cannonball2_state = "ready"
def fire_cannonball2(x,y):
    global cannonball2_state
    cannonball2_state = "fire"
    screen.blit(cannonball2Img, (x , y))
#cannon ball3
cannonball3Img = pygame.image.load('cannon-ball.png')
cannonball3X = 210
cannonball3Y = 410
cannonball3X_change = 10
cannonball3Y_change = 0
cannonball3_state = "ready"
def fire_cannonball3(x,y):
    global cannonball3_state
    cannonball3_state = "fire"
    screen.blit(cannonball3Img, (x , y))
#Create animation main_char
main_char_list=[]
main_char_steps=6
last_update=pygame.time.get_ticks()
animation_cooldown=200
frame=0

main_char_image=pygame.image.load('try3.png').convert_alpha()
main_char_sheet=join.formed(main_char_image)

for x in range(main_char_steps):
    main_char_list.append(main_char_sheet.get_image(x,120,2000,.6,black))


# cooldown 
# frame 
# last update 
# current_update
run = True
while run:

    screen.fill(bg)
    screen.blit(back,(0,0))

    current_time=pygame.time.get_ticks()
    if current_time-last_update>=animation_cooldown:
        frame+=1
        frame_cannon+=1
        last_update=current_time
        if frame>=len(main_char_list):
            frame=0
        if frame_cannon>=len(cannon1_list):
            frame_cannon=0
        if frame_cannon>=len(cannon2_list):
            frame_cannon=0
        if frame_cannon>=len(cannon3_list):
            frame_cannon=0 
    #image display
    screen.blit(tower_img,(-130,120))
    screen.blit(main_char_list[frame],(56,77))
    screen.blit(overlay_img,(-130,120))
 #   screen.blit(catapault_list[frame_catapault],(170,320))
 #   screen.blit(ballista_list[frame_ballista],(170,400))

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if cannonball_state == "ready":
                    fire_cannonball(cannonballX, cannonballY)
            if event.key == pygame.K_2:
                if cannonball2_state == "ready":
                    fire_cannonball2(cannonball2X, cannonball2Y)
            if event.key == pygame.K_3:
                if cannonball3_state == "ready":
                    fire_cannonball3(cannonball3X, cannonball3Y)
    #MOVEMENT MECHANICS OF CANNONBALL 1
    if cannonballX >= 1200:
        cannonballX = 200
        cannonball_state = "ready"

    if cannonball_state == "fire":
        fire_cannonball(cannonballX, cannonballY)
        cannonballX += cannonballX_change
    #MOVEMENT MECHANICS OF CANNONBALL 2
    if cannonball2X >= 1200:
        cannonball2X = 200
        cannonball2_state = "ready"

    if cannonball2_state == "fire":
        fire_cannonball2(cannonball2X, cannonball2Y)
        cannonball2X += cannonball2X_change
    #MOVEMENT MECHANICS OF CANNONBALL 3
    if cannonball3X >= 1200:
        cannonball3X = 200
        cannonball3_state = "ready"

    if cannonball3_state == "fire":
        fire_cannonball3(cannonball3X, cannonball3Y)
        cannonball3X += cannonball3X_change


    screen.blit(cannon1_list[frame_cannon],(170,320))
    screen.blit(cannon2_list[frame_cannon],(170,400))
    screen.blit(cannon3_list[frame_cannon],(170,480)) 
            

    pygame.display.update()        

pygame.quit()
