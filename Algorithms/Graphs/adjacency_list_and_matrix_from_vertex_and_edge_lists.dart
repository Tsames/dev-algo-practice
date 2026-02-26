/*
Create a class that takes a vertex/edge list of a directed graph in the constructor.
Suppose the inputted nodes are arbitrary strings.

Have 2 public methods:

(Map<string, int>, Array<Array<int>>) GraphConverter::getAsAdjacencyMatrix()
Return a tuple where the first value is a mapping to a row number and the second value is the VxV size matrix.

Map<string, List<string>> GraphConverter::getAsAdjacencyList()
Return a mapping from node ID to neighboring node IDs.

Example(s)
Suppose we have the following vertex list and edge list:
vertexList = ["n1", "n2", "n3"]
edgeList = [("n1", "n2")]

getAsAdjacencyList(vertexList, edgeList) should return
{
  "n1": ["n2"],
  "n2": [],
  "n3": [],
}

getAsAdjacencyMatrix(vertexList, edgeList) should return a tuple with the following values.

First value (IDs can be arbitrarily assigned in any order):
{
  "n1": 0,
  "n2": 1,
  "n3": 2,
}

Second value:
[
  [0, 1, 0],
  [0, 0, 0],
  [0, 0, 0],
]

class GraphConverter:
  def getAsAdjacencyList(self, vertexList: list[str], edgeList: list) -> dict[str, list[str]]:
  def getAsAdjacencyMatrix(self, vertexList: list[str], edgeList: list):
*/

class GraphConverter {
  final List<dynamic> vertexList;
  final List<(dynamic, dynamic)> edgeList;

  const GraphConverter({required this.vertexList, required this.edgeList});

  ({Map<dynamic, int> indexMap, List<List<int>> matrix}) getAsAdjacencyMatrix() {
    final vertexToIndexMap = {for (final (index, vertex) in vertexList.indexed) vertex: index};
    final adjacencyMatrix = [for (final _ in vertexList) List.filled(vertexList.length, 0)];

    for (final edge in edgeList) {
      adjacencyMatrix[vertexToIndexMap[edge.$1]!][vertexToIndexMap[edge.$2]!] = 1;
    }

    return (indexMap: vertexToIndexMap, matrix: adjacencyMatrix);
  }

  Map<dynamic, List<dynamic>> getAsAdjacencyList() {
    final adjList = {for (final vertex in vertexList) vertex: <dynamic>[]};
    for (final edge in edgeList) {
      adjList[edge.$1]?.add(edge.$2);
    }
    return adjList;
  }
}

typedef TestCase = ({
  List<dynamic> vertexList,
  List<(dynamic, dynamic)> edgeList,
  Map<dynamic, List<dynamic>> expectedAdjList,
  Map<dynamic, int> expectedIndexMap,
  List<List<int>> expectedAdjMatrix,
  String description,
});

main() {
  final testCases = <TestCase>[
    (
      vertexList: ["n1", "n2", "n3"],
      edgeList: [("n1", "n2")],
      expectedAdjList: {
        "n1": ["n2"],
        "n2": [],
        "n3": []
      },
      expectedIndexMap: {"n1": 0, "n2": 1, "n3": 2},
      expectedAdjMatrix: [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
      ],
      description: "Simple graph with one edge",
    ),
    (
      vertexList: ["a", "b", "c", "d"],
      edgeList: [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")],
      expectedAdjList: {
        "a": ["b"],
        "b": ["c"],
        "c": ["d"],
        "d": ["a"]
      },
      expectedIndexMap: {"a": 0, "b": 1, "c": 2, "d": 3},
      expectedAdjMatrix: [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
      ],
      description: "Cyclic graph",
    ),
    (
      vertexList: ["x", "y", "z"],
      edgeList: [],
      expectedAdjList: {"x": [], "y": [], "z": []},
      expectedIndexMap: {"x": 0, "y": 1, "z": 2},
      expectedAdjMatrix: [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
      ],
      description: "Graph with no edges",
    ),
    (
      vertexList: ["p", "q", "r"],
      edgeList: [("p", "q"), ("p", "r"), ("q", "r")],
      expectedAdjList: {
        "p": ["q", "r"],
        "q": ["r"],
        "r": []
      },
      expectedIndexMap: {"p": 0, "q": 1, "r": 2},
      expectedAdjMatrix: [
        [0, 1, 1],
        [0, 0, 1],
        [0, 0, 0]
      ],
      description: "Graph with multiple edges from a single node",
    ),
  ];

  for (final (index, test) in testCases.indexed) {
    final graphConverter = GraphConverter(
      vertexList: test.vertexList,
      edgeList: test.edgeList,
    );
    final actualAdjList = graphConverter.getAsAdjacencyList();
    if (actualAdjList.toString() != test.expectedAdjList.toString()) {
      throw Exception(
        'Failed for test ${index + 1}: ${test.description}\nExpected: ${test.expectedAdjList}\nActual: $actualAdjList',
      );
    }
    final actualAdjMatrix = graphConverter.getAsAdjacencyMatrix();
    if (actualAdjMatrix.matrix.toString() != test.expectedAdjMatrix.toString()) {
      throw Exception(
        'Failed for test ${index + 1}: ${test.description}\nExpected: ${test.expectedAdjMatrix}\nActual: $actualAdjMatrix',
      );
    }
    if (actualAdjMatrix.indexMap.toString() != test.expectedIndexMap.toString()) {
      throw Exception(
          'Test ${index + 1} index map failed: ${test.description}\nExpected: ${test.expectedIndexMap}\nActual: ${actualAdjMatrix.indexMap}');
    }
  }

  print('All tests passed!');
}
