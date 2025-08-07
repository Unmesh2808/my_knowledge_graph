import json
import networkx as nx
from pyvis.network import Network

def load_from_json(filename="knowledge_graph.json"):
    with open(filename) as f:
        data = json.load(f)
    G = nx.DiGraph()
    for node in data["nodes"]:
        G.add_node(node["id"], **{k: v for k, v in node.items() if k != "id"})
    for edge in data["edges"]:
        G.add_edge(edge["source"], edge["target"], relation=edge["relation"])
    return G

def export_visualization(graph, filename="knowledge_graph.html"):
    net = Network(notebook=True, directed=True)
    for node in graph.nodes:
        net.add_node(node, label=node, title=graph.nodes[node].get("desc", ""))
    for u, v in graph.edges:
        net.add_edge(u, v, label=graph.edges[u, v]["relation"])
    net.show(filename)

if __name__ == "__main__":
    kg = load_from_json()  # Load from JSON
    export_visualization(kg)  # Generate HTML
