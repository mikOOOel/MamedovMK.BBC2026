def calcplus(fn, sn, d):
    return fn + sn

def calcminus(fn, sn, d):
    return fn - sn

def calcmp(fn, sn, d):
    return fn * sn

def calcdiv(fn, sn, d):
    return fn // sn

fn = int(input())
sn = int(input())
d = input()

if d == '+':
    print(calcplus(fn, sn, d))

if d == '-':
    print(calcminus(fn, sn, d))

if d == '*':
    print(calcmp(fn, sn, d))

if d == '/':
    print(calcdiv(fn, sn, d))

