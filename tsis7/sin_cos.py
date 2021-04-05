import pygame
from math import sin, cos, pi, sqrt

#--------------------------------------------------------------------------------------------          
pygame.init()
screen = pygame.display.set_mode([900, 650])                                    # start
pygame.display.set_caption('sin&cos')               

is_clicked_sin, is_clicked_cos = False, False        # check if already clicked or not
#----------------------------------------------------------------------------------------------

sin_points, cos_points, sin_points2, cos_points2 = [], [], [], []
n, A = 5, 240
for x in range(720):
    y = sin(x / 600. * n * pi) * A + 266
    sin_points.append([x+100, y])
    sin_points2.append([x+101, y])
for x in range(720):                                           # detecting sin and cos points
    y = int(cos(x / 600. * n * pi) * A + 266) 
    cos_points.append([x+100, y])
    cos_points2.append([x+101, y])
clock = pygame.time.Clock()

#----------------------------------------------------------------------------------------------
def cos_graph(cos_points, color):
    for i in range(0, len(cos_points)-1, 2):
        pygame.draw.aaline(screen, color, cos_points[i], cos_points[i+1], 2)
        pygame.draw.aaline(screen, color, cos_points2[i], cos_points2[i+1], 2)
        clock.tick(120)
        pygame.display.update()

#-----------------------------------------------------------------------------------------------

def sin_graph(sin_points, color):
    pygame.draw.aalines(screen, color, False, sin_points, 2)
    pygame.draw.aalines(screen, color, False, sin_points2, 2)
    pygame.display.flip()

#------------------------------------------------------------------------------------------------

White = [255, 255, 255]
Crimson = [128, 0, 0]
Blue = [0, 0, 128]               # colors
Black = [0, 0, 0]

#--------------------------------------------------------------------------------------------------

def main():
    screen.fill(White)
    pygame.draw.rect(screen, Black, [80, 5, 760, 520], 2) # main rect
    #-----------------------------------------------------------------------------------------------
    pygame.draw.rect(screen, Black, [80, 5, 760, 260], 2)
    pygame.draw.rect(screen, Black, [80, 5, 380, 520], 2)
    pygame.draw.line(screen, Black, [100, 5], [100, 525], 2)        # main lines
    pygame.draw.line(screen, Black, [820, 5], [820, 525], 2)
    pygame.draw.line(screen, Black, [80, 25], [840, 25], 2)
    pygame.draw.line(screen, Black, [80, 505], [840, 505], 2)
    #---------------------------------------------------------------------------------------------------

    for i in range(100, 760, 120):
        pygame.draw.aaline(screen, Black, [i, 5], [i, 525], 2)      # vertical lines
        #-----------------------------------------------------------------------------------------
        pygame.draw.aaline(screen, Black, [i+15, 5], [i+15, 10], 2)
        pygame.draw.aaline(screen, Black, [i+30, 5], [i+30, 15], 2)
        pygame.draw.aaline(screen, Black, [i+45, 5], [i+45, 10], 2)
        pygame.draw.aaline(screen, Black, [i+60, 5], [i+60, 19], 2)        # top dashes
        pygame.draw.aaline(screen, Black, [i+75, 5], [i+75, 10], 2)
        pygame.draw.aaline(screen, Black, [i+90, 5], [i+90, 15], 2)
        pygame.draw.aaline(screen, Black, [i+105, 5], [i+105, 10], 2)
        #-------------------------------------------------------------------------------------------
        pygame.draw.aaline(screen, Black, [i+15, 525], [i+15, 520], 2)
        pygame.draw.aaline(screen, Black, [i+30, 525], [i+30, 515], 2)
        pygame.draw.aaline(screen, Black, [i+45, 525], [i+45, 520], 2)
        pygame.draw.aaline(screen, Black, [i+60, 525], [i+60, 511], 2)       # bottom dashes
        pygame.draw.aaline(screen, Black, [i+75, 525], [i+75, 520], 2)
        pygame.draw.aaline(screen, Black, [i+90, 525], [i+90, 515], 2)
        pygame.draw.aaline(screen, Black, [i+105, 525], [i+105, 520], 2)
        #-----------------------------------------------------------------------------------------------

    for i in range(25, 480, 60):
        pygame.draw.aaline(screen, Black, [80, i], [840, i], 2)              # horizontal lines
        #---------------------------------------------------------------------------------------------
        pygame.draw.aaline(screen, Black, [80, i+15], [85, i+15], 2)
        pygame.draw.aaline(screen, Black, [80, i+30], [89, i+30], 2)            # right side dashes
        pygame.draw.aaline(screen, Black, [80, i+45], [85, i+45], 2)
        #-----------------------------------------------------------------------------------------------
        pygame.draw.aaline(screen, Black, [840, i+15], [835, i+15], 2)
        pygame.draw.aaline(screen, Black, [840, i+30], [831, i+30], 2)          # left side dashes
        pygame.draw.aaline(screen, Black, [840, i+45], [835, i+45], 2)
        #-------------------------------------------------------------------------------------------------
    screen.fill(White, [462, 27, 200, 58])     # place for sin and cos text
    #-------------------------------------------------------------------------------------------------------

    font = pygame.font.SysFont('timesnewroman', 15)
    nums = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
    for i, px in enumerate(range(15, 540, 60), 0):
        text = font.render(nums[i], True, Black)
        screen.blit(text, (40, px))

    text = font.render('-3                     -2                    -1', True, Black)
    screen.blit(text, (106, 308))

    radians_1 = ['-3π', '-2π', ' -π', '  0', '  π', ' 2π', ' 3π']
    font = pygame.font.SysFont('timesnewroman', 20)
    for i, px in enumerate(range(86, 840, 120), 0):
        text = font.render(radians_1[i], True, Black)
        screen.blit(text, (px, 530))                                                                    

    radians_2, symbs = ['5π', '3π', ' π', ' π', '3π', '5π'], ['- —', '- —', '- —', '  —', '  —', '  —']       # drawing nums and radians of the graph
    for i, px in enumerate(range(150, 840, 120), 0):                                    
        text1 = font.render(radians_2[i], True, Black)
        text2 = font.render(symbs[i], True, Black)
        divider = font.render('2', True, Black)
        screen.blit(text1, (px, 525))
        screen.blit(text2, (px-9, 533))
        screen.blit(divider, (px+7, 545))

    #--------------------------------------------------------------------------------------------------------

    font = pygame.font.SysFont('timesnewroman', 30)
    x_symb = font.render('χ', True, Black)
    screen.blit(x_symb, (453, 550))

    font = pygame.font.SysFont('Verdana', 20)
    sin_txt = font.render('sin x', True, Black)
    cos_txt = font.render('cos x', True, Black)                          # drawing sin&cos text
    cos_line = font.render('-----', True, Blue)
    screen.blit(sin_txt, (568, 25))
    pygame.draw.line(screen, Crimson, [625, 40], [665, 40], 2)
    screen.blit(cos_txt, (565, 50))
    screen.blit(cos_line, (625, 50))
    pygame.display.flip()

    #-------------------------------------------------------------------------------------------------
    font = pygame.font.SysFont('timesnewroman', 20)
    text = font.render("click to see the graphs", True, Black)
    pygame.draw.circle(screen, Crimson, (90, 610), 15)
    pygame.draw.circle(screen, Blue, (140, 610), 15)                                      # notes
    screen.blit(text, (30, 625))
    cleartxt = font.render("Press F to remove graphs", True, Black)
    screen.blit(cleartxt, (650, 600))
    pygame.display.update()
    #---------------------------------------------------------------------------------------------------


main()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
    
            sqx1 = (x - 90)**2
            sqy1 = (y - 610)**2
            sqx2 = (x - 140)**2
            sqy2 = (y - 610)**2

            if (sqx1 + sqy1)**0.5 < 15 and not is_clicked_sin:
                sin_graph(sin_points, Crimson)
                is_clicked_sin = True
            elif (sqx2 + sqy2)**0.5 < 15 and not is_clicked_cos:
                cos_graph(cos_points, Blue)
                is_clicked_cos = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            is_clicked_sin, is_clicked_cos = False, False
            main()