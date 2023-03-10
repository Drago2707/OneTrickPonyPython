"""Parse a linked list from a string
Create a function parse which accepts exactly one argument 

string 
which is a string representation of a linked list. 

Your function must return the corresponding linked list, constructed from instances of the 
Node class/struct/type. The string representation of a list has the following format:

the value of the node, followed by a whitespace, an arrow and another whitespace
(" -> "), followed by the rest of the linked list. Each string representation of a
linked list will end in None

... your function should return:

For the simplicity of this Kata, the values of the nodes in the string 
representation will always ever be non-negative integers, so the following 
would not occur:
"Hello World -> Goodbye World -> 123 -> None" 

This also means that the values of each Node must also be non-negative
integers so keep that in mind when you are parsing the list from the string.
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(string: str):
    if string == "None":
        return None
    # list_string = string.split()
    # if len(list_string) == 1:
    #     return Node(int(string), None)
    # list_string = [element for element in list_string if not element in ["->","None"]]
    # return Node(element for element in list_string)
# NT you can do it
    elements = list(map(int,string.split(" -> ")[:-1]))
    head = None
    for i in reversed(range(len(elements))):
        head = Node(elements[i], head)
    return head


# head = Node(0, Node(1, Node(4, Node(9, Node(16)))))
print(linked_list_from_string("0"))
print(linked_list_from_string("0 -> 10 -> 20 -> 30 -> None"))
