'''Lab 12.2'''

from arraystack import ArrayStack
from arrayqueue import ArrayQueue


def stack_to_queue(stack):
    '''
    stack to queue
    '''
    return_elem = ArrayQueue()
    for elem in list(stack)[::-1]:
        return_elem.add(elem)
    return return_elem

test = ArrayStack()
