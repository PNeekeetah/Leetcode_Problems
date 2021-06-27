class ListNode:
    def __init__ (
            self, 
            val : int, 
            next_node : "ListNode" = None,
            prev_node : "ListNode" = None,
        ):
        self.val = val
        self.next = next_node
        self.prev = prev_node
    
    def get_prev (self):
        return self.prev
            
    def get_next (self):
        return self.next
    
    def get_val (self):
        return self.val
    
    def set_prev (
            self, 
            prev_node : "ListNode"
        ):
        self.prev = prev_node
    
    def set_next (
            self, 
            next_node : "ListNode"
        ):
        self.next = next_node
        
    def set_val (
            self, 
            val : int
        ):
        self.val = val
        
def advance_one(node : "ListNode") -> "ListNode":
    if node is not None:
        return node.next
    else:
        return None
    
def traverse_list (
        node : "ListNode",
        number_of_nodes : int, 
    ):
    current = node
    while number_of_nodes > 0:
        current = advance_one(current)
        number_of_nodes -= 1
    return current
    
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.linked_list_length = 0
        
    def _increase_length(self):
        self.linked_list_length += 1
    
    def _decrease_length(self):
        self.linked_list_length -= 1
    
    def _get_length(self):
        return self.linked_list_length
     
    def _initialize(self, val : int) -> None:
        self.head = ListNode(val)
        
    def get(
            self, 
            index: int
        ) -> int:
        if index >= self._get_length():
            return -1
        node = traverse_list(
            self.head,
            index,
        )
        return node.val

    def addAtHead(
            self, 
            val: int
        ) -> None:
        if self.head is None:
            self._initialize(val)
        else:
            new_node = ListNode(val)
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
        self._increase_length()

    def addAtTail(
            self, 
            val: int
        ) -> None:
        current = self.head
        current = traverse_list(
            current,
            self._get_length()-1,
        )
        new_node = ListNode(val)
        new_node.set_prev(current)
        current.set_next(new_node)
        self._increase_length()

    def addAtIndex(
            self, 
            index: int, 
            val: int
        ) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self._get_length():
            self.addAtTail(val)
        else:
            current = self.head
            current = traverse_list(
                current,
                index-1,
            )
            next_node = current.get_next()
            new_node = ListNode(val)
            new_node.set_prev(current)
            new_node.set_next(next_node)
            current.set_next(new_node)
            next_node.set_prev(new_node)
            self._increase_length()

    def deleteAtIndex(
            self, 
            index: int
        ) -> None:
        if index >= self._get_length():
            return
        
        if index == 0:
            if self._get_length() == 1:
                self.head = None
            else:
                self.head = self.head.get_next()
                self.head.set_prev(None)
        elif index == self._get_length():
             current = self.head 
             current = traverse_list(
                 current,
                 self._get_length(),
             )
             previous = current.get_prev()
             previous.set_next(None)
             current.set_prev(None)
        else:
            current = self.head 
            current = traverse_list(
                current,
                index,
            )
            previous = current.get_prev()
            next_node = current.get_next()
            previous.set_next(next_node)
            next_node.set_prev(previous)
            current.set_next(None)
            current.set_prev(None)
        self._decrease_length()

funcs = ["addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
args = [[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]

f = 0
mll = MyLinkedList()
for i in range (len(funcs)):
    exec("mll.{func}({arg})".format(func=funcs[i],arg=args[i][0]))
    f += 1