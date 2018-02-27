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

    # Check if G has more than 2 nodes
    if len(G) < 2:
        return "Error: G has not enough vertices to form an edge"

    # Retrive a set of vertices
    vertices = G.keys()

    # Retrieve the unique set of edges
    edges = set()
    for vertice in vertices:
        for edge in G[vertice]:
            # Set has unique value so if edge is already present
            # then it will not make duplicate copy
            if vertice > edge[0]:
                edges.add((edge[1], edge[0], vertice))
            elif vertice < edge[0]:
                edges.add((edge[1], vertice, edge[0]))

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

run_test_q1()
run_test_q2()
