class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        vals = []
        curr = self
        while curr != None:
            vals.append(curr.val)
            curr = curr.next
        return str(vals)
    
def mergeTwoLists(list1, list2):
    new = None
    next = None
    head = None
    while list1 != None and list2 != None:
        if list1 == None or list1.val > list2.val:
            next = list2
            list2 = list2.next
        elif list2 == None or list2.val >= list1.val:
            next = list1
            list1 = list1.next
        
        if head == None:
            new = next
            head = new
        else:
            new.next = next
            new = new.next
            new.next = None
        next = None
    if list1 == None and list2 != None:
        if new == None:
            new = list2
            head = new
        else:
            new.next = list2
    elif list2 == None and list1 != None:
        if new == None:
            new = list1
            head = new
        else:
            new.next = list1
    
    return head


list1 = ListNode(1)
list2 = None
print(mergeTwoLists(list1, list2))
