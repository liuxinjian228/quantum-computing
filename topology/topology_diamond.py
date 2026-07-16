import matplotlib.pyplot as plt
import networkx as nx

def create_chip_topology(rows=7, cols=15, show_labels=True, node_size=300):

    fig, ax = plt.subplots(figsize=(10, 8))
    positions = {}
    labels = {}

    node_counter = 1
    for r in range(rows):
        for c in range(cols):
            x_offset = 0.5 if r % 2 == 1 else 0
            positions[node_counter] = (c + x_offset, -r)
            labels[node_counter] = str(node_counter)
            node_counter += 1

    G = nx.Graph()
    for node_id, pos in positions.items():
        G.add_node(node_id, pos=pos)

    for node_id, (x, y) in positions.items():
        r = int(-y)
        # right_node = next((n for n, pos in positions.items()
        #                    if pos == (x + 1, y)), None)
        # if right_node:
        #     G.add_edge(node_id, right_node)
        if r % 2 == 0:
            down_left_node = next((n for n, pos in positions.items()
                                   if pos == (x - 0.5, y - 1)), None)
            if down_left_node:
                G.add_edge(node_id, down_left_node)

            down_right_node = next((n for n, pos in positions.items()
                                    if pos == (x + 0.5, y - 1)), None)
            if down_right_node:
                G.add_edge(node_id, down_right_node)
        else:
            down_node = next((n for n, pos in positions.items()
                              if pos == (x, y - 1)), None)
            if down_node:
                G.add_edge(node_id, down_node)

            down_left_node = next((n for n, pos in positions.items()
                                   if pos == (x - 0.5, y - 1)), None)
            if down_left_node:
                G.add_edge(node_id, down_left_node)

            down_right_node = next((n for n, pos in positions.items()
                                    if pos == (x + 0.5, y - 1)), None)
            if down_right_node:
                G.add_edge(node_id, down_right_node)

    pos = nx.get_node_attributes(G, 'pos')

    nx.draw_networkx_edges(G, pos,
                           edge_color='#1E90FF',
                           width=1.5)
    nx.draw_networkx_nodes(G, pos,
                           node_color='#1E90FF',
                           node_size=node_size,
                           edgecolors='white',
                           linewidths=1.5)

    # edges = [(1, 2, 'C1'), (2, 3, 'C2'), (1, 6, 'C3'), (8, 9, 'C4'), (5, 6, 'C5'), (3, 4, 'C6'), (2, 6, 'C7'), (9, 10, 'C8'),(4, 5, 'C11')
    #         ,(6, 7, 'C10'), (7, 3, 'C12'), (8, 7, 'C13'), (12, 6, 'C14')]
    edges = [(1, 8, 'C3'), (2, 9, 'C4'), (5, 11, 'C5'), (12, 6, 'C7'), (9, 16, 'C8'), (17, 10, 'C11'), (12, 6, 'C10'), (7, 13, 'C12'), (20, 13, 'C13'), (12, 19, 'C14')]

    for (u, v, w) in edges:
        x = (pos[u][0] + pos[v][0]) / 2
        y = (pos[u][1] + pos[v][1]) / 2
        text = ax.text(x, y, w,
                       fontsize=10, fontweight='bold',
                       ha='center', va='center',
                       bbox=dict(boxstyle='round,pad=0.4',
                                 facecolor='white',
                                 edgecolor='#1E90FF',
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
    create_chip_topology(5, 7, True, 1000)