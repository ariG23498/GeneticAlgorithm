import organism
phrase = input('Input a phrase as the target: ')
target = [ch for ch in phrase]
num_of_genes = len(target)
mutationRate = 0.1

print('*'*40)

word1=organism.Organism(num_of_genes)
print('GENES OF WORD1=',word1.genes)

word1.fitnessFunction(target)
print('FITNESS OF WORD1=',word1.fitness)

print('*'*40)

word2=organism.Organism(num_of_genes)
print('GENES OF WORD2=',word2.genes)

word2.fitnessFunction(target)
print('FITNESS OF WORD2=',word2.fitness)

print('*'*40)

childWord=word1.crossover(word2)
print('GENES OF CHILDWORD=',childWord.genes)

childWord.fitnessFunction(target)
print('FITNESS OF CHILDWORD=',childWord.fitness)

childWord.mutation(mutationRate)
print('GENES OF CHILDWORD AFTER MUTATION=',childWord.genes)