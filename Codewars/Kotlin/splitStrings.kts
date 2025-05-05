/*
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/kotlin
Split Strings
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second
character of the final pair with an underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
*/

fun splitStrings(s: String): List<String> {
    val adjustedString = if (s.length % 2 == 1) s + "_" else s
    // We learned the chunked function from the Kotlin standard library here
    return adjustedString.chunked(2)
}

data class SplitStringsTestCase(
    val input: String,
    val expected: List<String>,
    val description: String
)

fun main() {
    val testCases = listOf(
        SplitStringsTestCase("abc", listOf("ab", "c_"), "Odd-length string"),
        SplitStringsTestCase("abcdef", listOf("ab", "cd", "ef"), "Even-length string"),
        SplitStringsTestCase("", emptyList(), "Empty string"),
        SplitStringsTestCase("a", listOf("a_"), "Single character string"),
        SplitStringsTestCase("ab", listOf("ab"), "Two-character string")
    )

    for ((index, testCase) in testCases.withIndex()) {
        val result = splitStrings(testCase.input)
        assert(result == testCase.expected) {
            "Test ${index + 1} (${testCase.description}) failed. Expected ${testCase.expected}, but got $result"
        }
    }

    println("All tests passed!")
}

main()