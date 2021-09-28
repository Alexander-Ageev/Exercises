from main import Node, LinkedList

def sum_list1(list_1, list_2):
    if list_1.len() == list_2.len():
        super_list = []
        node_1, node_2 = list_1.head, list_2.head
        while node_1 != None:
            super_list.append(node_1.value + node_2.value)
            node_1 = node_1.next
            node_2 = node_2.next
        return super_list

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
n2 = Node(2)
n3 = Node(3)
s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(n3)

k1 = Node(1)
k2 = Node(2)
k3 = Node(3)
f_list = LinkedList()
f_list.add_in_tail(k1)
f_list.add_in_tail(k2)
f_list.add_in_tail(k3)

f = sum_list(s_list, f_list)
print(f.list_all_nodes()) 