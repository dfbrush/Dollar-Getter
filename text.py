import pygame 
from pygame.locals import * 
from colors import *

#Class that creates and modifys text for start and end screen
class Text(pygame.sprite.Sprite):

#Design of text and how it will be updated and created
  def __init__(self,pos,text):
    super().__init__()
    self.font = pygame.font.SysFont("Times New Roman",30)
    self.image = self.font.render(text,True,WHITE,BLACK)
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def update_text(self,text,stat):
    self.image = self.font.render(text.format(stat),True,WHITE,BLACK)

  def draw(self,screen):
    screen.blit(self.image,self.rect)
