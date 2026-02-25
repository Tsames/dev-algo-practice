/*
https://neetcode.io/problems/clone-graph/question?list=neetcode150

Clone Graph

Given a node in a connected undirected graph, return a deep copy of the graph.
Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

The graph is shown in the test cases as an adjacency list.
An adjacency list is a mapping of nodes to lists, used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.
For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph.
The index of each node within the adjacency list is the same as the node's value (1-indexed).
The input node will always be the first node in the graph and have 1 as the value.

Example 1:
Input: adjList = [[2],[1,3],[2]]
Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: The graph is empty.

Constraints:
0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.
*/
import './graph_node.dart';

GraphNode? cloneGraph(GraphNode? node) {
  /*
  We are guaranteed that there are no duplicate edges and no self loops in our graph.
  We are also cloning a connected and undirected graph.

  This means that no matter which vertex we are given, so long as it is not null, we will be able to visit all of the
  nodes in the graph starting from that vertex without issue.
  */

  // Here we create a map to store the nodes we have created copies for
  final Map<GraphNode, GraphNode> cloned = {};

  GraphNode dfs(GraphNode node) {
    if (cloned.containsKey(node)) return cloned[node]!;

    final clone = GraphNode(node.val);
    cloned[node] = clone;

    node.neighbors.forEach((neighbor) => clone.neighbors.add(dfs(neighbor)));
    return clone;
  }

  return node != null ? dfs(node) : null;
}

void main() {
  // empty graph returns null
  assert(cloneGraph(null) == null);

  // single node with no neighbors
  final singleNode = buildGraph([[]])!;
  final singleClone = cloneGraph(singleNode)!;
  assert(singleClone.val == 1);
  assert(singleClone.neighbors.isEmpty);

  // three node graph matches structure
  final node = buildGraph([
    [2],
    [1, 3],
    [2],
  ]);
  final clone = cloneGraph(node);
  assert(
    clone?.toAdjList().toString() ==
        [
          [2],
          [1, 3],
          [2],
        ].toString(),
  );

  // clone is a deep copy - nodes are different objects
  void assertDifferentNodes(GraphNode original, GraphNode copy, Set<int> visited) {
    if (visited.contains(original.val)) return;
    visited.add(original.val);
    assert(!identical(original, copy));
    for (int i = 0; i < original.neighbors.length; i++) {
      assertDifferentNodes(original.neighbors[i], copy.neighbors[i], visited);
    }
  }

  assertDifferentNodes(node!, clone!, {});

  print('all tests passed');
}
