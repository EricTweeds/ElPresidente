import pygame, sys, glob, random, time                                          #imports
from pygame.locals import *                                                     #more imports
pygame.init()                                                                   #intializing

def new_panel(panel, x):
    '''
    (int, int) -> int
    Preconditions: panel = 1-5, x = 0-1000
    The function determines if the program should display a new panel. If the player's x position is greater than
    900 and the panel is greater than 1 then it decreases the panel by 1 and if it is equal to 0 and the panel is less than 5
    the panel increases by 1. If none of the conditions are met it keeps the same panel.
    '''
    if x >= 900 and panel >1:
        panel -= 1
        return panel

    if x <= 10 and panel <5:
        panel += 1
        return panel

    else:
        return panel

def dealing (playing_cards):
    '''
    (list) -> list of string, string
    Precondiotions: playing_cards is a list with all the locations to different card images.
    When called the program chooses 2 random cards, 1 for you and 1 for the AI. The numbers choose a file name
    in the list 'playing_cards' then return it to be uploaded to the program.
    '''
    card1 = 0
    card2 = 0
    while card1 == card2:
        card1 = playing_cards[random.randint(0,51)]
        card2 = playing_cards[random.randint(0,51)]
    return card1, card2

def winner(your_card, opp_card):
    '''
    (string, string) -> string
    preconditions: the strings are file names to an image of the card, they contain a
    unique letter per face and a unique number.
    The program registers the cards that were played and determine if the result
    is win, loss or draw based on the value of the card.
    '''

    card1 = your_card[0]
    card2 = opp_card[0]
    value1 = int(your_card[1]+your_card[2])
    value2 = int(opp_card[1]+opp_card[2])
    if card1 == card2:
        return 'draw'
    if value1 < value2:
        return 'you win'
    if value2 < value1:
        return 'opp wins'

def resize(name):
    '''
    (string) -> dimensions (x,y)
    preconditions: name is a variable representing an image.
    Changes the size of all the characters so that they are the same and
    properly fit the screen.
    '''
    new_size = pygame.transform.scale(name, (400, 200))
    return new_size

def movement_x(event, x, ElPresidente):
    '''
    (event, int, image) -> list (int, image)
    preconditions: x in range 0-1000, event is a pygame event
    The program takes in the pygame event, the x value and the image of elpresidente and
    then changes them according to the event. x can increase or decrease and the image can face
    left or right.
    '''
    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:                #player moves right when d key is pressed
        x += 50                                                                 #moves by a factor of 50 pixels
        ElPresidente = ElPresidente_right
                                                                                #the character faces to the right

    if event.type == pygame.KEYDOWN and event.key == pygame.K_a:                #player moves left when a key is pressed
        x -= 50                                                                 #moves by a foctor of 50 pixels
        ElPresidente = ElPresidente_left

    return x, ElPresidente

def jump(event, y):
    '''
    (event, int) -> int
    precondition: y is 400 on key up and 375 on keydown
    Takes in the y value and event and changes accordingly.
    '''
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:            #press space bar for character to jump
        y -= 25                                                                 #moves up by a factor of 25 pixels

    if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:              #the counter action to the line above
        y += 25
    return y

def click(event, mouse_x, mouse_y, panel):
    '''
    (event, int, int, int) -> int(panel)
    preconditions: mouse_x in range (0,1000), mouse_y in range(0,600), panel is = (10 or 50 or 0)
    Covers all the clicking in the main screen, this involves starting the game and navigating the tutorial and credits.
    '''
    if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (425, 575) and mouse_y in range (50, 90) and panel == 10: #start
        panel = 3                                                               #when start is clicked it starts the game

    if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (390, 610) and mouse_y in range (200, 240) and panel == 10: #tutorial
        panel = 50

    if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (400, 600) and mouse_y in range (350, 390) and panel == 10: #credits
        panel = 0

    if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (0, 150) and mouse_y in range (0, 40) and panel == 50: #back button tutorial
        panel = 10

    if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (0, 150) and mouse_y in range (0, 40) and panel == 0: #back button credits
        panel = 10
    return panel

def startbattle(event, mouse_x, mouse_y, panel, temp_panel):
    '''
    (event, int, int, int, int) -> list(int, int)
    preconditions: mouse_x in range (0,1000), mouse_y in range(0,600), panel is = (1, 2, 3, 4, 5)
    This function controls the action of clicking on one of the characters to start the battles, it will then return
    the panel for the battle scene and save thhe panel the player was on so they can be returned later.
    '''
    if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (769, 969) and mouse_y in range (400, 600) and panel == 1 and temp_panel != panel: #starts battle with Justin
        panel = 33
        temp_panel = 1

    if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (550, 750) and mouse_y in range (300, 500) and panel == 2 and temp_panel != panel: #starts battle with Jerry
        panel = 33
        temp_panel = 2

    if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (850, 999) and mouse_y in range (400, 600) and panel == 3 and temp_panel != panel: #starts battle with Jesse
        panel = 33
        temp_panel = 3

    if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (150, 350) and mouse_y in range (400, 600) and panel == 4 and temp_panel != panel: #starts battle with james
        panel = 33
        temp_panel = 4

    if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (600, 800) and mouse_y in range (350, 550) and panel == 5 and temp_panel != panel: #starts battle with Jimmy
        panel = 33
        temp_panel = 5
    return panel, temp_panel



#The chunck below is initializing all the variables and importing the pictures

wins = 0
draws = 0
loses = 0

black = 0, 0, 0                                                                 #RGB for the colour black
white = 255, 255, 255                                                           #RGB for the colour white
blue = 0, 0, 255                                                                #RGB for the colour blue

screen = pygame.display.set_mode((1000, 600))                                   #sets the screen and the size
pygame.display.set_caption('El Presidente')                                     #names the game El Presidente

ElPresidente_right = pygame.image.load('img/elpres.png')
ElPresidente_left = pygame.image.load ('img/elpres2.png')
ElPresidente = ElPresidente_right

jimmy_pic = pygame.image.load('img/Jimmy.png')
jimmy_pic = resize(jimmy_pic)
james_pic = pygame.image.load('img/James.png')
james_pic = resize(james_pic)
jesse_pic = pygame.image.load('img/Jesse.png')
jesse_pic = resize(jesse_pic)
jerry_pic = pygame.image.load('img/Jerry.png')
jerry_pic = resize(jerry_pic)
justin_pic = pygame.image.load('img/Justin.png')
justin_pic = resize(justin_pic)
pbeens_pic = pygame.image.load('img/pbeens.png')
pbeens_pic = pygame.transform.scale(pbeens_pic, (25,25))

deck_pic = pygame.image.load('img/deck.png')
rules = pygame.image.load('img/Rules.png')
resources = pygame.image.load('img/resources.png')

background = pygame.image.load('img/beachback.png')
background = pygame.transform.scale(background,(1000, 600))
battlescene = pygame.image.load('img/jungle_clearing.png')
battlescene = pygame.transform.scale(battlescene, (1000, 600))
waldo = pygame.image.load('img/waldo.png')
waldo = pygame.transform.scale(waldo, (1000, 600))

font = pygame.font.SysFont("monospace", 40)                                     #initializes the monospace font
impact_font = pygame.font.SysFont('impact', 30)                                 #initializes the impact font at size 30
impact80_font = pygame.font.SysFont('impact', 80)                               #initializes the impact font at size 80
start = font.render('Start', 1, (0,0,0))
creds = font.render('Credits', 1, (0,0,0))
reset = font.render('Reset', 1, (140,0,0))
tutorial = font.render('Tutorial', 1, (0,0,0))
back = font.render('<-Back', 1, (0,0,0))
gagnez = impact80_font.render('!!!WINNER/GAGNEZ!!!', 1, black)
looser = impact80_font.render('Please play again', 1, black)
title = impact80_font.render ('El Presidente', 1, blue)
question = impact_font.render("Where's Beensdo?", 1, black)

clock = pygame.time.Clock()

x = 25
y = 400

panel = 10

stop = 0

play = 0

rounds = 0

temp_panel = 0

g = 0

r = 0

victor = 'blah'                                                                 #it had to equal some kind of string

playing_cards = ['A01.png','A02.png','A03.png','A04.png','K05.png','K06.png','K07.png','K08.png','Q09.png','Q10.png','Q11.png','Q12.png','J13.png','J14.png','J15.png','J16.png','B17.png','B18.png','B19.png','B20.png','C21.png','C22.png','C23.png','C24.png','D25.png','D26.png','D27.png','D28.png','E29.png','E30.png','E31.png','E32.png','F33.png','F34.png','F35.png','F36.png','G37.png','G38.png','G39.png','G40.png','H41.png','H42.png','H43.png','H44.png','I45.png','I46.png','I47.png','I48.png','T49.png','T50.png','T51.png','T52.png']

hand = dealing(playing_cards)

your_card = pygame.image.load("img/"+hand[0])
opp_card = pygame.image.load("img/"+hand[1])

#end of chunk


'''
Tips from the tutorial:
MOUSEBUTTONDOWN for mouse action, any mouse button pushed
importing sound = pygame.mixer
then sound.play()
soundbible has many sounds to use
for colour 0,0,0 = red,green,blue
keys for pressdown must be lower case
to rescale image elpres = pygame.transform.scale(ElPresidente(new dimesions))
pygame.mouse.get_pos() get the current coordinates of the mouse.

'''
while 1:                                                                        #The game will run until it is exited
    mouse_x,mouse_y = pygame.mouse.get_pos()                                    #determines the coordinates of the curser on the screen
    for event in pygame.event.get():                                            #detects every event for every tick

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:#game exits when escape button is pressed
                    pygame.quit(); sys.exit()

                movements = movement_x(event, x, ElPresidente)                  #runs movement function
                x = movements[0]                                                #seperates x from the list
                ElPresidente = movements[1]                                     #seperates ElPresidente from the list

                y = jump(event, y)                                              #runs the jump function

                panel = click(event, mouse_x, mouse_y,panel)                    #runs the panel function

                battle = startbattle(event, mouse_x, mouse_y, panel, temp_panel)# runs the start battle function
                panel = battle[0]                                               #seperates panel from list
                temp_panel = battle[1]                                          #seperates temp_panel from list

                if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (487, 600) and mouse_y in range (450, 525) and panel == 33 and play == 0:
                    play = 1                                                    #used for displaying the cards in the battle scene
                    rounds += 1

                if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (900, 1000) and mouse_y in range (500, 600) and panel == 10:
                    panel = 77

                if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (170, 185) and mouse_y in range (110, 125) and panel == 77:
                    panel = 69

    panel = new_panel(panel, x)                                                 #runs the new_panel function

    if panel == 10:
        #start screen
        screen.fill(white)                                                      #background

        screen.blit(start, (425, 50))                                           #start

        screen.blit(tutorial, (390, 200))                                       #tutorial

        screen.blit(creds, (400, 350))                                          #credits

        screen.blit(title, (280, 475))

        pygame.display.flip()                                                   #displays screen and images

    if panel == 0:
        #credits screen
        screen.fill(white)

        screen.blit(resources, (0,0))                                           #displays image of resources

        screen.blit(back, (0,0))                                                #displays back button

        pygame.display.flip()

    if panel == 33:
        # war , jungle
        wins_display = 'wins : '+ str(wins)                                     #sets word for number of wins
        draws_display = 'draws: '+ str(draws)                                   #sets word for number of draws
        loses_display = 'loses: '+ str(loses)                                   #sets word for number of loses

        win = impact_font.render(wins_display, 1, (0,140,0))                    #sets font for number of wins
        draw = impact_font.render(draws_display, 1, (0,0,140))                  #sets font for number of draws
        loss = impact_font.render(loses_display, 1, (140,0,0))                  #sets font for number of loses

        screen.fill(white)                                                      #sets background to white, not actually displayed

        screen.blit(battlescene, (0,0))                                         #changes background image

        screen.blit(ElPresidente_right, (200, 350))                             #places character in a fixed position
        #determines challenger
        if temp_panel == 1:
            challenger = justin_pic
        if temp_panel == 2:
            challenger = jerry_pic
        if temp_panel == 3:
            challenger = jesse_pic
        if temp_panel == 4:
            challenger = james_pic
        if temp_panel == 5:
            challenger = jimmy_pic

        screen.blit(challenger, (550, 350))                                     #fixes challenger in place

        if play == 0:
            hand = dealing(playing_cards)                                       #runs the dealing function

            your_card = pygame.image.load("img/"+hand[0])                              #the players card
            opp_card = pygame.image.load("img/"+hand[1])                               #the opponents card

            victor = str(winner(hand[0], hand[1]))                              #determines the winner

        if play ==1:

            screen.blit(your_card, (400,300))                                   #displays the players card

            screen.blit(opp_card, (600, 300))                                   #displays the challengers card

            if victor == 'you win':
                wins += 1
            if victor == 'draw':
                draws += 1
            if victor == 'opp wins':
                loses += 1
            victor = 'blah'                                                     # to prevent constant increasing score.

            if event.type == pygame.MOUSEBUTTONDOWN and mouse_x in range (475, 625) and mouse_y in range (540, 580):
                play = 0                                                        #when the reset word is clicked it will clear the cards off the screen.

        if rounds == 3 and play == 0:                                           #limits the amount of battles with one challenger to 3 at a time
            panel = temp_panel                                                  #returns character to the panel where they left off
            rounds = 0                                                          #resets the rounds for next time

        screen.blit(deck_pic, (487, 450))                                       #diplays the deck of cards

        screen.blit(reset, (475, 540))                                          #displays reset

        screen.blit(win, (0,0))                                                 #displays wins

        screen.blit(draw, (0,30))                                               #displays draws

        screen.blit(loss, (0, 60))                                              #displays loses

        pygame.display.flip()

    if panel == 1:
        #far right screen
        if x >= 900 and stop == 0:                                              #prevents player from walking off the screen
            x = 25
            stop = 1                                                            #part of the prevention
            screen.fill(black)
            pygame.display.flip()

        if x >= 900 and stop == 1:                                              #part of the prevention
            x = 900

        screen.fill(black)

        screen.blit(background, (0,0))

        screen.blit(justin_pic, (669, 400))

        screen.blit(ElPresidente, (x, y))

        pygame.display.flip()


    if panel == 2:
        #middle right screen
        stop = 0
        if x >= 900:                                                            #part of the prevention
            x = 25
            screen.fill(black)
            pygame.display.flip()

        if x <= 10:
            x = 875
            screen.fill(black)
            pygame.display.flip()

        screen.fill(white)

        screen.blit(background, (0,0))

        screen.blit(jerry_pic, (450, 300))

        screen.blit(ElPresidente, (x, y))

        pygame.display.flip()


    if panel == 3:
        #middle screen
        if x >= 900:                                                            #part of the prevention
            x = 25
            screen.fill(black)
            pygame.display.flip()

        if x <= 10:
            x = 875
            screen.fill(black)
            pygame.display.flip()

        screen.fill(white)

        screen.blit(background, (0,0))

        screen.blit(jesse_pic, (750, 400))

        screen.blit(ElPresidente, (x, y))

        pygame.display.flip()


    if panel == 4:
        #middle left screen
        stop = 0
        if x >= 900:                                                            #part of the prevention
            x = 25
            screen.fill(black)
            pygame.display.flip()

        if x <= 10:
            x = 875
            screen.fill(black)
            pygame.display.flip()

        screen.fill(black)

        screen.blit(background, (0,0))

        screen.blit(james_pic, (50, 400))

        screen.blit(ElPresidente, (x, y))

        pygame.display.flip()


    if panel == 5:
        #far left screen
        if x <= 10 and stop == 0:                                               #part of the prevention
            x = 875
            stop = 1
            screen.fill(black)
            pygame.display.flip()

        if x <= 10 and stop == 1:                                               #part of the prevention
            x = 10

        screen.fill(black)

        screen.blit(background, (0,0))

        screen.blit(jimmy_pic, (500, 350))

        screen.blit(ElPresidente, (x, y))

        pygame.display.flip()

    if wins == 10:
        panel = 69
    if loses == 10:
        panel = 420

    if panel == 69:
        #winning screen
        screen.fill((0,g,0))
        if g == 255:                                                            #causes green background to fade in and out
            g1 = -1
        if g == 0:
            g1 = 1
        g = g+g1

        screen.blit(gagnez, (175,250))

        pygame.display.flip()

    if panel == 420:
        #losing screen
        screen.fill((r,0,0))
        if r == 255:                                                            #causes red background to fade in and out
            r1 = -1
        if r == 0:
            r1 = 1
        r = r+r1

        screen.blit(looser, (200, 250))

        pygame.display.flip()

    if panel == 50:
        #instructions
        screen.fill(white)

        screen.blit(rules, (50,0))

        screen.blit(back, (0,0))

        pygame.display.flip()

    if panel == 77:
        #easter egg
        screen.blit(waldo, (0,0))

        screen.blit(pbeens_pic, (162, 103))

        screen.blit(question, (375, 0))

        pygame.display.flip()


    clock.tick(60)                                                              #limits the game to 60 fps to keep speed constant

'''
Some Credits:
    http://www.jfitz.com/cards/ Playing cards
    http://www.cartoonmovement.com/cartoon/1043 El Presidente
    http://www.gamedev.net/files/file/139-2d-character-model-ready-to-animate-and-customize/
'''


