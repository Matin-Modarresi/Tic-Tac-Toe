import pygame,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import time
#import Tic_Tac_Toe as tic

pygame.init()
clock=pygame.time.Clock()
windowSize = pygame.display.get_desktop_sizes()
#windowSize = [(800,800)]
length = 500
width = 10
space=length/6
selected_cell=[]


mid_length_hor = (windowSize[0][0]-length)/2
mid_width_hor = (windowSize[0][1]-width)/2
mid_length_ver = (windowSize[0][1]-length)/2
mid_width_ver = (windowSize[0][0]-width)/2


#cell= [[None for i in range(3)]for j in range(3)]
cell_hor=[];cell_ver=[]

for line,i in zip(range(-3,4,2),range(4)):
	cell_hor.append(mid_width_hor+space*line)
	cell_ver.append(mid_width_ver+space*line)

#for line,i in zip(range())		


def game_board(win,row,col,shape):
	global windowSize,length,width,mid_length,mid_width

	for i in range(1,3):
		pygame.draw.rect(win,(9,234,150),(mid_length_hor,cell_hor[i],length,width))
		pygame.draw.rect(win,(9,234,150),(cell_ver[i],mid_length_ver,width,length))

	if shape == 1:
		radius = 60
		pygame.draw.circle(win,(255,255,255),(cell_ver[col]+space,cell_hor[row]+space),radius,10)
	if shape==0:
		len_line=30
		pygame.draw.line(win,(255,255,255),(cell_ver[col]+len_line,cell_hor[row]+len_line),(cell_ver[col+1]-len_line,cell_hor[row+1]-len_line),15)
		pygame.draw.line(win,(255,255,255),(cell_ver[col]+len_line,cell_hor[row+1]-len_line),(cell_ver[col+1]-len_line,cell_hor[row]+len_line),15)



def click_on_cell(win):
	
	for i in range(3):#cell_hor
		for j in range(3):#cell_ver
			if cell_hor[i] < pygame.mouse.get_pos()[1] < cell_hor[i+1] and cell_ver[j] <pygame.mouse.get_pos()[0]< cell_ver[j+1] and pygame.mouse.get_pressed()[0]:
				if (i,j) in selected_cell:
					continue
				else:
					selected_cell.append((i,j))
					return i , j

	


len_rect = 105
width_rect = 45

def click_on_difficulty(win,x,y,state_diff,state_turn,start):

	basicFont = pygame.font.SysFont("Times New Roman", 40)
	
	if state_diff==1:
		text_diff = basicFont.render(' Hard', True,(255,0,0))
	else:
		text_diff = basicFont.render(' Easy', True,(255,0,0))


	if state_turn==1:
		text_turn = basicFont.render('Turn 2', True,(255,0,0))
	else:
		text_turn = basicFont.render('Turn 1', True,(255,0,0))

	text_start = basicFont.render(' Start', True,(255,255,255))

	button_diff = pygame.draw.rect(win,(255,255,255),(x,y,len_rect,width_rect),border_radius=5)
	button_turn = pygame.draw.rect(win,(255,255,255),(x,y+100,len_rect,width_rect),border_radius=5)
	button_start = pygame.draw.rect(win,(0,255,0),(x,y+200,len_rect,width_rect),border_radius=5) 
	win.blit(text_diff,(x,y))	
	win.blit(text_turn,(x,y+100))
	win.blit(text_start,(x,y+200))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = event.pos  # gets mouse position

			if button_diff.collidepoint(mouse_pos):
				#print(-state_diff)
				state_diff=-state_diff

			if button_turn.collidepoint(mouse_pos):
				#print(-state_turn)
				state_turn=-state_turn
				
			if button_start.collidepoint(mouse_pos):
				start=-start

			return state_diff,state_turn,start


def show_result(win,str,color):
	basicFont = pygame.font.SysFont("Times New Roman", 100)
	text = basicFont.render(str, True,color,(255,255,255))
	#pygame.draw.rect(win,(255,255,255),(windowSize[0][0]//2-2*space, windowSize[0][1]// 2-space,text.get_rect()[2],text.get_rect()[3]),border_radius=5)
	#textRect = text.get_rect()
	#textRect.center = (windowSize[0][0]//2, windowSize[0][1]// 2)
	win.blit(text,(windowSize[0][0]//2-2*space, windowSize[0][1]// 2-space))	