import pygame, subprocess, sys



class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 900, 570
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'data/8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.instructions = InstructionsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            return(2)



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y , color):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
        
class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 200

    def draw_cursor(self):
        self.game.draw_text('*', 25, self.cursor_rect.x, self.cursor_rect.y, self.game.WHITE)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.draw.circle(self.game.window, (255,255,0), (0,0), 150)
        enterkey=pygame.image.load("images/enterkey.png")
        self.game.window.blit(enterkey, (5, 5))
        updownkey=pygame.image.load("images/updown.png")
        self.game.window.blit(updownkey, (50, 10))
        backspacekey=pygame.image.load("images/backspace.png")
        self.game.window.blit(backspacekey, (20, 75))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        #self.game.WHITE = (255, 255, 255)
        self.startx, self.starty = self.mid_w, self.mid_h                     
        self.instructionsx, self.instructionsy = self.mid_w, self.mid_h + 100                 
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 50, self.game.DISPLAY_W / 2 + 14, self.game.DISPLAY_H / 2 - 200, self.game.WHITE )
            self.game.draw_text("Start Game", 30, self.startx, self.starty, self.game.WHITE)
            self.game.draw_text("Instructions", 30, self.instructionsx + 12, self.instructionsy, self.game.WHITE)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.instructionsx + self.offset, self.instructionsy)
                self.state = 'Instructions'
            elif self.state == 'Instructions':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.instructionsx + self.offset, self.instructionsy)
                self.state = 'Instructions'
            elif self.state == 'Instructions':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Instructions':
                self.game.curr_menu = self.game.instructions
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, 'data/moreinfo.txt'])
            self.run_display = False



class InstructionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            with open('data/instructions.txt', 'r') as file:
                count=0
                for i in file:
                    count+=1
                    self.game.draw_text(i.strip(), 13, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 180 +count*40, self.game.WHITE)
            self.game.draw_text('Instructions', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 250, self.game.WHITE)
            self.blit_screen()
            
            






 

