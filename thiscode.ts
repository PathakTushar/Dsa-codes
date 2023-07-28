function* range(start: number, end: number) {
    for (; start < end; start++) { 
        yield start; 
    }
}
function last<T>(arr: T[]) { return arr[arr.length - 1]; }
function* numericCombinations(n: number, r: number, loc: number[] = []): IterableIterator<number[]> {
    const idx = loc.length;
    if (idx === r) {
        yield loc;
        return;
    }
    for (let next of range(idx ? last(loc) + 1 : 0, n - r + idx)) { 
        yield* numericCombinations(n, r, loc.concat(next)); 
    }
}
function* combinations<T>(arr: T[], r: number) {
    for (let idxs of numericCombinations(arr.length, r)) { 
        yield idxs.map(i => arr[i]); 
    }
}
import { PathLike } from "fs";
import { readFile, writeFile } from "fs/promises";
const left = 0, right = 1;
function union(list1: string[], list2: string[]) {
    return Array.from(new Set([...list1, ...list2]))
}
async function loadModel(path: PathLike): Promise<[string[], string[], [string, string[]][]]> {
    const file = await readFile(path, "utf-8")
    const K = (file.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n",""))
	const V = (file.split("Variables:\n")[1].split("Productions:\n")[0].replace("Variables:\n","").replace("\n",""))
	const P = (file.split("Productions:\n")[1])
	return [cleanAlphabet(K), cleanAlphabet(V), cleanProduction(P)]
}
function cleanProduction(expression: string) {
    const result: [string, string[]][] = []
    const rawRules = expression.replace("\n", "").split("")
    for(const rule of rawRules) {
        const leftSide = rule.split(" -> ")[0].replace(" ", "")
        const rightSie = rule.split(" -> ")[1].split(" | ")
        for(const term of rightSie) {
            result.push([leftSide, term.split(" ")])
        }
    }
    return result
}
function cleanAlphabet(expression: string): string[] {
    return expression.replace("  ", " ").split(" ")
}
function seekAndDestroy(target: string, productions: [string, string[]][]): [string[], [string, string[]][]] {
    const trash: string[] = []
    const erased: [string, string[]][] = []
    for(const production of productions) {
        if(production[right].includes(target) && production[right].length === 1) {
            trash.push(production[left])
        }
        else {
            erased.push(production)
        }
    }
    return [trash, erased]
}
function setupObject(productions: [string, string[]][], variables: string[], terms: string[]) {
    const result: {[key: string]: string} = {}
    for(const production of productions) {
        if(
            variables.includes(production[left]) &&
            terms.includes(production[right][0]) &&
            production[right].length === 1   
        ) {
            result[production[right][0]] = production[left]
        }
    }
    return result
}
function rewrite(target: string, production: [string, string[]]) {
    const result: [string, string[]][] = []
    const positions = production[right].map((e, i) => {
        if(e === target) {
            return i
        }
    }) as number[]
    for(let i of range(0, positions.length+1)) {
        for(const element of combinations<number>(positions, i)) {
            const set: string[] = []
            for(i of range(0, production[right].length)) {
                if(!element.includes(i)) {
                    set.push(production[right][i])
                }
            }
            if(set.length) {
                result.push([production[left], set])
            }
        }
    }
    return result
}
function objectToSet(object: {[key: string]: string[]}) {
    const result: [string, string[]][] = []
    for(const key in object) {
        result.push([key, object[key]])
    }
    return result
}
function printRules(rules: [string, string[]][]) {
    for(const rule of rules) {
        let tot = ""
        for(const term of rule[right]) {
            tot += ` ${term}`
        }
        console.log(rule[left]+" ->"+tot)
    }
}
function prettyForm(rules: [string, string[]][]) {
    const dictionary: {[key: string]: string} = {}
    for(const rule of rules) {
        if(Object.keys(dictionary).includes(rule[left])) { 
            dictionary[rule[left]] += " | "+rule[right].join(" ")
        }
        else {
            dictionary[rule[left]] = rule[right].join("")
        }
    }
    let result = ""
    for(const key in dictionary) {
        result += key+" -> "+dictionary[key]+"\n"
    }
    return result
}
let K: string[] = []
let V: string[] = []
let Productions: [string, string[]][] = []
const variableJar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z"]
function isUnitary(rule: [string, string[]], variables: string[]) {
    if(variables.includes(rule[left]) && variables.includes(rule[right][0]) && rule[right].length === 1) {
        return true
    }
    return false
}
function isSimple(rule: [string, string[]]) {
    if(V.includes(rule[left]) && K.includes(rule[right][0]) && rule[right].length === 1) {
        return true
    }
    return false
}
V.forEach((nonTerminal, i) => {
    if(variableJar.includes(nonTerminal)) {
        variableJar.splice(i, 1)
    }
})
function start(productions: [string, string[]][], variables: string[]) {
    variables.push("S0")
    return ([["S0", [variables[0]]], ...productions] as [string, string[]][])
}
function term(productions: [string, string[]][], variables: string[]) {
    const newProductions: [string, string[]][] = []
    const dictionary = setupObject(productions, variables, K)
    for(const production of productions) {
        if(isSimple(production)) {
            newProductions.push(production)
        }
        else {
            for(const term of K) {
                production[right].forEach((value, index) => {
                    if(term === value && !Object.keys(dictionary).includes(term)) {
                        dictionary[term] = variableJar.pop() as string
                        V.push(dictionary[term])
                        newProductions.push([dictionary[term], [term]])
                        production[right][index] = dictionary[term]
                    }
                    else if(term === value) {
                        production[right][index] = dictionary[term]
                    }
                })
            }
            newProductions.push([production[left], production[right]])
        }
    }
    return newProductions
}
function bin(productions: [string, string[]][], variables: string[]) {
    const result: [string, string[]][] = []
    for(const production of productions) {
        const k = production[right].length
        if(k<=2) {
            result.push(production)
        }
        else {
            const newVar = variableJar.pop() as string
            variables.push(newVar+"1")
            result.push([production[left], [production[right][0], newVar+'1']])
            for(let i=1; i<k-2; i++) {
                const var1 = `${newVar}${i}`
                const var2 = `${newVar}${i+1}`
                variables.push(var2)
                result.push([var1, [production[right][i], var2]])
            }
            result.push([`${newVar}${k-2}`, production[right].filter((_, i) => i>=k-2 && i<k-2+k)])
        }
    }
    return result
}
function del(productions: [string, string[]][]) {
    const newSet: [string, string[]][] = []
    const [outlaws, _productions]  = seekAndDestroy("e", productions)
    for(const outlaw of outlaws) {
        for(const production of [..._productions, ...newSet.filter(e => !_productions.includes(e))]) {
            if(production[right].includes(outlaw)) {
                newSet.push(...rewrite(outlaw, production).filter(e => !newSet.includes(e)))
            }
        }
    }
    return [...newSet, ..._productions.filter(e => !newSet.includes(e))]
}
function routine(rules: [string, string[]][], variables: string[]) {
    const unitaries: [string, string][] = []
    const result: [string, string[]][] = []
    for(const rule of rules) {
        if(isUnitary(rule, variables)) {
            unitaries.push([rule[left], rule[right][0]])
        }
        else {
            result.push(rule)
        }
    }
    for(const unitary of unitaries) {
        for(const rule of rules) {
            if(unitary[right] === rule[left] && unitary[left] !== rule[left]) {
                result.push([unitary[left],rule[right]])
            }
        }
    }
    return result
}
function unit(productions: [string, string[]][], variables: string[]) {
    let i = 0
    let result = routine(productions, variables)
    let temp = routine(result, variables)
    while(result !== temp && i < 1000) {
        result = routine(productions, variables)
        temp = routine(result, variables)
        i++
    }
    return result
}
if(true) {
    console.log("The input is taken from model.txt")
    const modelPath = "model.txt"
    loadModel(modelPath).then(async e => {
        K = e[0]
        V = e[1]
        Productions = e[2]
        Productions = start(Productions, V)
        Productions = term(Productions, V)
        Productions = bin(Productions, V)
        Productions = del(Productions)
        Productions = unit(Productions, V)
        console.log(prettyForm(Productions))
        console.log(Productions.length)
        await writeFile("output.txt", prettyForm(Productions)).then(() => console.log("Written the output to output.txt"))
    })
}