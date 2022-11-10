import pygame, random, math
from pygame.locals import * 
from colors import *

#Class that creates and modifys dollars 
class Dollar(pygame.sprite.Sprite):

  #Dictates the actual design of the dollar and its interactions
  def __init__(self):
    super().__init__()
    size = (width,height) = (600,500)
    
    self.image = pygame.image.load("Dollar.png")
    self.image = pygame.transform.smoothscale(self.image,[70,90])
    
    self.rect = self.image.get_rect()
    self.rect.center = [width//2,height//2]
    self.speed = [random.randint(-5,5),random.randint(-5,5)]

#Function that reappears a dollar on the screen if clicked
  def handle_click(self,x,y):
    if self.rect.collidepoint(x,y):
        rand_x = random.randint(self.rect.width//2,500-self.rect.width//2)
        rand_y = random.randint(self.rect.height//2,500 - self.rect.width//2)
        self.rect.center = [rand_x,rand_y]
        self.speed = [random.randint(-5,5),random.randint(-5,5)]
        return True
      
    return False
      
#Sets limits as to where the dollar can move
  def update(self):
    if self.rect.right - 20 > 670:
      self.speed[0] *= -1

    if self.rect.bottom - 20 > 480:
      self.speed[1] *= -1

    if self.rect.top + 20 < 0:
      self.speed[1] *= -1

    if self.rect.left + 20 < 0:
      self.speed[0] *= -1

    self.rect.move_ip(self.speed)
  

  def draw(self,screen):
    screen.blit(self.image,self.rect)
