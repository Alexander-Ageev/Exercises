from main import Node, LinkedList

def sum_list(list_1, list_2):
    if list_1.len() == list_2.len():
        super_list = LinkedList()
        node_1, node_2 = list_1.head, list_2.head
        while node_1 != None:
            super_node = Node(node_1.value + node_2.value)
            super_list.add_in_tail(super_node)
            node_1 = node_1.next
            node_2 = node_2.next
        return super_list


n1 = Node(1)
s_list = LinkedList()
s_list.add_in_tail(n1)
print(s_list.get_head_tail())
