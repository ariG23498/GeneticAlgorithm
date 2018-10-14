import organism
phrase="to be or not to be that is the question."
target=[i for i in phrase]
num=len(target)
mutationRate=0.1
word1=organism.Organism(num)
print("GENES OF WORD1=",word1.genes)
word2=organism.Organism(num)
print("GENES OF WORD2=",word2.genes)
word1.fitnessFunction(target)
print("FITNESS OF WORD1=",word1.fitness)
word2.fitnessFunction(target)
print("FITNESS OF WORD2=",word2.fitness)
childWord=word1.crossover(word2)
print("GENES OF CHILDWORD=",childWord.genes)
childWord.fitnessFunction(target)
print("FITNESS OF CHILDWORD=",childWord.fitness)
childWord.mutation(mutationRate)
print("GENES OF CHILDWORD AFTER MUTATION=",childWord.genes)