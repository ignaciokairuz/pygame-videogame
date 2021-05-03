from C_renderization import *


TILESIZE=82

def create_board_surf(): #renders board
    board_surf = pygame.Surface((TILESIZE*4, TILESIZE*4))
    for y in range(4):
        for x in range(4):        
            pos = pygame.Rect(x * TILESIZE,y * TILESIZE, TILESIZE, TILESIZE)
            screen.blit(imageparcel, imageparcel.get_rect(center=pos.center))
    

def get_square_under_mouse(board): #registers under which square the pointe is
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) 
    x, y = [int(v // TILESIZE) for v in mouse_pos] #translates real coordinates to ones more simpler adapted to the amount of squares 
    for z in range(3):     
        if  800<=mouse_pos[0]<=882 and 60+z*(92)<=mouse_pos[1]<=60+(z+1)*82: return (board[4][z],z+0.5,4) 
            # (what crop is in that position, var id , just a random number) 
    if x >= 0 and y >= 0 and x<=3 and y<=3: return (board[y][x], x, y) #(what is that position, cord x, cord y)
    
    else: return None, None, None

def create_boards(): #creates boards
    board = []
    for y in range(4):
        board.append([])
        for x in range(4):
            board[y].append(None)
    board.append([6,7,8])
    return (board)

    


    
def draw_pieces(screen, board): #reders pieces continuosly (when dragged they can change color)
            
            

    for y in range(4):
        for x in range(4): 
            piece = board[y][x]
            pos = pygame.Rect(x * TILESIZE,y * TILESIZE, TILESIZE, TILESIZE)
            if piece==6: #goes over all the positions of the matrix till it founds an occupied one so later render it
                screen.blit(imagealoe, imagerf.get_rect(center=pos.center))
            if piece==7:
                screen.blit(imagem, imagealoe.get_rect(center=pos.center))
            if piece==8:
                screen.blit(imagerf, imagem.get_rect(center=pos.center))
    for q in range (3):
        piece=board[4][q]
        pos=pygame.Rect(( 800,60+q*92, TILESIZE, TILESIZE))
        if piece==6:
            screen.blit(imagealoe, imagerf.get_rect(center=pos.center))
        if piece==7:
            screen.blit(imagem, imagealoe.get_rect(center=pos.center))
        if piece==8:
            screen.blit(imagerf, imagem.get_rect(center=pos.center))
            
def draw_selector(screen, piece, x, y,selected_piece): #creates a red squares edges when hovering over a planted parcel and a green one in everyone under the pointer when 
    if piece != None and piece!=0:                                                                                                                      #MOUSEBUTTONSOWN
        for s in range(3):
            if x==(s+0.5):
                rect = ( 800,60+s*92, TILESIZE, TILESIZE)
                pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)
        if type(x)==int and y<4:            
            rect = (x * TILESIZE,y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
    
    
    if selected_piece: #when MOUSEBUTTONDOWN and no MOUSEBUTTONUP yet (keeps the clone/shadow in its old place till dropped) 
        spiece, sx, sy = selected_piece # (what's in the square, cord x, cord y)
        if sy<4:            
            rect = (sx * TILESIZE,sy * TILESIZE, TILESIZE, TILESIZE)  #what this second part does is that turns red where the image was substracted
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)

            

def draw_drag(screen, board, selected_piece):
    if selected_piece: #user clicked (MOUSEBUTTONDOWN) on a piece ()WORKS WRONG
        piece, x, y = get_square_under_mouse(board) #location of the piece
        for s in range(3):
            if x==(s+0.5):
                rect = ( 800,60+s*92, 82, 82)
                pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)                        #draws selector but when piece is dragged
                
        if type(x)==int:
            rect = (x * TILESIZE,y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
        
        pos = pygame.Vector2(pygame.mouse.get_pos())      
        if selected_piece[0]==6:
            screen.blit(imagealoe, imagealoe.get_rect(center=pos))
        if selected_piece[0]==7:
            screen.blit(imagem, imagem.get_rect(center=pos))
        if selected_piece[0]==8:
            screen.blit(imagerf, imagerf.get_rect(center=pos))        

        return (x,y)
    else: return (None,None)

def algorithm(x,y):
    h=((y+1)*(x+1)+abs(x-y-abs(y-3))*(y)-1)
    return(h)