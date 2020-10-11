import organism
from random import randint
from random import random

# class for creating a population
class Population:

	# constructor
	def __init__(self,target,mutationRate,size):
		# this is the list of all the organisms in a generation
		self.population=[]
		# matingPool of the population
		self.matingPool=[]
		# the size of a population
		self.size=size
		# this is the generation of the population
		self.generations=0
		# this takes care of the termination
		self.finished=False
		# this is the target that needs to match
		self.target=target
		self.mutationRate=mutationRate

		# creating the first population GENERATION 1
		for i in range(self.size):
			self.population.append(organism.Organism(len(self.target)))	
		# calculates the fitness of all the organisms
		self.calcFitness()

	def calcFitness(self):
		for i in self.population:
			i.fitnessFunction(self.target)
	
	# to select and mate according to an algorithm
	def naturalSelection(self):
		# creating a matingPool
		self.matingPool=[]
		maxFitness=0
		
		# to get the maxFitness
		for i in self.population:
			if maxFitness < i.fitness:
				maxFitness=i.fitness
		if maxFitness != 0.0:
			for i in self.population:
				fitness=(i.fitness)/(maxFitness)
				n=round(fitness*100)
				for j in range(n):
					self.matingPool.append(i)
		else:
			for i in self.population:
				self.matingPool.append(i)

	# genrate the children and place them in the previous generation to make new generation
	def generate(self):
		# create children with pairs
		for i in range (0,self.size):
			a=randint(0,len(self.matingPool)-1)
			b=randint(0,len(self.matingPool)-1)
			A=self.matingPool[a]
			B=self.matingPool[b]
			child=A.crossover(B)
			child.fitnessFunction(self.target)
			child.mutation(self.mutationRate)
			child.fitnessFunction(self.target)
			self.population[i]=child
		self.generations+=1

	# evaluates the whole generation's fitness
	def evaluate(self):
		worldRecord=0.0
		index=0
		for i in range(0,self.size):
			if self.population[i].fitness > worldRecord :
				index = i
				worldRecord = self.population[i].fitness
		printBest=''.join(self.population[index].genes)		
		print("BEST ",printBest)
		print("BEST FITNESS ",worldRecord)
		print("GENERATION",self.generations)
		if worldRecord == 100.0 :
			self.finished=True