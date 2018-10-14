from random import randint
from random import uniform

def newChar():
	c=chr(randint(65,90))
	return c	

class Organism:
	def __init__(self,num):
		self.num=num
		self.genes=[]
		self.fitness=0
		for i in range(0,num):
			self.genes.append(newChar())

	def getPhrase(self):
		self.genes=''.join(self.genes)

	def fitnessFunction(self,target):
		count=0
		for i in range(0,self.num):
			if self.genes[i] == target[i]:
				count+=1
		self.fitness=(count/self.num)*100

	def crossover(self,partner):
		child=Organism(self.num)
		midpoint=randint(0,self.num-1)
		for i in range(self.num):
			if i <= midpoint:
				child.genes[i]=(self.genes[i])
			else:
				child.genes[i]=(partner.genes[i])
		return child
					
	def mutation(self,mutationRate):
		for i in range(0,self.num):
			if uniform(0,1) < mutationRate:
				self.genes[i]=newChar()