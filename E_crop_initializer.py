import pygame,sys
from pygame.locals import *

def farminitializer():
    farm=[]
    for i in range(4):
        for j in range (4):
            p=[None,0,0,0,0,0,(i,j)] #(crop,amount of rain in given turn,temperature in given turn,speed of wind in that turn, points, turns crop alive)
            farm.append(p)
 
    return farm

def plant (a,drop_pos,piece,c,turn): #a,(x,y),piece,c
    z=c[0]
    for i in a:
        if i[6]==drop_pos:
            i[5]=turn
            if piece==6:
                i[0]=6
                c[0]-=1
                if c[0]<0:
                    i[0]=None   #meter un if abajo q evalue si hay algo plantado o no q seria evaluar i[0]
                    c[0]=z
                    
                    
            elif piece==7:
                i[0]=7
                c[0]-=5
                if c[0]<0:
                    i[0]=None   #meter un if abajo q evalue si hay algo plantado o no q seria evaluar i[0]
                    c[0]=z
                    
            elif piece==8:
                i[0]=8
                c[0]-=10
                if c[0]<0:
                    i[0]=None   #meter un if abajo q evalue si hay algo plantado o no q seria evaluar i[0]
                    c[0]=z
                    
        
            
           
            
   

   
           

           
