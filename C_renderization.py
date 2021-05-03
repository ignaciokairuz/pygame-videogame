import pygame,os,time

from D_growth_conditions import* #def of 4 functions


from E_crop_initializer import* #def of 4 functions

from F_weather import* #def of 7 functions

pygame.init() 
screen=pygame.display.set_mode((900,570))
pygame.display.set_caption("The Great Farmer")
image=pygame.image.load("images/field.jpg")
backgroundpic=pygame.transform.scale(image,(900,570))
c=[constants.initialnumberofcoins]
fontcoin=pygame.font.Font(None,30)
fonty=pygame.font.Font(None,25)
textfont=pygame.font.Font("data/8-BIT WONDER.TTF",16)
font=pygame.font.Font("data/pokemon.ttf",9)
numberofcoins=textfont.render("number of coins ",1,(255,255,255))
imagecoin=pygame.image.load("images/coin.png")
coin=pygame.transform.scale(imagecoin,(30,30))
redfruits=pygame.image.load("images/rf.png")
imagerf=pygame.transform.scale(redfruits,(70,70))
aloe=pygame.image.load("images/aloevera.png")
imagealoe= pygame.transform.scale(aloe,(70,70))
mush=pygame.image.load("images/mushrooms.png")
imagem= pygame.transform.scale(mush,(70,70))
parc=pygame.image.load("images/parcell.jpg")
imageparcel= pygame.transform.scale(parc,(82,82))
box=pygame.image.load("images/dialoguebox.png")
dialoguebox= pygame.transform.scale(box,(900,230))
ranges=pygame.image.load("images/ranges.png")
av_price_text=fonty.render("1$",1,(255,255,255))
m_price_text=fonty.render("5$",1,(255,255,255))
rf_price_text=fonty.render("10$",1,(255,255,255))




def background_blit():
    screen.blit(backgroundpic, (0, 0))  
    screen.blit(numberofcoins,(420,10))
    screen.blit(coin,(720,5))
    screen.blit(ranges,(370,50))
    screen.blit(dialoguebox,(0,340))
    screen.blit(av_price_text,(870,60))
    screen.blit(m_price_text,(870,150))
    screen.blit(rf_price_text,(870,240))

    

def text(data1,data2,data3,data4):
    screen.blit(font.render('The forecast for the next 3 turns, in order, is:',0,(0,0,0)),(27,382))
    screen.blit(font.render('Amount of rain in mm: %s ;Temperature in Celsius: %s ; Wind speed in km/h: %s' %data1,0,(0,0,0)),(27,414))
    screen.blit(font.render('Amount of rain in mm: %s ;Temperature in Celsius: %s ; Wind speed in km/h: %s' %data2,0,(0,0,0)),(27,446))
    screen.blit(font.render('Amount of rain in mm: %s ;Temperature in Celsius: %s ; Wind speed in km/h: %s' %data3,0,(0,0,0)),(27,478))
    screen.blit(font.render('END OF THE TURN %s    ▼' %data4,0,(0,0,0)),(27,510))
    


def text_ani(str, tuple):
    line_space = 16
    x, y = tuple
    y = 300+y*line_space ##shift text down by one line
    char = ''        ##new string that will take text one char at a time. Not the best variable name I know.
    letter = 0
    count = 0
    for i in range(len(str)):
        time.sleep(0.00005) ##change this for faster or slower text animation
        char = char + str[letter]
        text = font.render(char,True,(0, 0, 0),(255,255,255)) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y+50)) ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(text, textrect)
        pygame.display.update(0,340,900,570) ## update only the text just added without removing previous lines.
        count += 1
        letter += 1




