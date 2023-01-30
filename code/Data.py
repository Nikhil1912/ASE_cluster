from Utils import csv, kap
from Utils import map as mp
from Row import Row
from Cols import Cols
import math


class Data:
    """Container for ROWs, summarized into NUM or SYM columns"""
    def __init__(self, src={},the=None):
        self.rows = list()
        self.cols = None
        self.the = the
        if type(src) == str:
            csv(src, self.add)
        else:
            mp(src, self.add)

    def add(self, t):
        """Adds rows and columns"""
        if not self.cols:
            self.cols = Cols(t)
        else:
            if type(t) == list:
                t = Row(t)
                self.cols.add(t)
                self.rows.append(t)

    def clone(self, t, data):
        """Creates clone"""
        data = Data(list(self.cols.names))
        mp(t, self.add)
        return data

    def stats(self, nPlaces, cols=None,what='mid'):
        if not cols:
            cols = self.cols.x
        def fun(k, col):
            return col.rnd(getattr(col, what)(), nPlaces), col.txt

        return kap(cols, fun)

    def dist(self, row1, row2, cols=None):
        n = 0
        d = 0
        if not cols:
            cols = self.cols.x
        for _, col in enumerate(cols):
            n=n+1
            d=d+col.dist(row1.cells[col.at],row2.cells[col.at])**self.the['p']
        return (d/n)**(1/self.the['p'])

    def better(self,row1,row2,s1=0,s2=0,ys=None,x=0,y=0):
        if not ys:
            ys = self.cols.y
        for cols in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w*(x-y)/len(ys))
            s2 = s2 - math.exp(col.w*(y-x)/len(ys))
        return s1/len(ys) < s2/len(ys)

    def around(self,row1,rows=None,cols=None):
        if not rows:
            rows=self.rows
        if not cols:
            cols=self.cols.x
        def fun(row2):
            return {'row':row2,'dist':self.dist(row1,row2,cols)}
        return sorted(list(map(fun,rows)),key=lambda x:x['dist'])



