# ROS2 System Architecture Figure

## Purpose
论文和技术文档中的机器人系统总体架构图。

## Layers

```text
Sensors
 ├── Hesai MID360 LiDAR
 ├── RTK/IMU
 └── Chassis Encoder

        ↓

ROS2 Hardware Layer
 ├── LiDAR Driver
 ├── INS Driver
 └── Bunker CAN Driver

        ↓

Localization Layer
 ├── FAST-LIO2 Continuous Tracking
 ├── 3D LiDAR Global Localization
 └── Map-Odom Transformation

        ↓

Navigation Layer
 ├── Nav2 Planner
 ├── Controller
 └── Costmap

        ↓

Robot Platform
 └── Tracked Mobile Robot
```

## Output Requirements

- Academic style
- Vector format preferred
- Suitable for thesis and presentation
- Keep ROS2 data flow clear
