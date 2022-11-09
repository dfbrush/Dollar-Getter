import pygame, random, math, sys, os
from pygame.locals import *
from dollar import Dollar
from text import Text
from colors import *

pygame.init()

#This sets up the background for the game
size = (width,height) = (700,500)
icon = pygame.image.load('Closed-256.png')
pygame.display.set_caption('Playground')
pygame.display.set_icon(icon)

# Experimentation for Movement 
cursor = pygame.image.load('130906.png')
cursorX = 250
cursorY = 350

def cursor():
  screen.blit(cursor,(cursorX, cursorY))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman",30)

#create sprite groups
dollars = pygame.sprite.Group()

#Keeps track of the dollars clicked by the user and frequency
dollars_clicked = 0
seconds = 0
dollars_click_rate = 0

def end_screen():
  overt_text = font.render("Congratulations! You woke up from your dream and got $100!", True, PRUSSIAN_BLUE)
  screen.blit = (overt_text, (width//2,180))

def main():
  global dollars_clicked, seconds, dollars_click_rate

  for i in range(20):
    dollar = Dollar()
    dollars.add(dollar)

  dc_text = Text([width//2,100],"Dollars: 0")
  seconds_text = Text([width//2,200],"Time Passed: 0")
  dcr_text = Text([width//2,300],"Dollars Per Second: 0")
 # final_text = Text([width//2,180],"Congratulations! You woke up from your dream and got $100!")
 
  global screen, clock,size
  
  while True:
    addition = 1
    clock.tick(60)
    seconds = pygame.time.get_ticks()//1000
    if seconds != 0:
      dollars_click_rate = dollars_clicked/seconds
      dollars_click_rate = round(dollars_click_rate,2)
    
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
        for dollar in dollars:
          if dollar.handle_click(x,y):
            dollars_clicked += 10

          if dollars_clicked >= 100:
            end_screen()
            break
            
      if event.type == KEYDOWN:
        if event.key == K_f:
          screen = pygame.display.set_mode(size,pygame.FULLSCREEN) 
        if event.key == K_d:
          screen = pygame.display.set_mode(size)
    
    # score_text = font.render("Clicks: {}".format(clicks),True,WHITE,RED)
    
    dc_text.update_text("Dollars: {}",dollars_clicked)
    seconds_text.update_text("Time Passed: {}",seconds)
    dcr_text.update_text("Dollars Per Second: {}",dollars_click_rate)
   
    
    dollars.update()
    
    screen.fill(PRUSSIAN_BLUE)
  
    dc_text.draw(screen)
    seconds_text.draw(screen)
    dcr_text.draw(screen)

    dollars.draw(screen)

    pygame.display.flip()

if __name__ == "__main__":
  main()