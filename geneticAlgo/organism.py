# Aritra Roy Gosthipaty
# this module deals with the building of an organism

from random import randint
from random import random


# returns a new Caps Charater only
def newChar():
	c=randint(63,122)
	if c == 63 :
		c=32
	if c == 64:
		c=46	
	return chr(c)



# class for an organism		
class Organism:

	# constructor
	def __init__(self,num):
		self.num=num
		# num here is the number of genes of the organism
		self.genes=[]
		# this is a list for all the genes of the organism
		self.fitness=0
		# every organism has a fitness associated with it
		for i in range(0,num):
			self.genes.append(newChar())

	# calculates the fitness of the organism
	def fitnessFunction(self,target):
		count=0
		for i in range(0,self.num):
			if self.genes[i] == target[i]:
				count+=1
		self.fitness=(count/self.num)*100

	#this is the crossover to make a child method 
	def crossover(self,partner):
		child=Organism(self.num)
		midpoint=randint(0,self.num-1) 
		# randint(a,b) a<=value<=b
		for i in range(self.num):
			if i <= midpoint:
				child.genes[i]=(self.genes[i])
			else:
				child.genes[i]=(partner.genes[i])
		return child
	
	#mutates the child with a mutation rate 
	def mutation(self,mutationRate):
		for i in range(0,self.num):
			if random() < mutationRate:
				self.genes[i]=newChar()