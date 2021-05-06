import sys


class DictionaryGraph:
    def __init__(self, n):
        """
        :param n: The number of vertices
        """
        self.vertices = n
        self.dictionary = {}
        self.costs = {}
        for i in range(n):
            self.dictionary[i] = []

    def is_edge(self, x, y):
        return y in self.dictionary[x]

    def add_edge(self, x, y, cost):
        if not self.is_edge(x, y):
            self.dictionary[x].append(y)
            self.costs[(x, y)] = cost
            self.dictionary[y].append(x)
            self.costs[(y, x)] = cost

    def parse_x(self):
        return self.dictionary.keys()

    def prims_algorithm(self, starting_node):
        selected = [0] * self.vertices
        no_edge = 0
        selected[starting_node] = True
        print("  Edge  : Weight")
        while no_edge < self.vertices - 1:
            minimum = sys.maxsize
            x = 0
            y = 0
            for i in range(len(selected)):
                if selected[i] and len(self.dictionary[i]) > 0:
                    for j in range(len(selected)):
                        if not(selected[j]) and j in self.dictionary[i]:
                            if minimum > self.dictionary[i][j]:
                                x = i
                                y = j
            print(str(x) + "-" + str(y) + ":" + str(self.dictionary[x][y]))
            selected[y] = True
            no_edge += 1


class MainProgram:
    def __init__(self):
        file = open("input.txt", "r")
        number_of_vertices, number_of_edges = map(int, file.readline().split())
        self.g = DictionaryGraph(int(number_of_vertices))

        for edge in range(number_of_edges):
            x, y, cost = map(int, file.readline().split())
            self.g.add_edge(x, y, cost)

    def run(self):
        print(self.g.dictionary)
        x = input("Choose the starting node: ")
        x = int(x)
        self.g.prims_algorithm(x)


program = MainProgram()
program.run()

