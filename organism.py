# This module deals with the building of an individual organism

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
	def __init__(self,num_of_genes):
		self.num_of_genes=num_of_genes
		# num_of_genes signifies the number of genes in the organism
		self.genes=[]
		# this is a list for all the genes of the organism
		self.fitness=0
		# every organism has a fitness associated with it
		for idx in range(num_of_genes):
			self.genes.append(newChar())

	# calculates the fitness of the organism
	def fitnessFunction(self,target):
		count=0
		for idx in range(self.num_of_genes):
			if self.genes[idx] == target[idx]:
				count+=1
		self.fitness=(count/self.num_of_genes)*100
		# This helps in converting the fitness to a probability percentage

	#this is the crossover to make a child method 
	def crossover(self,partner):
		child=Organism(self.num_of_genes)
		midpoint=randint(0,self.num_of_genes-1) 
		# randint(a,b) a<=value<=b
		for idx in range(self.num_of_genes):
			if idx <= midpoint:
				child.genes[idx]=(self.genes[idx])
			else:
				child.genes[idx]=(partner.genes[idx])
		return child
	
	#mutates the child with a mutation rate 
	def mutation(self,mutationRate):
		for i in range(self.num_of_genes):
			# Each individual gene is subject to mutation
			if random() < mutationRate:
				self.genes[i]=newChar()