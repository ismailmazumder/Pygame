import pygame
pygame.init()
bg = pygame.image.load('road.png')#1200 400
display = pygame.display.set_mode((1200, 400))
car = pygame.image.load('tesla.png')
danger = pygame.image.load('danger.jpg')
car_x = 300
car_y = 150
danger_show = False
tf = True
while tf:
    pygame.event.get()
    keys = pygame.key.get_pressed()

    display.blit(bg,(0,0))
    display.blit(car, (car_y, car_x))
    if keys[pygame.K_UP]:
        car_x = car_x - .1
        print(car_x)
    if car_x <=60.300000000000885:
        danger_show = True
    else:
        danger_show = False
    #if car_x
    if danger_show:
        display.blit(danger,(0,0))
    if keys[pygame.K_DOWN]:
        car_x = car_x + .1
        #print(car_x)

    if keys[pygame.K_RIGHT]:
        car_y = car_y + .1
    elif keys[pygame.K_LEFT]:
        car_y = car_y - .1

    pygame.display.update()