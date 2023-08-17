import std/strutils
from std/sequtils import map

proc solution(x: int, y: int): int =
    result = x - y

let number_of_cases = parseInt(readLine(stdin));

for _ in 1 .. number_of_cases:
    let arr = readLine(stdin).split(' ').map(parseInt);
    echo solution(arr[0], arr[1])



import unittest

test "test solution":
    check solution(5, 2) == 3
    check solution(3, 3) == 0
    check solution(5, 4) == 1
    check solution(7, 5) == 2
