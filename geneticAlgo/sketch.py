import population
phrase="to be or not to be that is the question."
target=[i for i in phrase]
# print(target)
num=len(target)
size=200
mutationRate=0.1
pop=population.Population(target,mutationRate,size)

while not(pop.finished):
	pop.naturalSelection()
	pop.generate()
	pop.evaluate()