import "package:test/test.dart";
/*
  Weight for weight
  My friend John and I are members of the "Fat to Fit Club (FFC)".
  John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.
  I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list".
  It was decided to attribute a "weight" to numbers.
  The weight of a number will be from now on the sum of its digits.
  For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
  Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

  Example:
  "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:

  "100 180 90 56 65 74 68 86 99"
  When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:

  180 is before 90 since, having the same "weight" (9), it comes before as a string.

  All numbers in the list are positive numbers and the list can be empty.

  Notes
  it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
  For C: The result is freed.
*/

main() {
  String orderWeight(String s) {
    /*
      The first step we need to do is get all of the numbers as strings separated.
      Then we need to assign those numbers that are strings values or 'weights'.
      We might want to use a map for this.

      Then we need to have some way of iterating through that map and placing its contents into the string we are going to return
      The tricky part here might be resolving equal values as well as how we find the lowest weight number.

      I think that in this map we could use the weight as the key and have a list of values as the value.
      I guess we could sort the list of keys of the map and then construct a string from that ordered list.
      That would require that each list (value) at a key would already be sorted in the correct order.
    */

    final Map<int, List<String>> weightToNumberMap = {};
    for (var num in s.split(" ")) {
      final weight = num.split("").fold(0, (value, element) => value + int.parse(element));

      if (weightToNumberMap.containsKey(weight)) {
        for (final (index, otherNum) in weightToNumberMap[weight]!.indexed) {
          if (num.compareTo(otherNum) < 0) {
            weightToNumberMap[weight]!.insert(index, num);
            break;
          } else if (index == weightToNumberMap[weight]!.length - 1) {
            weightToNumberMap[weight]!.add(num);
            break;
          }
        }
      } else {
        weightToNumberMap[weight] = [num];
      }
    }

    final sortedKeys = weightToNumberMap.keys.toList()..sort();
    return sortedKeys.map((key) => weightToNumberMap[key]!.join(" ")).join(" ");
  }

  String orderWeightBetter(String s) {
    if (s.isEmpty) return s;

    int digitSum(String num) => num.split("").fold(0, (sum, d) => sum + int.parse(d));

    final numbers = s.split(" ");
    numbers.sort((a, b) {
      final weightDiff = digitSum(a) - digitSum(b);
      return weightDiff != 0 ? weightDiff : a.compareTo(b);
    });

    return numbers.join(" ");
  }

  void doTest(String strng, String expected) {
    test('orderWeight("$strng")', () => expect(orderWeight(strng), equals(expected)));
    test('orderWeightBetter("$strng")', () => expect(orderWeightBetter(strng), equals(expected)));
  }

  group("orderWeight", () {
    doTest("103 123 4444 99 2000", "2000 103 123 4444 99");
    doTest("2000 10003 1234000 44444444 9999 11 11 22 123", "11 11 2000 10003 22 123 1234000 44444444 9999");
    doTest("", "");
  });
}
