import "dart:math";
/*
Find The Parity Outlier

You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
 */

void main() {
  // ***** SOLUTION *****
  int find(List integers) {
    final even = integers.where((num) => num.isEven).toList();
    final odd = integers.where((num) => num.isOdd).toList();

    return even.length > 1 ? odd.first : even.first;
  }

  // ***** TEST HELPERS *****
  void test(String name, bool condition) {
    print(condition ? '✓ $name' : '✗ $name');
  }

  int generateOdd() {
    int oddNum = (Random.secure().nextInt(1000000) + 1);
    if (oddNum % 2 == 0) oddNum++;
    return oddNum;
  }

  // ***** TESTS *****
  test('odd at the end', find([2, 6, 8, 10, 3]) == 3);
  test('odd in the middle', find([2, 6, 8, 200, 700, 31, 84, 10, 4]) == 31);
  test('odd in the front', find([17, 6, 8, 10, 6, 12, 24, 36]) == 17);
  test('even in the front', find([2002, 1, 7, 17, 19, 211, 7]) == 2002);
  test('even in the middle', find([1, 1, 1, 1, 1, 144, 7, 7, 7, 7, 7, 7, 7, 7]) == 144);
  test(
    'even at the end',
    find([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 10002]) == 10002,
  );
  test('odd at the end (negative)', find([2, -6, 8, -10, -3523]) == -3523);
  test('odd in the middle (negative)', find([2, 6, 8, 2, -66, 34, -3523, 66, 700, 1002, -84, 10, 4]) == -3523);
  test('odd in the front (negative)', find([-1 * 10000000003, -18, 6, -8, -10, 6, 12, -24, 36]) == -1 * 10000000003);
  test('even in the front (negative)', find([-12, 1, 7, 17, 19, 211, 7]) == -12);
  test('even in the middle (negative)', find([1, 1, -1, 1, 1, -44, 7, 7, 7, 7, 7, 7, 7, 7]) == -44);

  List<int> largeList = List<int>.filled(10000000, 500);
  var targetOdd = generateOdd();
  largeList[898 + Random.secure().nextInt(100000) + 1] = targetOdd;
  test('large list (size 10000000)', find(largeList) == targetOdd);

  test('odd, with zeroes', find([0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 11);
  test('zero', find([3, 7, -99, 81, 90211, 0, 7]) == 0);

  for (int i = 0; i < 100; i++) {
    List<int> randomList = [];
    for (int j = 0; j < Random.secure().nextInt(500) + 3; j++) {
      randomList.add(generateOdd());
    }
    int target = generateOdd() * 2;
    randomList[Random.secure().nextInt(randomList.length - 1)] = target;
    test('random even, trial ${i + 1}', find(randomList) == target);
  }

  for (int i = 0; i < 100; i++) {
    List<int> randomList = [];
    for (int j = 0; j < Random.secure().nextInt(500) + 3; j++) {
      randomList.add(generateOdd() * 2);
    }
    int target = generateOdd();
    randomList[Random.secure().nextInt(randomList.length - 1)] = target;
    test('random odd, trial ${i + 1}', find(randomList) == target);
  }
}
