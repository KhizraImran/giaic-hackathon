# Hardware Requirements

This course is technically demanding, sitting at the intersection of Physics Simulation, Visual Perception, and Generative AI. Due to the computational intensity, specific hardware is required for an optimal learning experience.

## 1. The "Digital Twin" Workstation (Required per Student)

This is the most critical component, as NVIDIA Isaac Sim (an Omniverse application) requires RTX (Ray Tracing) capabilities. Standard laptops (MacBooks or non-RTX Windows machines) will not work.

*   **GPU (The Bottleneck):** NVIDIA RTX 4070 Ti (12GB VRAM) or higher. (Ideal: RTX 3090 or 4090 with 24GB VRAM for smoother Sim-to-Real training).
*   **CPU:** Intel Core i7 (13th Gen+) or AMD Ryzen 9. (Physics calculations in Gazebo/Isaac are CPU-intensive).
*   **RAM:** 64 GB DDR5 (32 GB is the absolute minimum, but will crash during complex scene rendering).
*   **OS:** Ubuntu 22.04 LTS. (ROS 2 is native to Linux; dual-booting or dedicated Linux machines are mandatory).

## 2. The "Physical AI" Edge Kit

Since a full humanoid robot is expensive, students will learn "Physical AI" by setting up the nervous system on a desk before deploying it to a robot. This kit covers Module 3 (Isaac ROS) and Module 4 (VLA).

*   **The Brain:** NVIDIA Jetson Orin Nano (8GB) or Orin NX (16GB). (Industry standard for embodied AI).
*   **The Eyes (Vision):** Intel RealSense D435i or D455. (Provides RGB and Depth data, essential for VSLAM and Perception).
*   **The Inner Ear (Balance):** Generic USB IMU (BNO055). (Often built into RealSense D435i or Jetson boards, but a separate module helps teach IMU calibration).
*   **Voice Interface:** A simple USB Microphone/Speaker array (e.g., ReSpeaker) for the "Voice-to-Action" Whisper integration.

## 3. The Robot Lab (Optional, depending on budget)

For the "Physical" part of the course, there are three tiers of options:

*   **Option A: The "Proxy" Approach (Recommended for Budget):** Use a quadruped (dog) or robotic arm as a proxy (e.g., Unitree Go2 Edu). Software principles transfer effectively.
*   **Option B: The "Miniature Humanoid" Approach:** Small, table-top humanoids (e.g., Unitree G1, Robotis OP3, or Hiwonder TonyPi Pro as a budget alternative).
*   **Option C: The "Premium" Lab (Sim-to-Real specific):** For deploying the Capstone to a real humanoid (e.g., Unitree G1 Humanoid).

## Summary of Architecture / Cloud-Native Lab (High OpEx)

If RTX-enabled workstations are unavailable, the course can rely on cloud-based instances (e.g., AWS RoboMaker or NVIDIA's Omniverse cloud delivery). While this introduces latency and cost complexity, it is an alternative.

*   **Cloud Workstations (AWS/Azure):** Instance Types like AWS g5.2xlarge (A10G GPU, 24GB VRAM).
*   **Local "Bridge" Hardware:** Still requires Edge AI Kits (Jetson Kit) and potentially one physical robot for the final demo.
