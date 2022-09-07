#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromicBorder' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def mod(x):
    return x % 1000000007

class trie(object):
    def __init__(self, depth=0, parent=None, data=None):
        self.count = 0
        self.depth = depth
        self.parent = parent
        self.data = data
        self.next = {}
        
    def get(self, char):
        if char in self.next:
            return self.next[char]
        ans = trie(self.depth + 2, self, char)
        self.next[char] = ans
        return ans
    
    def children(self):
        return self.next.values()

def dfs(node):
    ans = 0
    stack = []
    stack.append((node, True))
    while len(stack) > 0:
        node, extend = stack.pop()
        if extend:
            stack.append((node, False))
            for child in node.children():
                stack.append((child, True))
        else:
            for child in node.children():
                node.count += child.count
            if node.depth > 0:
                ans = mod(ans + mod(node.count * (node.count - 1) // 2))
    return ans

def pr(node):
    print(' ' * node.depth + '%s (%d:%d)' % (chr(node.data) if node.data else ' ', node.depth, node.count))
    for child in node.children():
        pr(child)

def score(string):
    # ascii values
    string = list(map(ord, string))
    N = len(string)*2 + 1
    c = [0] * N
    c[1::2] = string
    # initialize trie pointers
    odd = trie(depth = -1)
    even = trie()
    center, radius = 0, 0
    left, right = 0, 0
    # manacher's algorithm
    node = [even]
    span = [0]
    for i in range(1, N):
        if i > radius:
            node.append(odd.get(c[i]) if (i & 1) else even)
            span.append(0)
            left = i - 1
            right = i + 1
        else:
            mirror = center * 2 - i
            if span[mirror] < radius - i:
                span.append(span[mirror])
                node.append(node[mirror])
                left = -1
            else:
                span.append(radius - i)
                node.append(node[mirror])
                while node[i].depth > radius - i:
                    node[i] = node[i].parent
                right = radius + 1
                left = i * 2 - right
        while left >= 0 and right < N and c[left] == c[right]:
            if c[right]:
                node[i] = node[i].get(c[right])
            span[i] += 1
            left -= 1
            right += 1
        node[i].count += 1
        if i + span[i] > radius:
            center = i
            radius = i + span[i]
    # accumulate count
    return mod(dfs(odd) + dfs(even))
    
print(score(str(input())))


