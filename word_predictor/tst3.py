import threading
import heapq
import operator
import re
from threading import Thread
from tkinter import *
import r
           
class Extract():
    def __init__(self,m=None,p=None,d=None):
        self.d=m
        self.ptr=p
        self.direction=d

class Char():
    def __init__(self, s,freq=0):
        self.char = s
        self.index = 0
        self.size = len(s)
        self.pre = ''
        self.count = 0
        self.frequency=int(freq)
        

    def charatindex(self):
        return self.char[self.index]

    def getchar(self):
        return self.char

    def getindex(self):
        return self.index

    def decindex(self):
        self.index -= 1
        return self.index

    def incindex(self):
        self.index += 1
        return self.index

    def addchar(self, prechar):
        self.pre = self.pre + str(prechar)
        # print(self.pre)

    def removechar(self):
        x = len(self.pre)
        self.pre = self.pre[0:x - 1]
        # print(self.pre)


class Node:
    def __init__(self, val=None):
        self.data = val.charatindex()
        self.leftchild = None
        self.midchild = None
        self.rightchild = None
        self.bit=1;
        self.isleaf=0

        self.max = 1
        self.max1 = 1
        self.max2 = 1

        if val.size == 0:
            self.bit = 1

        if val.getindex() == val.size - 1:
            self.bit = val.frequency
            self.isleaf=1
        else:
            self.bit = -1*self.bit

    def insert(self, d):

        if self.data == d.charatindex():
            # print('=')
            if self.midchild:
                if d.size == 0:
                    return self.midchild.insert(d)
                else:
                    d.incindex()
                    return self.midchild.insert(d)
            else:
                # print('here')
                d.incindex()
                while d.getindex() < d.size:
                    # print(d.charatindex())
                    self.midchild = Node(d)
                    d.incindex()
                    self = self.midchild


        elif self.data > d.charatindex():
            if self.leftchild:
                return self.leftchild.insert(d)
            else:
                self.leftchild = Node(d)
                this_node = self.leftchild
                d.incindex()
                while d.getindex() < d.size:
                    # print(d.charatindex())
                    this_node.midchild = Node(d)
                    d.incindex()
                    this_node = this_node.midchild
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(d)
            else:
                self.rightchild = Node(d)
                this_node = self.rightchild
                d.incindex()
                while d.getindex() < d.size:
                    # print(d.charatindex())
                    this_node.midchild = Node(d)
                    d.incindex()
                    this_node = this_node.midchild
                return True

    def inc_freq_bit(self,d):
        if d.getindex() == d.size - 1 and self.isleaf == 1 and self.data == d.charatindex():
            self.bit+=1
            #print(self.bit)
            return True
        else:
            if (self.data == d.charatindex()):
                if self.midchild:
                    if d.size == 0:
                        #self.bit+=-1
                        return self.midchild.inc_freq_bit(d)
                    else:
                        #self.bit+=-1
                        #print(self.bit)
                        d.incindex()
                        return self.midchild.inc_freq_bit(d)
                else:
                    return False
            elif self.data > d.charatindex():
                if self.leftchild:
                    return self.leftchild.inc_freq_bit(d)
                else:
                    return False
            else:
                if self.rightchild:
                    return self.rightchild.inc_freq_bit(d)
                else:
                    return False


    def dic_visited(self,dic):
        try:
            return dic[self]
        except KeyError:
            return 1

    def DFSUtil(self,dictionary,data,dic):
 
                dic[self]=0
                data.addchar(self.data)
                if self.isleaf ==1:
                    dictionary[data.pre]=self.bit

                if self.leftchild and self.leftchild.dic_visited(dic):
                    if self.leftchild.bit<0:
                        bit2=-1*self.leftchild.bit
                    else:
                        bit2=self.leftchild.bit
                    data.removechar()
                    self.leftchild.DFSUtil(dictionary,data,dic)


                if self.midchild and self.midchild.dic_visited(dic):
                    if self.midchild.bit<0:
                        bit1=-1*self.midchild.bit
                    else:
                        bit1=self.midchild.bit
                    
                    self.midchild.DFSUtil(dictionary,data,dic)
                    data.removechar()

                if self.rightchild and self.rightchild.dic_visited(dic): 
                    if self.rightchild.bit<0:
                        bit3=-1*self.rightchild.bit
                    else:
                        bit3=self.rightchild.bit
                    data.removechar()
                    self.rightchild.DFSUtil(dictionary,data,dic)
 
    def DFS(self,dictionary,data,dic):
        self.DFSUtil(dictionary,data,dic)

    def predict(self,dictinary,d):
        if d.getindex() == d.size - 1 and self.data == d.charatindex():
            
            d.addchar(self.data)
            #print(d.pre)
            #print(self.data)
            dic ={}
            self.midchild.DFS(dictinary,d,dic)
            

        else:
            if (self.data == d.charatindex()):
                if self.midchild:
                    d.incindex()
                    d.addchar(self.data)

                    return self.midchild.predict(dictinary,d)
                else:
                    return False
            elif self.data > d.charatindex():
                if self.leftchild:
                    return self.leftchild.predict(dictinary,d)
                else:
                    return False
            else:
                if self.rightchild:
                    return self.rightchild.predict(dictinary,d)
                else:
                    return False

class Tree:
    def __init__(self):
        self.root = None
        self.list = []
        self.final_list=[]

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            this_node = self.root
            data.incindex()
            while data.getindex() < data.size:
                # print(data.charatindex())
                this_node.midchild = Node(data)
                # print('i',this_node.midchild.data)
                data.incindex()
                this_node = this_node.midchild
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def predict(self,dictinary, data):
        if self.root:
            return self.root.predict(dictinary,data)
        else:
            return False

    def inc_freq_bit(self,data):
        #print('tree')
        if self.root:
            return self.root.inc_freq_bit(data)
        else:
            return False

tst = Tree()


class ternary(threading.Thread):
    def run(self):
        try:
            symbols=".!@#$%^/&*()_\"<>?:_-'"
            with open('word3.txt', 'r') as f:
                for line in f:
                    for word in line.split():

                        for i in range(0,len(symbols)):
                            word=word.replace(symbols[i],"")

                        r = re.compile("([a-zA-Z]+)([0-9]+)")
                        m = r.match(str(word))
                        #print(m.group(1))
                        #print(m.group(2))
                        x = Char(str(m.group(1)),m.group(2))
                        try:
                            tst.insert(x)
                        except:
                            pass
        except:
            print('unavailable to open')

        print('Finished')

final = ternary()
final.start()




def print_me(tst,data):
    y=Char(data)
    tst.inc_freq_bit(y)
    r.updatefile(data)

def findPredictedWords(tst):
    tst.final_list = tst.list
    root1=Tk()
    if len(tst.final_list)==0:
        button = Button(root1 , text = "No suggestion found !" , width = "18" , bg="white" , fg="red" , command =lambda : print_me(tst,"No suggestion found !"))
        button.grid(columnspan=3)


    for x  in range(0,len(tst.final_list)):#-2
        if x==0:
            button2 = Button(root1 , text = tst.final_list[0] , width = "18" , bg="white" , fg="red" , command =lambda : print_me(tst,tst.final_list[0]))
            button2.grid(columnspan=3)
        if x==1:
            button3 = Button(root1 , text = tst.final_list[1] , width = "18" , bg="white" , fg="blue" , command =lambda : print_me(tst,tst.final_list[1]))
            button3.grid(columnspan=3)
        if x==2:
            button4 = Button(root1 , text = tst.final_list[2] , width = "18" , bg="white" , fg="purple" , command =lambda : print_me(tst,tst.final_list[2]))
            button4.grid(columnspan=3)
        if x==3:
            button2 = Button(root1 , text = tst.final_list[3] , width = "18" , bg="white" , fg="red" , command =lambda : print_me(tst,tst.final_list[3]))
            button2.grid(columnspan=3)
        if x==4:
            button3 = Button(root1 , text = tst.final_list[4] , width = "18" , bg="white" , fg="blue" , command =lambda : print_me(tst,tst.final_list[4]))
            button3.grid(columnspan=3)
        if x==5:
            button4 = Button(root1 , text = tst.final_list[5] , width = "18" , bg="white" , fg="purple" , command =lambda : print_me(tst,tst.final_list[5]))
            button4.grid(columnspan=3)
        if x==6:
            button = Button(root1 , text = tst.final_list[6] , width = "18" , bg="white" , fg="red" , command =lambda : print_me(tst,tst.final_list[6]))
            button.grid(columnspan=3)
    root1.mainloop()


root = Tk()

label1 = Label(root , text="Enter your text : ")
entry1 = Entry(root)

label1.grid( row=0,column=0)
entry1.grid(row=0,column=2)

dictionary ={}

def store ():
    var1 = entry1.get()
    print(var1)
    y = Char(var1)
    tst.predict(dictionary,y)
    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(-1))
    #print(sorted_x)
    a1_sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
    for r in a1_sorted_keys:
        tst.list.append(r)
    findPredictedWords(tst)
    del tst.list[:]
 
button = Button(root , text="Predict" , command=store)
button.grid(row=2,column=2, sticky=W , pady = 4)

root.mainloop()




