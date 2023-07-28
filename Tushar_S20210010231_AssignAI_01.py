import random

def algo_genetic_fitness(res_genetic_algo):
    temp_var = int(res_genetic_algo, 2)
    return temp_var ** 2

def algo_genetic_population_select(sampleCollections, k=2):
    return max(random.sample(sampleCollections, k), key=algo_genetic_fitness)

def single_cross_newChild(node_guardian1, node_guardian2):
    particularNode = random.randint(1, len(node_guardian1) - 1)
    firstChild_geneticAlgo = node_guardian1[:particularNode] + node_guardian2[particularNode:]
    secondChild_geneticAlgo = node_guardian2[:particularNode] + node_guardian1[particularNode:]
    return firstChild_geneticAlgo, secondChild_geneticAlgo

def double_cross_newChild(node_guardian1, node_guardian2):
    particularNode1 = random.randint(1, len(node_guardian1) - 1)
    particularNode2 = random.randint(1, len(node_guardian1) - 1)
    if particularNode2 < particularNode1:
        particularNode1, particularNode2 = particularNode2, particularNode1
    firstChild_geneticAlgo = node_guardian1[:particularNode1] + node_guardian2[particularNode1:particularNode2] + node_guardian1[particularNode2:]
    secondChild_geneticAlgo = node_guardian2[:particularNode1] + node_guardian1[particularNode1:particularNode2] + node_guardian2[particularNode2:]
    return firstChild_geneticAlgo, secondChild_geneticAlgo

def crossingByBitManupulating(res_genetic_algo, pm=0.1):
    var_temp_mutate = ""
    for eachBit in res_genetic_algo:
        if random.random() < pm:
            var_temp_mutate += "0" if eachBit == "1" else "1"
        else:
            var_temp_mutate += eachBit
    return var_temp_mutate

def crossingBySwapping(res_genetic_algo, pm=0.1):
    var_temp_mutate = list(res_genetic_algo)
    for i in range(len(var_temp_mutate)):
        if random.random() < pm:
            j = random.randint(0, len(var_temp_mutate) - 1)
            var_temp_mutate[i], var_temp_mutate[j] = var_temp_mutate[j], var_temp_mutate[i]
    return "".join(var_temp_mutate)

def main_genetic_algorithm_function(p, c=0, m=0, t=0, x=10, i=100):
    sampleCollections = ["".join([random.choice(["0", "1"]) for _ in range(5)]) for _ in range(p)]
    requiredResult = max(sampleCollections, key=algo_genetic_fitness)
    modificationNum = 0
    for generation in range(i):
        node_guardian1 = algo_genetic_population_select(sampleCollections)
        node_guardian2 = algo_genetic_population_select(sampleCollections)
        if c == 0:
            firstChild_geneticAlgo, secondChild_geneticAlgo = single_cross_newChild(node_guardian1, node_guardian2)
        else:
            firstChild_geneticAlgo, secondChild_geneticAlgo = double_cross_newChild(node_guardian1, node_guardian2)
        if m == 0:
            firstChild_geneticAlgo = crossingByBitManupulating(firstChild_geneticAlgo)
            secondChild_geneticAlgo = crossingByBitManupulating(secondChild_geneticAlgo)
        else:
            firstChild_geneticAlgo = crossingBySwapping(firstChild_geneticAlgo)
            secondChild_geneticAlgo = crossingBySwapping(secondChild_geneticAlgo)
        child1_fitness = algo_genetic_fitness(firstChild_geneticAlgo)
        child2_fitness = algo_genetic_fitness(secondChild_geneticAlgo)
        if child1_fitness > child2_fitness:
            if child1_fitness > algo_genetic_fitness(sampleCollections[-1]):
                sampleCollections[-1] = firstChild_geneticAlgo
        else:
            if child2_fitness > algo_genetic_fitness(sampleCollections[-1]):
                sampleCollections[-1] = secondChild_geneticAlgo
        if algo_genetic_fitness(sampleCollections[-1]) > algo_genetic_fitness(requiredResult):
            requiredResult = sampleCollections[-1]
            modificationNum = 0
        else:
            modificationNum += 1
        if t == 0 and modificationNum >= x:
            break
        elif t == 1 and generation == i - 1:
            break
    return requiredResult

x=10;
i=100;
p=int(input("Enter the value of p: "))
c=int(input("press either 0 or 1 for the value of c: "))
m=int(input("press either 0 or 1 for the value of m: "))
t=int(input("press either 0 or 1 for the value of t: "))  
if t==0:
    x=int(input("Enter the value of x: "))
else:
    i=int(input("Enter the value of i: "))

requiredOutput = main_genetic_algorithm_function(p,c,m,t,x,i);

print("Highest fitness value solution : "+requiredOutput);
