from random import *
from pygame import *
from Bullet import *
image_path = 'enemi.png'
enemies = sprite.Group()

class Enemy(sprite.Sprite):

    enemies = sprite.Group()
    def __init__(self, image_path, x, y):
        sprite.Sprite.__init__(self) #mandatory calling of the constructor of the parent class
        # each sprite should store the image property—its image
        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (64,64)) # resize the image
 
        # each sprite should store the rect property—the rectangle into which it is inscribed
        self.rect = self.image.get_rect() #we get a rectangle from the image
        #we set its location
        self.start_x = randint(60,740)
        self.start_y =30
        self.rect.x = x
        self.rect.y = y

    def dead(self,bullets):
        for bullet in bullets:
            if enemy.collide(bullet):
                self.kill()
    def update(self,screen):
        self.update(screen)
        self.rect.y -= 3
        if self.getY() > 600:
            self.kill()
enemy = Enemy('enemi.png', randint(60,740), 60)

    
        
        
