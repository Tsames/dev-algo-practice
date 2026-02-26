import "package:test/test.dart";
/*
  Roman Numerals Decoder
  Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
  You don't need to validate the form of the Roman numeral.

  Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
  starting with the leftmost digit and skipping any 0s.
  So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).
  The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

  Example:
  "MM"      -> 2000
  "MDCLXVI" -> 1666
  "M"       -> 1000
  "CD"      ->  400
  "XC"      ->   90
  "XL"      ->   40
  "I"       ->    1

  Help:
  Symbol    Value
  I          1
  V          5
  X          10
  L          50
  C          100
  D          500
  M          1,000
*/

main() {
  int romanToInt(String s) {
    /*
      So we receive a roman numeral whose form we do not need to validate.
      This would be as straightforward as building a map between symbols and values, but
      Some symbol of smaller value can go before a symbol of greater value to indicate the difference.
      Additionally, those kinds of differences mean that two symbols indicate one value rather than 1-1.

      So that means that we end up with two problems to solve:
        1. How do we identify each individual roman numeral from the whole?
        2. How do we calculate

      We know that at most two symbols can map to one value.
      We also know that when two symbols map to one value, the first of those symbols represents a lesser value.
      That means that when we are evaluating any symbol, we should potentially check the value that comes after it (if there is one)
      If the symbol that comes after it is a represent a larger value, then we should consider both symbols representative of one value.

      When evaluating symbols, if the symbol is only one character long, we should simply look it up in our map.
      If its two symbols long, we should do the same for each character, then we should subtract the first character from the second character.
    */
    int res = 0;
    final symbolToValueMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000};

    var i = 0;
    while (i < s.length) {
      final valueAtIndex = symbolToValueMap[s[i]]!;
      if (i < s.length - 1) {
        final valueAtNextIndex = symbolToValueMap[s[i + 1]]!;
        if (valueAtIndex < valueAtNextIndex) {
          res += (valueAtNextIndex - valueAtIndex);
          i += 2;
          continue;
        }
      }
      res += valueAtIndex;
      i += 1;
    }
    return res;
  }

  test("Sample Tests", () {
    expect(romanToInt('I'), equals(1));
    expect(romanToInt('IV'), equals(4));
    expect(romanToInt('LVIII'), equals(58));
    expect(romanToInt('MCMXCIV'), equals(1994));
  });
}

/*
    Similar solution, but a bit cleaner.

    int romanToInt(String s){
      Map toDec = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,};

      int ans = 0;
      List <int> temp = [];

      s.split('').forEach((e) => temp.add(toDec[e]));

      for (int i = 0; i < temp.length; i++) {
        i == temp.length - 1 || temp[i] >= temp[i + 1]
            ? ans += temp[i]
            : ans -= temp[i];
      }

      return ans;
    }
 */
