class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def transfer_board(self, board):
        for row in board:
            for cell in row:
                self.insert(cell)

    def traverse_to_board(self, board):
        node = self.head
        for i in range(8):
            for j in range(8):
                if node:
                    board[i][j] = node.element
                    node = node.next
