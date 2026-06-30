class MyQueue :   # Defines a class MyQueue that simulates a queue using two stacks.
          
    '''
    Construter
    '''
    def __init__(self):      # Initializes two lists (stack_in and stack_out) to act as stacks
        self.stack_in = []     # stack_in: Used to store elements when they are pushed (enqueue)
        self.stack_out = []    # stack_out handles all popping and peeking
    
    def push(self, x: int) -> None:
        self.stack_in.append(x)    #  Adds a new element x to stack_in

    def _move_elements(self):     # A  method to move elements only when necessary
        if not self.stack_out:    # Transfers elements from stack_in to stack_out, but only if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def pop(self)  -> int :      # Ensure stack_out has the oldest elements
        self._move_elements()     # Calls _move_elements() to ensure correct order
        return self.stack_out.pop()  # Removes and returns the front element of the queue (top of stack_out)
    
    def peek(self) -> int :     # Ensure stack_out has the oldest elements
        self._move_elements()     # Calls _move_elements() if needed
        return self.stack_out[-1]   # Returns the front element without removing it (last element of stack_out)
    
    def empty(self)  -> bool:
        return not self.stack_in and not self.stack_out  #Returns True if both stacks are empty, meaning the queue has no elements
