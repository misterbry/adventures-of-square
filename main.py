import pygame
import sys

class Player(object):
   def __init__(self):
      self.player = pygame.rect.Rect((300, 400, 50, 50))
      self.color = "white"

   def move(self, x_speed, y_speed):
      self.player.move_ip((x_speed, y_speed))

   def change_color(self, color):
      self.color = color

   def draw(self, game_screen):
      pygame.draw.rect(game_screen, self.color, self.player)

paused = False
pygame.font.init()
font = pygame.font.SysFont(pygame.font.get_default_font(), 48)
screen_width, screen_height = 800, 600
pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
pygame.display.set_caption("The Adventures of Square")
player = Player()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

def pause():
   global paused
   while paused:
       screen.fill((0, 0, 0))
       pause_text = font.render("PAUSE", True, (255, 255, 255))
       text_rect = pause_text.get_rect(center=(screen_width // 2, screen_height // 2))
       screen.blit(pause_text, text_rect)
       pygame.display.flip()
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             global running
             running = False
             paused = False
          if event.type == pygame.JOYBUTTONDOWN:
             print(event)
             if pygame.joystick.Joystick(0).get_button(9):
                paused = False

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.JOYBUTTONDOWN:
         print(event)
         if pygame.joystick.Joystick(0).get_button(1):
            player.change_color("red")
         elif pygame.joystick.Joystick(0).get_button(2):
            player.change_color("blue")
         elif pygame.joystick.Joystick(0).get_button(9):
            if paused:
               paused = False
            else:
               paused = True
               pause()
            
      if event.type == pygame.JOYAXISMOTION:
         print(event)

   x_speed = round(pygame.joystick.Joystick(0).get_axis(3))
   y_speed = round(pygame.joystick.Joystick(0).get_axis(4))
   player.move(x_speed, y_speed)
   
   screen.fill((0, 0, 0))
   player.draw(screen)
   pygame.display.update()

pygame.quit()
