def calc(fn, sn, d):
    if d == '+':
        return(fn + sn)
    if d == '-':
        return(fn - sn)
    if d == '*':
        return(fn * sn)
    if d == '/':
        if sn == 0:
            return("Division by zero!")
        else:
            return(fn / sn)
    if d == '%':
        if sn == 0:
            return("Division by zero!")
        else:
            return(fn % sn)
    if d == '//':
        if sn == 0:
            return  ("Division by zero!")
        else:
            return (fn // sn)

g = 0
while g != 1:
    a = int(input())
    b = int(input())
    c = str(input())
    print(calc(a, b, c))
