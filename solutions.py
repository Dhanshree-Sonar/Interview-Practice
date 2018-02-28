def question1(s,t):
    # Check whether arguements are of string data-type
    if type(s) != str or type(t) != str:
        return "Error: Argument(s) not string"

    # Check whether 't' is an empty string
    if len(t) == 0:
        return True

    # Check if s is smaller than 't' or 's' is an empty string
    if len(s) < len(t) or len(s) == 0:
        return False

    # Convert strings to lower case
    s = s.lower()
    t = t.lower()

    l = len(t)
    for i in range(len(s)):
        if sorted(s[i:(i+l)]) == sorted(t):
            return True

    return False

def run_test_q1():
    print "\nQuestion1 Test Cases:"
    # Should return True
    print " question1(\"udacity\", \"ad\"): %s" % (question1("udacity", "ad"))
    # Should return Flase
    print " question1(\"udacity\", \"udy\"): %s" % (question1("udacity", "udy"))
    # Should return True
    print " question1(\"udacity\", \"\"): %s" % (question1("udacity", ""))
    # Should return False
    print " question1(\"\", \"ad\"): %s" % (question1("", "ad"))
    # Should return False
    print " question1(\"ad\", \"udacity\"): %s" % (question1("ad", "udacity"))
    # Should return Error
    print " question1(\"udacity\", 1): %s" % (question1("udacity", 1))

def question2(a):
    # Check whether arguement is of string data-type
    if type(a) != str:
        return "Error: Argument is not a string"

    # If string is empty or single character then return string as it is
    if len(a) < 2:
        return a

    longest = ""
    a = a.lower()
    for i in range(len(a)):
        # Traverse the each substring after the i position
        for j in range(i+1, len(a)+1):
            # Check if substring is palindrom and if it is logner than the current one
            if a[i:j] == a[i:j][::-1] and len(longest) < len(a[i:j]):
                longest = a[i:j]

    return longest

def run_test_q2():
    print "\nQuestion2 Test Cases:"
    # Should return racecar
    print " question2(\"asRacecarde\"): %s" % (question2("asRacecarde"))
    # Should return dddd
    print " question2(\"asaddddghj\"): %s" % (question2("asaddddghj"))
    # Should return able was i ere i saw elba
    print " question2(\"Able was I ere I saw Elba\"): %s" % (question2("Able was I ere I saw Elba"))
    # Should return p
    print " question2(\"p\"): %s" % (question2("p"))
    # Should return ''
    print " question2(\"\"): %s" % (question2(""))
    # Should return Error
    print " question2(121): %s" % (question2(121))

def question3(G):

    # Use Kruskal's algorithm(Greedy algorithm) to find the minimum spanning tree
    # Find out unique edges and sort them by weight.
    # Take edges one by one and form a tree unless all vertices convered
    # Skip the edge if it forming a cycle

    # Check if G is a dictionary
    if type(G) != dict:
        return "Error: G is not a dictionary"

    # Check if G empty
    if len(G) == 0:
        return {}

    # Check if G has less than 2 vertices
    if len(G) < 2:
        return "Error: G has no edge to form a tree"

    # Retrive a set of vertices
    vertices = G.keys()

    # Retrieve the unique set of edges
    edges = set()
    for vertex in vertices:
        for edge in G[vertex]:
            # Set has unique value so if edge is already present
            # then it will not make duplicate copy
            if vertex > edge[0]:
                edges.add((edge[1], edge[0], vertex))
            elif vertex < edge[0]:
                edges.add((edge[1], vertex, edge[0]))

    # Sort the edges by weight
    edges = sorted(list(edges))

    # Add edge to minimum spanning tree if it is not forming a cycle
    # Loop throght edges till all the vertices are covered
    mst = []
    # Convert the vertices in the for of set
    vertices = [set(i) for i in vertices]
    for edge in edges:
        # Retrive indexes of both vertices
        for i in xrange(len(vertices)):
            if edge[1] in vertices[i]:
                v1 = i
            if edge[2] in vertices[i]:
                v2 = i

        # Union both the vertices set and store the result in smaller vertices
        # Pop the larger vertices set
        # Store the edge in mst
        if v1 < v2:
            vertices[v1] = set.union(vertices[v1], vertices[v2])
            vertices.pop(v2)
            mst.append(edge)
        if v1 > v2:
            vertices[v1] = set.union(vertices[v1], vertices[v2])
            vertices.pop(v1)
            mst.append(edge)

        # If all vertices are covered the stop the operation
        if len(vertices) == 1:
            break

    # Generate output MST Graph (Adjacency list structured)
    mst_graph = {}
    for edge in mst:
        if edge[1] in mst_graph:
            mst_graph[edge[1]].append((edge[2], edge[0]))
        else:
            mst_graph[edge[1]] = [(edge[2], edge[0])]

        if edge[2] in mst_graph:
            mst_graph[edge[2]].append((edge[1], edge[0]))
        else:
            mst_graph[edge[2]] = [(edge[1], edge[0])]

    return mst_graph

def run_test_q3():
    G = {'A': [('B', 15), ('C', 25)],
         'B': [('A', 15), ('E', 10), ('H', 5), ('I', 25)],
         'C': [('A', 25), ('D', 10), ('E', 20)],
         'D': [('C', 10)],
         'E': [('B', 10), ('C', 20), ('F', 10), ('G', 5)],
         'F': [('E', 10)],
         'G': [('E', 5)],
         'H': [('B', 5), ('I', 15)],
         'I': [('B', 25), ('H', 15)]}

    G_MST = {'A': [('B', 15)],
             'B': [('H', 5), ('E', 10), ('A', 15)],
             'C': [('D', 10), ('E', 20)],
             'D': [('C', 10)],
             'E': [('G', 5), ('B', 10), ('F', 10), ('C', 20)],
             'F': [('E', 10)],
             'G': [('E', 5)],
             'H': [('B', 5), ('I', 15)],
             'I': [('H', 15)]}

    H = {'A':[]}

    print "\nQuestion3 Test Cases:"
    # Should return G_MST
    print " question3(G): %s" % (question3(G))
    # Should return error
    print " question3(\"graph\"): %s" % (question3("graph"))
    # Should return error
    print " question3(H): %s" % (question3(H))
    # Should return {}
    print " question3({}): %s" % (question3({}))

def question4(T, r, n1, n2):
    # Check if T is not a set
    if type(T) != list:
       return "Error: T is not a set"
    # Check if T is empty
    if len(T) == 0:
        return "Error: T is empty"
    # Check if r, n1, and n2 are non-negative
    if r < 0 or n1 < 0 or n2 <0:
        return "Error: Node(s) can not be less than 0"
    # Check if r, n1 and n2 are non-integer
    if type(r) != int or type(n1) != int or type(n2) != int:
        return "Error: Node(s) can not be non-integer"
    # Check if n1 and n2 are equal
    if n1 == n2:
        return "Error: n1 and n2 should not be equal"
    # Check if n1 or n2 are same sa root
    if n1 == r or n2 == r:
        return "Error: Node(s) value can not be same as root"
    # Check if n1 or n2 are greater than largest tree element
    if n1 >= len(T) or n2 >= len(T):
        return "Error: Nodes can not be greater than largest tree element"

    # Define a list for all ancestors of n1
    n1_parents = []
    # Find all the parents of n1 staring from most recent parent till root
    while n1 != r:
        n1 = parent(T, n1)
        n1_parents.append(n1)

    # If no parents found retunr -1
    if len(n1_parents) == 0:
        return -1
    # Find all the parents of n2 staring from most recent parent till root
    while n2 != r:
        n2 = parent(T, n2)
        # if the recent parent is in the n1 parents list then return that node
        if n2 in n1_parents:
            return n2

    return -1

def parent(T, n):
    for i in range(len(T)):
        # Check which row(node) has 'n' as a child node
        if T[i][n] == 1:
            return i

    return -1

def run_test_q4():
    T = [[0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]]

    print "\nQuestion4 Test Cases:"
    # Should return 3
    print " question4(T,3,1,4): %s" % (question4(T,3,1,4))
    # Should return error
    print " question4(1,3,1,4): %s" % (question4(1,3,1,4))
    # Should return error
    print " question4([],3,1,4): %s" % (question4([],3,1,4))
    # Should return error
    print " question4(T,3,-1,4): %s" % (question4(T,3,-1,4))
    # Should return error
    print " question4(T,3,1,4.2): %s" % (question4(T,3,1,4.2))
    # Should return error
    print " question4(T,3,1,5): %s" % (question4(T,3,1,5))

def question5(ll, m):
    # Check if m is an integer
    if type(m) != int:
        return "Error: 'm' is not an integer"

    # Check if m is smaller than or equal to 0
    if m <= 0:
        return None

    # Check if position to fetch the element is equal to linked list length
    l = ll.length()
    if m == l:
        return ll.head.data

    position = l - m
    # Check if m is greater than the length of ll
    if position < 1:
        return None

    return ll.get_element(position)


class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList(object):
    def __init__(self, new_element):
        self.head = Node(new_element)

    def append(self, new_element):
        node = Node(new_element)
        node.next = self.head
        self.head = node

    def length(self):
        length = 1
        current = self.head
        while current.next != None:
            length += 1
            current = current.next

        return length

    def get_element(self, position):
        counter = 0
        current = self.head
        while counter <= position and current:
            if counter == position:
                return current.data
            counter += 1
            current = current.next

        return None


def run_test_q5():
    ll = LinkedList(20)
    ll.append(12)
    ll.append(45)
    ll.append(37)
    ll.append(24)
    ll.append("cat")
    ll.append(11)

    print "\nQuestion5 Test Cases:"
    # Should return 12
    print " question5(ll, 2): %s" % (question5(ll, 2))
    # Should return 37
    print " question5(ll, 4): %s" % (question5(ll, 4))
    # Should return cat
    print " question5(ll, 6): %s" % (question5(ll, 6))
    # Should return None
    print " question5(ll, 0): %s" % (question5(ll, 0))
    # Should return None
    print " question5(ll, 8): %s" % (question5(ll, 8))
    # Should return Error
    print " question5(ll, 3.5): %s" % (question5(ll, 3.5))

run_test_q1()
run_test_q2()
run_test_q3()
run_test_q4()
run_test_q5()
