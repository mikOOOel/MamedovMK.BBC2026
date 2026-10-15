fn = int(input())
sn = int(input())
d = str(input())
if d == '+':
    print(fn + sn)
if d == '-':
    print(fn - sn)
if d == '*':
    print(fn * sn)
if d == '/':
    if sn == 0:
        print("Division by zero!")
    else:
        print(fn / sn)
if d == '%':
    if sn == 0:
        print("Division by zero!")
    else:
        print(fn % sn)
if d == '//':
    if sn == 0:
        print("Division by zero!")
    else:
        print(fn // sn)
