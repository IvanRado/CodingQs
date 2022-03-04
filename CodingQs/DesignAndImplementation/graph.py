class Graph():
    def __init__(self) -> None:
        self.num_nodes = 0
        self.adjacency_list = {}

    def addVertex(self, node):
        self.adjacency_list[node] = []
        self.num_nodes += 1

    # Undirected graph
    def addEdge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def showConnections(self):
        for key, val in self.adjacency_list.items():
            print(f"Node: {key}, Connections:{list(set(val))}")

    def bfs(self, value):
        seen = {}

        if int(value) > self.num_nodes:
            return None

        queue = [('0', self.adjacency_list['0'], ['0'])]
        while queue:
            node_val, connections, path = queue.pop(0)
            # print("Node value: ",node_val)
            # print("Connections: ", connections)
            # print("Path: ", path)
            if node_val not in seen.keys():
                seen[node_val] = 1
            else:
                continue

            if node_val == value:
                return path

            for conn in connections:
                n_path = path + [conn]
                queue.append((conn, self.adjacency_list[conn], n_path))

        return None

    def dfs(self, value):
        seen = {}

        if int(value) > self.num_nodes:
            return None

        stack = [('0', self.adjacency_list['0'], ['0'])]
        while stack:
            node_val, connections, path = stack.pop()

            print("Node value: ", node_val)
            print("Connections: ", connections)
            print("Path: ", path)
            if node_val not in seen.keys():
                seen[node_val] = 1
            else:
                continue

            if node_val == value:
                return path

            for conn in connections:
                n_path = path + [conn]
                stack.append((conn, self.adjacency_list[conn], n_path))

        return None

mygraph = Graph()
mygraph.addVertex('0')
mygraph.addVertex('1')
mygraph.addVertex('2')
mygraph.addVertex('3')
mygraph.addVertex('4')
mygraph.addVertex('5')
mygraph.addVertex('6')
mygraph.addEdge('3', '1')
mygraph.addEdge('3', '4')
mygraph.addEdge('4', '2')
mygraph.addEdge('4', '5')
mygraph.addEdge('1', '2')
mygraph.addEdge('1', '0')
mygraph.addEdge('0', '2')
mygraph.addEdge('6', '5')

mygraph.showConnections()

print(mygraph.dfs('5'))