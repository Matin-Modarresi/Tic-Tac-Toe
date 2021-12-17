import pygame,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowSize = pygame.display.get_desktop_sizes()
#windowSize = [(800,800)]
length = 500
width = 10
space=length/6
selected_cell=[]
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


def game_board(win,row,col,shape):
	global windowSize,length,width,mid_length,mid_width

	for i in range(4):
		pygame.draw.rect(win,(9,234,150),(mid_length_hor,cell_hor[i],length,width))
		pygame.draw.rect(win,(9,234,150),(cell_ver[i],mid_length_ver,width,length))

	if shape == 1:
		radius = 60
		pygame.draw.circle(win,(255,255,255),(cell_ver[col]+space,cell_hor[row]+space),radius,10)
	if shape==0:
		length=30
		pygame.draw.line(win,(255,255,255),(cell_ver[col]+length,cell_hor[row]+length),(cell_ver[col+1]-length,cell_hor[row+1]-length),15)
		pygame.draw.line(win,(255,255,255),(cell_ver[col]+length,cell_hor[row+1]-length),(cell_ver[col+1]-length,cell_hor[row]+length),15)



def click_on_cell(win):
	pass
	for i in range(3):#cell_hor
		for j in range(3):#cell_ver
			if cell_hor[i] < pygame.mouse.get_pos()[1] < cell_hor[i+1] and cell_ver[j] <pygame.mouse.get_pos()[0]< cell_ver[j+1] and pygame.mouse.get_pressed()[0]:
				if (i,j) in selected_cell:
					continue
				else:
					selected_cell.append((i,j))
					return i , j

	
	



	