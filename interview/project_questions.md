# Robotics Project Interview Questions

## Autonomous Navigation System

### Q1: Why not use RTK as the primary localization source?

Answer direction:

Outdoor environments with trees and obstacles can reduce GNSS availability. Therefore, LiDAR-based localization is used as the primary localization source, while RTK provides auxiliary constraints.

---

### Q2: Why choose FAST-LIO2?

Answer direction:

FAST-LIO2 provides high-frequency LiDAR-inertial odometry with strong real-time performance and is suitable for mobile robots requiring continuous state estimation.

---

### Q3: What is the relationship between global localization and odometry?

Answer direction:

Global localization provides the map-to-odom initialization, while odometry estimation maintains local continuous motion tracking.

---

### Q4: How do you handle challenging outdoor environments?

Answer direction:

Consider sensor selection, point cloud processing, localization robustness, vibration characteristics, and navigation map quality together.

---

### Q5: What is your contribution compared with existing open-source algorithms?

Answer direction:

The contribution focuses on system integration, engineering optimization, deployment, and validation under real robot scenarios.