# Exceptions

https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

Errors detected during execution are called exceptions.

## Examples:

### ZeroDivisionError
This error is raised when the second argument of a division or modulo operation is zero.
```
>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero
```

### ValueError
This error is raised when a built-in operation or function receives an argument that has the right type 
but an inappropriate value.

```
>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'
```

## Sample Input
```
3
1 0
2 $
3 1
```

## Sample Output
```
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
```