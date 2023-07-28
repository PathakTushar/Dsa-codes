from itertools import permutations

def algoForConstraintSatisfactionAlgorithm(arrayOfStrings, string):
    differentCharInSets = set()
    for eachWord in arrayOfStrings:
        differentCharInSets.update(set(eachWord))
    differentCharInSets.update(set(string))

    cspMatching = permutations(range(10), len(differentCharInSets))

    for cspMatch in cspMatching:
        tempDictionary = {char: digit for char, digit in zip(differentCharInSets, cspMatch)}

        valuesOfArrayInCSP = [int(''.join([str(tempDictionary[char])
                        for char in eachWord])) for eachWord in arrayOfStrings]
        valuesOfStringInCSP = int(''.join([str(tempDictionary[char]) for char in string]))

        if sum(valuesOfArrayInCSP) == valuesOfStringInCSP:
            return "Yes"

    return "No"

strings = input('Enter the array of strings : ');
arrayOfStrings = strings.split();

string = input('Enter the String: ')

print(algoForConstraintSatisfactionAlgorithm(arrayOfStrings, string))

