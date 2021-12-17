import pygame,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowSize = pygame.display.get_desktop_sizes()
length = 500
width = 10
space=length/6

mids = [(windowSize[0][0]-length)/2,(windowSize[0][1]-width)/2,(windowSize[0][1]-length)/2,
		(windowSize[0][0]-width)/2]

mid_length_hor = (windowSize[0][0]-length)/2
mid_width_hor = (windowSize[0][1]-width)/2
mid_length_ver = (windowSize[0][1]-length)/2
mid_width_ver = (windowSize[0][0]-width)/2


cell= [[None for i in range(3)]for j in range(3)]
cell_hor=[];cell_ver=[]

for line,i in zip(range(-3,4,2),range(4)):
	cell_hor.append(mid_width_hor+space*line)
	cell_ver.append(mid_width_ver+space*line)

#for line,i in zip(range())		


def game_board(win,col,row,shape):
	global windowSize,length,width,mid_length,mid_width

	for i in range(4):
		pygame.draw.rect(win,(9,234,150),(mid_length_hor,cell_hor[i],length,width))
		pygame.draw.rect(win,(9,234,150),(cell_ver[i],mid_length_ver,width,length))

	if shape == 1:
		radius = 60
		pygame.draw.circle(win,(255,255,255),(cell_ver[row]+space,cell_hor[col]+space),radius,10)
	else:
		length=30
		pygame.draw.line(win,(255,255,255),(cell_ver[row]+length,cell_hor[col]+length),(cell_ver[row+1]-length,cell_hor[col+1]-length),15)
		pygame.draw.line(win,(255,255,255),(cell_ver[row]+length,cell_hor[col+1]-length),(cell_ver[row+1]-length,cell_hor[col]+length),15)

	#pygame.draw.rect(win,(9,234,150),(mid_length_hor,cell_hor[1],length,width))
	#pygame.draw.rect(win,(9,234,150),(mid_length_hor,cell_hor[2],length,width))
	#pygame.draw.rect(win,(9,234,150),(cell_ver[1],mid_length_ver,width,length))
	#pygame.draw.rect(win,(9,234,150),(cell_ver[2],mid_length_ver ,width,length))

	

	

	