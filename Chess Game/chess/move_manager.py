class MoveManager:
    def __init__(self):
        self.undo_stack = []  
        self.redo_stack = []  

    def record_move(self, move):
        self.undo_stack.append(move)
        self.redo_stack.clear()  

    def undo(self):
        if self.undo_stack:
            move = self.undo_stack.pop()
            self.redo_stack.append(move)
            return move  
        return None

    def redo(self):
        if self.redo_stack:
            move = self.redo_stack.pop()
            self.undo_stack.append(move)
            return move  
        return None
