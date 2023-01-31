import math
from Main import coerce
import os
import random


def rnd(n, nPlaces=3):
    mult = pow(10, nPlaces)
    return math.floor(n * mult + 0.5) / mult


def rand(lo=0, hi=1, Seed=937162211):
    # Seed=937162211
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi - lo) * Seed / 2147483647, Seed


def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))


def csv(src, fun):
    if not os.path.isfile(src):
        print("\nfile " + src + " doesn't exists!")
        sys.exit(2)
    with open(src, 'r') as file1:
        for line in file1:
            temp = []
            for j in line.strip().split(','):
                temp.append(coerce(j))
            fun(temp)


def map(src, fun):
    for i in src:
        fun(i)


def kap(t, fun, u={}):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(k, v)
        if not k:
            u[len(u)] = v
        else:
            u[k] = v
    return u


def cosine(a, b, c):
    x1 = (a ** 2 + c ** 2 - b ** 2) / (2 * c)
    x2 = max(0, min(1, x1))
    y = math.sqrt(a ** 2 - x2 ** 2)
    return x2, y


def many(t, n):
    return random.choices(t, k=n)

def any(t):
    return random.choices(t)

def show(node,what,cols,nPlaces,lvl=0):
    if node:
        print("| "*lvl+str(len(node["data"].rows))) 
        if not node["left"] or lvl==0:
            print(node["data"].stats("mid",node["data"].cols.y,nPlaces))
        else:
            print("")
        show(node["left"], what,cols, nPlaces, lvl+1)
        show(node["right"], what,cols,nPlaces, lvl+1)

    



"""
function show(node,what,cols,nPlaces,    lvl) --> nil; prints the tree generated from `DATA:tree`.
  if node then
    lvl = lvl or 0
    io.write(("| "):rep(lvl)..#node.data.rows.."  ")
    print((not node.left or lvl==0) and  o(node.data:stats("mid",node.data.cols.y,nPlaces)) or "")
    show(node.left, what,cols, nPlaces, lvl+1)
    show(node.right, what,cols,nPlaces, lvl+1) end end

"""
