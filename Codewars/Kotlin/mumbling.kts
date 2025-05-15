/*
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/kotlin

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
 */

fun accum(s:String): String {
    // TODO
    return ""
}

fun elegantAccum(s:String): String {
    //TODO
    return ""
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
//    result = elegantAccum(testCase.input)
//    assert(result == testCase.expected) {
//        "Test ${index + 1} (${testCase.description}) failed. Expected \"${testCase.expected}\", but got \"$result\""
//    }
}

println("All tests passed!")