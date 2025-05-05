/*
https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/kotlin

Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]
 */

fun multiplicationTable(size: Int): Array<IntArray> {
    // TODO
    return arrayOf(intArrayOf(0))
}

data class MultiplicationTableTestCase(
    val size: Int,
    val expected: Array<IntArray>,
    val description: String
)

fun main() {
    val testCases = listOf(
        MultiplicationTableTestCase(
            1,
            arrayOf(intArrayOf(1)),
            "1x1 multiplication table"
        ),
        MultiplicationTableTestCase(
            2,
            arrayOf(intArrayOf(1, 2), intArrayOf(2, 4)),
            "2x2 multiplication table"
        ),
        MultiplicationTableTestCase(
            3,
            arrayOf(intArrayOf(1, 2, 3), intArrayOf(2, 4, 6), intArrayOf(3, 6, 9)),
            "3x3 multiplication table"
        ),
        MultiplicationTableTestCase(
            4,
            arrayOf(
                intArrayOf(1, 2, 3, 4),
                intArrayOf(2, 4, 6, 8),
                intArrayOf(3, 6, 9, 12),
                intArrayOf(4, 8, 12, 16)
            ),
            "4x4 multiplication table"
        )
    )

    for ((index, testCase) in testCases.withIndex()) {
        val result = multiplicationTable(testCase.size)
        assert(result.contentDeepEquals(testCase.expected)) {
            "Test ${index + 1} (${testCase.description}) failed. Expected ${testCase.expected.contentDeepToString()}, but got ${result.contentDeepToString()}"
        }
    }

    println("All tests passed!")
}

main()