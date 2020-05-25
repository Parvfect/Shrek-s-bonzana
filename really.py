import pygame
import time
import random

pygame.init() #Initiates pygame and all the modules that come with it

display_width=800
display_height=600

#Setting color resolution (RGB)
black=(0,0,0) #Absence of all colors therefore No colour in black
white=(254,250,250) #All colours are in white
red=(200,0,0)
blue=(243,0,0)
green=(0,200,0)
bright_red=(255,0,0) #To make the buttons change color when mousr hovers over it
bright_green=(0,255,0)



gameDisplay=pygame.display.set_mode((display_width,display_height)) #Resolution of the game((width,height))

pygame.display.set_caption('Shrek''s bonzana') #Sets module name

clock=pygame.time.Clock() #Controls time variable and used for the frames per second

Img=pygame.image.load('shrek.jpg') #inputting picture that has to be displayed
Img = pygame.transform.scale(Img, (100, 100))
car_width=120

def game_intro():
    intro=True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        
        TextSurf, TextRect = text_objects("Shrek's bonzana", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        #button(msg,x,y,w,h,ic,ac)
        button("It's shrek time",150,450,150,50,bright_green,green,'play')
        button("Make shrek sad",550,450,150,50,bright_red,red,'quit')        
        
        
        
        
        pygame.display.update()
        clock.tick(5)


def button(msg,x,y,w,h,ic,ac,action=None): #message, position, width and height, inactive and active color
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    print(click)


    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None: #pygame checks button clicks as x,y,z where buttons are ordinated
             if action =='play':
                 game_loop()
             elif action =='quit':
                 pygame.quit()
                 quit()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    
    

    
    smallText=pygame.font.Font("freesansbold.ttf",15)
    textSurf,textRect=text_objects(msg,smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def things(thing_x,thing_y,thing_w,thing_h,color):  #objects that clutter the screen to show relative movement
    pygame.draw.rect(gameDisplay, color, [thing_x, thing_y,thing_w,thing_h])
 
def things_dodged(count):  
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def shree(x,y): #Runs game image in background using blit
    gameDisplay.blit(Img,(x,y)) #Displaying the picture at specific position, tuples is one parameter

def crash(): #Crash case
    message_display('MR Shrek is not able to save your soul')

def text_objects(text,font): #Returns text surface and the text rectangle
    textSurface=font.render(text, True, black)   #Paramters - the text, anti aliasing and color
    return textSurface,textSurface.get_rect()


def message_display(text): #Displays input text to game window
    largeText=pygame.font.Font('freesansbold.ttf',30) #Text can be manipulated by the rectange that encases the text
    TextSurf, TextRect= text_objects(text,largeText)
    TextRect.center=((display_width/2,display_height/2)) #Centers the text
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep(2) #Time till text remains in the street
    game_loop()


def game_loop(): #Main game logic
    x=(display_width * 0.45) #Origin at top left, x increases towards right and y increases towards down
    y=(display_height*0.8)
    x_change=0
    thing_startx=random.randrange(0,display_width) #Starting position of the object for the cars
    thing_starty=-600 #Should start off the screen to accomadate sizes
    thing_speed=7
    thing_width=120
    thing_height=120
    car_speed=0
    dodged=0
   # if(thing_startx>(display_width/2)): #Generating second object criteria position
    #    t=random.randrange(0,thing_startx) #Second object x variable
   # else:
   #     t=random.randrange(thing_startx,display_width)
    gameExit=False #Only game exit variable
    while not gameExit: #Game loop
        for event in pygame.event.get():    #Getting user inputs and any events per frame per second
            if event.type == pygame.QUIT: #Asking if user wants to quit the game (x at the tab)
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN: #Checks if a key is being pressed
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP: #Checks if a pressed key has been released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        
        x += x_change
        #print(event)  Note here that the background processes are usually not the taxing part, but displaying them is
        gameDisplay.fill(white) #Background game display, should be before displaying the image
        
        
        
        
        #things(thing_x,thing_y,thing_w,thing_h,color)
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        #things(t,thing_starty,thing_width,thing_height,red) second object display
        thing_starty+=thing_speed #x coordinate should remain constant while the object moves down the screen according to the speed
        shree(x,y)
        things_dodged(dodged)

        #Logic of the game loop - objects overlap and the game logic calls it a crash
        if x>display_width-car_width or x<0: #X is the top left corner of the image so the right boundary should be adjusted accordingly
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
        

        if thing_starty+thing_height > y: #Checking if the bottom is crossing over, remember that the object is referenced with top left corner
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
            #if x > t and x < t + thing_width or x+car_width > t and x + car_width < t+thing_width:
               # crash()

             

        
        


        if thing_starty>display_height:
            thing_starty=0 - thing_height
            thing_startx=random.randrange(0,display_width)


            


        pygame.display.update() #or pygame.display.flip() used to update the foreground, parameter only changes if parameter, flip updates the whole surface
        clock.tick(60) #Number entered here is the frames per second

game_intro()
game_loop()
pygame.quit() #ends pygame
quit() #Quits window






