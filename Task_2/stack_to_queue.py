'''Lab 12.2'''

from arraystack import ArrayStack
from arrayqueue import ArrayQueue


def stack_to_queue(stack):
    '''
    stack to queue
    '''
    return ArrayQueue(list(stack)[::-1])

test = ArrayStack()

stack = ArrayStack()
for i in range(10):
   stack.add(i)
queue = stack_to_queue(stack)
print(queue)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(stack)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(stack.pop())
# 9
print(queue.pop())
# 9
stack.add(11)
queue.add(11)
print(queue)
# [8, 7, 6, 5, 4, 3, 2, 1, 0, 11]
print(stack)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]