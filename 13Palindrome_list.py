'''
Q: 연결리스트가 팰린드롬 구조인지 판별하기

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
'''

class Listnode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

#리스트 활용
class solution(object):
    def isPalimdrome(self, head):
        q = []

        if not head:
            return True

        node = head

        while node:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True

# deque 활용
# Definition for singly-linked list.

import collections

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        q = collections.deque()

        if not head:
            return True

        node = head

        while node:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True