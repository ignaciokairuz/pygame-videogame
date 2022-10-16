from G_game_menu import Game
from B_pygame_functions import *
import copy



def main():
    # displays menu screen
    g = Game()       
    b=0
    while g.running:
        g.curr_menu.display_menu()     
        b=g.game_loop()
        if b==2:
            break
    screen=pygame.display.set_mode((900,570))
    board = create_boards()  #creates boards (lists)  
    clock = pygame.time.Clock()
    selected_piece = None
    drop_pos = None
    a=farminitializer() #contains info about the crop in a given parcel (allotment.py)
    b=weatherinitializer() #list of lists containing data of the weather parameters for each turn (weather.py)
    turn=0
    def coins():
        Number_coins=fontcoin.render(str(c[0]),1,(255,255,255))
        screen.blit(Number_coins,(665,10))
    c=[constants.initialnumberofcoins]
    coin_backup=copy.deepcopy(c)
    parcels_backup=copy.deepcopy(a)
    renders_backup=copy.deepcopy(board)


    data=[(b[0][0]+' - '+b[0][1],b[0][2]+' - '+b[0][3],b[0][4]+' - '+b[0][5]),(b[1][0]+' - '+b[1][1],b[1][2]+' - '+b[1][3],b[1][4]+' - '+b[1][5]),(b[2][0]+' - '+b[2][1],b[2][2]+' - '+b[2][3],b[2][4]+' - '+b[2][5]),(0)]
    while turn<24:
        background_blit()
        coins()
        create_board_surf()
        piece, x, y = get_square_under_mouse(board)#(what crop is in that position, var id , just a random number)
        events = pygame.event.get()                        # or (what is that position, cord x, cord y)
        for e in events:
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if piece != None:      # is clicked on a an occupied square
                    selected_piece = piece, x, y   # that information is now called " selected_piece "

            if e.type == pygame.MOUSEBUTTONUP:
                if drop_pos[0]!= None and drop_pos[1]<4:  # if i drop the image in an allowed spot, what means (x,y != None, None) WRONG IT ENTERS ANYWAY. x,y come from get_square_un...
                    piece, old_x, old_y = selected_piece     # when i drop image, the place whree i fist clicked will be called (piece, old_x, old_y)
                    board[int(old_y)][int(old_x)] = None    # that same place , as there's no image left, will be empty
                    new_x, new_y = drop_pos                  # 
                    board[int(new_y)][int(new_x)] = piece   # registers which crop is being planted on each parcel
                    plant (a,(drop_pos),piece,c,turn)
                    board[new_y][new_x]=a[algorithm(new_x,new_y)][0]
                selected_piece = None #after droping image, there's no selected_piece
                board[4]=[6,7,8]#drop_pos = None,None #its useless i guess cause "drop_pos" is gonna be overwritten in a few lines ahead
            if e.type == pygame.KEYDOWN:                    
                if e.key==K_RETURN:
                    rain(b,turn,a) #g is the amonut of rain accumulated till given turn (idk why not including this turn)
                    wind(b,turn,a)
                    temperature(b,turn,a)
                    growth(a)
                    harvest(a,c,turn)
                    turn=turn+1
                  
                    if turn<22:
                        turn0=turn
                        turn1=turn+1
                        turn2=turn+2
                    else:
                        turn0=21
                        turn1=22
                        turn2=23
                    data=[(b[turn0][0]+' - '+b[turn0][1],b[turn0][2]+' - '+b[turn0][3],b[turn0][4]+' - '+b[turn0][5]),(b[turn1][0]+' - '+b[turn1][1],b[turn1][2]+' - '+b[turn1][3],b[turn1][4]+' - '+b[turn1][5]),(b[turn2][0]+' - '+b[turn2][1],b[turn2][2]+' - '+b[turn2][3],b[turn2][4]+' - '+b[turn2][5]),(turn)]
                    pygame.draw.rect(screen,(255,255,255),(26,380,850,160))
                    text_ani('The forecast for the next 3 turns, in order, is:', (27, 2)) # text string and x, y coordinate tuple.
                    text_ani('Amount of rain in mm: %s ;Temperature in Celsius: %s ; Wind speed in km/h: %s' %data[0], (27, 4))
                    text_ani('Amount of rain in mm: %s ;Temperature in Celsius: %s ; Wind speed in km/h: %s' %data[1], (27, 6))
                    text_ani('Amount of rain in mm: %s ;Temperature in Celsius: %s ; Wind speed in km/h: %s' %data[2], (27, 8))
                    text_ani('END OF THE TURN %s    ▼' %data[3], (27, 10))
                    coin_backup=copy.deepcopy(c)
                    parcels_backup=copy.deepcopy(a)
                    renders_backup=copy.deepcopy(board)
                    
                if e.key==K_BACKSPACE:
                    c=copy.deepcopy(coin_backup)
                    a=copy.deepcopy(parcels_backup)
                    board=copy.deepcopy(renders_backup)               


        text(data[0],data[1],data[2],data[3])
        draw_pieces(screen, board) #updates pieces draws 
        draw_selector(screen, piece, x, y,selected_piece) #updates selector draws
        drop_pos = draw_drag(screen, board, selected_piece) #updates pieces draws that are being dragged
        for o in range(4):
            for w in range (4):
                board[o][w]=a[algorithm(o,w)][0]
        pygame.display.flip() 
        clock.tick(60)
    sys.exit()    
        
if __name__ == '__main__':
    main()
