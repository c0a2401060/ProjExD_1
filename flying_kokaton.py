import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習３
    bg_img2 = pg.transform.flip(bg_img,True,False)#続き２
    kk_img = pg.image.load("fig/3.png") #練習２前半
    kk_img = pg.transform.flip(kk_img,True,False) #練習２後半
    kk_rct = kk_img.get_rect()#続き５の１
    kk_rct.center = 300,200#続き５の２


    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr    
        y = 0
        z = 0

        key_lst = pg.key.get_pressed()#続き５の３
        if key_lst[pg.K_UP]:
            z = -1
        
        if key_lst[pg.K_DOWN]:
            z = 1
            
        if key_lst[pg.K_RIGHT]:
            y = 2
           
        if key_lst[pg.K_LEFT]:
            y = -1       

        kk_rct.move_ip((-1+y,0+z))


        screen.blit(bg_img,[-x,0])
        screen.blit(bg_img2, [-x+1600,0])#続き３
        screen.blit(bg_img, [-x+3200,0])#続き4
        #screen.blit(kk_img, [300, 200]) #練習３
        screen.blit(kk_img,kk_rct) 
        
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習５

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()