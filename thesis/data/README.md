# Thesis Experiment Data

This directory stores structured experimental data for thesis evaluation.

## Recommended structure

```text
thesis/data/
├── rosbag_info.yaml
├── localization_results/
│   ├── trajectory.csv
│   ├── ate.csv
│   └── rpe.csv
└── navigation_results/
    ├── goals.csv
    └── metrics.csv
```

The data should be generated from real robot tests whenever possible.
