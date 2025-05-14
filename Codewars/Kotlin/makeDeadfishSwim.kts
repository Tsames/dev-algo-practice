/*
https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/kotlin

Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to 0.

It uses four single-character commands:

i: Increment the value
d: Decrement the value
s: Square the value
o: Output the value to a result array
All other instructions are no-ops and have no effect.

Examples
Program "iiisdoso" should return numbers [8, 64].
Program "iiisdosodddddiso" should return numbers [8, 64, 3600].
 */

fun parse(data: String): List<Int> {
    return listOf()
}

val testCases = listOf(
    Pair("iiisdoso", listOf(8, 64)), // Increment 3 times, square, output, square, output
    Pair("iiisdosodddddiso", listOf(8, 64, 3600)), // Similar to above with additional decrements and operations
    Pair("dddd", emptyList()), // Decrement 4 times, no output
    Pair("iisdo", listOf(4)), // Increment 2 times, square, output
    Pair("sososo", listOf(0, 0, 0)), // Square and output repeatedly starting from 0
    Pair("", emptyList()), // Empty input, no output
    Pair("xyz", emptyList()) // Invalid commands, no output
)

for ((input, expected) in testCases) {
    val result = parse(input)
    assert(result == expected) {
        "Test failed for input \"$input\". Expected $expected, but got $result"
    }
}

println("All tests passed!")