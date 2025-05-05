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
    /*
     We know that the first IntArray in our return Array will be all natural numbers (excluding 0) up to and including size
     We also know that the 0th index of each IntArray after that will be its index in the return Array plus 1.

     We can create our return Array first.
     Then we can loop through once and fill our unique first IntArray with 1..size.
     Then we can loop through the rest of the IntArrays and fill them with the first IntArray multiplied by their index + 1.
     */
    val table = Array(size) { IntArray(size) }
    for (i in 1..size) {
        table[0][i - 1] = i
    }

    for (i in 1 until size) {
        for (j in 0 until size) {
            table[i][j] = table[0][j] * (i + 1)
        }
    }

    return table
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