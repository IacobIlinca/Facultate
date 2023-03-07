package graph;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * a class used for manipulating graphs.
 * @param <T>
 */
public class Components<T> {

    private Graph<T> graph;

    public Components(Graph<T> graph) {
        this.graph = graph;
    }

    /**
     * a classic depth first method, recursively.
     * @param node the current node that is visited.
     * @param visited to remember the nodes that were already visited.
     * @param currentComponent where are stored all the new nods.
     */
    private void DFS(T node, Set<T> visited, List<T> currentComponent) {
        if (visited.contains(node)) return;
        visited.add(node);
        currentComponent.add(node);
        for (T nextNode : graph.map.get(node)) {
            if (!visited.contains(nextNode)) {
                DFS(nextNode, visited, currentComponent);
            }
        }
    }

    /**
     * Computes the number of the connected components in the graph
     * It runs a DFS starting in every single node and when it finds
     * a not already visited node, it adds to a list
     * @return a list of lists of elements representing the list of components
     */
    public List<List<T>> ConnectedComponents() {
        List<List<T>> components = new ArrayList<>();
        Set<T> visitedNodes = new HashSet<>();
        for (var node : graph.map.keySet()) {
            if (!visitedNodes.contains(node)) {
                List<T> currentComponent = new ArrayList<>();
                DFS(node, visitedNodes, currentComponent);
                components.add(currentComponent);
            }
        }
        return components;
    }
}
