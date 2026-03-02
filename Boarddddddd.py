import pygame as pg ; import os ; SCREEN_SIZE = 800 ; running = True ;  BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class GameBoard:
    def __init__(self,path,size):
        self.img_path = os.path.join(BASE_DIR, path) ; self.size = size
        self.image = pg.image.load(self.img_path).convert_alpha()
        self.image = pg.transform.scale(self.image ,(self.size,self.size))
    def draw(self,screen,coordinates):
        screen.blit(self.image,(coordinates,coordinates))

class Piece:
    def __init__(self,path,size):
        self.img_path = os.path.join(BASE_DIR, path) ; self.size = size
        self.image = pg.image.load(self.img_path).convert_alpha()
        self.image = pg.transform.scale(self.image ,(self.size,self.size))
    def draw(self,screen,coordinates):
        screen.blit(self.image,(coordinates,coordinates))




pg.init() ; screen = pg.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
chess_board =  GameBoard("Board.png",SCREEN_SIZE) ; chess_board.draw(screen)
Pawn = Piece()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit();quit()
    pg.display.update()
