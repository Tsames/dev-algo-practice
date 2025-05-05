/*
https://www.codewars.com/kata/54b724efac3d5402db00065e/train/kotlin

Decode Morse Code
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decodeMorse('.... . -.--   .--- ..- -.. .')
//should return "HEY JUDE"
NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.
*/

fun decodeMorse(code: String): String {
    //Todo
    return ""
}

data class DecodeMorseTestCase(
    val input: String,
    val expected: String,
    val description: String
)

fun main() {
    val testCases = listOf(
        DecodeMorseTestCase(
            ".... . -.--   .--- ..- -.. .",
            "HEY JUDE",
            "Basic decoding with spaces between words"
        ),
        DecodeMorseTestCase(
            "... --- ...",
            "SOS",
            "Decoding the SOS distress signal"
        ),
        DecodeMorseTestCase(
            "   .... . -.--   ",
            "HEY",
            "Decoding with extra spaces around the input"
        ),
        DecodeMorseTestCase(
            "- .... .. ...   .. ...   .-   - . ... -",
            "THIS IS A TEST",
            "Decoding a longer sentence"
        ),
        DecodeMorseTestCase(
            "",
            "",
            "Empty input string"
        )
    )

    for ((index, testCase) in testCases.withIndex()) {
        val result = decodeMorse(testCase.input)
        assert(result == testCase.expected) {
            "Test ${index + 1} (${testCase.description}) failed. Expected '${testCase.expected}', but got '$result'"
        }
    }

    println("All tests passed!")
}

main()