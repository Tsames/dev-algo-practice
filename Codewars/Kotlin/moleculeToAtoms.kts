/*
https://www.codewars.com/kata/52f831fa9d332c6591000511/train/kotlin

For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).

For example:

var water = 'H2O';
parseMolecule(water); // return {H: 2, O: 1}

var magnesiumHydroxide = 'Mg(OH)2';
parseMolecule(magnesiumHydroxide); // return {Mg: 1, O: 2, H: 2}

var fremySalt = 'K4[ON(SO3)2]2';
parseMolecule(fremySalt); // return {K: 4, O: 14, N: 2, S: 4}
As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
 */

fun moleculeToAtom(formula: String): Map<String, Int> {
    val stack = mutableListOf<MutableMap<String, Int>>()
    var currentMap = mutableMapOf<String, Int>()
    var i = 0

    while (i < formula.length) {
        when (val char = formula[i]) {
            in 'A'..'Z' -> { // Start of an atom
                val atom = buildString {
                    append(char)
                    if (i + 1 < formula.length && formula[i + 1] in 'a'..'z') {
                        append(formula[++i])
                    }
                }
                val count = parseNumber(formula, i + 1).also { i += it.second }
                currentMap[atom] = currentMap.getOrDefault(atom, 0) + count.first
            }
            '(', '[', '{' -> { // Opening bracket
                stack.add(currentMap)
                currentMap = mutableMapOf()
            }
            ')', ']', '}' -> { // Closing bracket
                val multiplier = parseNumber(formula, i + 1).also { i += it.second }.first
                val poppedMap = stack.removeAt(stack.lastIndex)
                currentMap.forEach { (atom, count) ->
                    poppedMap[atom] = poppedMap.getOrDefault(atom, 0) + count * multiplier
                }
                currentMap = poppedMap
            }
            in '0'..'9' -> throw IllegalArgumentException("Invalid formula: unexpected number at position $i")
        }
        i++
    }

    return currentMap
}

fun parseNumber(formula: String, start: Int): Pair<Int, Int> {
    if (start >= formula.length || formula[start] !in '0'..'9') return Pair(1, 0)
    var i = start
    while (i < formula.length && formula[i] in '0'..'9') i++
    return Pair(formula.substring(start, i).toInt(), i - start)
}

val testCases = listOf(
    Pair("H2O", mapOf("H" to 2, "O" to 1)), // Simple molecule
    Pair("Mg(OH)2", mapOf("Mg" to 1, "O" to 2, "H" to 2)), // Molecule with parentheses
    Pair("K4[ON(SO3)2]2", mapOf("K" to 4, "O" to 14, "N" to 2, "S" to 4)), // Nested brackets
    Pair("Fe(NO3)2", mapOf("Fe" to 1, "N" to 2, "O" to 6)), // Molecule with multiplier outside parentheses
    Pair("C6H12O6", mapOf("C" to 6, "H" to 12, "O" to 6)), // Glucose molecule
    Pair("NaCl", mapOf("Na" to 1, "Cl" to 1)), // Simple salt
    Pair("Al2(SO4)3", mapOf("Al" to 2, "S" to 3, "O" to 12)), // Molecule with multiplier outside parentheses
    Pair("H", mapOf("H" to 1)), // Single atom
    Pair("", emptyMap()) // Empty input
)

for ((input, expected) in testCases) {
    val result = moleculeToAtom(input)
    assert (result == expected) {
        "TEst failed for input $input. Expected $expected, but got $result"
    }
}

println("All tests passed!")