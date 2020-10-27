


"""
Given 2 strings, write a method to decide if one is a permutation of the other.
"""
def permutation(string1, string2):
    if(string1 == None or string2 == None):
        return False #assuming if None, invalid input, rather than considering case of if both None
    chardict1 = {}
    chardict2 = {}
    for char in string1:
        if char not in chardict1:
            chardict1[char] = 1
        else:
            chardict1[char] += 1
    for char in string2:
        if char not in chardict2:
            chardict2[char] = 1
        else:
            chardict2[char] += 1
    return chardict1 == chardict2

assert(permutation("aaaccc", "ccaaca") == True)
assert(permutation("!$#!", "#$!!") == True)
assert(permutation("", "23") == False)
assert(permutation(None, None) == False) # assuming any None would be invalid input



"""
Let's have a singly linked list
"""
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

"""
Let's make a Stack
"""
class Stack:
    def __init__(self):
        self.list = []
    def add(self, value):
        self.list.append(value)

    def peek(self):
        return self.list[-1]
    def pop(self):
        self.list = self.list[:len(self.list)-1]
        return self.list[-1]