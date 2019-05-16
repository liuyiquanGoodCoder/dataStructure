#create List

#create the List's structure and output
class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

head = None
for count in range(1,6):
    head = Node(count,head)

while head != None:
    print(head.data)
    head = head.next


#ergodic
probe = head
while probe != None:
    probe = probe.next

#search
#targetItem 查找的目标数字
targetItem = 1
probe = head
while probe != None and targetItem != probe.data:
    probe = probe.next
if probe != None:
    print("target is found")
else:
    print("target is not in this linked structure")

#访问链表中的第i(index)项
probe = head
index = 5
while index > 0:
    probe = probe.next
    index -= 1

print(probe.data)

#replace
#若目标不存在，返回false，否则替换相应的项，并返回true
probe = head
newItem = 5
class SolutionOne:
    def replaceFuc(self,probe,newItem):
        while probe != None and newItem != probe.data:
            probe = probe.next

        if probe != None:
            probe.data = newItem
            return True
        else:
            return False

#开始处插入
head = Node(newItem,head)

#在末尾插入
#一、head的指针为None，此时代码将搜索最后一个节点，并将其next指针指向新的节点
#二、head不为None，此时代码将搜索最后一个节点，并将其next指针指向新的节点

newNode = Node(newItem)
if head is None:
    head = newItem
else:
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = newNode

#从开始处删除
head = head.next

#从末尾删除
#一、只有一个节点，head指针设置为None
#二、在最后一个节点之前没有节点，只需要倒数第二个节点的next指向None即可
if head.next is None:
    head = None
else:
    probe = head
    while probe.next.next != None:
        probe = probe.next
    probe.next = None

#在任何位置插入
#一、该节点的next指针为None。这意味着，i>=n，因此，应该将新的项放在链表结构末尾
#二、该节点的next指针不为None，这意味这，0<i<n,因此需将新的项放在i-1和i之间
if head is None or index <= 0:
    head = Node(newItem,head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
    probe.next = Node(newItem,probe.next)

#在任意位置删除
#一、i<=0 使用删除第一项的代码
#二、0<i<n 搜索位于i-1位置的节点，删除其后面的节点
#三、i>n 删除最后一个节点

if index <= 0 or head.next is None:
    head = head.next
else:
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1

probe.next = probe.next.next






# class ListNode:
#     def __init__(self,x):
#         self.val = x
#         self.next = None

class Solution:
    def printListFromTailToHead(self,ListNode):
        result = []
        while ListNode:
            result.insert(0,ListNode.val)
            ListNode = ListNode.next
        return result

    #删除链表中重复的点
    def deleteDuplication(self,pHead):
        pPre = None
        pCur = pHead
        pNext = None
        while pCur != None:
            if pCur.next != None and pCur.val == pCur.next.val:
                pNext = pCur.next
                while pNext.next != None and pNext.next.val == pCur.val:
                    pNext = pNext.next




