from Algorithms.Linked_Lists.linked_list_node import ListNode

"""
❓ PROMPT
Given a linked list, return an array with all the elements in reverse.

Example(s)
head = 1 -> 3 -> 5 -> 2
createArrayInReverse(head) == [2,5,3,1]
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function createArrayInReverse(node) {
def createArrayInReverse(node: Node) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

"""


def createArrayInReverse(node: ListNode) -> list[int]:
    res = []

    # Write data of each node to our result array
    while node:
        res.append(node.val)
        node = node.next

    # Reverse our array
    left, right = 0, len(res) - 1
    while left < right:
        res[left], res[right] = res[right], res[left]
        left += 1
        right -= 1

    return res


testNodeHead = ListNode(1)
testNodePointer = testNodeHead
for i in range(2, 10):
    newNode = ListNode(i)
    testNodePointer.next = newNode
    testNodePointer = newNode

print(createArrayInReverse(testNodeHead))
