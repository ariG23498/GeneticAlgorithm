# Genetic Algorithm

This code base is built for the basic understanding of the Genetic Algorithm. The problem statement is to evolve characters and finally obtain a valid word. The optimization takes place with the help of evolution. The [video series of GA](https://youtu.be/9zfeTw-uFCw) has helped me understand the concepts to a great extent.

The three key points to remember are:
1. Heridity - Crossover
2. Variation - Mutation
3. Selection - Natural Selection

To achieve the desired results here is the mental map of the procedures:
1. Create a population with random genetic material.
2. Calculate the fitness of each of the individuals in the population.
    1. Choose `2` parents with respect to the probability.
    2. Crossover the genetic material. (Choice of procedure to crossover is subject to further inspection)
    3. Mutate the genetic material of the off spring. (The probability of mutation is subject to further retrospection)