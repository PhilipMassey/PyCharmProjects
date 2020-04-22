class Node:
    def __init__(self, data):
        self.l_node = None
        self.r_node = None
        self.data = data

    def __repr__(self):
        return "data {0}".format(self.data)
        #return " data {0}, l_node {1}, r_node {2}\n".format(self.data, self.l_node, self.r_node)



def insert_node(root, node):
    if root is None:
        root = node
    if node.data > root.data:
        if root.l_node is None:
            root.l_node = node
        else:
            insert_node(root.l_node, node)
    else:
        if root.r_node is None:
            root.r_node = node
        else:
            insert_node(root.r_node, node)


def preOrderPrint(node):
   # print('node ' + str(node.data))
    if node.r_node is not None:
        preOrderPrint(node.r_node)
    print(node.data, end=',')
    if node.l_node is not None:
        preOrderPrint(node.l_node)


def inOrderPrint(node):
    # print('node {0}'.format(node.data))
    if node.l_node is not None:
        inOrderPrint(node.l_node)
    print(node.data, end=',')
    if node.r_node is not None:
        inOrderPrint(node.r_node)


top = Node(3)
insert_node(top, Node(2))
insert_node(top, Node(1))
insert_node(top, Node(7))
insert_node(top, Node(6))
insert_node(top, Node(5))
insert_node(top, Node(4))
#insert_node(top, Node(9))
#insert_node(top, Node(8))
#insert_node(top, Node(12))
#insert_node(top, Node(11))

#inOrderPrint(top)
print()
preOrderPrint(top)