import json
from typing import Dict, Any, Optional


class BitDataManager:

    def __init__(self):
        self.bits: Dict[str, Dict[str, Any]] = {}

    def add_bit(self, bit_number: str, drive_freq: float, T1: float,
                T2: float, Readout_0: float,Readout_1: float,Gate_fidelity, **kwargs) -> None:
        self.bits[bit_number] = {
            "Drive_freq": drive_freq,
            "T1": T1,
            "T2": T2,
            "Readout_0": Readout_0,
            "Readout_1": Readout_1,
            "Gate_fidelity": Gate_fidelity,
            **kwargs
        }

    def save_to_json(self, filename: str) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.bits, f, indent=2, ensure_ascii=False)
        print(f"数据已保存到 {filename}")

    def load_from_json(self, filename: str) -> None:
        with open(filename, "r", encoding="utf-8") as f:
            self.bits = json.load(f)

    def get_bit(self, bit_number: str) -> Optional[Dict[str, Any]]:
        return self.bits.get(bit_number)


if __name__ == "__main__":
    manager = BitDataManager()

    extra_params = {
        "Tls": [0.2,0.3],
    }

    # 添加比特数据
    manager.add_bit("Q1", 4.7e9, 15, 5, 0.9,0.85,0.992, **extra_params)
    manager.add_bit("Q2", 4.27e9, 10, 2, 0.92,0.89,0.994)
    manager.add_bit("Q3", 4.78e9, 11, 3,0.94,0.92,0.996)
    manager.add_bit("Q4", 4.32e9, 20, 10,0.96,0.91,0.998)

    manager.save_to_json("Qubit_para.json")

    # q1_data = manager.get_bit("Q1")
    # print(f"Q1的数据: {json.dumps(q1_data, indent=2, ensure_ascii=False)}")

