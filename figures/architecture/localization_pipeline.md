# Localization Pipeline Figure

## Goal
描述复杂户外环境下移动机器人定位流程。

## Pipeline

```text
3D LiDAR Scan
        |
        v
Point Cloud Pre-processing
        |
        +----------------+
        |                |
        v                v
Global Localization   FAST-LIO2
(Map Matching)        (Odometry)
        |                |
        +-------+--------+
                |
                v
          Pose Estimation
                |
                v
          map -> odom TF
                |
                v
             Nav2
```

## Key Message

Global localization provides initial/recovery pose.

FAST-LIO2 provides high-frequency local tracking.

RTK/IMU can be used as auxiliary constraints.

## Figure Style

- Conference paper style
- Clear module boundaries
- Highlight localization relationship
