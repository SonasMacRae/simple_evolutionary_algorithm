# Author: Sonas MacRae
# Date: 15/08/2019
# First evoultionary computing script

import random
import matplotlib.pyplot as plt

digits = [128,64,32,16,8,4,2,1]


# Initialises the population with binary strings between the values of 0 and 5
def InitPopulation():
    population = []

    for x in range(10):
        value = DecimalToBinary(random.randint(0,5))
        population.append(value)

    return population


# Converts a decimal number to its equivalent 8 digit binary string
# Doesn't work for decimal numbers over 255 or those below 0
def DecimalToBinary(decimal):
    temp = decimal
    output = ""

    for x in digits:
        if temp < x:
            output += "0"

        if temp >= x:
            temp -= x
            output += "1"

    return output


# Converts an 8 digit binary string to its decimal equivalent
def BinaryToDecimal(binary):
    temp = str(binary)
    counter = 0
    output = 0

    for x in temp:
        if x == "1":
            output += digits[counter]

        counter += 1

    return output


# Creates 2 child binary strings from 2 existing binary strings
# by taking attributes from both parents
def CrossOver(parent1, parent2):

    child1 = ""
    child2 = ""

    rng = random.randint(1,7)

    for x in range(rng):

        child1 += parent1[x]
        child2 += parent2[x]

    for y in range(rng,8):
        child1 += parent2[y]
        child2 += parent1[y]

    offsprings = (child1, child2)

    return offsprings


# Mutates binary strings by randomly changing one of its values
def Mutate(individual):
    rng = random.randint(0,7)

    individual = list(individual)

    if individual[rng] == "0":
        individual[rng] = "1"

    else:
        individual[rng] = "0"

    individual = "".join(individual)

    return individual


# Gets rid of the weakest individuals (although there should be a chance
# that the weak survive, this is not optimal)
def Selection(population):
    population.sort()

    for x in range(10):
        del population[x]

    return population


# Prints information about the current state of the population
def Info(population, counter):
    total = 0
    biggest = 0
    mean = 0

    for x in population:
        total += BinaryToDecimal(x)
        if BinaryToDecimal(x) > biggest:
            biggest = BinaryToDecimal(x)

    mean = total/10

    print("Generation: ", counter)
    print("The total value is: ", total)
    print("The mean value is: ", mean)
    print("The highest value of this generation is: ", biggest, "\n")

    return mean


# Plots a line graph of the mean score of each generation
def Graph(scores):
    generation = []
    meanScores = []

    for x in range(10):
        generation.append(x + 1)

    for x in scores:
        meanScores.append(x)

    plt.title('Stats of algorithm')
    plt.xlabel('Generation')
    plt.ylabel('Mean score of generation')

    plt.plot(generation,meanScores)

    plt.show()


def App():
    stats = []
    population = InitPopulation()

    for g in range(10):

        stats.append(Info(population,g))

        tempList = []

        # Lists used to select the parents of the next generation
        temp = []
        list1 = []
        list2 = []

        for x in population:
            temp.append(x)

        # Randomly assorts the individuals from the population into 2 lists
        # Parents are pared up based on their corresponding indexes between
        # the lists
        for x in range(9):
            rng = random.randint(0,len(temp)-1)
            list1.append(temp[rng])

            rng = random.randint(0,len(temp)-1)
            list2.append(temp[rng])

        # Crossover stage
        for y in range(len(list1)):
            tempTuple = CrossOver(list1[y],list2[y])
            tempList.append(tempTuple[0])
            tempList.append(tempTuple[1])

            # Mutates each new individual
            for z in range(len(tempList)):
                tempList[z] = Mutate(tempList[z])

        # Adds all of the new individuals to the population
        for y in tempList:
            population.append(y)

        # Selection stage, removes the weak individuals from the population
        population = Selection(population)

    print(stats)
    Graph(stats)


App()
