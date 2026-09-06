# Engineering Failure Analysis

## RTK degradation in outdoor environments

### Problem
GNSS positioning quality decreases in tree-covered environments due to signal blockage and multipath effects.

### Analysis
- Satellite visibility reduction
- Multipath interference
- Unstable absolute positioning

### Engineering Solution
Use LiDAR-based localization as the primary positioning source:

```
Global LiDAR Localization
        |
        v
FAST-LIO2 Continuous Tracking
        |
        v
Navigation Framework
```

RTK is treated as an auxiliary source instead of the only localization reference.

---

## Localization loss recovery

### Problem
Robot may lose tracking after restart or severe environmental changes.

### Solution
- Global localization provides initial map alignment.
- LIO maintains high-frequency local tracking.
- Recovery mechanism re-establishes map-to-odom transformation.

---

## Outdoor mapping challenges

### Problem
Vegetation, slopes and dynamic objects influence point cloud quality.

### Solution direction
- Ground segmentation
- Elevation-aware map processing
- Dynamic object filtering
