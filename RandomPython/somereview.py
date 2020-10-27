


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
    def toList(self):
        currentNode = self
        list = []
        while(currentNode != None):
            list.append(currentNode.val)
            currentNode = currentNode.next
        return list

"""
Write code to remove duplicates from an unsorted linked list
Assumption: linked list is singly linked
"""
def rmvduplicates(head):
    if(head == None):
        return head
    charexists = set() #set
    prevNode = head # default
    currentNode = head
    while(currentNode != None):
        if(currentNode.val in charexists):
            # if value is in the set, means it already exists, so we must remove it
            prevNode.next = currentNode.next # prev skips current
        else:
            charexists.add(currentNode.val)
        prevNode = currentNode
        currentNode = currentNode.next
    return head

# let's run a little test
# feed this linkedlist into rmvduplicates
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(3)

# should get this result linkedlist
head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(3)

assert(rmvduplicates(head).toList() == head2.toList())


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

"""
Let's make a Queue
"""
class Queue:
    def __init__(self):
        self.list = []
    def add(self, value):
        self.list.append(value)
    def remove(self):
        toberemoved = self.list[0]
        self.list = self.list[1:-1]
        return toberemoved
