REP_ARROW = "->"
REP_OR = "|"
REP_EMPTY = "e"
REP_END_CHAR = "$"
REP_START_VAR_CHAR = "S"

print('write the production rules')
print('You can use -> for arrow, | for or, e for empty, $ for endChar, S for starting state ')
print('Refer to this example for inputting values')
# print('S->AAA|B\nA->aA|B\nB->e\n$')
print('S->a|aA|B\nA->aBB|e \nB->Aa|b\n$')
print('<------------------------------------------------------------------------------------------->')
print('Enter the production rules:')


class Production_Rule:
    def __init__(self, leftHandSide, rightHandSide):
        self.leftHandSide = leftHandSide
        self.rightHandSide = rightHandSide


class Algorithm_CYK:
    def __init__(self, productionRules):
        self.productionRules = productionRules
        self.algorithm_matrix = []

    def code_run(self):
        inputRulesToExamine = input().replace(" ", "")
        while inputRulesToExamine != REP_END_CHAR:
            self.create_final_matrix(inputRulesToExamine)
            print("True" if self.start_var_in_last_cell() else "False")
            self.display_matrix()
            inputRulesToExamine = input().replace(" ", "")

    def start_var_in_last_cell(self):
        return REP_START_VAR_CHAR in self.algorithm_matrix[0][-1]

    def create_final_matrix(self, string):
        lengthOfmatrix = len(string)
        algorithm_matrix = [[set() for k in range(lengthOfmatrix)] for j in range(lengthOfmatrix)]
        for i in range(lengthOfmatrix):
            algorithm_matrix[i][i] = self.findingVarOfProducts([string[i]])

        for j in range(lengthOfmatrix):
            for i in range(j, -1, -1):
                matchingMatrix = set()
                for incrementer in range(1, j-i+1):
                    leftRule = j - incrementer
                    downRule = (j-i+1) - incrementer + i
                    for variable_1 in algorithm_matrix[i][leftRule]:
                        for variable_2 in algorithm_matrix[downRule][j]:
                            MergingVars = [variable_1, variable_2]
                            matchingMatrix.update(self.findingVarOfProducts(MergingVars))
                algorithm_matrix[i][j].update(matchingMatrix)
        self.algorithm_matrix = algorithm_matrix

    def findingVarOfProducts(self, eachProduct):
        matchingMatrix = set()
        for eachRule in self.productionRules:
            for eachProd in eachRule.rightHandSide:
                if eachProd == eachProduct:
                    matchingMatrix.add(eachRule.leftHandSide)
        return matchingMatrix

    def display_matrix(self):
        for x in self.algorithm_matrix:
            print(x)


class CNF_Convert:
    def __init__(self):
        self.productionRules = list()
        self.check_is_it_cnf = True

    def check_is_it_cnf(self):
        return self.check_is_it_cnf

    def insertingRules(self, leftHandSide, rightHandSide):
        self.productionRules.append(Production_Rule(leftHandSide, rightHandSide))

    def display_rules(self):
        for eachRule in self.productionRules:
            print(eachRule.leftHandSide + " -> ", end='')
            print(eachRule.rightHandSide)

    def fetchingRules(self):
        return self.productionRules

    @staticmethod
    def create_varStyle(incrementer):
        return "(V" + incrementer + ")"

    def decreasingVarToTwo(self):
        counterForVariable = 0
        variable_new = list()
        wasThereAnyChange = True
        while wasThereAnyChange:
            wasThereAnyChange = False
            for eachRule in self.productionRules:
                for eachProduct in eachRule.rightHandSide:
                    if len(eachProduct) > 2:
                        wasThereAnyChange = True
                        self.check_is_it_cnf = False
                        varFirst = eachProduct[0]
                        varSecond = eachProduct[1]
                        eachProduct.pop(0)
                        eachProduct.pop(0)
                        new_var_product = [varFirst,varSecond]
                        if new_var_product in variable_new:
                            name_var_new = self.create_varStyle(str(variable_new.index(new_var_product)))
                        else:
                            name_var_new = self.create_varStyle(str(counterForVariable))
                            variable_new.append(new_var_product)
                            counterForVariable += 1
                        eachProduct.insert(0, name_var_new)

        for charVar in variable_new:
            name_var_new = self.create_varStyle(str(variable_new.index(charVar)))
            self.insertingRules(name_var_new, [charVar])

    @staticmethod
    def create_terminalStyle(incrementer):
        return "(T" + incrementer + ")"

    def createVariableForTerminal(self):
        counterForVariable = 0
        variable_new = list()
        for eachRule in self.productionRules:
            for eachProduct in eachRule.rightHandSide:
                for i, charVar in enumerate(eachProduct):
                    if len(eachProduct) > 1 and charVar.islower():
                        self.check_is_it_cnf = False
                        if charVar in variable_new:
                            name_var_new = self.create_terminalStyle(str(variable_new.index(charVar)))
                        else:
                            name_var_new = self.create_terminalStyle(str(counterForVariable))
                            variable_new.append(charVar)
                            counterForVariable += 1
                        eachProduct[i] = charVar.replace(charVar, name_var_new)

        for terminal_char in variable_new:
            name_var_new = self.create_terminalStyle(str(variable_new.index(terminal_char)))
            self.insertingRules(name_var_new, [[terminal_char]])


class CFG_Input:
    def __init__(self):
        self.productionRules = set()
        self.nullValues = set()
        self.graphDependency = dict()
        self.variableGenerative = set()
        self.variableReachable = set()

        self.cnfGrammar = CNF_Convert()
        self.counterForCnf = 0        
        self.grammar = {}
        self.terminal_start = "S"


    def findingCombVal(self, leftCollSet, rightCollSet):
        valComb = []
        for collNum, collLeft in enumerate(leftCollSet):
            collRight = rightCollSet[collNum]
            for itemLeft in collLeft:
                for itemRight in collRight:
                    initComb = itemLeft + itemRight
                    for key, value in self.grammar.items():
                        if initComb in value:
                            if not key in valComb:
                                valComb.append(key)
        return valComb

    def findingCollSets(self, getFullTable, findingXPosition, findingXOffset):
        segmentTable = []
        findingYPosition = 0
        while findingXOffset >= 2:
            setsItems = getFullTable[findingYPosition][findingXPosition:findingXPosition+findingXOffset]
            if findingXOffset > len(setsItems):
                return None
            segmentTable.append(setsItems)
            findingXOffset -= 1
            findingYPosition += 1
        findingVerticalCombinations = []
        findingHorizontalCombinations = []
        for item in segmentTable:
            findingVerticalCombinations.append(item[0])
            findingHorizontalCombinations.append(item[-1])
        return findingVerticalCombinations[::-1], findingHorizontalCombinations
        
    def letsGenerateTable(self, checkingWord):
        myTable = [[]]
        for symbol in checkingWord:
            validStatesForRules = []
            for key, value in self.grammar.items():
                if symbol in value:
                    validStatesForRules.append(key)
            myTable[0].append(validStatesForRules)
        for findingXOffset in range(2,len(checkingWord)+1):
            myTable.append([])
            for findingXPosition in range(len(checkingWord)):
                collSetsRules = self.findingCollSets(myTable, findingXPosition, findingXOffset)
                if collSetsRules:
                    myTable[-1].append(self.findingCombVal(*collSetsRules))
        
        return myTable
        
    def wordCheckingForRule(self, checkingWord):
        return self.terminal_start in self.letsGenerateTable(checkingWord)[-1][-1]

    def insertingRules(self, leftHandSide, rightHandSide):
        self.productionRules.add(Production_Rule(leftHandSide, rightHandSide))

    def rulesInputToProceed(self):
        self.productionRules = set()
        inputRulesToExamine = input().replace(" ", "")
        while inputRulesToExamine != REP_END_CHAR:
            var, eachRule = list(inputRulesToExamine.split(REP_ARROW))
            var_rules = set(eachRule.split(REP_OR))
            self.insertingRules(var, var_rules)
            inputRulesToExamine = input().replace(" ", "")

    def display_rules(self):
        for eachRule in self.productionRules:
            print(eachRule.leftHandSide + " -> ", end='')
            first_for = True
            for eachProduct in eachRule.rightHandSide:
                if not first_for:
                    print(" | ", end="")
                first_for = False

                if isinstance(eachProduct, str):
                    print(eachProduct, end='')
                else:
                    print("".join(eachProduct), end='')


            print()

    def display_cnf(self):
        self.cnfGrammar.display_rules()

    
    def findingNullValues(self):
        self.nullValues = set()
        settingOldSize = -1
        while len(self.nullValues) != settingOldSize:
            settingOldSize = len(self.nullValues)
            for eachRule in self.productionRules:
                if REP_EMPTY in eachRule.rightHandSide:  
                    self.nullValues.add(eachRule.leftHandSide)
                    eachRule.rightHandSide.remove(REP_EMPTY)
                    continue

                for eachProduct in eachRule.rightHandSide: 
                    is_nullable = True
                    for var in eachProduct:
                        if var not in self.nullValues:
                            is_nullable = False
                    if is_nullable:
                        self.nullValues.add(eachRule.leftHandSide)

    def remove_e(self):
        self.findingNullValues()
        for var_null_values in self.nullValues:
            for eachRule in self.productionRules:
                settingOldSize = 0
                while len(eachRule.rightHandSide) != settingOldSize:  
                    settingOldSize = len(eachRule.rightHandSide)
                    for eachProduct in eachRule.rightHandSide.copy():
                        for charVar in eachProduct:
                            if charVar == var_null_values:
                                s = eachProduct.replace(charVar, "", 1)
                                if s != "":
                                    eachRule.rightHandSide.add(s)


    def creatingGraphDependency(self):
        self.graphDependency = dict()
        for eachRule in self.productionRules:
            self.graphDependency[eachRule.leftHandSide] = set()
            for eachProduct in eachRule.rightHandSide:
                for charVar in eachProduct:
                    if charVar.isupper():
                        self.graphDependency[eachRule.leftHandSide].add(charVar)
                        

    def isproducingUnit(self, s):
        return len(s) == 1 and s.isupper()

    def findingNonUnitProducts(self, charVar):
        productsNonUnit = set()
        for eachRule in self.productionRules:
            if eachRule.leftHandSide == charVar:
                for eachProduct in eachRule.rightHandSide:
                    if not self.isproducingUnit(eachProduct):
                        productsNonUnit.add(eachProduct)
        return productsNonUnit

    def replacingForUnitProductions(self, charVar, flag_visited):
        productsReplaced = set()
        if charVar in flag_visited:
            return productsReplaced
        flag_visited.append(charVar)

        if charVar not in self.graphDependency:
            self.removingProductsForVariables(charVar)
        else:
            for var in self.graphDependency[charVar]:
                if var != charVar:
                    productsReplaced.update(self.findingNonUnitProducts(var))
                    productsReplaced.update(self.replacingForUnitProductions(var, flag_visited)) 

        return productsReplaced

    def tryingToRemoveUnitProductions(self):
        self.creatingGraphDependency()
        for eachRule in self.productionRules:
            for eachProduct in eachRule.rightHandSide.copy():
                if self.isproducingUnit(eachProduct):
                    eachRule.rightHandSide.update(self.replacingForUnitProductions(eachProduct, []))
                    eachRule.rightHandSide.remove(eachProduct)

    def removingProductsForVariables(self, charVar):
        for eachRule in self.productionRules:
            for eachProduct in eachRule.rightHandSide.copy():
                if charVar in eachProduct:
                    eachRule.rightHandSide.remove(eachProduct)

    def creatingGenerativeVariables(self):
        variableGenerative = set()
        settingOldSize = -1
        while settingOldSize != len(variableGenerative):
            settingOldSize = len(variableGenerative)
            for eachRule in self.productionRules:
                for eachProduct in eachRule.rightHandSide:
                    checkingIsGenerative = (len(eachProduct) > 0)
                    for charVar in eachProduct:
                        if charVar.isupper() and charVar not in variableGenerative:
                            checkingIsGenerative = False
                    if checkingIsGenerative:
                        variableGenerative.add(eachRule.leftHandSide)
        self.variableGenerative = variableGenerative

    def nonGenerativeRemoving(self):
        self.creatingGenerativeVariables()
        for eachRule in self.productionRules.copy():
            if eachRule.leftHandSide not in self.variableGenerative:
                self.removingProductsForVariables(eachRule.leftHandSide)
                self.productionRules.remove(eachRule)
            else:
                if len(eachRule.rightHandSide) == 0:
                    self.productionRules.remove(eachRule)

    def creatingReachableVariable(self, start_var, flag_visited):
        if start_var in flag_visited:
            return
        flag_visited.append(start_var)
        self.variableReachable.add(start_var)
        if start_var not in self.graphDependency: 
            self.removingProductsForVariables(start_var)
        else:
            for to_var in self.graphDependency[start_var]:
                self.creatingReachableVariable(to_var, flag_visited)

    def removingNonReachableVariables(self):
        self.creatingGraphDependency()
        self.creatingReachableVariable(REP_START_VAR_CHAR, [])
        for eachRule in self.productionRules.copy():
            if eachRule.leftHandSide not in self.variableReachable:
                self.removingProductsForVariables(eachRule.leftHandSide)
                self.productionRules.remove(eachRule)

    def separatingProductionFromVar(self):
        self.counterForCnf = 0
        variable_new = list()
        for eachRule in self.productionRules:
            productsNew = list() 
            for eachProduct in eachRule.rightHandSide:
                productNew = list()  
                for charVar in eachProduct:
                    productNew.append(charVar)
                productsNew.append(productNew)

            self.cnfGrammar.insertingRules(eachRule.leftHandSide, productsNew)

    def convert_to_CNF(self):
        self.separatingProductionFromVar()  
        self.cnfGrammar.createVariableForTerminal()
        self.cnfGrammar.decreasingVarToTwo()
        self.productionRules = self.cnfGrammar.fetchingRules()

    def check_is_it_cnf(self):
        return self.cnfGrammar.check_is_it_cnf



cfg = CFG_Input()
cfg.rulesInputToProceed()
cfg.remove_e()
cfg.tryingToRemoveUnitProductions()
cfg.nonGenerativeRemoving()
cfg.removingNonReachableVariables()
print("Production rules after converting to cnf")
cfg.convert_to_CNF()
cfg.display_rules()

s = input("Enter the String to check if it belongs to grammar or not: ");

R = {}

for eachRule in cfg.productionRules:
            temp = [];
            for eachProduct in eachRule.rightHandSide:
                if isinstance(eachProduct, str):
                    temp.append(eachProduct)
                else:
                    temp.append("".join(eachProduct))
            R[eachRule.leftHandSide] = temp


cfg.grammar = R;


if cfg.wordCheckingForRule(s):
		print(s+" belongs to the given Grammar")
else:
    print(s+" does not belong to the given Grammar")

# S->a|aA|B 
# A->aBB|e 
# B->Aa|b
# $

