'''Lab 12.2'''

from arrayqueue import ArrayQueue
from arraystack import ArrayStack

def queue_to_stack(queue):
    '''
    queue to stack
    '''
    return_elem = ArrayStack()
    for elem in list(queue)[::-1]:
        return_elem.add(elem)
    return return_elem

test = ArrayQueue()
