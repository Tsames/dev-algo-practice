'''
❓ PROMPT
You are given four arrays representing two lists of operands, one list of operators,
and a list of results. For any index, i, your task is to check to see if:

operands1[i] operators[i] operands2[i] = results[i]

For input arrays arrays like:

operands1 = [1, 2]
operators = ['+', '-']
operands2 = [2, 3] 
results = [3, 0]

then the result of this function should be [true, false] since 1 + 2 = 3 and 2 - 3 ≠ 0.

The numbers will be integers, and the signs can be "+", "-", "*", "/".
Round to the nearest whole number for division.

Example(s)
Given the following:

operands1 = [1, 2]
operators = ['+', '-']
operands2 = [2, 3] 
results = [3, 0]

At index 0, we have 1 + 2 = 3. This evaluation is True
At index 1, we have 2 - 3 = 0. This evaluation is False

We should return [True, False] as there are two operands in the input list.

Another Example:
operands1_1 = [1, 5, 2]
operators_1 = ['+', '-', '*']
operands2_1 = [2, 3, 4]
results_1 = [3, 2, 8]

At index 0, we have 1 + 2 = 3. This evaluation is True
At index 1, we have 5 - 3 = 2. This evaluation is True
At index 2 we have 2 * 4 = 8. This evaluation is True

We should return [True, True, True]
 

🔎 EXPLORE
List your assumptions & discoveries:
 
I would assume that the four arrays that are provided are all of the same length. Should I account for the case
where the arrays are of differing lengths?

What result should be returned if empty arrays are provided as arguments? An empty array?

Can you provide more detail about how the numbers are rounded in the case of division? Should they always be rounded
down? Should they always be rounded up?

Insightful & revealing test cases:
 
Division is definitely an operator that needs a tad bit more baby sitting, as we have to round to the nearest
integer, however this step does not need to be applied to addition, subtraction, or multiplication. 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()

First we declare our result array as an empty array. We'll add to it later.
 
Presumably, all four arrays that are given as arguments will be of the same length, so we can iterate
through a range using the index to access each piece of the expression we are evaluating.

Since division requires some extra code, we could have a switch statement that evaluates the operand array at the
given index, and adds the 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function checkArithmeticExpressions(operands1, operators, operands2, results) // returns an array of booleans
'''

def check_arithmetic_expressions(operands1, operators, operands2, results):
    result = []

    for i in range(len(operators)):
        match (operators[i]):
            case "+":
                result.append(operands1[i] + operands2[i] == results[i])
            case "-":
                result.append(operands1[i] - operands2[i] == results[i])
            case "*":
                result.append(operands1[i] * operands2[i] == results[i])
            case "/":
                result.append(round(operands1[i] / operands2[i]) == results[i])
    
    print(result)
    return result

'''
🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# operands1 = [1, 2]
# operators = ['+', '-']
# operands2 = [2, 3] 
# results = [3, 0]

# Should return [True, False] and does

check_arithmetic_expressions([1, 2], ['+', '-'], [2, 3], [3, 0])

# operands1_1 = [1, 5, 2]
# operators_1 = ['+', '-', '*']
# operands2_1 = [2, 3, 4]
# results_1 = [3, 2, 8]

# Should return [True, True, True] and does

check_arithmetic_expressions([1, 5, 2], ['+', '-', '*'], [2, 3, 4], [3, 2, 8])

# operands1 = [1, 2]
# operators = ['+', '-']
# operands2 = [2, 3] 
# results = [3, 0]

# Should return  [True, False] and does

check_arithmetic_expressions([1, 2], ['+', '-'], [2, 3], [3, 0])