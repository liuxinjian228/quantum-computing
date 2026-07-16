import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def create_chip_topology(rows=7, cols=15, show_labels=True, node_size=300):

    fig, ax = plt.subplots(figsize=(10, 8))

    positions = {}
    labels = {}

    node_counter = 1
    for r in range(rows):
        for c in range(cols):
            positions[node_counter] = (c, -r)  # 使用-y使图形从上到下排列
            if r % 2 == 0:
                labels[node_counter] = r * cols + c + 1
            else:
                labels[node_counter] = r * cols + cols - c
            node_counter += 1
    print(labels)
    G = nx.Graph()
    for node_id, pos in positions.items():
        G.add_node(node_id, pos=pos)

    for node_id, (x, y) in positions.items():
        # print(x,y)
        right_node = next((n for n, pos in positions.items()
                           if pos == (x + 1, y)), None)
        if right_node:
            G.add_edge(node_id, right_node)

        if x == cols-1 and (-y) % 2==0:
            down_node = next((n for n, pos in positions.items()
                              if pos == (x, y - 1)), None)
            if down_node:
                G.add_edge(node_id, down_node)
        elif x == 0 and (-y) % 2 == 1:
            down_node = next((n for n, pos in positions.items()
                              if pos == (x, y - 1)), None)
            if down_node:
                G.add_edge(node_id, down_node)

    pos = nx.get_node_attributes(G, 'pos')

    nx.draw_networkx_edges(G, pos,
                           edge_color='blue',
                           width=1.5)

    nx.draw_networkx_nodes(G, pos,
                           node_color='blue',
                           node_size=node_size,
                           edgecolors='white',
                           linewidths=1.5)

    edges = [(1, 2, 'C1'), (2, 3, 'C2'), (3, 4, 'C3'), (4, 5, 'C4'), (5, 6, 'C5'), (6, 7, 'C6'), (7, 8, 'C7'), (8, 9, 'C8')]
    print(pos)
    for (u, v, w) in edges:
        x = (pos[labels[u]][0] + pos[labels[v]][0]) / 2
        y = (pos[labels[u]][1] + pos[labels[v]][1]) / 2
        text = ax.text(x, y, w,
                       fontsize=10, fontweight='bold',
                       ha='center', va='center',
                       bbox=dict(boxstyle='round,pad=0.4',
                                 facecolor='white',
                                 edgecolor='blue',
                                 alpha=1,
                                 linewidth=1.5), zorder=5)
    if show_labels:
        nx.draw_networkx_labels(G, pos,
                                labels=labels,
                                font_size=11,
                                font_color='white',
                                font_weight='bold')

    plt.axis('off')
    plt.tight_layout()
    plt.show()

    return G, positions

if __name__ == "__main__":
    create_chip_topology(4,5,True,1000)