"""
1678. Goal Parser Interpretation

You own a Goal Parser that can interpret a string command.
The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Example 2:
Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:
Input: command = "(al)G(al)()()G"
Output: "alGalooG"
"""


class Solution:
    """
    >>> Solution().interpret(command = "G()(al)")
    'Goal'
    >>> Solution().interpret(command = "G()()()()(al)")
    'Gooooal'
    >>> Solution().interpret(command = "(al)G(al)()()G")
    'alGalooG'
    """
    def interpret(self, command: str) -> str:
        len_o = 2
        len_al = 4
        res = []

        i = 0

        while i < len(command):
            if command[i] != '(':
                res.append(command[i])
                i += 1
            else:
                if command[i+1] == ')':
                    res.append('o')
                    i += len_o
                else:
                    res.append('al')
                    i += len_al
        return "".join(res)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
