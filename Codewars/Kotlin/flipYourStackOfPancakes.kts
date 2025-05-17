import jdk.internal.joptsimple.internal.Messages.message

/*
https://www.codewars.com/kata/6472390e0d0bb1001d963536

Background
Pat Programmer is worried about the future of jobs in programming because of the advance of AI tools like ChatGPT, and he decides to become a chef instead! So he wants to be an expert at flipping pancakes.

A pancake is characterized by its diameter, a positive integer.
Given a stack of pancakes, you can insert a spatula under any pancake and then flip, which reverses the order of all the pancakes on top of the spatula.

Task
Write a function that takes a stack of pancakes and returns a sequence of flips that arranges them in order by diameter, with the largest pancake at the bottom and the smallest at the top. The pancakes are given as a list of positive integers, with the left end of the list being the top of the stack.

Based on Problem 4.6.2 in Skiena & Revilla, "Programming Challenges".

Example
Consider the stack [1,5,8,3]. One way of achieving the desired order is as follows:

The 8 is the biggest, so it should be at the bottom. Put the spatula under it (position 2 in the list) and flip.
This transforms the stack into [8,5,1,3], with the 8 at the top. Then flip the entire stack (spatula position 3).
This transforms the stack into [3,1,5,8], which has the 8 at the bottom.
And since the 5 is in the correct position as well, now flip the 1 and 3 (spatula position 1).
The stack is now [1,3,5,8], as desired. The function should return [2,3,1].

Note
You don't have to find the shortest sequence of flips. That is a hard problem - see https://en.wikipedia.org/wiki/Pancake_sorting. However, don't include unnecessary flips, in the following sense:

If two consecutive flips leave the stack in the same state, they should be omitted.
For example, [2,3,2,2,1] also arranges [1,5,8,3] correctly, but 2,2 is unnecessary.
Flipping only the top pancake doesn't achieve anything.
Performance should not be a issue. If Pat can flip 1,000 pancakes with diameters between 1 and 1,000, he thinks he can get a job!
 */

fun flipPancakes(stack: MutableList<Int>): MutableList<Int> {
    //TODO
    return mutableListOf()
}

data class TestCase(
    val input: MutableList<Int>,
    val expected: List<Int>,
    val description: String
)

val testCases = listOf(
    TestCase(
        mutableListOf(1, 5, 8, 3),
        listOf(2, 3, 1),
        "Sort stack [1, 5, 8, 3] into [1, 3, 5, 8]"
    ),
    TestCase(
        mutableListOf(4, 3, 2, 1),
        listOf(4, 3, 2, 1),
        "Sort stack [4, 3, 2, 1] into [1, 2, 3, 4]"
    ),
    TestCase(
        mutableListOf(10, 1, 7, 3),
        listOf(1, 4, 2, 3),
        "Sort stack [10, 1, 7, 3] into [1, 3, 7, 10]"
    ),
    TestCase(
        mutableListOf(1),
        listOf(),
        "Single pancake stack [1] requires no flips"
    ),
    TestCase(
        mutableListOf(5, 4, 3, 2, 1),
        listOf(5, 4, 3, 2, 1),
        "Sort stack [5, 4, 3, 2, 1] into [1, 2, 3, 4, 5]"
    )
)

for ((index, case) in testCases.withIndex()) {
    val result = flipPancakes(case.input)
    if (result != case.expected) {
        throw AssertionError("Test $index (${case.description}) failed. Expected ${case.expected} but got " +
                "$result.")
    }
}

println("All tests passed!")