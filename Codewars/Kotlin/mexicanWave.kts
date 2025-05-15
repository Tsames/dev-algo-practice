/*
https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

Introduction
The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal rhythm achieved in a packed stadium when successive groups of spectators briefly stand, yell, and raise their arms. Immediately upon stretching to full height, the spectator returns to the usual seated position. The result is a wave of standing spectators that travels through the crowd, even though individual spectators never move away from their seats. In many large arenas the crowd is seated in a contiguous circuit all the way around the sport field, and so the wave is able to travel continuously around the arena; in discontiguous seating arrangements, the wave can instead reflect back and forth through the crowd. When the gap in seating is narrow, the wave can sometimes pass through it. Usually only one wave crest will be present at any given time in an arena, although simultaneous, counter-rotating waves have been produced.

(Wikipedia)

Task
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return an array of strings where an uppercase letter is a person standing up.

Rules
1.  The input string will always consist of lowercase letters and spaces, but may be empty, in which case you must return an empty array. 2.  If the character in the string is whitespace then pass over it as if it was an empty seat

Examples
"hello" => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
" s p a c e s " => [ " S p a c e s ", " s P a c e s ", " s p A c e s ", " s p a C e s ", " s p a c E s ", " s p a c e S "]
Good luck and enjoy!
 */

/*
Learning mapIndex from Mumbling last time, we used a variation of the mapIndex method
This time using mapIndexeedNotNull to exclude nulls as the result of our transform
 */
fun wave(str: String): List<String> {
    return str.mapIndexedNotNull{i, c ->
        if (c.isLetter()) str.substring(0, i) + c.uppercase() + str.substring(i + 1) else null
    }
}


data class TestCase(
    val input: String,
    val expected: List<String>,
    val description: String
)

val testCases = listOf(
    TestCase("hello", listOf("Hello", "hEllo", "heLlo", "helLo", "hellO"), "Basic case with a simple word"),
    TestCase(" s p a c e s ", listOf(" S p a c e s ", " s P a c e s ", " s p A c e s ", " s p a C e s ", " s p a c E s ", " s p a c e S "), "String with spaces between letters"),
    TestCase("", emptyList(), "Empty string input"),
    TestCase("     ", emptyList(), "String with only spaces"),
    TestCase("a", listOf("A"), "Single character input"),
    TestCase(" gap ", listOf(" Gap ", " gAp ", " gaP "), "String with leading and trailing spaces"),
    TestCase("123", emptyList(), "String with numbers only"),
    TestCase("a1b2", listOf("A1b2", "a1B2"), "String with mixed letters and numbers"),
    TestCase("hello world", listOf("Hello world", "hEllo world", "heLlo world", "helLo world", "hellO world", "hello World", "hello wOrld", "hello woRld", "hello worLd", "hello worlD"), "String with spaces between words"),
    TestCase("multiple   spaces", listOf("Multiple   spaces", "mUltiple   spaces", "muLtiple   spaces", "mulTiple   spaces", "multIple   spaces", "multiPle   spaces", "multipLe   spaces", "multiplE   spaces", "multiple   Spaces", "multiple   sPaces", "multiple   spAces", "multiple   spaCes", "multiple   spacEs", "multiple   spaceS"), "String with multiple spaces")
)

for ((index, testCase) in testCases.withIndex()) {
    val result = wave(testCase.input)
    if (result == testCase.expected) {
        throw AssertionError("Test ${index + 1} (${testCase.description}) failed. Expected ${testCase
            .expected}, but got $result")
    }
}

println("All tests passed!")