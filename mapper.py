import pygame 

import odometryHandler 

x = odometry.getX() 
y = odometry.getY() 

drawer = pygame.draw

visualizer = pygame.display.set_mode([500, 400]) 

drawer.line(screen, (0, 0, 0), x, y, 1) 

