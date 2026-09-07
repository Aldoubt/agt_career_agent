# Robotics System Design Interview Notes

## Navigation Architecture

map -> odom -> base_link

Global localization provides absolute pose recovery.
FAST-LIO2 provides high frequency local tracking.
Nav2 handles planning and control.

## Design Questions

### Why not RTK as primary localization?

Because outdoor environments with trees can cause GNSS degradation and multipath effects. LiDAR localization provides a more stable environmental reference.

### How to handle vibration?

Consider IMU mounting, filtering, sensor calibration and robust state estimation.

### How to evaluate navigation?

Use localization accuracy, goal reaching error, success rate, runtime performance and recovery ability.
