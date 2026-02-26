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

  //   (Map<string, int>, Array<Array<int>>) GraphConverter::getAsAdjacencyMatrix()
  //    Return a tuple where the first value is a mapping to a row number and the second value is the VxV size matrix.

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
    final result = graphConverter.getAsAdjacencyList();
    if (result.toString() != test.expectedAdjList.toString()) {
      throw Exception(
        'Failed for test ${index + 1}: ${test.description}\nExpected: ${test.expectedAdjList}\nActual: $result',
      );
    }
  }

  print('All tests passed!');
}
