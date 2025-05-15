/*
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/kotlin

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
 */

// Learned about the StringBuilder class in Kotlin
// Don't forget to cast it back to a String in the end.

// Don't forget that ranges in Kotlin are inclusive at the start and exclusive at the end.
// If you did not want to include the final element, you would use the until function.
// i in 1..5 -> 1, 2, 3, 4, 5
// For example, i in 1 until 5 -> 1, 2, 3, 4
fun accum(s:String): String {
    val res = StringBuilder("")
    for((index, value) in s.withIndex()) {
        res.append(value.uppercase())
        for (i in 1..index) {
            res.append(value.lowercase())
        }
        res.append("-")
    }
    return res.toString().dropLast(1)
}

/*
This solution that was submitted on Codewars is pretty clever and takes advantage of Kotlin
methods I didn't know were available.
First of all they use the mapIndex to include both the index in the String s and the value at
that index.
This creates an array of strings in the format we want.
Then we just join the array with a "-" in between each element.
 */
fun elegantAccum(s:String): String {
    return s.mapIndexed { i, c -> c.uppercase() + c.lowercase().toString().repeat(i) }.joinToString("-")
}

data class TestCase(
    val input: String,
    val expected: String,
    val description: String
)

val testCases = listOf(
    TestCase("abcd", "A-Bb-Ccc-Dddd", "Basic case with lowercase letters"),
    TestCase("RqaEzty", "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy", "Mixed case input"),
    TestCase("cwAt", "C-Ww-Aaa-Tttt", "Mixed case with alternating letters"),
    TestCase("", "", "Empty string input"),
    TestCase("A", "A", "Single uppercase letter"),
    TestCase("z", "Z", "Single lowercase letter")
)

for ((index, testCase) in testCases.withIndex()) {
    var result = accum(testCase.input)
    assert(result == testCase.expected) {
        "Test ${index + 1} (${testCase.description}) failed. Expected \"${testCase.expected}\", but got \"$result\""
    }
    result = elegantAccum(testCase.input)
    assert(result == testCase.expected) {
        "Test ${index + 1} (${testCase.description}) failed. Expected \"${testCase.expected}\", but got \"$result\""
    }
}

println("All tests passed!")