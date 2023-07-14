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
cannon_list=[]
cannon_steps=5
animation_cooldown=50
frame_cannon=0

cannon_image=pygame.image.load('cannon.png').convert_alpha()
cannon_sheet=join.formed(cannon_image)

for x in range(cannon_steps):
    cannon_list.append(cannon_sheet.get_image(x,128,652,1.6,black))

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
                    
        if frame_cannon>=len(cannon_list):
            frame_cannon=0
            
    #image display
            
    screen.blit(tower_img,(-130,120))
    screen.blit(main_char_list[frame],(56,77))
    screen.blit(overlay_img,(-130,120))
    


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if cannonball_state == "ready":
                    fire_cannonball(cannonballX, cannonballY)
    if cannonballX >= 1200:
        cannonballX = 200
        cannonball_state = "ready"

    if cannonball_state == "fire":
        fire_cannonball(cannonballX, cannonballY)
        cannonballX += cannonballX_change

    screen.blit(cannon_list[frame_cannon],(120,490))
    pygame.display.update()
pygame.quit()
