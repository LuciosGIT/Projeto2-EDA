import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph_layered(kg: KnowledgeGraph):
    G = nx.DiGraph()

    # Mapeamento de camadas
    layers = {
        "Jogador": 0,
        "Técnico": 0,
        "Time": 1,
        "Campeonato": 2
    }

    node_layers = {}

    # Adiciona nós com camada
    for entity_id, data in kg.graph.items():
        layer = layers.get(data["type"], 1)
        G.add_node(entity_id, layer=layer, type=data["type"])
        node_layers[entity_id] = layer

    # Adiciona arestas
    for source, data in kg.graph.items():
        for relation, targets in data["relations"].items():
            for target in targets:
                G.add_edge(source, target, label=relation)

    # Layout multipartite (camadas)
    pos = nx.multipartite_layout(G, subset_key="layer", align="vertical")

    # Cores por tipo
    color_map = {
        "Jogador": "#8fd3f4",
        "Técnico": "#f7b267",
        "Time": "#aed9e0",
        "Campeonato": "#f28482"
    }

    node_colors = [
        color_map[G.nodes[n]["type"]] for n in G.nodes
    ]

    # Desenho
    plt.figure(figsize=(14, 9))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=2200,
        font_size=9,
        font_weight="bold",
        edgecolors="black"
    )

    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=8
    )

    plt.title("Knowledge Graph - Futebol Brasileiro (Layout em Camadas)", fontsize=14)
    plt.axis("off")
    plt.show()
