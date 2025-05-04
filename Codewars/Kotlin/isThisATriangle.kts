/*
https://www.codewars.com/kata/56606694ec01347ce800001b

Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

Examples:
Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false
*/

fun isThisATriangle(a: Int, b: Int, c: Int): Boolean {
    // We use the Triangle Inequality Theorem
    if (a + b <= c) return false
    if (a + c <= b) return false
    if (b + c <= a) return false
    return true
}

data class TestCase(
    val a: Int,
    val b: Int,
    val c: Int,
    val expected: Boolean,
    val description: String
)

fun main() {
    val testCases = listOf(
        TestCase(1, 2, 2, true, "Valid triangle with sides 1, 2, 2"),
        TestCase(4, 2, 3, true, "Valid triangle with sides 4, 2, 3"),
        TestCase(2, 2, 2, true, "Equilateral triangle with sides 2, 2, 2"),
        TestCase(1, 2, 3, false, "Invalid triangle with sides 1, 2, 3"),
        TestCase(-5, 1, 3, false, "Negative side length"),
        TestCase(0, 2, 3, false, "Zero side length"),
        TestCase(1, 2, 9, false, "One side too long")
    )

    for ((index, testCase) in testCases.withIndex()) {
        val result = isThisATriangle(testCase.a, testCase.b, testCase.c)
        assert(result == testCase.expected) {
            "Test ${index + 1} (${testCase.description}) failed. Expected ${testCase.expected}, but got $result"
        }
    }

    println("All tests passed!")
}

main()