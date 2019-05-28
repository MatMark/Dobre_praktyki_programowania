import ctypes as c
import math


# g++ -Wall -fPIC -O2 -c permutations.cpp
# g++ -shared -W -o permutations.dll permutations.o

# python setup.py sdist bdist_wheel

def permute():
    f = c.CDLL('./permutations.dll').perm
    # f = c.CDLL('/home/matmark/Pulpit/DPP/CPlusPlusPlusPython/CPP/permutations.dll').perm
    txt = str(input("Podaj słowo [do 5 znaków]: "))
    size = len(txt)
    if size > 5:
        print("Zbyt długi ciąg znaków")
        return
    rng = math.factorial(size)
    f.restype = c.POINTER(c.c_char_p * rng)
    f.argtypes = [c.c_char_p]
    data = f(str.encode(txt))
    for i in range(rng):
        print(data.contents[i])
    return


permute()

# libUTILS = c.cdll.LoadLibrary('/home/matmark/Pulpit/DPP/CPlusPlusPlusPython/CPP/permutations.so')
#
# txt = str(input("Podaj słowo: "))
#
# prot = c.CFUNCTYPE(
#     c.c_char_p,
#     c.c_char_p
# )
#
# func = prot(('perm', libUTILS))
#
# res = func(c.c_char_p(str.encode(txt)))


# f = c.CDLL('/home/matmark/Pulpit/DPP/CPlusPlusPlusPython/CPP/permutations.so').function
# f.restype = c.POINTER(c.c_int * 10)
# data = f()
# for i in data.contents:
#     print(data.contents[i])
