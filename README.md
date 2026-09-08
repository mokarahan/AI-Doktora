This is a pHD project to determine the RUL of a Lithium-Ion Battery with CNN-MHA-TCN-FCL hybrid model with NASA Battery dataset.

AI-Doktora/
├── Dataset
│   └── NASA
│       ├── 5. Battery Data Set
│       │   ├── 1. BatteryAgingARC-FY08Q4
│       │   │   ├── B0005.mat
│       │   │   ├── B0006.mat
│       │   │   ├── B0007.mat
│       │   │   ├── B0018.mat
│       │   │   └── README.txt
├── docs
│   ├── download.txt
│   ├── kısaltmalar.txt
│   ├── Main_Paper_Review_Literature.pdf
│   ├── NASA_Batarya_SOH_RUL_Tahmin_Yontemi.docx
│   ├── NASA_Batarya_SOH_RUL_Tahmin_Yontemi.pdf
│   ├── Ozet.docx
│   ├── papers
│   │   ├── A_Two-Stage_Transfer_Regression_CNN.pdf
│   │   ├── Based_on_1D-CNN-BLSTM-NN.pdf
│   │   ├── CNN-DNN_model_for_battery.pdf
│   │   ├── Remaining_useful_life_estimation.pdf
│   │   └── Reservoir-Spiking-Neural.pdf
│   └── terminoloji.txt
├── download_data.sh
├── metadata.csv
├── prepare_data.sh
├── run.sh
├── src
│   ├── CNN.py
│   ├── data.zip
│   ├── DrawFile.py
│   ├── Generator.py
│   ├── LoadBatteryData.py
│   ├── metadata.csv
│   ├── ReadModelData.py
│   ├── tmp
│   └── utils.py
└── test
    ├── sample.py
    └── split.sh
