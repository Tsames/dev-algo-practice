"""
https://leetcode.com/problems/asteroid-collision/description/

735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right,
negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:
2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

def asteroidCollision(asteroids):
    # declare a stack
    stack = []

    # iterate through my array
    for roid in asteroids:
        # while loop
        # roid is opposite direction of top of stack
        if stack and stack[len(stack) - 1] > 0 and roid < 0:
            while stack and stack[len(stack) - 1] > 0 and roid < 0:
                # If they differ in sign - then calculate collision
                top = stack.pop()

                if abs(roid) == abs(top):
                    break
                elif abs(roid) < abs(top):
                    stack.append(top)
                    break
                elif not stack:
                    stack.append(roid)
                    break
                elif stack and stack[len(stack) - 1] < 0:
                    stack.append(roid)
        else:
            stack.append(roid)

    # return our stack
    return stack


print(asteroidCollision([5, 10, -5]) == [5, 10])
print(asteroidCollision([5, 5, -10]) == [-10])
print(asteroidCollision([-8, 8]) == [-8, 8])
