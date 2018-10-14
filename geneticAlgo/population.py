import dna
from random import randint

def mapping(value,leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = float(leftMax - leftMin)
    rightSpan = float(rightMax - rightMin)

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

class Population:
	def __init__(self,p,m,num):
		self.population=[]
		self.size=num
		self.matingPool=[]
		self.generations=0
		self.finished=False
		self.target=p
		self.mutationRate=m
		self.perfectScore=100
		for i in range(0,num):
			self.population.append(dna.Organism(len(self.target)))
		self.matingPool=[]	
		self.calcFitness()

	def calcFitness(self):
		for i in self.population:
			i.fitnessFunction(self.target)
	
	def naturalSelection(self):
		self.matingPool=[]
		maxFitness=0
		for i in self.population:
			if maxFitness < i.fitness:
				maxFitness=i.fitness
		for i in self.population:
			fitMap=mapping(i.fitness,0,maxFitness,0,1)
			n=int(fitMap*100)
			for j in range(0,n+1):
				self.matingPool.append(i)

	def generate(self):
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


	def evaluate(self):
		worldRecord=0.0
		index=0
		for i in range(0,self.size):
			if self.population[i].fitness > worldRecord :
				index = i
				worldRecord = self.population[i].fitness
		print("BEST ",self.population[index].genes)
		print("BEST FITNESS ",worldRecord)
		print("GENERATION",self.generations)
		if int(worldRecord) == self.perfectScore :
			self.finished=true
