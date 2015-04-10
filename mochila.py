#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
 
    def __str__(self):
        return "Value: %d - Weight: %d" % (self.value, self.weight)
    
    def __repr__(self):
        return self.__str__()

items = [Item(3, 2),
         Item(5, 4),
         Item(4, 3),

        ]
'''
         Item(1, 5),
         Item(9, 7),
         Item(7, 4),
         Item(11, 6),
         Item(7, 4),
         Item(4, 3),
'''

start_time = time.time()
max_weight = 6
c = 0
def ks(index, weight):
    global items
    global c
    c += 1
 
    if index >= len(items):
        #print "+ Iteration %d: Weight %d. index %d. PARA ATRAS!" % (c, weight, index)
        return 0
 
    item = items[index]
 
    if item.weight > weight:
        #print "+ Iteration %d: Weight %d. index %d. Item(%d,%d)" % (c, weight, index, item.value, item.weight)
        return ks(index + 1, weight)
    else:
        #print "- Iteration %d: Weight %d. index %d. Item(%d,%d)." % (c, weight, index, item.value, item.weight)
        return max(ks(index + 1, weight),ks(index + 1, weight - item.weight) + item.value)
print "================================="
print "Fuerza bruta"
print "================================="
print "Max sum: %d" % (ks(0, max_weight),)
print "Iterations %d" % (c,)
print("--- %s seconds ---" % ((time.time() - start_time)*100))

start_time = time.time()
c = 0
mem = {}
def ks2(index, weight):
    global items
    global c
    global mem
    c += 1
 
    case = (index, weight)
    if case in mem:
        return mem[case]
 
 
    if index >= len(items):
        mem[case] = 0
        return mem[case]
 
    item = items[index]
    grab_case = (index + 1, weight - item.weight)
    no_grab_case = (index + 1, weight)
 
    if item.weight > weight:
        mem[case] = ks2(*no_grab_case)
        return mem[case]
    else:
        if no_grab_case not in mem:
            mem[no_grab_case] = ks2(index + 1, weight)
        if grab_case not in mem:
            mem[grab_case] = ks2(index + 1, weight - item.weight) + item.value
        mem[case] = max(mem[grab_case], mem[no_grab_case])
        return mem[case]
print "================================="
print "Programación dinámica (recursiva)"
print "================================="
print "Max sum: %d" % (ks2(0, max_weight),)
print "Iterations %d" % (c,)
print("--- %s seconds ---" % ((time.time() - start_time)*100))

start_time = time.time()
c = 0
mem = {}
def ks3(items, weight):
    mem = [[0 for j in xrange(weight + 1)]
           for i in xrange(len(items) + 1)]
    
    grab = [[0 for j in xrange(weight + 1)]
           for i in xrange(len(items) + 1)]
    
    
    for i, item in enumerate(items, start=1):
        for j in xrange(1, weight + 1):
            if item.weight <= j:
                if item.value + mem[i][j - item.weight] >= mem[i - 1][j]:
                    mem[i][j] = item.value + mem[i][j - item.weight]
                    grab[i][j] = 1
                else:
                    mem[i][j] = mem[i - 1][j]
            else:
                mem[i][j] = mem[i - 1][j]
                
    itemList = []
    n = len(items)
    while n > 0 and weight >= 0:
        if grab[n][weight]:
            itemList.append(items[n-1])
            weight -= items[n-1].weight
        n -= 1
    return itemList
print "================================="
print "Programación dinámica (Iterativa)"
print "================================="
print (items)
print (max_weight)
print ks3(items, max_weight)
print("--- %s seconds ---" % ((time.time() - start_time)*100))