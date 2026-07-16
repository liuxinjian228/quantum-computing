import json
import functools


def init_para_file(length,output_file):

    value = {
        "Drive_freq": 0,
        "T1": 0,
        "T2": 0,
        "Readout_0": 0,
        "Readout_1": 0,
        "Gate_fidelity": 0,
        "Tls": []
    }
    dicts = {}
    for i in range(length):
        dicts[f'Q{i+1}'] = value

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dicts, f, indent=2, ensure_ascii=False)

def init_config_file(chip_name,bus,qubit,output_file):

    chip_info = {
      "name": f"{chip_name}",
      "All_Qubits": [
        "Q3"
      ],
      "current_Qubit": "Q3",
      "crossTalk_Qubits": [
        "Q3"
      ],
      "crossTalkMatrix_bias": [
        [
          1.0
        ]
      ],
      "crossTalkMatrix_pulse": [
        [
          1.0
        ]
      ],
      "high_sRate": 10000000000.0
    }
    NA = {
      "NA": "",
      "DrivMW": ""
    }
    ADC = {
      "All_PROBs": [
        "B1"
      ],
      "current_PROB": "B1",
      "global": {
        "master_ch": "ADC.MASTER",
        "timeSeq": {
          "period": 0.0002,
          "wdLen": 8e-05,
          "probT0": 7.5e-05,
          "gapTime": 3e-07,
          "switchGap": 0
        },
        "readout": {
          "Matrix": [
            [0.95625, 0.043750000000000004],
            [0.12910156250000002, 0.8708984375000001]
          ]
        }
      }
    }
    Bus = {
      "Multi_Readout": {
        "Qubits": [
          "Q3"
        ],
        "carryFreqList": [
          6279040000.0
        ],
        "carryPhaseList": [
          0
        ],
        "carryScaleList": [
          0.1
        ],
        "demodFreqList": [
          10000000.0
        ],
        "demodPhaseList": [
          0
        ],
        "demodPointStartList": [
          1000
        ],
        "demodPointLenList": [
          3000
        ],
        "demodWeightList": [
          1
        ]
      },
      "inst": {
        "ADCCh": "",
        "probLoCh": "",
        "DDS_Ch": "",
        "probChI": "",
        "probChQ": "",
        "probSwitchCh": "",
        "ADCTrigCh": "",
        "probDAT": ""
      },
      "para": {
        "ADC_sRate": 2800000000.0,
        "pointNum": 4800,
        "shots": 2000,
        "triggerDelay": 7.5e-05,
        "probLoFreq": 0,
        "probLoPower": 0,
        "probAtt": 0,
        "sRate": 4800000000,
        "shape": "rising_tech",
        "width": 2e-06,
        "shape_kw": {
          "mode": "DC-DC",
          "pre_width": 2e-07,
          "factor": 0.5
        }
      },
      "cali": {
        "probIQcali": {
          "off_I": 0,
          "off_Q": 0,
          "off_I_wd": 0,
          "off_Q_wd": 0
        },
        "readoutIQcali": {
          "scal_i": 0,
          "scal_q": 1,
          "phas_err": 0
        }
      },
      "setting": {}
    }
    Qubit = {
        "index": 1,
        "type": "Transmon",
        "para": {
          "E_C": 0,
          "F_ge_max": 0,
          "F_ge_min": 0,
          "F_cav_bare": 0,
          "g_qr": 0,
          "d_squid": 0,
          "F_cav_dispersive": 0,
          "F_ge": 0,
          "F_ef": 0,
          "E_J_max": 0,
          "probLoFreq": 0,
          "probLoPower": 0,
          "probAtt": 0,
          "probFreq": 0,
          "probCarryFreq": 0,
          "probCarryPhase": 0,
          "probCarryScale": 0,
          "demodPhase": 0,
          "demodPointStart": 1000,
          "demodPointLen": 3000,
          "demodWeight": 1,
          "drivLoFreq": 0,
          "drivLoPower": 0,
          "drivAtt": 0,
          "drivFreq": 0,
          "drivCarryFreq": 0,
          "pulseAmpPeriod": 1,
          "biasPeriod": 1,
          "biasSweetPoint": 0,
          "biasValue": 0,
          "fluxValue": 0
        },
        "gate": {
          "waveform": {
            "X": None,
            "Y": None,
            "Z": None
          },
          "sRate": {
            "XY": 4800000000.0,
            "Z": 1200000000.0,
            "M": 4800000000.0
          },
          "U_gates": {
            "pi_len": 2e-08,
            "pi_amp": 0.16553,
            "z_amp": 0,
            "buff": 2e-09,
            "shape": "CosPulse",
            "sRate": [
              4800000000.0,
              1200000000.0
            ],
            "lambda1": -0.5568,
            "Delta2": -227532463.06439415,
            "use_drag": True
          },
          "X_12": {
            "width": 2.666824723476891e-08,
            "sRate": [
              4800000000.0,
              1200000000.0
            ],
            "amp": 0.08,
            "Ec": -227335740.3322592,
            "buff": 2e-09,
            "shape": "CosPulse"
          },
          "CZ": {
            "amp": 1,
            "during": 5e-08,
            "width": 5.1999999999999996e-08,
            "lambda1": 1.02196,
            "lambda2": 0.10153,
            "theta_f": 1.57,
            "g12": 15350000.0,
            "omega1": 4106477990.2695165,
            "omega2": 4471774010.094136,
            "alpha2": -218000000.0,
            "omega_ss2": 4471936589.776692,
            "d2": 0.2191138,
            "peroid2": 1,
            "sRate": [
              4800000000.0,
              1200000000.0
            ],
            "phase": -1.4820549234807159
          },
          "iSWAP": {
            "amp": -0.535,
            "during": 2.1e-08,
            "buff": 6e-09,
            "delay": 0,
            "edge": 4e-09,
            "sRate": 2000000000.0
          },
        },
        "JPA_Setting": {
          "status": "ON",
          "mwDrivSour": "",
          "fluxCH": "",
          "flux": 0.1822,
          "pump_power": -3.01,
          "pump_freq": 12580000000.0
        },
        "inst": {
          "ADC_PROB": "",
          "mwDrivSour": "",
          "DDS_Ch": "",
          "xyGateChI": "",
          "xyGateChQ": "",
          "zGateCh": "",
          "xySwitchCh": "",
          "fluxCH": "",
          "drivDAT": ""
        },
        "cali": {
          "probIQcali": {
            "scale_Q": 1,
            "phase_Q": 0
          },
          "drivIQcali": {
            "scale_Q": 1,
            "phase_Q": 0,
            "off_I": 0,
            "off_Q": 0,
            "off_I_wd": 0,
            "off_Q_wd": 0
          },
          "Delay": {
            "XY": 0,
            "Z": 0,
            "M": 0
          },
          "xyReflection": {
            "tau": 0,
            "A": 0,
            "phi": 0
          },
          "zCali": {
            "tau1": 0,
            "A1": 0,
            "tau2": 0,
            "A2": 0,
            "tau3": 0,
            "A3": 0,
            "tau4": 0,
            "A4": 0,
            "tau5": 0,
            "A5": 0
          },
          "singleShot": {
            "c0": {
              "real": 0,
              "imag": 0
            },
            "c1": {
              "real": 0,
              "imag": 0
            },
            "r0": 0,
            "r1": 0,
            "thr": 0,
            "phi": 0
          }
        }
      }
    dicts = {}

    dicts['Chip'] = chip_info
    dicts['NA_Meas'] = NA
    dicts['ADC_Meas'] = ADC
    for i in range(bus):
        dicts['ADC_Meas'][f'B{i+1}'] = Bus
    for i in range(qubit):
        dicts[f'Q{i+1}'] = Qubit

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dicts, f, indent=2, ensure_ascii=False)



# init_para_file(10,'para_file_test1.json')
init_config_file('test_chip',1,5,'test_config.json')
