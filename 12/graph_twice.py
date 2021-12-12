import collections
from collections import defaultdict

example_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

example_input_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

example_input_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

def main():
    with open('input.txt') as f:
        input = read_input(f.read())

    g = Graph(input)
    _, paths = g.find_all_paths('start', 'end')
    print(len(paths))


def read_input(input=example_input):
    lines = [x for x in input.splitlines()]

    ret = []
    for x in lines:
        (left, right) = x.split('-')
        ret.append((left, right))
    return ret


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def find_all_paths(self, node1, node2, path=[], result=[]):
        path = path + [node1]
        if node1 == node2:
            return path, result
        if node1 not in self._graph:
            return None, result
        for node in self._graph[node1]:
            if node.isupper() or \
                    (node not in path) or \
                    (node != 'start' and all_lowercase_lt_two(path)):
                (new_path, result) = self.find_all_paths(node, node2, path, result)
                if new_path:
                    result.append(new_path)

        return None, result

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def all_lowercase_lt_two(path):
    c = collections.Counter(path)
    for elemn in c:
        if elemn.islower():
            if c[elemn] > 1:
                return False
    return True


if __name__ == "__main__":
    main()
