"""
716. Max Stack (Easy)

Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

    MaxStack() Initializes the stack object.
    void push(int x) Pushes element x onto the stack.
    int pop() Removes the element on top of the stack and returns it.
    int top() Gets the element on the top of the stack without removing it.
    int peekMax() Retrieves the maximum element in the stack without removing it.
    int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.



Example 1:

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.



Constraints:

    -107 <= x <= 107
    At most 104 calls will be made to push, pop, top, peekMax, and popMax.
    There will be at least one element in the stack when pop, top, peekMax, or popMax is called.
"""


class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.arr.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.arr)

    def popMax(self):
        """
        :rtype: int
        """
        max_num = max(self.arr)

        for i, v in enumerate(self.arr[::-1]):
            if v == max_num:
                return self.arr.pop(len(self.arr) - i - 1)

