class GraphNode {
  final int val;
  final List<GraphNode> neighbors;

  GraphNode(this.val) : neighbors = [];

  List<List<int>> toAdjList() {
    // Assumes graph is connected
    final visited = <int, GraphNode>{};
    final result = <int, List<int>>{};

    void dfs(GraphNode node) {
      if (visited.containsKey(node.val)) return;
      visited[node.val] = node;
      result[node.val] = node.neighbors.map((neighbor) => neighbor.val).toList();
      node.neighbors.forEach(dfs);
    }

    dfs(this);

    return List.generate(visited.length, (i) => result[i + 1]!);
  }
}

GraphNode? buildGraph(List<List<int>> adjList) {
  if (adjList.isEmpty) return null;

  final nodes = List.generate(adjList.length, (i) => GraphNode(i + 1));

  for (int i = 0; i < adjList.length; i++) {
    for (final neighborVal in adjList[i]) {
      nodes[i].neighbors.add(nodes[neighborVal - 1]);
    }
  }

  return nodes[0];
}
