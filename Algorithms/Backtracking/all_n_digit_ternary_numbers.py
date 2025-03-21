"""
The decimal system uses the digits 0-9, the binary system uses the digits 0 and 1,
and the hexadecimal system uses the digits 0-9 and the letters A-F.
The ternary system is a base-3 numeral system that uses the digits 0, 1, and 2.

Given a number *n*, write a function that generates all *n*-digit ternary numbers.

Example(s)
Numbers starting with zero shouldn't normally be included but the ternary representing
the zero value is a valid 1-digit ternary. No other strings should start with a "0"!

generateNDigitTernaries(1) == ["0","1","2"]
generateNDigitTernaries(2) == ["10","11","12","20","21","22"]


Brainstorming

To generate a n digit ternary number we need to
"""
class Solution:
    def generate_all_n_digit_ternary_numbers(self, digits: int) -> list[str]:
        # Handle the case where digits = 0
        if digits == 0: return []
        res = []

        def generate_permutations(digit: list[int]) -> None:
            if len(digit) == digits:
                res.append("".join(digit))
                return

            # For first position with digits > 1, don't use 0
            # Otherwise use all 3 digits (0,1,2)
            if len(digit) == 0 and digits > 1:
                conditional_range = ['1', '2']
            else:
                conditional_range = ['0', '1', '2']

            for d in conditional_range:
                digit.append(d)
                generate_permutations(digit)
                digit.pop()

        generate_permutations([])
        return res

solution = Solution()

# Test case 1: digits = 0 (empty input)
expected = []
actual = solution.generate_all_n_digit_ternary_numbers(0)
assert actual == expected, f"Test 1 failed. Expected: {expected}, but got: {actual}"

# Test case 2: digits = 1 (single-digit ternary numbers)
expected = ['0', '1', '2']
actual = solution.generate_all_n_digit_ternary_numbers(1)
assert actual == expected, f"Test 2 failed. Expected: {expected}, but got: {actual}"

# Test case 3: digits = 2 (two-digit ternary numbers)
expected = ['10', '11', '12', '20', '21', '22']
actual = solution.generate_all_n_digit_ternary_numbers(2)
assert actual == expected, f"Test 3 failed. Expected: {expected}, but got: {actual}"

# Test case 4: digits = 3 (three-digit ternary numbers)
expected = [
    '100', '101', '102', '110', '111', '112', '120', '121', '122',
    '200', '201', '202', '210', '211', '212', '220', '221', '222'
]
actual = solution.generate_all_n_digit_ternary_numbers(3)
assert actual == expected, f"Test 4 failed. Expected: {expected}, but got: {actual}"

# Test case 5: digits = 4 (four-digit ternary numbers)
expected = [
    '1000', '1001', '1002', '1010', '1011', '1012', '1020', '1021', '1022',
    '1100', '1101', '1102', '1110', '1111', '1112', '1120', '1121', '1122',
    '1200', '1201', '1202', '1210', '1211', '1212', '1220', '1221', '1222',
    '2000', '2001', '2002', '2010', '2011', '2012', '2020', '2021', '2022',
    '2100', '2101', '2102', '2110', '2111', '2112', '2120', '2121', '2122',
    '2200', '2201', '2202', '2210', '2211', '2212', '2220', '2221', '2222'
]
actual = solution.generate_all_n_digit_ternary_numbers(4)
assert actual == expected, f"Test 5 failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")