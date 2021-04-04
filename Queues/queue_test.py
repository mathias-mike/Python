from queue_list import Queue as queue_l
from queue_circular import Queue as queue_c
from queue_linkedlist import Queue as queue_ll

print("\n ---------------------------List------------------------------------\n")
queue1 = queue_l()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(5)
print(queue1)
print(queue1.peek())
print(queue1.dequeue())
print(queue1.dequeue())
print(queue1)

print("\n\n----------------List with capacity (Circular)------------------------\n")
queue2 = queue_c(10)
queue2.enqueue(1)
queue2.enqueue(2)
queue2.enqueue(3)
queue2.enqueue(4)
queue2.enqueue(5)
print(queue2)
print(queue2.peek())
print(queue2.dequeue())
print(queue2.dequeue())
print(queue2)
print("List capacity", queue2.capacity)


print("\n\n----------------------Linked list-------------------------------\n")
queue3 = queue_ll()
queue3.enqueue(1)
queue3.enqueue(2)
queue3.enqueue(3)
queue3.enqueue(4)
queue3.enqueue(5)
print(queue3)
print(queue3.peek())
print(queue3.dequeue())
print(queue3.dequeue())
print(queue3)