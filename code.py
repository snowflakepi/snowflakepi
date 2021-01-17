#using python version 3.8.2
import pygame #using pygame version 1.9.6
import random
pygame.font.init()
pygame.display.init()
pygame.display.set_caption("Confusing parkour")
screen=pygame.display.set_mode(size=(500,500))
time=0
time2=0
color=(255,255,255)
font=pygame.font.SysFont(None,50)
won=False
letters="abcdefghijklmnopqrstuvwxyz"
def choices():
    x=[]
    y=list(range(0,26))
    for i in range(4):
        choice=random.randint(0,len(y)-1)
        x+=[y[choice]]
        y=y[:choice]+y[choice+1:]
    return x
buttons=choices()
white=(255,255,255)
txt = font.render(letters[0],True,white)
player=(50,390)
xspeed=0
yspeed=0
clock=pygame.time.Clock()
floor=False
def block(x,y,width,height):
    global player
    global xspeed
    global yspeed
    global floor
    left=x
    right=x+width
    pl=player[0]
    pr=player[0]+10
    top=y
    bot=y+height
    pu=player[1]
    pb=player[1]+10
    if (pb>top and pu<bot):
        if (pl>=right-5 and pl<=right):
            player=(right,player[1])
            pl=player[0]
            pr=player[0]+10
            xspeed=0
        if (pr<=left+5 and pr>=left):
            player=(left-10,player[1])
            xspeed=0
            pl=player[0]
            pr=player[0]+10
    if (pr>left and pl<right):
        if (pb<=top+10 and pb>=top):
            player=(player[0],top-10)
            yspeed=0
    
            floor=True
        elif (pu>=bot-10 and pu<=bot):
            player=(player[0],bot)
    
            yspeed=1
    
    pygame.draw.rect(screen,(0,255,0),(x,y,width,height))
    
def win(x,y,width,height):
    global won
    global player
    left=x
    right=x+width
    pl=player[0]
    pr=player[0]+10
    top=y
    bot=y+height
    pu=player[1]
    pb=player[1]+10
    if (pb>top and pu<bot):
        if (pr>left and pl<right):
            won=True
    pygame.draw.rect(screen,(255,255,0),(x,y,width,height))
class move:
    def __init__(self):
        self.xes=()
        self.yes=()
        self.x=0
        self.y=0
        self.width=0
        self.height=0
    def up(self):
        self.x+=1
        self.y+=1
        self.x%=len(self.xes)
        self.y%=len(self.yes)
        block(self.xes[self.x],self.yes[self.y],self.width,self.height)
class blink:
    def __init__(self):
        self.x=0
        self.y=0
        self.xes=()
        self.yes=()
        self.width=0
        self.height=0
    def change(self):
        self.x+=1
        self.y+=1
        self.x%=len(self.xes)
        self.y%=len(self.yes)
    def up(self):
        block(self.xes[self.x],self.yes[self.y],self.width,self.height)
move2=blink()
move2.width=40
move2.height=40
move2.xes=(300,350)
move2.yes=(250,250)
move3=blink()
move3.width=40
move3.height=40
move3.xes=(200,250)
move3.yes=(250,250)
move4=blink()
move4.width=40
move4.height=40
move4.xes=(100,150)
move4.yes=(250,250)
move5=blink()
move5.width=40
move5.height=20
move5.xes=(25,25)
move5.yes=(210,170,130,90)
move1=move()
move1.width=80
move1.height=20
move1.xes=tuple(range(76,400,2))+tuple(range(400,56,-2))
move1.yes=(380,400)[:1]
move6=move()
move6.width=40
move6.height=20
move6.xes=(115,115)
move6.yes=tuple(range(150,90,-1))
while True:
    floor=False
    pygame.draw.rect(screen,(0,0,0),(0,0,500,500))
    timer=pygame.time.get_ticks()
    if (not won):
        if (timer>time*4000):
            move2.change()
            move3.change()
            move4.change()
            move5.change()
            time=int(timer/4000)+1
            buttons=choices()
        keys=pygame.key.get_pressed()[97:123]
        yspeed+=0.65
        if (yspeed>9):
            yspeed=9
            
        player=(player[0]+xspeed,player[1]+int(yspeed))
        block(450,310,20,20)
        block(430,260,20,20)
        block(25,400,40,20)
        block(400,360,80,20)
        block(25,250,40,20)
        block(65,90,50,20)
        block(95,90,20,80)
        block(155,0,20,130)
        block(165,150,60,20)
        block(300,150,60,20)
        block(400,120,60,20)
        win(425,110,10,10)
        move1.up()
        move2.up()
        move3.up()
        move4.up()
        move5.up()
        move6.up()
        if(keys[buttons[1]]):
            xspeed-=1
        if(keys[buttons[2]]):
            yspeed+=1
        if(keys[buttons[3]]):
            xspeed+=1
        if (keys[buttons[0]] and floor):
            yspeed=-9
        
        if (not(keys[buttons[1]] or keys[buttons[3]])):
            if xspeed>0:
                xspeed-=1
            if xspeed<0:
                xspeed+=1
        if (player[1]>=500):
            player=(50,390)
            xspeed=0
            yspeed=0
        if (xspeed>5):
            xspeed=5
        if (xspeed<-5):
            xspeed=-5
        
        pygame.draw.rect(screen,(0,0,255),(player[0],player[1],10,10))

        
        txt = font.render(str(int((time*4000-timer)/1000)+1),True,white)
        screen.blit(txt,(int(450-txt.get_rect()[2]/2),int(50-txt.get_rect()[3]/2)))
        pygame.draw.lines(screen,white,True,((375,375),(425,375),(425,425),(475,425),(475,475),(425,475),(425,425),(375,425),(325,425),(325,475),(375,475),(375,425)))
        pygame.draw.line(screen,white,(375,475),(425,475))
        txt = font.render(letters[buttons[0]],True,white)
        screen.blit(txt,(int(400-txt.get_rect()[2]/2),int(400-txt.get_rect()[3]/2)))
        txt = font.render(letters[buttons[1]],True,white)
        screen.blit(txt,(int(350-txt.get_rect()[2]/2),int(450-txt.get_rect()[3]/2)))
        txt = font.render(letters[buttons[2]],True,white)
        screen.blit(txt,(int(400-txt.get_rect()[2]/2),int(450-txt.get_rect()[3]/2)))
        txt = font.render(letters[buttons[3]],True,white)
        screen.blit(txt,(int(450-txt.get_rect()[2]/2),int(450-txt.get_rect()[3]/2)))
    else:
        txt = font.render("You win!",True,white)
        screen.blit(txt,(int(250-txt.get_rect()[2]/2),int(250-txt.get_rect()[3]/2)))
        


    
    
    
    
    if pygame.event.get(12):
        pygame.display.quit()
        break
    else:
        pygame.event.clear()
    clock.tick()
    pygame.time.delay(50-clock.get_time())
    pygame.display.update()
    
    
