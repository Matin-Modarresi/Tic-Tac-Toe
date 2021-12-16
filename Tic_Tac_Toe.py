import copy
import coordinates as cor
import os
game_board = [['-' for i in range(3)]for j in range(3)]

def print2d(arr):
	for i in arr:
		print(*i,sep=' ')




class Node:
	def __init__(self,map):

		self.leaves=[]
		self.rows=[]
		self.value=0
		self.map=map
		self.row=0
		self.col=0
		self.status = 0
		
		self.detail_val ={ 'nozoli':0 , 'soudi':0, 'ofoghi':0 , 'amoodi':0}




	def printTree_bfs(self,file):

		for j in self.leaves:

			file.write(f"{round(j.value,2):<6}"+' '*10)
			print(f"{round(j.value,2):<6}",end=' '*10)
		
		file.write('\n')
		print()

		for i in self.detail_val:
			for j in self.leaves:
		
				file.write(f"{i:<6}"+str(j.detail_val[i])+' \t')
				print(f"{i:<6}",j.detail_val[i],end=' \t')
			print()
			file.write('\n')
			
		for i in range(3):
			for j in self.leaves:
				print(*j.map[i],end=' '*11)
		
				for letter in j.map[i]:
					file.write(letter+' ')
				file.write(' '*10)
		
			file.write('\n')
			print()


		

def MAX(self,index=0,row=0,col=0):
	global last_level,stop_turn
	stop = stop_condition(self,row,col)
	
	self.row = row
	self.col = col

	

	if stop==1: 
		self.value/=index
		return 1

	if stop==-1:
		self.value/=index
		return -1
	

	if index==stop_turn:
		last_level+=1
		return 0


	map_copy=[]
	
	#print2d(self.map)
	#print()
	
	for i in range(3):
		for j in range(3):

			if self.map[i][j] != '-':
				continue

			map_copy  = copy.deepcopy(self.map)


			if index%2==0:
				map_copy[i][j]='x'
			else:
				map_copy[i][j]='o'

			
			self.leaves.append(Node(map_copy))
			MAX(self.leaves[-1],index+1,i,j)
			
			#if ignore==1 or ignore==-1:
			#	break;


	if index%2==0:
		maximum = -1000000*state_turn
		if len(self.leaves)==0:
			maximum=0

		for i in self.leaves:	
			if i.value*state_turn > maximum*state_turn:
				maximum = i.value
		
		self.value+=maximum
	
	else:
		minimum = 1000000*state_turn
		if len(self.leaves)==0:
			minimum=0

		for i in self.leaves:
			if i.value*state_turn < minimum*state_turn:
				minimum=i.value
	
		self.value+=minimum


def stop_condition(self,row,col):
	global state_turn
	value=0
	range_  = [
			   [ [(row,row+3),(col,col+3)]      ,[(row-1,row-3,-1),(col-1,col-3,-1)] ],
			   [ [(row,row-3,-1),(col,col+3)]   ,[( row+1,row+3),(col-1,col-3,-1)]   ],
			   [ [(row,row+3),col]				,[(row-1,row-3,-1),col]				 ],
			   [ [row,(col,col+3)]				,[row,(col-1,col-3,-1)]				 ]
			  ]


	for i in range_:
		count = 0
		check = None
		self.value=0
		

		for j in i:
			check_=False
			if i==range_[0] or i==range_[1]:
				for n,m in zip(range(*j[0]),range(*j[1])):
					condition,count,check,check_ = conditions(self,n,m,count,check,check_)
					if not condition:
						break

				if i==range_[0]:
					self.detail_val['nozoli']=self.value

					
				else:
					self.detail_val['soudi'] =self.value
			
					

			
			if i==range_[2]:
				for n in range(*j[0]):
					condition,count,check,check_ = conditions(self,n,j[1],count,check,check_)
					if not condition:
						break

				self.detail_val['amoodi'] =self.value
	
				


			if i==range_[3]:
				for m in range(*j[1]):
					condition,count,check,check_ = conditions(self,j[0],m,count,check,check_)
					if not condition:
						break

				self.detail_val['ofoghi'] =self.value
				
				

		
		value+=self.value

		

		if count>=3:
			self.status = 1
			self.value+=1000
			return 1

		if count<=-3:
			self.status =-1
			self.value-=1000
			return -1

	self.value=value
	return 0



def conditions(self,row,col,count,check,check_):
	global state_turn
	
	
	if row>=3 or col>=3 or row<=-1 or col<=-1:
		return False,count,check,check_


	if self.map[row][col]=='-':
		if not check_:
			check_=True
		if check=='x':
			self.value +=.5*state_turn
		else:
			self.value-=.5*state_turn





	if self.map[row][col]=='x':

		if check==None or check=='x':
			if check_:
				self.value+=1*state_turn
			else:
				count+=1*state_turn
				self.value+=1*state_turn
				check='x'

		if check=='o':
			return False,count,check,check_

	
	
	if self.map[row][col]=='o':

		if check==None or check=='o':
			if check_:
				self.value-=1*state_turn
			else:
				count-=1*state_turn
				self.value-=1*state_turn
				check='o'

		if check=='x':
			return False,count,check,check_

	return True,count,check,check_


column=None ; row=None

last_level=0
turn = 0
stop_turn=6
stop=0

game_finished = False



process = open('Process.txt','w')



state_turn=-1
state_difficulty = -1
	

while not game_finished:
	
	tree=Node(game_board)
	MAX(tree,turn)


	if turn%2==1:	
		maximum=-1000000*state_difficulty
		
		for i,index in zip(tree.leaves,range(len(tree.leaves))):
			if i.value*state_difficulty>maximum*state_difficulty:
				maximum=i.value
				index_max=index
			
		
		process = open('Process.txt','a',buffering=1)
		
		process.write('index_max '+str(index_max)+'\n')
		process.write(str(tree.leaves[index_max].row)+ ' ' +str(tree.leaves[index_max].col)+'\n')

	

		process.write('\n')

		for i in tree.leaves[index_max].map:
			for j in i:
				process.write(str(j)+' ')
			process.write('\n')

		process.write('\n')
		
		print()
		print(index_max)
		
		print(tree.leaves[index_max].row,tree.leaves[index_max].col)
		
		print2d(tree.leaves[index_max].map)

		if tree.leaves[index_max].status==1:
			print("you lose")
			process.close()
			game_finished = True
			break

		print()
		process.write('\n')

		tree.printTree_bfs(process)
		
		print()

		process.write('\n')

		tree.leaves[index_max].printTree_bfs(process)

		process.write('\n'+'#'*165+'\n')

		print()
		
		tree=tree.leaves[index_max]

	else:
		cor.gotoxy(0,0)
		print('select a column: ',end='')

		
		column=int(input())
		

		
		os.system('cls')

		if tree.leaves[column].status == -1:
			print('you win')
			process.close()
			#esm.send_email('Process.txt','Process.txt',0)

			game_finished = True
			break

		tree=tree.leaves[column]		

	game_board=copy.deepcopy(tree.map)
	turn+=1

	stop_turn=6+turn