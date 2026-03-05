import pygame as pg ; import os ; from abc import ABC,abstractmethod ;  SCREEN_SIZE = 800 ; SQUARE_SIZE = 100 ; pieces = []
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) ; SHIFT = 10 ; PIECE_SIZE = SQUARE_SIZE-20 ;  running = True
active_piece = None ; old_pos = None ; turn = 'white' ; pg.init() ; screen = pg.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
White_Pawns = 0xFF00#
#----------------------VARIABLES-----------------
class GameBoard:
    def __init__(self,path,size):
        self.img_path = os.path.join(BASE_DIR, path) ; self.size = size
        self.image = pg.image.load(self.img_path).convert_alpha()
        self.image = pg.transform.scale(self.image ,(self.size,self.size))
    def draw(self,surface):
        surface.blit(self.image,(0,0))

class Piece(ABC):
    def __init__(self,path,size,x,y,color):
        self.img_path = os.path.join(BASE_DIR, path) ; self.size = size
        self.image = pg.image.load(self.img_path).convert_alpha()
        self.image = pg.transform.scale(self.image ,(self.size,self.size))
        self.rect = self.image.get_rect()
        self.color = color
        self.rect.topleft = (x + SHIFT, y + SHIFT)
        self.LEGAL_MOVES = []
        self.drag = False
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    @abstractmethod
    def get_legal_moves(self):
        pass

class Pawn(Piece):
    def __init__(self,path,size,x,y,color):
        super().__init__(path,size,x,y,color)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400),(500,500)]
        return self.LEGAL_MOVES

class Rock(Piece):
    def __init__(self,path,size,x,y,color):
        super().__init__(path,size,x,y,color)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400),(600,600)]
        return self.LEGAL_MOVES

class Knight(Piece):
    def __init__(self,path,size,x,y,color):
        super().__init__(path,size,x,y,color)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400)]
        return self.LEGAL_MOVES

class Bishop(Piece):
    def __init__(self,path,size,x,y,color):
        super().__init__(path,size,x,y,color)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400)]
        return self.LEGAL_MOVES

class Queen(Piece):
    def __init__(self,path,size,x,y,color):
        super().__init__(path,size,x,y,color)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400),(100,200)]
        return self.LEGAL_MOVES

class King(Piece):
    def __init__(self,path,size,x,y,color):
        super().__init__(path,size,x,y,color)
    def draw(self,surface):
        surface.blit(self.image,self.rect.topleft)
    def get_legal_moves(self):
        self.LEGAL_MOVES = [(100, 100), (200, 200), (300, 300), (400, 400)]
        return self.LEGAL_MOVES
#----------------------CLASSES-----------------


















#----------------------GAME_LOOP-----------------
chess_board =  GameBoard("Images/Board.png",SCREEN_SIZE) ; chess_board.draw(screen)
W_Pawn1 = Pawn("Images/w_pawn_png_128px.png",PIECE_SIZE,0,600,"white")  ; W_Pawn1.draw(screen) ; pieces.append(W_Pawn1)
W_Pawn2 = Pawn("Images/w_pawn_png_128px.png",PIECE_SIZE,100,600,"white") ; W_Pawn2.draw(screen) ; pieces.append(W_Pawn2)
W_Pawn3 = Pawn("Images/w_pawn_png_128px.png",PIECE_SIZE,200,600,"white") ; W_Pawn3.draw(screen) ; pieces.append(W_Pawn3)
W_Pawn4 = Pawn("Images/w_pawn_png_128px.png",PIECE_SIZE,300,600,"white") ; W_Pawn4.draw(screen) ; pieces.append(W_Pawn4)
W_Pawn5 = Pawn("Images/w_pawn_png_128px.png", PIECE_SIZE, 400, 600,"white") ; W_Pawn5.draw(screen) ; pieces.append(W_Pawn5)
W_Pawn6 = Pawn("Images/w_pawn_png_128px.png", PIECE_SIZE, 500, 600,"white") ; W_Pawn6.draw(screen) ; pieces.append(W_Pawn6)
W_Pawn7 = Pawn("Images/w_pawn_png_128px.png", PIECE_SIZE, 600, 600,"white") ; W_Pawn7.draw(screen) ; pieces.append(W_Pawn7)
W_Pawn8 = Pawn("Images/w_pawn_png_128px.png", PIECE_SIZE, 700, 600,"white") ; W_Pawn8.draw(screen) ; pieces.append(W_Pawn8)
W_Knight1 = Knight("Images/w_knight_png_128px.png", PIECE_SIZE, 600, 700,"white") ; W_Knight1.draw(screen) ; pieces.append(W_Knight1)
W_Knight2 = Knight("Images/w_knight_png_128px.png", PIECE_SIZE, 100, 700,"white") ; W_Knight1.draw(screen) ; pieces.append(W_Knight2)
W_Rock1 = Rock("Images/w_rook_png_128px.png", PIECE_SIZE, 700, 700,"white") ; W_Rock1.draw(screen) ; pieces.append(W_Rock1)
W_Rock2 = Rock("Images/w_rook_png_128px.png", PIECE_SIZE, 000, 700,"white") ; W_Rock2.draw(screen) ; pieces.append(W_Rock2)
W_Bishop1 = Bishop("Images/w_bishop_png_128px.png", PIECE_SIZE, 200, 700,"white") ; W_Bishop1.draw(screen) ; pieces.append(W_Bishop1)
W_Bishop2 = Bishop("Images/w_bishop_png_128px.png", PIECE_SIZE, 500, 700,"white") ; W_Bishop2.draw(screen) ; pieces.append(W_Bishop2)
W_King1 = King("Images/w_king_png_128px.png", PIECE_SIZE, 400, 700,"white") ; W_King1.draw(screen) ; pieces.append(W_King1)
W_Queen1 = Queen("Images/w_queen_png_128px.png", PIECE_SIZE, 300, 700,"white") ; W_Queen1.draw(screen) ; pieces.append(W_Queen1)

B_Pawn1 = Pawn("Images/b_pawn_png_128px.png",PIECE_SIZE,0,100,"black") ; B_Pawn1.draw(screen) ; pieces.append(B_Pawn1)
B_Pawn2 = Pawn("Images/b_pawn_png_128px.png",PIECE_SIZE,100,100,"black") ; B_Pawn2.draw(screen) ; pieces.append(B_Pawn2)
B_Pawn3 = Pawn("Images/b_pawn_png_128px.png",PIECE_SIZE,200,100,"black") ; B_Pawn3.draw(screen) ; pieces.append(B_Pawn3)
B_Pawn4 = Pawn("Images/b_pawn_png_128px.png",PIECE_SIZE,300,100,"black") ; B_Pawn4.draw(screen) ; pieces.append(B_Pawn4)
B_Pawn5 = Pawn("Images/b_pawn_png_128px.png", PIECE_SIZE, 400, 100,"black") ; B_Pawn5.draw(screen) ; pieces.append(B_Pawn5)
B_Pawn6 = Pawn("Images/b_pawn_png_128px.png", PIECE_SIZE, 500, 100,"black") ; B_Pawn6.draw(screen) ; pieces.append(B_Pawn6)
B_Pawn7 = Pawn("Images/b_pawn_png_128px.png", PIECE_SIZE, 600, 100,"black") ; B_Pawn7.draw(screen) ; pieces.append(B_Pawn7)
B_Pawn8 = Pawn("Images/b_pawn_png_128px.png", PIECE_SIZE, 700, 100,"black") ; B_Pawn8.draw(screen) ; pieces.append(B_Pawn8)
B_Knight1 = Knight("Images/b_knight_png_128px.png", PIECE_SIZE, 600, 000,"black") ; B_Knight1.draw(screen) ; pieces.append(B_Knight1)
B_Knight2 = Knight("Images/b_knight_png_128px.png", PIECE_SIZE, 100, 000,"black") ; B_Knight1.draw(screen) ; pieces.append(B_Knight2)
B_Rock1 = Rock("Images/b_rook_png_128px.png", PIECE_SIZE, 700, 000,"black") ; B_Rock1.draw(screen) ; pieces.append(B_Rock1)
B_Rock2 = Rock("Images/b_rook_png_128px.png", PIECE_SIZE, 000, 000,"black") ; B_Rock2.draw(screen) ; pieces.append(B_Rock2)
B_Bishop1 = Bishop("Images/b_bishop_png_128px.png", PIECE_SIZE, 200, 000,"black") ; B_Bishop1.draw(screen) ; pieces.append(B_Bishop1)
B_Bishop2 = Bishop("Images/b_bishop_png_128px.png", PIECE_SIZE, 500, 000,"black") ; B_Bishop2.draw(screen) ; pieces.append(B_Bishop2)
B_King1 = King("Images/b_king_png_128px.png", PIECE_SIZE, 400, 000,"black") ; B_King1.draw(screen) ; pieces.append(B_King1)
B_Queen1 = Queen("Images/b_queen_png_128px.png", PIECE_SIZE, 300, 000,"black") ; B_Queen1.draw(screen) ; pieces.append(B_Queen1)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit();quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            for piece in pieces:
                if piece.rect.collidepoint(event.pos) and piece.color == turn:
                    piece.drag = True
                    active_piece = piece
                    old_pos = piece.rect.topleft ; break

        elif event.type == pg.MOUSEBUTTONUP:
            if active_piece:
                active_piece.drag = False
                active_piece.rect.x = (active_piece.rect.x // SQUARE_SIZE) * SQUARE_SIZE + SHIFT
                active_piece.rect.y = (active_piece.rect.y // SQUARE_SIZE) * SQUARE_SIZE + SHIFT
                new_pos = (active_piece.rect.x,active_piece.rect.y)
                if((active_piece.rect.x // SQUARE_SIZE) * SQUARE_SIZE , (active_piece.rect.y // SQUARE_SIZE) * SQUARE_SIZE) in active_piece.get_legal_moves() and new_pos != old_pos:
                   for piece in pieces:
                       if piece.rect.x == active_piece.rect.x and piece.rect.y == active_piece.rect.y and piece.color != active_piece.color:
                           pieces.remove(piece) ; break
                   turn = 'black' if turn == 'white' else 'white'
                else:
                   active_piece.rect.topleft = old_pos
                active_piece = None
        elif event.type == pg.MOUSEMOTION and active_piece:
            active_piece.rect.center = event.pos
    screen.fill((0,0,0))
    chess_board.draw(screen)
    for piece in pieces:
        piece.draw(screen)
    pg.display.update()
    pg.time.Clock().tick(60)



