# Contribution Statement

## Research Topic

Outdoor autonomous navigation for mobile robots under GNSS degraded environments.

## Main Contributions

### 1. LiDAR-centric localization framework

Develop a localization architecture using 3D LiDAR global localization as the absolute reference source under unreliable GNSS conditions.

### 2. Global localization and continuous tracking integration

Combine global pose initialization with continuous LIO tracking:

- Global Localization: map -> odom
- FAST-LIO2 tracking: odom -> base_link

### 3. Real robot system validation

Validate the complete ROS2 autonomous navigation pipeline on a tracked mobile robot platform.

## Engineering Value

The work focuses on bridging algorithm research and practical robot deployment.
