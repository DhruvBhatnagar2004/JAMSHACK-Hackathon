import pygame
import join
import random
import health

#initialisation
pygame.init()

#Caption and display
screen=pygame.display.set_mode((1200,700))
pygame.display.set_caption("Sprites")

dead=0
game_over=pygame.image.load('game_over.png')
game_over=pygame.transform.scale(game_over,(1200,700))
font=pygame.font.Font("freesansbold.ttf",16)
font_x=15
font_y=20

#tower
tower_img=pygame.image.load('Asset 24.png')
tower_img=pygame.transform.scale(tower_img,(265*1.1,472*1.1))
destroytower_img=pygame.image.load('Asset 31.png')
destroytower_img=pygame.transform.scale(destroytower_img,(265*1.1,472*1.1))

#tower part
overlay_img=pygame.image.load('part.png')
overlay_img=pygame.transform.scale(overlay_img,(265*1.1,472*1.1))

#counters
flag=0
flag2=0
flag3=0
flag4=0
flag5=0
flag6=0

# hp
healthbar=health.hp(15,35,150,20,300)

#screen 
black=(0,0,0)
bg=(0,100,50)
back=pygame.image.load('1.jpg')
back=pygame.transform.scale(back,(1200,700))

#Character animation
enemy_1_list=[]
enemy_3_list=[]
enemy_1_steps=6
enemy_3_steps=6
char1_cooldown=150
char3_cooldown=150
frame_char=0
frame3_char=0
enemy1hp=[]
enemy3hp=[]
last_char_update=pygame.time.get_ticks()
last_char3_update=pygame.time.get_ticks()

#Enemy_1
No_of_enemy_1=20
enemy_1_x_axis=[530]
enemy_1_y_axis=[1195]
enemy_rect=[]


for i in range(No_of_enemy_1-1):
    enemy_1_y_axis.append(random.randrange(1200,3000,500))
    enemy_1_x_axis.append(random.randrange(400,530,80))
 
enemy_1_image=pygame.image.load('enemy1.2_try.png').convert_alpha()
enemy_1_sheet=join.formed(enemy_1_image)

for x in range(enemy_1_steps):
    enemy_1_list.append(enemy_1_sheet.get_image(x,150,200,.6,black))
enemy_1_x_axis.sort()
for i in range(No_of_enemy_1):
    enemy_rect.append(enemy_1_list[0].get_rect()) 
    enemy_rect[i].x=enemy_1_y_axis[i]
    enemy_rect[i].y=enemy_1_x_axis[i]
    enemy1hp.append(4)

#Enemy_3
No_of_enemy_3=20
enemy3_rect=[]
enemy_3_y_axis=[1900]
enemy_3_x_axis=[]

enemy_3_image=pygame.image.load('enemy3.2_try.png').convert_alpha()
enemy_3_sheet=join.formed(enemy_3_image)

for i in range(No_of_enemy_3):
    enemy_3_x_axis.append(random.randrange(400,530,80))
    enemy_3_y_axis.append(random.randrange(2000,4000,500))

enemy_3_x_axis.sort()

for x in range(enemy_3_steps):
    enemy_3_list.append(enemy_3_sheet.get_image(x,150,200,.6,black))

for i in range(No_of_enemy_3):
    enemy3_rect.append(enemy_3_list[0].get_rect()) 
    enemy3_rect[i].x=enemy_3_y_axis[i]
    enemy3_rect[i].y=enemy_3_x_axis[i]
    enemy3hp.append(8)

def show_text(x,y):
    score=font.render("Tower Health",True,(0,0,0))
    screen.blit(score,(x,y))
    

#static Character animation
enemy_list=[]
enemy_steps=6
char_cooldown=150
framestats_char=0
laststats_char_update=pygame.time.get_ticks()

#static villians
enemy=1
counter4killcanon=0
enemy_image=pygame.image.load('d.png').convert_alpha()
enemy_sheet=join.formed(enemy_image)

for x in range(enemy_steps):
    enemy_list.append(enemy_sheet.get_image(x,500,2000,.6,black))
# static enemy2
enemy3_list=[]
enemy3_steps=6
char_cooldown=150
framestats_char=0
laststats3_char_update=pygame.time.get_ticks()

#static villians
enemy3=1
enemy3_image=pygame.image.load('enemy2_attack.png').convert_alpha()
enemy3_sheet=join.formed(enemy3_image)

for x in range(enemy3_steps):
    enemy3_list.append(enemy3_sheet.get_image(x,200,200,.6,black))

    
#cannon animation
cannon1_list=[]
cannon_steps=5
animation_cooldown=200
frame_cannon=0
cannon_hp=100

cannon1_image=pygame.image.load('cannon.png').convert_alpha()
cannon1_sheet=join.formed(cannon1_image)

for x in range(cannon_steps):
    cannon1_list.append(cannon1_sheet.get_image(x,128,652,1.7,black))

#cannon2
cannon2_list=[]
cannon_steps=5
animation_cooldown=200
frame_cannon=0
cannon2_hp=100

cannon2_image=pygame.image.load('cannon.png').convert_alpha()
cannon2_sheet=join.formed(cannon2_image)

for x in range(cannon_steps):
    cannon2_list.append(cannon2_sheet.get_image(x,128,652,1.7,black))
#cannon3
cannon3_list=[]
cannon_steps=5
animation_cooldown=200
frame_cannon=0
cannon3_hp=100

cannon3_image=pygame.image.load('cannon.png').convert_alpha()
cannon3_sheet=join.formed(cannon3_image)

for x in range(cannon_steps):
    cannon3_list.append(cannon3_sheet.get_image(x,128,652,1.7,black))

#cannon ball
cannonballImg = pygame.image.load('cannon-ball.png')
cannonballX = 210
cannonballY = 575
ball_rect=pygame.Rect(210,575, 16, 16)
#print(ball_rect)
cannonballX_change = 10
cannonballY_change = 0
cannonball_state = "ready"
cannonballdead="dead"
cannonballpower=1

def fire_cannonball(x,y):
    global cannonball_state
    cannonball_state = "fire"
    screen.blit(cannonballImg, (x , y))
    
#cannon ball2
cannonball2Img = pygame.image.load('cannon-ball.png')
cannonball2X = 210
cannonball2Y = 500
ball2_rect=pygame.Rect(210,500, 16, 16)
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
cannonball3Y = 420
ball3_rect=pygame.Rect(210,420, 16, 16)
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
# jump
jump_char_list=[]
jump_char_steps=6
lastjump_update=pygame.time.get_ticks()
animationjump_cooldown=500
framejump=0
jump_char_image=pygame.image.load('hero_jump1.2.png').convert_alpha()
jump_char_sheet=join.formed(jump_char_image)

for x in range(jump_char_steps):
    jump_char_list.append(jump_char_sheet.get_image(x,200,1200,.6,black))
# walk
walk_char_list=[]
walk_counter=0
walk_char_steps=6
walkxaxis=50
lastwalk_update=pygame.time.get_ticks()
animationwalk_cooldown=200
framewalk=0
walk_char_image=pygame.image.load('hero_walk.png').convert_alpha()
walk_char_sheet=join.formed(walk_char_image)

for x in range(walk_char_steps):
    walk_char_list.append(walk_char_sheet.get_image(x,200,1200,.6,black))

count=No_of_enemy_1+No_of_enemy_3
run = True
while run:
 
    screen.fill(bg)
    screen.blit(back,(0,0))
    towerhp=cannon_hp+cannon2_hp+cannon3_hp
    healthbar.hp=towerhp
    healthbar.draw(screen)
    if towerhp<=0:
        dead=1
        screen.blit(destroytower_img,(-130,120))
        cannonball_state="finaldead"
        cannonball2_state="finaldead"
        cannonball3_state="finaldead"
        pygame.time.wait(1500)

    else:
        screen.blit(tower_img,(-130,120))
        
    for i in range(No_of_enemy_1):
        if enemy_rect[i].colliderect(ball_rect):
            cannonballX=210
            ball_rect.x=210
            cannonball_state="ready"
            enemy1hp[i]-=cannonballpower
            if enemy1hp[i]<=0:
                count-=1
                enemy_1_x_axis[i]=-9000
                enemy_rect[i].x=-9000
        if enemy_rect[i].colliderect(ball2_rect):
            cannonball2X=210
            ball2_rect.x=210
            cannonball2_state="ready"
            enemy1hp[i]-=cannonballpower
            if enemy1hp[i]<=0:
                count-=1
                enemy_1_x_axis[i]=-9000
                enemy_rect[i].x=-9000
        if enemy_rect[i].colliderect(ball3_rect):
            cannonball3X=210
            ball3_rect.x=210
            cannonball3_state="ready"
            enemy1hp[i]-=cannonballpower
            if enemy1hp[i]<=0:
                count-=1
                enemy_1_x_axis[i]=-9000
                enemy_rect[i].x=-9000
    for i in range(No_of_enemy_3):
        if enemy3_rect[i].colliderect(ball_rect):
            cannonballX=210
            ball_rect.x=210
            cannonball_state="ready"
            enemy3hp[i]-=cannonballpower
            if enemy3hp[i]<=0:
                count-=1
                enemy_3_x_axis[i]=-9000
                enemy3_rect[i].x=-9000
        if enemy3_rect[i].colliderect(ball2_rect):
            cannonball2X=210
            ball2_rect.x=210
            cannonball2_state="ready"
            enemy3hp[i]-=cannonballpower
            if enemy3hp[i]<=0:
                count-=1
                enemy_3_x_axis[i]=-9000
                enemy3_rect[i].x=-9000
        if enemy3_rect[i].colliderect(ball3_rect):
            cannonball3X=210
            ball3_rect.x=210
            cannonball3_state="ready"
            enemy3hp[i]-=cannonballpower
            if enemy3hp[i]<=0:
                count-=1
                enemy_3_x_axis[i]=-9000
                enemy3_rect[i].x=-9000
        


    current_time=pygame.time.get_ticks()
    if current_time-last_update>=animation_cooldown:
        frame+=1
        frame_cannon+=1
        framewalk+=1
        last_update=current_time
        if frame>=len(main_char_list):
            frame=0
        if framewalk>=len(walk_char_list):
            framewalk=0
        if frame_cannon>=len(cannon1_list):
            frame_cannon=0

    currentjump_time=pygame.time.get_ticks()
    if currentjump_time-lastjump_update>=animationjump_cooldown:
        framejump+=1
        lastjump_update=currentjump_time
        if framejump>=len(jump_char_list):
            framejump=0
            
    # static villian
    char_time=pygame.time.get_ticks()
    if char_time-laststats_char_update>=char_cooldown:
        laststats_char_update=char_time
        if enemy_1_y_axis[0] <= 275 or counter4killcanon==1:
            counter4killcanon=1
            framestats_char+=1
        if framestats_char>=len(enemy_list):
            framestats_char=0
            if flag==0:
                cannon_hp-=(1*c)
            if flag2==0:
                cannon2_hp-=(1*c2)           
            if flag3==0:
                cannon3_hp-=(1*c3)             
            if flag4==0:
                cannon_hp-=(1*c4)               
            if flag5==0:
                cannon2_hp-=(1*c5)             
            if flag6==0:
                cannon3_hp-=(1*c6)            
            
    #Character display
    #enemy1
    char_time=pygame.time.get_ticks()
    if char_time-last_char_update>=char1_cooldown:
        frame_char+=1
        last_char_update=char_time
        if frame_char>=len(enemy_1_list):
            frame_char=0
            
    for i in range(No_of_enemy_1):
        if enemy_1_y_axis[i] <= 275:  
            screen.blit(enemy_list[framestats_char],(80,enemy_1_x_axis[i]))
        else:
            screen.blit(enemy_1_list[frame_char],(enemy_1_y_axis[i],enemy_1_x_axis[i]))
            enemy_1_y_axis[i]-=1.0
        
            if  enemy_rect[i].x > 275:
                enemy_rect[i].x-=.9
    c=0    
    for i in range(No_of_enemy_1):
        if enemy_1_y_axis[i] <= 275 and enemy_1_y_axis[i]>0 and enemy_1_x_axis[i]>=440:
            c+=1   

    c2=0    
    for i in range(No_of_enemy_1):
        if enemy_1_y_axis[i] <= 275 and enemy_1_y_axis[i] >= 0 and enemy_1_x_axis[i] >=370 and enemy_1_x_axis[i] < 440:
            c2+=1   

    c3=0    
    for i in range(No_of_enemy_1):
        if enemy_1_y_axis[i] <= 275 and enemy_1_y_axis[i] >=0 and enemy_1_x_axis[i] >370 and enemy_1_x_axis[i] <=400:
            c3+=1   
    #enemy3
    char_time=pygame.time.get_ticks()
    if char_time-last_char3_update>=char1_cooldown:
        frame3_char+=1
        last_char3_update=char_time
        if frame3_char>=len(enemy_1_list):
            frame3_char=0
            
    for i in range(No_of_enemy_3):
        if enemy_3_y_axis[i] <= 275 and enemy_3_y_axis[i] >=0:  
            screen.blit(enemy3_list[framestats_char],(270,enemy_3_x_axis[i]))
        else:
            screen.blit(enemy_3_list[frame3_char],(enemy_3_y_axis[i],enemy_3_x_axis[i]))
            enemy_3_y_axis[i]-=1.0
        
            if  enemy3_rect[i].x > 275:
                enemy3_rect[i].x-=.9

    c4=0    
    for i in range(No_of_enemy_3):
        if enemy_3_y_axis[i] <= 275 and enemy_3_y_axis[i] >=0 and enemy_3_x_axis[i]>=440:
            c4+=1   
    c5=0    
    for i in range(No_of_enemy_3):
        if enemy_3_y_axis[i] <= 275 and enemy_3_y_axis[i] >=0 and enemy_3_x_axis[i] >=370 and enemy_3_x_axis[i] < 440:
            c5+=1   
    c6=0    
    for i in range(No_of_enemy_3):
        if enemy_3_y_axis[i] <= 275 and enemy_3_y_axis[i] >=0 and enemy_3_x_axis[i] >370 and enemy_3_x_axis[i] <=400:
            c6+=1 

    #image display
    if count!=0:
        screen.blit(main_char_list[frame],(56,77))
        screen.blit(overlay_img,(-130,120))
    else:
        if walk_counter==0:
            screen.blit(jump_char_list[framejump],(5,77))
            walk_counter=1
        screen.blit(walk_char_list[framewalk],(walkxaxis,500))
        walkxaxis+=0.9
        #if(walkaxis>=1200):
            ###############################################################################################



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if cannonball_state == "ready":
                    for i in range(cannon_steps):
                        screen.blit(cannon1_list[i],(170,480))
                    fire_cannonball(cannonballX, cannonballY)
            if event.key == pygame.K_2:
                if cannonball2_state == "ready":
                    for i in range(cannon_steps):
                        screen.blit(cannon2_list[i],(170,400))
                    fire_cannonball2(cannonball2X, cannonball2Y)
            if event.key == pygame.K_3:
                if cannonball3_state == "ready":
                   for i in range(cannon_steps):
                        screen.blit(cannon3_list[i],(170,320))
                   fire_cannonball3(cannonball3X, cannonball3Y)
# OVEMENT MECHANICS OF CANNONBALL 1
    if cannonballX >= 1200:
        cannonballX = 210
        ball_rect.x=210
        cannonball_state = "ready"

    if cannonball_state == "fire":
        fire_cannonball(cannonballX, cannonballY)
        ball_rect.x+=cannonballX_change
        cannonballX += cannonballX_change

    #MOVEMENT MECHANICS OF CANNONBALL 2
    if cannonball2X >= 1200:
        cannonball2X = 210
        ball2_rect.x=210
        cannonball2_state = "ready"

    if cannonball2_state == "fire":
        fire_cannonball2(cannonball2X, cannonball2Y)
        ball2_rect.x+=cannonball2X_change
        cannonball2X += cannonball2X_change

    #MOVEMENT MECHANICS OF CANNONBALL 3
    if cannonball3X >= 1200:
        cannonball3X = 210
        ball3_rect.x=210
        cannonball3_state = "ready"

    if cannonball3_state == "fire":
        fire_cannonball3(cannonball3X, cannonball3Y)
        ball3_rect.x+=cannonball3X_change        
        cannonball3X += cannonball3X_change

    screen.blit(cannon1_list[0],(170,480))
    screen.blit(cannon2_list[0],(170,400))
    screen.blit(cannon3_list[0],(170,320))
    if dead==1:
        screen.blit(game_over,(0,0))
                
    show_text(font_x,font_y)
    pygame.display.flip()
    pygame.display.update()        

pygame.quit()
