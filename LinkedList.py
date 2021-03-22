"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


class Item:
    def __init__(self, data):
        self.data = data
        self.next = None


class CustomList:

    def __init__(self, *data):
        self.start_node = None
        for i in data:
            self.append(i)

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.data, " ", end='')
                n = n.next

    def append(self, value):
        new_node = Item(value)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.next = new_node

    def add_start(self, value):
        new_node = Item(value)
        new_node.next = self.start_node
        self.start_node = new_node

    def remove(self, value):
        if self.start_node.data == value:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.next is not None:
            if n.next.data == value:
                break
            n = n.next

        if n.next is None:
            raise ValueError
        else:
            n.next = n.next.next

    def __getitem__(self, index):
        try:
            if self.start_node is None:
                return
            n = self.start_node
            temp_index = 0
            while n is not None:
                if temp_index == index:
                    return n.data
                n = n.next
                temp_index += 1
        except:
            raise IndexError

    def __setitem__(self, index, data):
        try:
            if index > self.__len__() - 1:
                raise IndexError
            if self.start_node is None:
                return
            n = self.start_node
            temp_index = 0
            while n is not None:
                if temp_index == index:
                    n.data = data
                n = n.next
                temp_index += 1
        except:
            raise IndexError

    def __delitem__(self, index):
        temp_index = 0
        if temp_index == index:
            self.start_node = self.start_node.next
            return

        n = self.start_node
        while n.next is not None:
            if temp_index == index:
                break
            n = n.next
            temp_index += 1

        if n.next is None:
            raise IndexError
        else:
            n.data = n.next.data
            n.next = n.next.next

    def find(self, value):
        if self.start_node is None:
            return
        n = self.start_node
        index = 0
        while n is not None:
            if n.data == value:
                return index
            n = n.next
            index += 1
        raise ValueError

    def clear(self):
        for i in range(self.__len__()):
            self.start_node = self.start_node.next

    def __len__(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        length = 0
        while n is not None:
            length += 1
            n = n.next
        return length

    def __iter__(self):
        n = self.start_node
        while n is not None:
            yield n.data
            n = n.next



