import pygame as pg ; import os ; BOARD_SIZE = 800 ; Running = True

screen = pg.display.set_mode((BOARD_SIZE,BOARD_SIZE))
path = os.path.join("/Users/bandarbinhazza/PycharmProjects/PythonProject",'Armagedon','Board.png')
Board = pg.image.load(path).convert() ; Board = pg.transform.scale(Board,size=(BOARD_SIZE,BOARD_SIZE))




# game Loop-----------------------------
screen.blit(Board, (0, 0))
while Running:
    for event in pg.event.get():
        if event == pg.QUIT:
            pg.quit();quit()
    pg.display.update()