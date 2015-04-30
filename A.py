import random
S=0
game=[]
count=0


	
	

for i in range(15*35):
	game.append(".")






def begin():
	global count
	count=0
	for i in range(25):
		a=random.randint(0,15*35 - 1)
		game[a]="C"
		


begin()
for i in range(35):
	game[i]="X"

for i in range(15*35):
	if (i % 35) == 0:
		game[i]="X"
	elif (i%35) == 34:
		game[i]="X"

for i in range(14*35,15*35):
	game[i]="X"





for j in range(22):
	b=random.randint(0,15*35 - 1)
	if game[b]=="C":
		game[b+1]="X"
	else:
		game[b]="X"









posp=0
posg=0
pospo=0

class Person:
	
	def __init__(self):
		self.pos=random.randint(0, 15*35 - 1)

	def get_position(self):
		return self.pos



class Pacman(Person):
	

	
	def __init__(self):
		global pospo
		global game
		Person.__init__(self)
		pospo=Person.get_position(self)
		if game[pospo]=="X":
			self.__init__()
		else:
			game[pospo]="P"
		

	
		
	
	def mov (self):
		global posp
		global pospo
		print "move:",
		
		move=raw_input().lower()
		
		

		if move=="w" and pospo >= 35:
			posp=pospo-35
			return True
		elif move=="s" and pospo > 35*14:
			posp=pospo
			return True	
		elif move=="s" and pospo <= 35*14:
			posp=pospo+35
			return True
		elif move=="d" :
			posp=pospo+1
			return True
		elif move=="a" :
			posp=pospo-1
			return True
		elif move=="q":

			return False
		
		else:
			return 2
				


	


	def collectcoin(self):
		global posp
		global game
		global pospo
		global S
		global count
		if game[posp]=="C":
			game[posp]="P"
			S = S + 1
			count=count-1
			
		
			game[pospo]="."
			pospo=posp
			return True
		return False
		
			
		


	def checkWall(self):
		global posp
		global game
	
		global pospo
		if game[posp]!="X":
			game[posp]="P"
			game[pospo]="."
			
			pospo=posp
			return True
		return False
		
			
		


	def checkghost(self):
		global posp
		global posg
		if posp==posg:
			return True

	
			

			


class Ghost(Person):

	def __init__(self):
		global posg
		global game
		Person.__init__(self)	
	def _ghost_position(self):
		global posg
		global game
		posg=Person.get_position(self)
		if game[posg]=="X":
			self.__init__()
			self._ghost_position()
		else:
			game[posg]="G"

	
	def __randmove__(self):
		global posg
		global game
	
		k=random.sample([1,-1,35,-35],1)
		n=k[0]

		if posg > 35 and posg < 14*35:
			if game[posg+n]=="X":
				self.__randmove__()	
			else:
				game[posg+n]="G"
				game[posg]="."
				posg=posg+n
			

		if posg < 35 and n==-35:
			if game[posg+35]=="X":
				self.__randmove__()
			else:
				game[posg+35]="G"
				game[posg]="."
				posg=posg+35

		
		if posg > 14*35 and n==35:
			if game[posg-35] == "X":
				self.__randmove__()
			else:
				game[posg-35]="G"
				game[posg]="."
				posg=posg-35


		if posg == 15*35 - 1 and n==1:
			if game[posg-35] == "X":
				self.__randmove__()
			else:
				game[posg-35]="G"
				game[posg]="."
				posg=posg-35

	
		
def prin():
	global S

	
	for m in range(15*35):
		if m%35==0:
			print "\n"
		
		print game[m],
	
	print "\n"
	print "score:",S


#begin()


P=Pacman()
G=Ghost()
G._ghost_position()

def count1():
	global game
	global count
	for i in range(15*35):
		if game[i]=="C":
			count=count+1
		


count1()
while True:
		
	prin()
	a =P.mov()
	if a== False:
		break
	elif a==2:
		continue
		
	
	
	b=P.collectcoin()
	if b==False:
		P.checkWall()
	G.__randmove__()
	
	if P.checkghost() == True:
		break
	
	prin()
	if count==0:
		begin()
		count1()
		
		
		


prin()
	
	


