import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def create_chip_topology(rows=7, cols=15, show_labels=True, node_size=300):
    """
    创建芯片拓扑结构图

    参数:
    rows: 行数
    cols: 列数
    show_labels: 是否显示节点标签
    node_size: 节点大小
    """

    # 创建图形
    plt.figure(figsize=(15, 8))

    # 创建网格布局
    positions = {}
    labels = {}

    # 生成节点位置和标签
    node_counter = 1
    for r in range(rows):
        for c in range(cols):
            positions[node_counter] = (c, -r)  # 使用-y使图形从上到下排列
            labels[node_counter] = str(node_counter)
            node_counter += 1

    # 创建NetworkX图
    G = nx.Graph()

    # 添加节点
    for node_id, pos in positions.items():
        G.add_node(node_id, pos=pos)

    # 添加边（网格连接）
    for node_id, (x, y) in positions.items():
        # 向右连接
        right_node = next((n for n, pos in positions.items()
                           if pos == (x + 1, y)), None)
        if right_node:
            G.add_edge(node_id, right_node)

        # 向下连接
        down_node = next((n for n, pos in positions.items()
                          if pos == (x, y - 1)), None)
        if down_node:
            G.add_edge(node_id, down_node)

    # 绘制图形
    pos = nx.get_node_attributes(G, 'pos')

    # 绘制边
    nx.draw_networkx_edges(G, pos,
                           edge_color='blue',
                           width=1.5)

    # 绘制节点
    nx.draw_networkx_nodes(G, pos,
                           node_color='blue',
                           node_size=node_size,
                           edgecolors='white',
                           linewidths=1.5)

    edge_labels = {
        (1, 2): "C12",
        (2, 3): "C23",
        (3, 4): "C34",

    }

    # 绘制标签
    if show_labels:
        nx.draw_networkx_labels(G, pos,
                                labels=labels,
                                font_size=8,
                                font_color='white',
                                font_weight='bold')

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                 font_color='#ff9999', font_size=10)

    # 设置图形属性
    # plt.gca().set_facecolor('white')
    plt.axis('off')
    plt.title('xx Chip Topology',
              fontsize=16)

    # 调整布局
    plt.tight_layout()
    plt.show()

    return G, positions


# 使用示例
if __name__ == "__main__":
    create_chip_topology(5,7,True,1000)