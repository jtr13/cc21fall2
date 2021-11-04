from py2neo import Graph, Node, Relationship

graph = Graph("http://localhost:7474", auth = ("test", "1234"))

# Node(label, name)
alice = Node("Person", name = "Alice")
dog = Node("Dog", name = "Dog")

alice_dog = Relationship(alice, "friend", dog)

graph.create(alice_dog)


# find number of persons
len(graph.nodes.match("Person"))
# match(n) return n;