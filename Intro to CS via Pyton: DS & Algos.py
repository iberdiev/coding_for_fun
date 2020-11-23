def fib(n):
    """
    >>> l = []
    >>> for i in range(10):
    ...     l.append(fib(i))
    >>> l
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    return 1 if n == 0 or n == 1 else fib(n-1) + fib(n-2)


class Point():
    """
    Object Point allow to create a points of Cartesian plane.

    >>> point1 = Point(3,4)
    >>> point1.get()
    (3, 4)
    >>> point1.zero_distance()
    5.0
    """
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({},{})'.format(self.x, self.y)
    
    def get(self):
        return self.x, self.y

    def zero_distance(self):
        return (self.x**2+self.y**2)**(1/2)

    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**(1/2)
    
    def midpoint(self, point):
        if self.x > point.x:
            mid_x = self.x - point.x
        else:
            mid_x = point.x - self.x
        if self.y > point.y:
            mid_y = self.y - point.y
        else:
            mid_y = point.y - self.y
        return (mid_x, mid_y)
            
class RationalNumber():
    
    def __init__(self,num:int,denom:int=1):

        self.num, self.denom = num, denom
        self._invariant()
        
    def __str__(self)-> str:
        return '({}, {})'.format(self.num, self.denom)

    def __eq__(self, other):
        return (self.num*other.denom) == (other.num*self.denom)and(type(self)==type(other))

    def __lt__(self, other):
        return (self.num * other.denom < self.denom * other.num if self.denom * other.denom > 0 else self.num * other.denom > self.denom * other.num)

    def __mul__(self, other):
        return RationalNumber(self.num*other.num, self.denom*other.denom)
    
    def __add__(self, other):
        return (self.num*other.denom + self.denom*other.num)/ self.denom*other.num
    
    def _invariant(self):
        assert self.denom != 0, 'Aero self.denom!: {}/{}'.format(self.num, self.denom)

class Person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

class Student(Person):
    def __init__(self, name, num):
        Person.__init__(self, name)
        self.num = num 

class Rect():

    def __init__(self, corners):
        self.corners = corners[:]
    
    def area(self):
        """
        >>> asdf = Rect([Point(0,0),Point(4,0),Point(4,4),Point(0,4)])
        >>> asdf.area()
        16.0
        """
        return ((self.corners[0].distance(self.corners[1]))
              *(self.corners[1].distance(self.corners[2])))
    
    def perimeter(self):
        """
        >>> asdf = Rect([Point(0,0),Point(4,0),Point(4,4),Point(0,4)])
        >>> asdf.perimeter()
        16.0
        """
        return ((self.corners[0].distance(self.corners[1]))
              +(self.corners[1].distance(self.corners[2])))*2

class Triangle():

    def __init__(self, corners):
        self.corners = corners[:]
        
    def perimeter(self):
        """
        >>> asdf = Triangle([Point(0,0),Point(4,0),Point(0,3)])
        >>> asdf.perimeter()
        12.0
        """
        a = self.corners[0].distance(self.corners[1])
        b = self.corners[1].distance(self.corners[2])
        c = self.corners[2].distance(self.corners[0])
        return (a + b + c)

    def area(self): ## Geron's formula for any triangle
        """
        >>> asdf = Triangle([Point(0,0),Point(10,0),Point(0,10)])
        >>> asdf.area()
        50.0
        """
        return (((self.perimeter()/2)
               *((self.perimeter()/2)-self.corners[0].distance(self.corners[1]))
               *((self.perimeter()/2)-self.corners[1].distance(self.corners[2]))
               *((self.perimeter()/2)-self.corners[2].distance(self.corners[0])))
               **(1/2))

class Stack():
    def __init__(self, data):
        """
        Initiating an Abstract Object.
        >>> asdf = Stack([1,2,3])
        >>> type (asdf)
        <class '__main__.Stack'>
    
        """
    
        self.data = data
        
    def __str__(self):
        """
        String representation of the abstract Object.
        >>> asdf = Stack([1,2,3])
        >>> print (asdf)
        [1, 2, 3]
        """
        return str(self.data)
    
    def length(self):
        """
        Method that determines the length of the abstract object.
        >>> asdf = Stack([1,2,3])
        >>> asdf.length()
        3
        """
        return len(self.data)

    def put(self, item):
        """
        Method that puts an item to the abstract object.
        >>> asdf = Stack([1,2,3])
        >>> asdf.put(4)
        >>> print (asdf)
        [1, 2, 3, 4]
        """
        self.data.append(item)
        return None
    
    def peek(self):
        if self.data:
            return self.data[-1]
        else:
            return 'No data'

    def remove(self):
        """
        Method that deletes an item to the abstract object.
        >>> asdf = Stack([1,2,3])
        >>> asdf.remove()
        >>> print (asdf)
        [1, 2]
        """
        if self.data:
            self.data.pop(-1)
            return None
        else:
            return "Nothing to remove"

    def is_empty(self):
        """
        Method that checks if the abstract object is empty. Return True if empty, and False if not.
        >>> asdf = Stack([1])
        >>> asdf.is_empty()
        False
        >>> asdf.remove()
        >>> asdf.is_empty()
        True
        """
        if self.length() > 0:
            return False
        else:
            return True

def is_balanced_all(line):
    """
    Function that checks if the string is balanced or not.
    >>> is_balanced_all('({{(sdsdf),(dvdvdv)sdfsd}sdfsdf})')
    True
    >>> is_balanced_all(')(')
    False
    """
    asdf = Stack([])
    for letter in line:
        if letter == '(' or letter == '[' or letter == '{':
            asdf.put(letter)
        elif letter == ')':
            if asdf.is_empty():
                asdf.put(letter)
            else:
                if asdf.peek() == '(':
                    asdf.remove()
                else:
                    asdf.put(letter)
        elif letter == ']':
            if  asdf.is_empty():
                asdf.put(letter)
            else:
                if asdf.peek() == '[':
                    asdf.remove()
                else:
                    asdf.put(letter)
        elif letter == '}':
            if asdf.is_empty():
                asdf.put(letter)
            else:
                if asdf.peek() == '{':
                    asdf.remove()
                else:
                    asdf.put(letter)
    return asdf.is_empty()

class Node():

    def __init__(self, dataval = None):
        """
        Initializing an instance of class Node.
        >>> asdf = Node()
        >>> type(asdf)
        <class '__main__.Node'>
        """
        self.dataval = dataval
        self.nextval = None

    def get_value(self):
        """
        Getting the value of the Node.
        >>> asdf = Node(1)
        >>> asdf.get_value()
        1
        """        
        return self.dataval

    def get_next(self):
        """
        Getting the value of the Node.
        >>> asdf = Node(1)
        >>> asdf.set_next(Node(2))
        >>> asdf.get_next().get_value()
        2
        """        
        return self.nextval
    
    def set_value(self, newVal):
        """
        Setting new value to the instance.
        >>> asdf = Node(1)
        >>> asdf.get_value()
        1
        >>> asdf.set_value(1.0)
        >>> asdf.get_value()
        1.0
        """   
        self.dataval = newVal

    def set_next(self, next_val):
        """
        Setting next value to the instance.
        >>> asdf = Node(1)
        >>> asdf.get_value()
        1
        >>> asdf.set_value(1.0)
        >>> asdf.get_value()
        1.0
        """   
        self.nextval = next_val

    def is_empty(self):
        return not self.dataval

    def __str__(self):
        return str(self.dataval)

class LinkedList:
    def __init__(self):
        """
        Initializing an instance of class LinkedList
        >>> asdf = LinkedList()
        >>> type(asdf)
        <class '__main__.LinkedList'>
        """ 
        self.headval = None

    def listprint(self):
        """
        Prints the Linked List.
        >>> asdf = LinkedList()
        >>> asdf.headval = Node(1)
        >>> asdf.headval.nextval = Node(2)
        >>> asdf.headval.nextval.nextval = Node(3)
        >>> asdf.listprint()
        '[1, 2, 3, ]'
        """ 
        printval = self.headval
        listString = '['
        while printval is not None:
            listString += str(printval.dataval) + ', '
            printval = printval.nextval
        listString += ']'
        return listString

    def addb(self, newdata):
        """
        Adding an element to the beginning of the list.
        >>> asdf = LinkedList()
        >>> asdf.addb(1)
        >>> asdf.addb(2)
        >>> print(asdf)
        [2, 1, ]
        """
        newNode = Node(newdata)
        newNode.nextval = self.headval
        self.headval = newNode

    def adde(self,newdata):
        """
        Adding an element to the end of the list.
        >>> asdf = LinkedList()
        >>> asdf.adde(1)
        >>> asdf.adde(2)
        >>> print(asdf)
        [1, 2, ]
        """  
        newNode = Node(newdata)
        if self.headval is None:
            self.headval = newNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = newNode

    def removeb(self):
        """
        Removes an item from the beginning of the LinkedList, and returns removed item.
        >>> asdf = LinkedList()
        >>> asdf.adde(1)
        >>> asdf.adde(2)
        >>> asdf.removeb()
        1
        >>> print(asdf)
        [2, ]
        
        """
        value = None
        if not self.is_empty():
            value = self.headval.dataval
            self.headval = self.headval.nextval
        return value

    def removee(self):
        """
        Removes an item from the end of the LinkedList, and returns removed item.
        >>> asdf = LinkedList()
        >>> asdf.adde(1)
        >>> asdf.adde(2)
        >>> asdf.removee()
        2
        >>> print(asdf)
        [1, ]
        """
        value = None
        
        if self.size() > 1:
            last = self.headval
            while(last.nextval):
                node = last
                last = last.nextval
            node.nextval = None
            return last.dataval
        elif self.size() == 1:
            value = self.headval.dataval
            self.headval = None
            return value

    def size(self):
        """
        Returns the size of the list.
        >>> asdf = LinkedList()
        >>> asdf.adde(1)
        >>> asdf.adde(2)
        >>> asdf.size()
        2
        """
        item = self.headval
        
        if item == None:
            return 0
        elif item.nextval == None:
            return 1
        else:
            count = 1
            while (item.nextval):
                count = count + 1
                item = item.nextval
            return count

    def item(self,index,count=0):
        """
        Returns dataval of the Node with specified index in the LinkedList.
        >>> asdf = LinkedList()
        >>> asdf.adde(1)
        >>> asdf.adde(2)
        >>> asdf.adde(3)
        >>> asdf.item(0)
        1
        >>> asdf.item(1)
        2
        >>> asdf.item(2)
        3
        """
        item = self.headval
        while count != index:
            count +=1
            item = item.nextval
        return item.dataval

    def __str__(self):
        """
        String representation of the list
        >>> asdf = LinkedList()
        >>> asdf.addb(1)
        >>> asdf.adde(2)
        >>> asdf.adde(True)
        >>> print(asdf)
        [1, 2, True, ]
        """
        return self.listprint()

    def is_empty(self):
        return not self.headval

    def popPositiveIndex(self,i):
        node = self.headval
        if i == 0:
         return self.removeb()
        elif i == (self.size()-1):
            return self.removee()
        elif i > 0:
            while i != 1:
                node = node.nextval
                i -=1
            val = node.nextval.dataval
            node.nextval = node.nextval.nextval
        return val
        
def stprint1(asdf):
    """
    >>> a = Node(1)
    >>> b = Node(2)
    >>> c = Node(3)
    >>> a.set_next(b)
    >>> b.set_next(c)
    >>> stprint1(a)
    1
    2
    3
    """
    if not asdf.is_empty():
        print(asdf.dataval)
        if asdf.nextval:
            stprint1(asdf.nextval)

def stprint2(asdf):
    """
    >>> a = Node(1)
    >>> b = Node(2)
    >>> c = Node(3)
    >>> a.set_next(b)
    >>> b.set_next(c)
    >>> stprint2(a)
    3
    2
    1
    """
    if not asdf.is_empty():
        if asdf.nextval:
            stprint2(asdf.nextval)
        print(asdf.dataval)

class Queue:
    
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def hot_potato(name_list, num):
    queue = Queue()
    for name in name_list:
        queue.enqueue(name)
    for i in range(num):
        queue.enqueue(queue.dequeue())
        print(queue)
    return queue.dequeue()

class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop()
        
    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop(0)
        
    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def palindrome_checker(word):
    deque1 = Deque()
    deque2 = Deque()
    for ch in word:
        deque1.add_rear(ch)
        deque2.add_front(ch)
    return deque1.items == deque2.items

class Queue_LL:
    """
    Class Queue is the linear data structure (FIFO) that build with help of the class LinkedList.
    """
    def __init__(self):
        """
        Initializing an instance of Queue_LL
        >>> asdf = Queue_LL()
        >>> type(asdf)
        <class '__main__.Queue_LL'>
        """
        self.items = LinkedList()

    def enqueue(self, item):
        """
        Adds an item to the queue.
        >>> asdf = Queue_LL()
        >>> asdf.enqueue(1)
        >>> print(asdf)
        [1, ]
        """
        self.items.addb(item)

    def dequeue(self):
        """
        Removes the first item in queue, and returns it.
        >>> asdf = Queue_LL()
        >>> asdf.enqueue(1)
        >>> asdf.enqueue(2)
        >>> asdf.dequeue()
        1
        """
        if not self.items.is_empty():
            return self.items.removee()

    def is_empty(self):
        """
        Check if the queue is empty.
        >>> asdf = Queue_LL()
        >>> asdf.is_empty()
        True
        >>> asdf.enqueue(1)
        >>> asdf.is_empty()
        False
        """
        return self.items.is_empty()

    def size(self):
        """
        Returns number of items in queue.
        >>> asdf = Queue_LL()
        >>> asdf.size()
        0
        >>> asdf.enqueue(1)
        >>> asdf.size()
        1
        """
        return self.items.size()

    def __str__(self):
        """
        String representation of the queue as a list, where right side is front, left - end.
        >>> asdf = Queue_LL()
        >>> print(asdf)
        []
        """
        return self.items.listprint()

class Deque_LL:
    """
    Class Deque is the linear data structure that has 2 ends, and build with the help of class LinkedList.
    """
    def __init__(self):
        """
        Initializing an instance of Queue_LL
        >>> asdf = Deque_LL()
        >>> type(asdf)
        <class '__main__.Deque_LL'>
        """
        self.items = LinkedList()

    def add_front(self, item):
        """
        Adds an item to the front of the queue.
        >>> asdf = Deque_LL()
        >>> asdf.add_front(1)
        >>> asdf.add_front(2)
        >>> print(asdf)
        [1, 2, ]
        """
        self.items.adde(item)

    def add_rear(self, item):
        """
        Adds an item to the end of the queue.
        >>> asdf = Deque_LL()
        >>> asdf.add_rear(1)
        >>> asdf.add_rear(2)
        >>> print(asdf)
        [2, 1, ]
        """
        self.items.addb(item)

    def remove_front(self):
        """
        Removes the first item in the queue, and returns it.
        >>> asdf = Deque_LL()
        >>> asdf.add_front(1)
        >>> asdf.add_front(2)
        >>> asdf.remove_front()
        2
        """
        if not self.is_empty():
            return self.items.removee()
        
    def remove_rear(self):
        """
        Removes the last item the queue, and returns it.
        >>> asdf = Deque_LL()
        >>> asdf.add_rear(1)
        >>> asdf.add_rear(2)
        >>> asdf.remove_rear()
        2
        """
        if not self.is_empty():
            return self.items.removeb()
        
    def is_empty(self):
        """
        Check if the queue is empty.
        >>> asdf = Deque_LL()
        >>> asdf.is_empty()
        True
        >>> asdf.add_rear(1)
        >>> asdf.is_empty()
        False
        """
        return self.items.is_empty()

    def size(self):
        """
        Returns number of items in queue.
        >>> asdf = Deque_LL()
        >>> asdf.size()
        0
        >>> asdf.add_rear(1)
        >>> asdf.size()
        1
        """
        return self.items.size()

    def __str__(self):
        """
        String representation of the queue as a list, where right side is front, left - end.
        >>> asdf = Deque_LL()
        >>> print(asdf)
        []
        """
        return self.items.listprint()

def insert_noloop(index, node, LL, count=0, item=None):
    """
    Inserting an item by ID to the Linked List without using loops.
    >>> asdf = LinkedList()
    >>> asdf.adde(1)
    >>> asdf.adde(2)
    >>> asdf.adde(3)
    >>> asdfa = insert_noloop(2, Node(0), asdf)
    >>> print(asdfa)
    [1, 2, 0, 3, ]
    """  
    if index == 0:
        item = LL.headval
        LL.headval = node
        LL.headval.nextval = item
    elif index > 0 and count == 0:
        item = LL.headval
        insert_noloop(index, node, LL, count + 1, item = item)
    elif index > 0 and count > 0 and count != index:
        item = item.nextval
        insert_noloop(index, node, LL, count + 1, item)
    elif index == count:
        node.nextval = item.nextval
        item.nextval = node
    return LL.listprint()

def nexto(l):
    return l[1:]

def eliminate(x,l):
    if len(l)!=0:
        if x == l[0]:
            return nexto(l)
        else:
            a = eliminate(x,nexto(l))
            a.insert(0,l[0])
            return a

def sum_nest1(list1):
    """
    Function takes a list and returns the sum of all items in the list(+nested)
    >>> sum_nest1([1,1,[1,[1],[1,[[[1]]]]]])
    6
    """
    sum1 = []
    for item in list1:
        if type(item) == int:
            sum1.append(item)
        elif type(item) == list:
            sum1.append(sum_nest1(item))
    return sum(sum1)

def sum_nest2(l):
    """
    Function takes a list and returns the sum of all items in the list(+nested)
    >>> sum_nest2([1,1,[1,[1],[1,[[[1]]]]]])
    6
    """
    if l != []:
        if type(l[0]) == int:
            return l[0] + sum_nest2(l[1:])
        else:
            return sum_nest2(l[0]) + sum_nest2(l[1:])
    else:
        return 0

def find_depth(list1):
    """
    Takes the nested list and returns the deepest list order.
    >>> find_depth([[[],[],[]],[[],[[[[[]]]]]]])
    7
    """
    if type(list1) == int:
        return 0
    elif type(list1) == list:
        if list1 == []:
            return 1
        else:
            return max(find_depth(list1[0]) + 1, find_depth(list1[1:]))
        
def factorial(n):
    """
    Return factorial of n
    >>> factorial(3)
    6
    """
    return 1 if n==0 or n==1 else n * factorial(n-1)

def pascals_triangle(row):
    """
    Return n+1 rows of the pascals triangle
    >>> pascals_triangle(4)
    [1.0]
    [1.0, 1.0]
    [1.0, 2.0, 1.0]
    [1.0, 3.0, 3.0, 1.0]
    [1.0, 4.0, 6.0, 4.0, 1.0]
    """
    l = []
    for i in range(row+1):
        num = factorial(row)/(factorial(i)*factorial(row-i))
        l.append(num)
    if row > 0:
        print(pascals_triangle(row-1))
    return l

def sum_without_sum(n1, n2):
    """
    Finds the sum of 2 numbers represented as lists with their digits.
    >>> sum_without_sum([1,1,1],[9,9,9])
    [1, 1, 1, 0]
    """
    if len(n2) > len(n1):
        n1, n2 = n2, n1
    for i in range(len(n2)):
        n1[-(i+1)] += n2[-(i+1)]
    for i in range(len(n1)):
        if i == len(n1)-1 and n1[-(i+1)] > 9:
            n1[-(i+1)] -= 10
            n1.insert(0,1)
        elif n1[-(i+1)] > 9:
            n1[-(i+1)] -= 10
            n1[-(i+2)] += 1
    return n1

def sum_without_loop(n1,n2,r=0,count=0,s=[]):
    """
    Recursively adds 2 numbers represented as lists of digits.
    >>> sum_without_loop([9,9,9,9,9,9],[1],0,0,[])
    [1, 0, 0, 0, 0, 0, 0]
    >>> sum_without_loop([1,9],[8,0],0,0,[])
    [9, 9]
    >>> sum_without_loop([5,5],[5,5],0,0,[])
    [1, 1, 0]
    """
    if len(n2) > len(n1):
        n1, n2 = n2,n1
    if len(n1) != count:
        temp = n2[-(count+1)] if len(n2)>=count+1 else 0
        s.insert(0,(temp+n1[-(count+1)] + r))
        if s[-(count+1)] > 9:
            s[-(count+1)] -= 10
            sum_without_loop(n1,n2,1,count+1,s)
        else:
            sum_without_loop(n1,n2,0,count+1,s)
    elif r:
        s.insert(0,1) if len(s) == count else None
    return s

def sum_using_LL(n1,n2,r=0,count=0,s=LinkedList()):
    """
    Recursively adds 2 numbers represented as lists of digits using Linked List data structure.
    >>> n1 = LinkedList()
    >>> n2 = LinkedList()
    >>> n1.adde(1)
    >>> n2.adde(9)
    >>> n2.adde(9)
    >>> n2.adde(9)
    >>> sum_using_LL(n1,n2)
    '[1, 0, 0, 0, ]'
    """
    if n2.size() > n1.size():
        n1, n2 = n2, n1
    if n1.size() != count:
        temp = n2.item((n2.size()-1)-count) if n2.size() >= count+1 else 0
        s.addb((temp+ n1.item((n1.size()-1)-count) + r))
        if s.headval.dataval > 9:
            s.headval.dataval -= 10
            sum_using_LL(n1,n2,1,count+1,s)
        else:
            sum_using_LL(n1,n2,0,count+1,s)
    elif r:
        s.addb(1) if s.size() == count else None
    return s.listprint()

def max_len_of_conseq_ascend(l):
    """
    Function that takes a linked list and returns the max number of consecutive numbers that are in ascending order.
    >>> asdf = LinkedList()
    >>> asdf.adde(3)
    >>> asdf.adde(4)
    >>> asdf.adde(5)
    >>> asdf.adde(1)
    >>> asdf.adde(2)
    >>> asdf.adde(3)
    >>> asdf.adde(4)
    >>> asdf.adde(5)
    >>> max_len_of_conseq_ascend(asdf)
    5
    """
    count = 1
    m_list = []
    for i in range(l.size()-1):
        if l.item(i) <= l.item(i+1):
            count +=1
        else:
            m_list.append(count)
            count = 1
    m_list.append(count)
    return print(max(m_list))

def dec_to_bin(n):
    """
    Converts decimals to binary.
    >>> dec_to_bin(97644)
    10111110101101100
    """
    l = []
    r = None
    result = ''
    while n:
        r = n%2
        n = n//2
        l.insert(0,str(r))
    for i in l:
        result+=i
    return print(int(result))

def bin_to_dec(n):
    """
    Converts binary to decimals.
    >>> bin_to_dec(11011111111001110101100101111101101111101010111100)
    984738927409852
    """
    l = len(str(n))-1
    res = 0
    index = 0
    for i in str(n):
        res += int(str(n)[index]) * 2 ** l
        index +=1
        l -= 1
    return print(res)

def selection_sort(l,t='a'):
    """
    Sorting python list using SELECTION SORT in ascending order by default, put 'd' for descending order.
    >>> asdf = [5,2,8,4,7,1,6,7,7,7,3,2,5,7,3]
    >>> selection_sort(asdf,'d')
    [8, 7, 7, 7, 7, 7, 6, 5, 5, 4, 3, 3, 2, 2, 1]
    >>> selection_sort(asdf)
    [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 7, 8]
    """
    for i in range(len(l)):
        temp = l[i]
        temp1 = i
        for j in range(len(l)-1):
            if i < j+1:
                if (temp<l[j+1] if t=='d' else temp>l[j+1]):
                    temp = l[j+1]
                    temp1 = j+1
        l[i], l[temp1] = temp, l[i]      
    return l

def insertion_sort(l,t='a'):
    """
    Sorting python list using INSERTION SORT in ascending order by default, put 'd' for descending order.
    >>> asdf = [5,2,8,4,7,1,6,7,7,7,3,2,5,7,3]
    >>> insertion_sort(asdf,'d')
    [8, 7, 7, 7, 7, 7, 6, 5, 5, 4, 3, 3, 2, 2, 1]
    >>> insertion_sort(asdf)
    [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 7, 8]
    """
    for i in range(len(l)-1):
        l.insert(0, l.pop(i+1))
        count = 0
        while (l[count] < l[count+1] if t == 'd' else l[count] > l[count+1]):
            l[count], l[count+1] = l[count+1], l[count]
            count +=1
            if count > i:
                break
    return l

def bubble_sort(l,t='a'):
    """
    Sorting python list using BUBBLE SORT in ascending order by default, put 'd' for descending order.
    >>> asdf = [5,2,8,4,7,1,6,7,7,7,3,2,5,7,3]
    >>> bubble_sort(asdf,'d')
    [8, 7, 7, 7, 7, 7, 6, 5, 5, 4, 3, 3, 2, 2, 1]
    >>> bubble_sort(asdf)
    [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 7, 8]
    """
    n = len(l)-1
    while n != 0:
        for i in range(n):
            if (l[i] < l[i+1] if t =='d' else l[i] > l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
        n-=1
    return l

def merge_sort(l, t='a'):
    """
    Sorting python list using MERGE SORT in ascending order by default, put 'd' for descending order.
    >>> asdf = [5,2,8,4,7,1,6,7,7,7,3,2,5,7,3]
    >>> merge_sort(asdf,'d')
    [8, 7, 7, 7, 7, 7, 6, 5, 5, 4, 3, 3, 2, 2, 1]
    >>> merge_sort(asdf)
    [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 7, 8]
    """
    divide = len(l)//2
    l1, l2 = l[:divide], l[divide:]
    if divide > 0:
        l1, l2 = merge_sort(l1,t=t), merge_sort(l2,t=t)
    temp = []
    while l1 and l2:
        if (l1[0] > l2[0] if t =='d' else l1[0] < l2[0]):
            temp.append(l1.pop(0))
        else:
            temp.append(l2.pop(0))
    temp = temp + l1 + l2
    return temp

def quick_sort(l,t='a'):
    """
    Sorting python list using QUICK SORT in ascending order by default, put 'd' for descending order.
    >>> asdf = [5,2,8,4,7,1,6,7,7,7,3,2,5,7,3]
    >>> quick_sort(asdf,'d')
    [8, 7, 7, 7, 7, 7, 6, 5, 5, 4, 3, 3, 2, 2, 1]
    >>> asdf = [5,2,8,4,7,1,6,7,7,7,3,2,5,7,3]
    >>> quick_sort(asdf)
    [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 7, 8]
    """
    s1,s2 = [],[]
    if l:
        pivot = l.pop(0)
        for i in l:
            s1.append(i) if (i > pivot if t=='d' else i < pivot) else s2.append(i)
        s1, s2 = quick_sort(s1,t=t), quick_sort(s2,t=t)
        s1.append(pivot)
    return s1+s2

##import random
##from time import time
##import sys
##
##sys.setrecursionlimit(1100)
##
##asdf = random.sample(range(9999999),1000)
##
##t0 = time()
##selection_sort(asdf)
##t1 = time()
##
##t2 = time()
##insertion_sort(asdf)
##t3 = time()
##
##t4 = time()
##bubble_sort(asdf)
##t5 = time()
##
##t6 = time()
##merge_sort(asdf)
##t7 = time()
##
##t8 = time()
##quick_sort(asdf)
##t9 = time()
##
##print('selection_sort', t1-t0)
##print('insertion_sort', t3-t2)
##print('bubble_sort   ', t5-t4)
##print('merge_sort    ', t7-t6)
##print('quick_sort    ', t9-t8)

def numbers_from_2_to_n_LL(n, count = 2, l = LinkedList()):
##    """
##    Returns Linked List of natural numbers from 2 to n.
##    >>> numbers = None
##    >>> print(numbers_from_2_to_n_LL(15))
##    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ]
##    """
    if n > 1 and count!=n+1:
        l.adde(count)
        numbers_from_2_to_n_LL(n,count+1,l)
    return l

def eliminate_multiples_from_LL(n,l,count=0):
##    """
##    Takes linked list and removes all numbers which are divisible by n.
##    >>> numbers = None
##    >>> numbers = numbers_from_2_to_n_LL(15)
##    >>> print(eliminate_multiples_from_LL(5, numbers))
##    [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, ]
##    """
    if count != l.size():
        if (l.item(count) % n) == 0 and l.item(count)!=n:
            l.popPositiveIndex(count)
            eliminate_multiples_from_LL(n,l, count = count)
        else:
            eliminate_multiples_from_LL(n,l, count + 1)
    return l

def sieve_of_eratosthenes_recursive(n, l=None, count = 0):
##    """
##    Returns prime numbers from 2 to n in a Linked List using 2 functions above.
##    >>> numbers = None
##    >>> print(sieve_of_eratosthenes_recursive(50))
##    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, ]
##    """
    if count == 0:
        l = numbers_from_2_to_n_LL(n)
        eliminate_multiples_from_LL(l.item(count),l)
        sieve_of_eratosthenes_recursive(n, l, count+1)
    elif count < l.size():
        eliminate_multiples_from_LL(l.item(count),l)
        sieve_of_eratosthenes_recursive(n, l, count+1)    
    return l

def create(x):
    l = []
    if x == 2:
        return [2]
    elif x < 2:
        return "x must be an integer and more than 1"
    else:
        l += create(x-1)
        l.append(x)
    return l

def create(n,a=LinkedList()):
    if n == 2:
        a.adde(n)
    elif n < 2:
        return LinkedList()
    else:
        create(n-1)
        a.adde(n)
    return a

def elim(n,l,count=0):

    if count != l.size():
        if (l.item(count) % n) == 0 and l.item(count)!=n:
            l.popPositiveIndex(count)
            eliminate_multiples_from_LL(n,l, count = count)
        else:
            eliminate_multiples_from_LL(n,l, count + 1)
    return l

def elim(l,count=0):
    if l.item(0) == l.item(count+1):
        l.popPositiveIndex(count+1)
    else:
        elim(l,count+1)
        
def elimqqq(L,count=0,found=None,i=0):
    if L.item(count) % 2 == 0:
        elimqqq(L,count+1,found,i+1)
    else:
        if found == None:
            found = L.item(count)
        L.popPositiveIndex(i+1) if found == L.item(i+1) else elimqqq(L, count, found, i+1)
    return L

class LL:
    
    def __init__(self, value=None, nextval=None):
        self.value = value
        self.nextval = nextval
        if value != None:
            self.nextval = LL()

    def __str__(self):
        string, printval = '[', self
        while not printval.is_empty():
            string += str(printval.value) + ', '
            printval = printval.nextval
        string += ']'
        return string

    def is_empty(self):
        return True if self.value == None else False

    def appendend(self, value):
        if self.is_empty():
            self.value = value
            self.nextval = LL()
            return
        new, last = LL(value), self
        while not last.nextval.is_empty():
            last = last.nextval
        last.nextval = new
        
    def appendbegin(self,newVal):
        temp = LL(self.value)
        temp.nextval = self.nextval
        self.value = newVal
        self.nextval = temp
        return

    def remove_first_occurence(self, value):
        """
        >>> l1, LL = [1,2,4,5], LL()
        >>> for i in l1:
        ...     LL.appendend(i)
        >>> LL.remove_first_occurence(4)
        >>> print(LL)
        [1, 2, 5, ]
        """
        if not self.is_empty():
            if self.value == value:
                temp = self
                if not temp.nextval.is_empty():
                    self.value = temp.nextval.value
                    self.nextval = temp.nextval.nextval
                else:
                    self.value = None
                    self.nextval = None
                return
            else:
                return self.nextval.remove_first_occurence(value)

    def loop_insert_sorted(self, node):
        """
        >>> asdf = LL(0)
        >>> asdf.appendend(2)
        >>> asdf.appendend(4)
        >>> asdf.loop_insert_sorted(LL(3))
        >>> print(asdf)
        [0, 2, 3, 4, ]
        """
        temp = self
        while node.value > temp.nextval.value:
            temp = temp.nextval
            if temp.nextval == None:
                break
            
        node.nextval = temp.nextval
        temp.nextval = node
        return
    
    def recursive_insert_sorted(self, node):
        """
        >>> asdf = LL(0)
        >>> asdf.appendend(2)
        >>> asdf.appendend(4)
        >>> asdf.recursive_insert_sorted(LL(3))
        >>> print(asdf)
        [0, 2, 3, 4, ]
        """
        if self.is_empty():
            self.value = node.value
            self.nextval = LL()
        else:
            if node.value < self.value:
                temp = LL(self.value)
                temp.nextval = self.nextval
                self.value = node.value
                self.nextval = temp
            elif self.nextval.is_empty():
                self.nextval = node
            else:
                self.nextval.recursive_insert_sorted(node) 
        return

    def recursive_insert_final(self, node):
        """
        >>> asdf = LL(0)
        >>> asdf.appendend(2)
        >>> asdf.appendend(4)
        >>> asdf.recursive_insert_final(LL(5))
        >>> print(asdf)
        [0, 2, 4, 5, ]
        """
        if self.is_empty():
            self.value, self.nextval = node.value, LL()
        else:
            if node.value < self.value:
                temp, temp1 = self.value, self.nextval
                self.value, self.nextval = node.value, LL(temp, temp1)
            elif self.nextval == None:
                self.nextval = node
            else:
                return self.nextval.recursive_insert_final(node)

    def loop_cumulative_sum_LL(self, s_temp=0):
        """
        >>> asdf = LL()
        >>> for i in range(10):
        ...     asdf.appendend(i)
        >>> asdf.loop_cumulative_sum_LL()
        [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, ]
        """ 
        s = LL()
        temp = self
        while not temp.is_empty():
            s.appendend(temp.value + s_temp)
            s_temp = s_temp + temp.value
            temp = temp.nextval
        return print(s)
    
    def recursive_cumulative_sum_LL(self, t = 0, list1 = None, first = True):
        """
        >>> asdf = LL()
        >>> for i in range(10):
        ...     asdf.appendend(i)
        >>> print(asdf.recursive_cumulative_sum_LL())
        [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, ]
        """ 
        if self.is_empty():
            return print("List is empty.")
        else:
            if first:
                list1, first = LL(), False
            list1.appendend(self.value + t)
            temp = self
            if not temp.nextval.is_empty():
                temp.nextval.recursive_cumulative_sum_LL(self.value + t, list1,first)         
            return list1

    def loop_shuffle_odd_even_LL(self, switch = True):
        """
        >>> asdf = LL()
        >>> for i in range(20):
        ...     asdf.appendend(i)
        >>> l1, l2 = asdf.loop_shuffle_odd_even_LL()
        >>> print("List 1:", l1)
        List 1: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, ]
        >>> print("List 2:", l2)
        List 2: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, ]
        """
        l1, l2 = LL(), LL()
        temp = self
        while temp:
            if switch:
                l1.appendend(temp.value)
                switch = not switch
            else:
                l2.appendend(temp.value)
                switch = not switch
            temp = temp.nextval
        return l1, l2
    
    def recursive_shuffle_odd_even_LL(self, l1 = None, l2 = None, first = True, switch = True):
        """
        >>> asdf = LL()
        >>> for i in range(20):
        ...     asdf.appendend(i)
        >>> l1, l2 = asdf.recursive_shuffle_odd_even_LL()
        >>> print("List 1:", l1)
        List 1: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, ]
        >>> print("List 2:", l2)
        List 2: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, ]
        """
        if self.is_empty():
            return "Empty", "Empty"
        else:
            if first:
                l1, l2, first = LL(), LL(), False
            if switch:
                l1.appendend(self.value)
            else:
                l2.appendend(self.value)
            temp = self
            if temp.nextval:
                temp.nextval.recursive_shuffle_odd_even_LL(l1, l2, first, not switch)
        return l1, l2

    def loop_riffle_shuffle_LL(self, list2):
        """
        >>> list1, list2 = LL(), LL()
        >>> for i in range(20):
        ...     list1.appendend(i) if i % 2 == 0 else list2.appendend(i)
        >>> list1.loop_riffle_shuffle_LL(list2)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ]
        >>> list2.loop_riffle_shuffle_LL(list1)
        [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, ]
        """  
        t1 , t2, shuffled, switch = self, list2, LL(), True
        while t1 and t2:
            if switch:
                shuffled.appendend(t1.value)
                t1, switch = t1.nextval, not switch
            else:
                shuffled.appendend(t2.value)
                t2, switch = t2.nextval, not switch
        shuffled.loop_catenate(t2) if t2 else shuffled.loop_catenate(t1)
        return print(shuffled)

    def recursive_riffle_shuffle_LL(self, list2, t1 = None, shuffled = None, switch = True, first = True):
        """
        >>> list1, list2 = LL(), LL()
        >>> for i in range(20):
        ...     list1.appendend(i) if i % 2 == 0 else list2.appendend(i)
        >>> print(list1.recursive_riffle_shuffle_LL(list2))
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ]
        """
        if first:
            t1, shuffled, first = self, LL(), False
            if self.is_empty():
                return (print("Both lists are empty") if list2.is_empty() else print(list2))
            elif list2.is_empty():
                return (print("Both lists are empty") if self.is_empty() else print(self))

        if self.nextval.is_empty():
            shuffled.appendend(self.value)
            return shuffled.loop_catenate(list2)
        elif list2.nextval.is_empty():
            shuffled.appendend(list2.value)
            return shuffled.loop_catenate(self)
        
        if switch:
            shuffled.appendend(self.value)
            self.recursive_riffle_shuffle_LL(list2, self.nextval, shuffled, not switch , False)
        else:
            shuffled.appendend(list2.value)
            self.nextval.recursive_riffle_shuffle_LL(list2.nextval, t1, shuffled, not switch, False)
        return shuffled

    def loop_catenate(self, LL):
        """
        >>> left, right = LL(), LL()
        >>> for i in range(20):
        ...     left.appendend(i) if i % 2 == 0 else right.appendend(i)
        >>> left.loop_catenate(right)
        >>> print(left)
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, ]
        """ 
        last = self
        while not last.nextval.is_empty():
            last = last.nextval
        last.nextval = LL
        return
    
    def recursive_catenate(self, LL):
        """
        >>> left, right = LL(), LL()
        >>> for i in range(20):
        ...     left.appendend(i) if i % 2 == 0 else right.appendend(i)
        >>> left.recursive_catenate(right)
        >>> print(left)
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, ]
        """ 
        if self.nextval.is_empty():
            self.nextval = LL
        else:
            self.nextval.recursive_catenate(LL)
        return

    def loop_reverse_LL(self):
        """
        >>> asdf = LL()
        >>> for i in range(10):
        ...     asdf.appendend(i)
        >>> print(asdf.loop_reverse_LL())
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, ]
        """
        reversed_list, temp = LL(self.value), self
        while not temp.nextval.is_empty():
            reversed_list.appendbegin(temp.nextval.value)
            temp = temp.nextval
        return reversed_list

    def recursive_reverse_LL(self, reversed_list = None, first = True):
        """
        >>> asdf = LL()
        >>> for i in range(10):
        ...     asdf.appendend(i)
        >>> print(asdf.recursive_reverse_LL())
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, ]
        """
        if first:
            reversed_list = LL()
        if not self.is_empty():
            reversed_list.appendbegin(self.value)
            self.nextval.recursive_reverse_LL(reversed_list, False)
        return reversed_list

    def belongs(self, n):
        """
        >>> asdf = LL()
        >>> for i in range(10):
        ...     asdf.appendend(i)
        >>> asdf.belongs(90)
        False
        >>> asdf.belongs(2)
        True
        """
        if self.value == n:
            return True 
        elif self.nextval == None:
            return False
        else:
            return self.nextval.belongs(n)

    def intersection(self, LL, res=[]):
        """
        >>> l1, l2, ll1, ll2 = [1,4,8,5,3], [5,7,4,8], LL(), LL()
        >>> for i in l1:
        ...     ll1.appendend(i)
        >>> for i in l2:
        ...     ll2.appendend(i)
        >>> ll1.intersection(ll2)
        [4, 8, 5]
        """

        if self.value:
            if LL.belongs(self.value):
                res.append(self.value)
            if self.nextval == None:
                return res
            else:
                return self.nextval.intersection(LL, res)
        else:
            return res

    def union(self, LL, res = None):
        """
        >>> l1, l2, LL1, LL2 = [1,4,8,5,3], [5,7,4,8], LL(), LL()
        >>> for i in l1:
        ...     LL1.appendend(i)
        >>> for i in l2:
        ...     LL2.appendend(i)
        >>> print(LL1.union(LL2))
        [1, 4, 8, 5, 3, 7, ]
        """
        if not res:
            res = self
        if self.is_empty():
            return res
        if not LL.is_empty():
            if not self.belongs(LL.value):
                self.appendend(LL.value)
            if not LL.nextval.is_empty():
                return self.union(LL.nextval, res)
            else:
                return res

    def complementary(self, LL, res=None):
        """
        >>> l1, l2, LL1, LL2 = [1,4,8,5,3], [5,7,4,8], LL(), LL()
        >>> for i in l1:
        ...     LL1.appendend(i)
        >>> for i in l2:
        ...     LL2.appendend(i)
        >>> print(LL1.complementary(LL2, None))
        [1, 3, ]
        """
        if not res:
            res = self
        if LL.is_empty():
            return res
        else:
            if res.belongs(LL.value):
                res.remove_first_occurence(LL.value)
                return self.complementary(LL.nextval, res)
            else:
                return self.complementary(LL.nextval, res)
            

class BinaryTree():
    """
    Class of Binary Tree where each node can have 2 values at most.
    """
    def __init__(self, data=None, left=None, right=None):
        """
        Initializing the Tree Node with its DATA, RIGHT and LEFT values.
        >>> asdf = BinaryTree()
        >>> type(asdf)
        <class '__main__.BinaryTree'>
        """
        self.data = data
        self.left = left
        self.right = right
        if self.data != None:
            self.left, self.right = BinaryTree(), BinaryTree()

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left.data if self.left != None else None

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right.data if self.right != None else None

    def is_leaf(self):
        return True if (self.left == None and self.right == None) else False

    def is_empty(self):
        """
        Checks whether the Binary tree is empty or not.
        >>> asdf = BinaryTree()
        >>> asdf.is_empty()
        True
        >>> asdf.data = 5
        >>> asdf.is_empty()
        False
        """
        return False if self.data != None else True
    
    def insert(self, val):
        """
        Insert a value to the Binary Tree.
        >>> asdf = BinaryTree()
        >>> asdf.insert(42)
        >>> asdf.insert(3)
        >>> asdf.data
        42
        >>> asdf.left.data
        3
        """
        if self.is_empty():
            self.data, self.left, self.right = val, BinaryTree(), BinaryTree()
            
        else:
            if val < self.data:
                self.left.insert(val)
            else:
                self.right.insert(val)
        return None

    def leaf_count(self):
        """
        Return number of leaves in binary tree.
        >>> l = [42, 15, 9, 27, 86, 3, 48, 12, 39, 5]
        >>> asdf = BinaryTree()
        >>> for n in l:
        ...     asdf.insert(n)
        >>> asdf.leaf_count()
        4
        """
        if self.is_empty():
            return 0
        if self.left.is_empty() and self.right.is_empty():
            return 1
        elif self.left.is_empty() and  not self.right.is_empty():
            return self.right.leaf_count()
        elif not self.left.is_empty() and self.right.is_empty():
            return self.left.leaf_count()
        else:
            return self.left.leaf_count() + self.right.leaf_count()

    def tree_height(self):
        """
        Return HEIGHT of binary tree.
        >>> l = [42, 15, 9, 27, 86, 3, 48, 12, 39, 5]
        >>> asdf = BinaryTree()
        >>> for n in l:
        ...     asdf.insert(n)
        >>> asdf.tree_height()
        5
        """
        if self.is_empty():
            return 0
        elif self.left == None and self.right == None:
            return 1
        elif self.left == None and self.right !=None:
            return self.right.tree_height() + 1
        elif self.left != None and self.right ==None:
            return self.left.tree_height() + 1
        else:
            return max(self.left.tree_height(),self.right.tree_height()) + 1

    def print_preorder(self,res=[]):    
        """
        Prints PRE-ORDER list of the binary tree.
        >>> l = [42, 15, 9, 27, 86, 3, 48, 12, 39, 5]
        >>> asdf = BinaryTree()
        >>> for n in l:
        ...     asdf.insert(n)
        >>> asdf.print_preorder()
        [42, 15, 9, 3, 5, 12, 27, 39, 86, 48]
        """
        if self.data == None:
            return None
        else:
            if self.data !=None:
                res.append(self.data)
            if self.left != None:
                self.left.print_preorder()
            if self.right != None:
                self.right.print_preorder()
        return res

    def print_inorder(self,res=[]):
        """
        Prints IN-ORDER list of the binary tree.
        >>> l = [42, 15, 9, 27, 86, 3, 48, 12, 39, 5]
        >>> asdf = BinaryTree()
        >>> for n in l:
        ...     asdf.insert(n)
        >>> asdf.print_inorder(res = [])
        [3, 5, 9, 12, 15, 27, 39, 42, 48, 86]
        """
        if self.data == None:
            return None
        else:
            if self.left !=None:
                self.left.print_inorder(res)        
            if self.data !=None:
                res.append(self.data)
            if self.right !=None:
                self.right.print_inorder(res)
        return res

    def print_postorder(self,res=[]):
        """
        Prints POST-ORDER list of the binary tree.
        >>> l = [42, 15, 9, 27, 86, 3, 48, 12, 39, 5]
        >>> asdf = BinaryTree()
        >>> for n in l:
        ...     asdf.insert(n)
        >>> asdf.print_postorder()
        [5, 3, 12, 9, 39, 27, 15, 48, 86, 42]
        """
        if self.data == None:
           return None
        else:
            if self.left !=None:
                self.left.print_postorder()
            if self.right !=None:
                self.right.print_postorder()
            if self.data !=None:
                res.append(self.data)
        return res

    def max_value_in_sorted(self):
        """
        Return the max value in the binary tree.
        >>> l = [42, 15, 9, 27, 86, 3, 48, 12, 39, 5]
        >>> asdf = BinaryTree()
        >>> for n in l:
        ...     asdf.insert(n)
        >>> asdf.max_value_in_sorted().data
        86
        """
        if self.data == None:
            return None
        else:
            if self.right.is_empty():
                return self
            else:
                return self.right.max_value_in_sorted()
            
    def min_value_in_sorted(self):
        """
        Return the min value in the binary tree.
        >>> l = [42, 15, 9, 27, 86, 3, 48, 12, 39, 5]
        >>> asdf = BinaryTree()
        >>> for n in l:
        ...     asdf.insert(n)
        >>> asdf.min_value_in_sorted().data
        3
        """
        if self.data == None:
            return None
        else:
            if self.left.is_empty():
                return self
            else:
                return self.left.min_value_in_sorted()


    def remove(self, n):
        """
        >>> l = [42, 15, 9, 27, 86, 3, 48, 12, 39, 5]
        >>> asdf = BinaryTree()
        >>> for n in l:
        ...     asdf.insert(n)
        >>> asdf.print_inorder(res=[])
        [3, 5, 9, 12, 15, 27, 39, 42, 48, 86]
        >>> asdf.remove(27).print_inorder()
        [3, 5, 9, 12, 15, 39, 42, 48, 86]
        """
        if self.data == None:
            return print("There is no given number in tree.")
        else:
            if self.data == n:
                if not self.left.is_empty():
                    temp = self.left.max_value_in_sorted()
                    self.data, temp.data, temp.left = temp.data, temp.left.data, temp.left.left
                elif not self.right.is_empty():
                    temp = self.right.min_value_in_sorted()
                    self.data, temp.data, temp.left = temp.data, temp.right.data, temp.right.left
                else:
                    self.data, self.left, self.right = None, None, None
            else:
                self.right.remove(n) if n > self.data else self.left.remove(n)                    
        return self
    
    def reverse(self):
        """
        Method that reverses left and right branches of Binary Tree.
        >>> l, asdf = [45,6,3,23,76,2], BinaryTree()
        >>> for i in l:
        ...     asdf.insert(i)
        >>> asdf.print_inorder(res = [])
        [2, 3, 6, 23, 45, 76]
        >>> asdf.reverse()
        >>> asdf.print_inorder(res = [])
        [76, 45, 23, 6, 3, 2]
        """
        if self.data is None:
            return self
        else:
            self.right, self.left = self.left, self.right
            self.right.reverse()
            self.left.reverse()
    def path_to(self, x, res = []):
        """
        Method that outputs a path from root to number x.
        >>> l, asdf = [45,6,3,23,76,2], BinaryTree()
        >>> for i in l:
        ...     asdf.insert(i)
        >>> asdf.path_to(2, res = [])
        [45, 6, 3, 2]
        >>> asdf.path_to(76, res = [])
        [45, 76]
        """
        if self.data is not None:
            res.append(self.data)
            return (self.right.path_to(x, res) if x > self.data else self.left.path_to(x,res))
        else:
            return res
        
    def path_from_to(self, x, y):
        """
        Method that ouptuts a path from number x to number y.
        >>> l, asdf = [45,6,3,23,76,2], BinaryTree()
        >>> for i in l:
        ...     asdf.insert(i)
        >>> asdf.path_from_to(2, 76)
        [2, 3, 6, 45, 76]
        """
        route1 = self.path_to(x)
        route2 = self.path_to(y, res = [])
        route1.reverse()
        done, index = False, 1
        while not done:
            if route1[-(index)] == route2[0]:
                route2 = route2[1:]
            else:
                done = True
        res = route1 + route2
        return res

def insert_LL_to_BST(LL, result = BinaryTree()):
    if LL == None or LL.value == None:
        return print(result.print_inorder())
    else:
        result.insert(LL.value)
        insert_LL_to_BST(LL.nextval, result)

def insert_BST_to_LL(BST, result = LL()):
    if BST.left != None:
        insert_BST_to_LL(BST.left, result)
    if BST.data != None:
        result.appendend(BST.data)
    if BST.right != None:
        insert_BST_to_LL(BST.right, result)
    return result

class HashTable:
    
    def __init__(self, data = None):
        self.list = []
        self.index = []
        for i in range(900):
            self.list.append(None)
        if data:
            self.list[data%900] = data
            self.index.append(data % 997)

    def printlist(self):
        """
        >>> asdf = HashTable()
        >>> l = [45,6,3,23,76,2]
        >>> for i in l:
        ...     asdf.append(i)
        >>> asdf.printlist()
        [45, 6, 3, 23, 76, 2]
        """
        temp = []
        for i in self.index:
            if self.list[i]:
                temp.append(self.list[i])
        return temp
    
    def append(self, data, index = None):
        """
        >>> asdf = HashTable()
        >>> asdf.append(2)
        >>> asdf.printlist()
        [2]
        """
        if index == None:
            if self.list[data % 900] is not None:
                self.append(data, ((data % 900) + 1) % 900)
            else:
                self.list[data % 900] = data
                self.index.append(data % 900)
        else:
            if self.list[index] is not None:
                self.append(data, (index + 1) % 900)
            else:
                self.list[index] = data
                self.index.append(index)
                
    def search(self, data, index = None):
        """
        >>> asdf = HashTable()
        >>> l = [45,6,3,23,76,2]
        >>> for i in l:
        ...     asdf.append(i)
        >>> asdf.search(46)
        False
        >>> asdf.search(45)
        True
        """
        if data < 900 and not index:
            if self.list[data] is None:
                return False
            if self.list[data] == data:
                return True
            else:
                return self.search(data, (data +1) % 900)
        elif data >= 900 and not index:
            return self.search(data, data % 900)
        else:
            if self.list[index] is None:
                return False
            if self.list[index] == data:
                return True
            else:
                return self.search(data, index + 1)

    def delete(self, data):
        """
        >>> asdf = HashTable()
        >>> l = [45,6,3,23,76,2]
        >>> for i in l:
        ...     asdf.append(i)
        >>> asdf.delete(46)
        Not found given data.
        >>> asdf.delete(45)
        Deleted.
        >>> asdf.printlist()
        [6, 3, 23, 76, 2]
        """
        if self.search(data):
            if self.list[data%900] == data:
                self.list[data%900] = None
                return print("Deleted.")
        else:
            return print('Not found given data.')

    def size(self):
        """
        >>> asdf = HashTable()
        >>> l = [45,6,3,23,76,2]
        >>> for i in l:
        ...     asdf.append(i)
        >>> asdf.size()
        6
        """
        return len(self.printlist())

def buy_sell(LL):
    """
    Function that outputs a lists with days to buy in such way to sell on the next day and earn money.
    Prices are given as LinkedList for 30 days
    >>> prices, asdf = [4,8,5,7,0,2,4,7,5,6,3,6,3,7,9,6,4,3,5,1,9,5,8,6,7,8,9,4,3,5], LinkedList()
    >>> for price in prices:
    ...     asdf.adde(price)
    >>> print(buy_sell(asdf))
    [0, 2, 4, 5, 6, 8, 10, 12, 13, 17, 19, 21, 23, 24, 25, 28]
    """
    index, days = 0, []
    while index is not 29:
        buy, sell = LL.item(index), LL.item(index+1)
        if buy < sell:
            days.append(index)
        index += 1
    return days

if __name__ == "__main__":
    import doctest
    doctest.testmod()
