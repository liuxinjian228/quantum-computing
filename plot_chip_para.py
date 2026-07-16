import matplotlib.pyplot as plt
import numpy as np
import json


def plot_bar(para,start,length,para_file,output_file):

    with open(para_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    bit_names = []
    paraList = []
    for i in range(length):
        bit_names.append(f"Q{start+i}")
    # print(bit_names)
    for bit in bit_names:
        paraList.append(data[bit][para])

    plt.figure()
    x_positions = np.arange(len(bit_names))

    bars = plt.bar(x_positions, paraList,
                   color=plt.cm.viridis(np.linspace(0.2, 0.8, len(bit_names))),
                   edgecolor='black', linewidth=1.2, alpha=0.8)

    plt.ylabel(para, fontsize=12, fontweight='bold')
    plt.xticks(x_positions, bit_names, rotation=45,fontsize=12)
    plt.yticks(fontsize=12)

    for i, (bar, value) in enumerate(zip(bars, paraList)):
        height = bar.get_height()
        if para == 'Drive_freq':
            plt.text(bar.get_x() + bar.get_width() / 2, height + max(paraList) * 0.01,
                     f'{value:.3e}', ha='center', va='bottom', fontsize=9, fontweight='bold')
        else:
            plt.text(bar.get_x() + bar.get_width() / 2, height + max(paraList) * 0.01,
                    f'{value}', ha='center', va='bottom', fontsize=11, fontweight='bold')

    plt.grid(True, axis='y', alpha=0.3, linestyle='--')
    plt.gca().set_axisbelow(True)
    plt.tight_layout()

    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"柱状图已保存到: {output_file}")
    else:
        plt.show()

def plot_bar_sorted(para,start,length,para_file,output_file):

    with open(para_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    bit_names = []
    paraList = []
    for i in range(length):
        bit_names.append(f"Q{start+i}")
    # print(bit_names)
    for bit in bit_names:
        paraList.append(data[bit][para])
    paired = list(zip(paraList, bit_names))
    paired_sorted = sorted(paired,reverse=True)

    sorted_paras, sorted_qubits = zip(*paired_sorted)
    plt.figure()
    x_positions = np.arange(len(bit_names))

    bars = plt.bar(x_positions, sorted_paras,
                   color=plt.cm.viridis(np.linspace(0.2, 0.8, len(sorted_qubits))),
                   edgecolor='black', linewidth=1.2, alpha=0.8)

    plt.ylabel(para, fontsize=12, fontweight='bold')
    plt.xticks(x_positions, sorted_qubits, rotation=45,fontsize=12)
    plt.yticks(fontsize=12)

    for i, (bar, value) in enumerate(zip(bars, sorted_paras)):
        height = bar.get_height()
        if para == 'Drive_freq':
            plt.text(bar.get_x() + bar.get_width() / 2, height + max(sorted_paras) * 0.01,
                     f'{value:.3e}', ha='center', va='bottom', fontsize=9, fontweight='bold')
        else:
            plt.text(bar.get_x() + bar.get_width() / 2, height + max(sorted_paras) * 0.01,
                    f'{value}', ha='center', va='bottom', fontsize=11, fontweight='bold')

    plt.grid(True, axis='y', alpha=0.3, linestyle='--')
    plt.gca().set_axisbelow(True)
    plt.tight_layout()

    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"柱状图已保存到: {output_file}")
    else:
        plt.show()

def get_statistics_data(para_file,output_file):

    data_process = {}
    with open(para_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    for item in ['T1','T2','Drive_freq','Readout_0','Readout_1','Gate_fidelity']:
        process_values = {name: data.get(item, 0) for name, data in json_data.items() if item in data}
        data_process[item] = {'min':min(process_values.values()),'max':max(process_values.values()),'average':round(np.average(list(process_values.values())),3)}

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data_process, f, indent=2, ensure_ascii=False)

plot_bar('T1',1,10,r'D:\Desktop\chip_para_plot\Qubit_para.json','')
# get_statistics_data(r'D:\Desktop\chip_para_plot\Qubit_para.json','statistics.json')