# Robotics Data Integration Plan

## Goal

Integrate existing robotics experiment assets into agt_career_agent:

- v2 navigation repository experiment results
- lio-benchmark-tool evaluation results
- process monitoring / profiling capability repository

The goal is to transform engineering data into reusable assets for:

- thesis experiments
- resume quantitative achievements
- interview discussion
- technical reports

---

## Data Sources

### 1. Navigation System Experiments

Source:

- v2 repository
- v3 repository future tests

Data types:

- rosbag metadata
- localization trajectory
- navigation success records
- maps
- screenshots
- demo videos

Target:

```
thesis/data/navigation/
```

---

### 2. LIO Benchmark Results

Source:

- lio-benchmark-tool

Data types:

- ATE
- RPE
- trajectory files
- runtime statistics
- algorithm comparison

Target:

```
thesis/data/lio_benchmark/
```

---

### 3. System Profiling Data

Source:

- process monitoring repository

Data types:

- CPU usage
- memory usage
- GPU usage
- node frequency
- latency

Target:

```
thesis/data/system_profile/
```

---

## Unified Experiment Schema

Each experiment should contain:

```
experiment.yaml
trajectory.csv
metrics.yaml
figures/
report.md
```

Example:

```yaml
experiment:
  name: outdoor_navigation_test
  platform: bunker_robot
  lidar: MID360
  localization: FAST-LIO2
  navigation: Nav2

metrics:
  ate:
  rpe:
  success_rate:
  cpu_average:
```

---

## Production Pipeline

```
Robot Test
    |
    v
Raw Data
    |
    v
Evaluation Scripts
    |
    +---- Thesis Figures
    |
    +---- Resume Metrics
    |
    +---- Interview Evidence
```

---

## Next Implementation Steps

1. Import v2 experiment metadata.
2. Define lio benchmark parser.
3. Add system profiling report generator.
4. Connect metrics to resume generator.
