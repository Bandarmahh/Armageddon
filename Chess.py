import pygame as pg ; import os ; from abc import ABC,abstractmethod ;  SCREEN_SIZE = 800 ; SQUARE_SIZE = 100
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) ; SHIFT = 10 ; PIECE_SIZE = SQUARE_SIZE-20 ;  running = True

class GameBoard:
    def __init__(self,path,size):
        self.img_path = os.path.join(BASE_DIR, path) ; self.size = size
        self.image = pg.image.load(self.img_path).convert_alpha()
        self.image = pg.transform.scale(self.image ,(self.size,self.size))
    def draw(self,surface):
        surface.blit(self.image,(0,0))

class Piece(ABC):
    def __init__(self,path,size,x,y):
        self.img_path = os.path.join(BASE_DIR, path) ; self.size = size
        self.image = pg.image.load(self.img_path).convert_alpha()
        self.image = pg.transform.scale(self.image ,(self.size,self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x + SHIFT, y + SHIFT)
        self.LEGAL_MOVES = []
        self.drag = False
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    @abstractmethod
    def get_legal_moves(self):
        pass

class Pawn(Piece):
    def __init__(self,path,size,x,y):
        super().__init__(path,size,x,y)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400)]
        return self.LEGAL_MOVES

class Rock(Piece):
    def __init__(self,path,size,x,y):
        super().__init__(path,size,x,y)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400)]
        return self.LEGAL_MOVES

class Knight(Piece):
    def __init__(self,path,size,x,y):
        super().__init__(path,size,x,y)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400)]
        return self.LEGAL_MOVES

class Bishop(Piece):
    def __init__(self,path,size,x,y):
        super().__init__(path,size,x,y)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400)]
        return self.LEGAL_MOVES

class Queen(Piece):
    def __init__(self,path,size,x,y):
        super().__init__(path,size,x,y)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400)]
        return self.LEGAL_MOVES

class King(Piece):
    def __init__(self,path,size,x,y):
        super().__init__(path,size,x,y)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400)]
        return self.LEGAL_MOVES
#------------------------------Game Mechanics


















#------------------------------Game Loop
pg.init() ; screen = pg.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
chess_board =  GameBoard("Board.png",SCREEN_SIZE) ; chess_board.draw(screen)
Pawn1 = Pawn("w_pawn_png_128px.png",PIECE_SIZE,100,600) ; Pawn1.draw(screen)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit();quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if Pawn1.rect.collidepoint(event.pos):
               Pawn1.drag = True
               old_x, old_y = Pawn1.rect.topleft
        elif event.type == pg.MOUSEBUTTONUP:
            if(Pawn1.drag):
               Pawn1.drag = False
               if((Pawn1.rect.x // SQUARE_SIZE) * SQUARE_SIZE , (Pawn1.rect.y // SQUARE_SIZE) * SQUARE_SIZE) in Pawn1.get_legal_moves():
                  Pawn1.rect.x = (Pawn1.rect.x // SQUARE_SIZE) * SQUARE_SIZE + SHIFT
                  Pawn1.rect.y = (Pawn1.rect.y // SQUARE_SIZE) * SQUARE_SIZE + SHIFT
               else:
                Pawn1.rect.topleft = (old_x, old_y)
        elif event.type == pg.MOUSEMOTION and Pawn1.drag:
            Pawn1.rect.center = event.pos

    screen.fill((0,0,0))
    chess_board.draw(screen)
    Pawn1.draw(screen)
    pg.display.update()
