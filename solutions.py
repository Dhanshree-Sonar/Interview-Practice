import unittest

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

class question1TestCase(unittest.TestCase):
    """Test cases for question1."""

    def test_result_to_pass(self):
        self.assertEqual(question1("udacity", "ad"), True)

    def test_result_to_fail(self):
        self.assertEqual(question1("udacity", "udy"), False)

    def test_string2_empty(self):
        self.assertEqual(question1("udacity", ""), True)

    def test_string1_empty(self):
        self.assertEqual(question1("", "ad"), False)

    def test_string2_larger(self):
        self.assertEqual(question1("ad", "udacity"), False)

    def test_string2_not_string(self):
        self.assertEqual(question1("udacity", 1), "Error: Argument(s) not string")


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

class question2TestCase(unittest.TestCase):
    """Test cases for question2."""

    def test_result_to_pass(self):
        self.assertEqual(question2('Able was I ere I saw Elba'), 'able was i ere i saw elba')

    def test_result_to_fail(self):
        self.assertEqual(question2(121), 'Error: Argument is not a string')

    def test_string_single_char(self):
        self.assertEqual(question2('p'), 'p')

    def test_string_empty(self):
        self.assertEqual(question2(''), '')

    def test_string_case_insensitive(self):
        self.assertEqual(question2('asRacecarde'), 'racecar')


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

class question3TestCase(unittest.TestCase):
    """Test cases for question3."""

    def test_result_to_pass(self):
        self.assertEqual(question3(G), G_MST)

    def test_result_to_fail(self):
        self.assertEqual(question3('graph'), 'Error: G is not a dictionary')

    def test_no_edges_graph(self):
        self.assertEqual(question3(H), 'Error: G has no edge to form a tree')

    def test_empty_graph(self):
        self.assertEqual(question3({}), {})


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

    # Initialize the BST
    root = BSTNode(r)
    initialize(T, root)

    # Use lca to find the least common ancestor
    return lca(root, n1, n2)


class BSTNode:
    # Create a new BST node object
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def initialize(T, n):
    for i in range(len(T)):
        # Check if child is greater than the node
        if (T[n.value][i] == 1 and i > n.value):
            # Make the child as right child
            n.right = BSTNode(i)
            initialize(T, n.right)

        # Check if child is smaller than the node
        if (T[n.value][i] == 1 and i < n.value):
            # Make the child as left child
            n.left = BSTNode(i)
            initialize(T, n.left)

def lca(root, n1, n2):
    # Check if n1 and n2 are smaller than root
    # if true means lies the LCA in left
    if(root.value > n1 and root.value > n2):
        return lca(root.left, n1, n2)

    # Check if n1 and n2 are greater than root
    # if true means lies the LCA in right
    if(root.value < n1 and root.value < n2):
        return lca(root.right, n1, n2)

    return root.value


T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]

class question4TestCase(unittest.TestCase):
    """Test cases for question4."""

    def test_result_to_pass(self):
        self.assertEqual(question4(T,3,1,4), 3)

    def test_result_to_fail(self):
        self.assertEqual(question4(1,3,1,4), 'Error: T is not a set')

    def test_tree_empty(self):
        self.assertEqual(question4([],3,1,4), 'Error: T is empty')

    def test_node_less_than_zero(self):
        self.assertEqual(question4(T,3,-1,4), 'Error: Node(s) can not be less than 0')

    def test_node_noninteger(self):
        self.assertEqual(question4(T,3,1,4.2), 'Error: Node(s) can not be non-integer')

    def test_node_greater_than_root(self):
        self.assertEqual(question4(T,3,1,5), 'Error: Nodes can not be greater than largest tree element')


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

run_test_q5()


if __name__ == '__main__':
    unittest.main()
