# Part of Cosmos by OpenGenus Foundation

Queue = {'front': None, 'back': None}

class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next  
    
def Enqueue(Queue, element):
  N = Node(element, None)
  if Queue['back'] is None:
    Queue['front'] = N
    Queue['back'] = N
  else:
    Queue['back'].next = N
    Queue['back'] = Queue['back'].next
    
def Dequeue(Queue):
  if Queue['front'] is None:
    if Queue['back'] != None:
      Queue['back'] = None
    return 'Cannot dequeue because queue is empty'

  else:
    first = Queue['front']
    Queue['front'] = Queue['front'].next
    return first.data

Enqueue(Queue, 'a')
Enqueue(Queue, 'b')
Enqueue(Queue, 'c')
print Dequeue(Queue)
