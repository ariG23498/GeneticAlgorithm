import dna
import population
num=200
m=0.1
target=['P','0','P','C','0','R','N']
pop=population.Population(target,m,num)
while pop.finished != True:
	pop.naturalSelection()
	pop.generate()
	# pop.calcFitness()
	pop.evaluate()
