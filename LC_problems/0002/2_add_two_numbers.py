# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        vaddi = 0
        nextExists = True
        final = ListNode()
        count = 0
        while nextExists:
            
            mySum = l1.val + l2.val + vaddi
            vaddi = int(mySum/10) if mySum > 9 else 0
            
            if final.val == 0 and final.next is None and count < 1:
                final =  ListNode(int(str(mySum)[-1]), next= None)
                temp = final
            else:
                temp.next = ListNode(int(str(mySum)[-1]), next= None)
                temp = temp.next

            count = count + 1

            if (l1.next) and (l2.next):
                l1 = l1.next
                l2 = l2.next
            elif (l1.next):
                l1 = l1.next
                l2.val = 0
            elif (l2.next):
                l2 = l2.next
                l1.val = 0
            else:
                if vaddi > 0:
                    temp.next = ListNode(vaddi, next= None)
                return final


list1 = [2, 4, 3]
list2 = [5, 6, 4]

ff = Solution()
ff.addTwoNumbers(ListNode(list1[0], list1[1:]), ListNode(list2[0], list2[1:]))

# def addNums(l1, l2):
#     liNew = []
#     sum = int(''.join(map(str,l1[::-1]))) + int(''.join(map(str,l2[::-1])))
#     if sum == 0:
#         return [sum]
#     else:
#         while sum > 0:
#             last = sum%10
#             sum = int(sum / 10)
#             liNew.append(last)
#         return liNew


# sum = addNums([2,4,3], [5,6,4])
# print(sum)
# sum = addNums([0], [0])
# print(sum)
# sum = addNums([9,9,9,9,9,9,9], [9,9,9,9])
# print(sum)


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         gg = True
#         while gg:
#             print(l1.next == None)
#             if len(l1.next.val) > 1:
#                 output = l1.val + l2.val
#                 print(output)
#                 l1 = l1.next
#                 l2 = l2.next
#             else:
#                 gg = False


# list1 = [2,4,3]
# list2 = [5,6,4]

# def list_to_ListNode(arr):
#     if len(arr) > 1:
#         return ListNode(arr[0], ListNode(arr[1:]))
#     else:
#         return ListNode(arr[0])

# if __name__ == "__main__":
#     ff = Solution()
#     l1 = list_to_ListNode(list1)
#     l2 = list_to_ListNode(list2)
#     ff.addTwoNumbers(l1, l2)
