**several tools and software** that can help in **simulating battery performance, flight time, and power requirements** for drone. Here are some of the best options:  

---

## **1. Online Calculators for Battery & Flight Time Estimation**
### ✅ **eCalc (DroneCalc) - Best for Multi-Rotor Drones**  
🔗 **[https://www.ecalc.ch/xcoptercalc.php](https://www.ecalc.ch/xcoptercalc.php)**  
🛠 **Features:**  
- Enter **battery specs, drone weight, motor details, and propeller size**  
- Estimates **flight time, power draw, and efficiency**  
- Helps find the best battery & motor combination  

💡 **Best for:** Quick **LiPo & Li-Ion battery performance checks** for drones like Phantom 4.  

---

### ✅ **Rotorgeeks LiPo Flight Time Calculator**  
🔗 **[https://rotorgeeks.com/lipo-calculator](https://rotorgeeks.com/lipo-calculator)**  
🛠 **Features:**  
- Enter **battery capacity, voltage, and discharge rate**  
- Estimates **approximate flight time** based on **power draw**  
- Works well for **racing & photography drones**  

💡 **Best for:** Fast **battery discharge rate analysis** for your drone.  

---

## **2. Battery Simulation Software**
### ✅ **WebOCalc - Open Source Drone Power Calculator**  
🔗 **[https://www.miniquadtestbench.com/tools/webocalc.html](https://www.miniquadtestbench.com/tools/webocalc.html)**  
🛠 **Features:**  
- Estimates **battery endurance based on drone power consumption**  
- Helps determine **current draw & efficiency at different throttle levels**  
- Supports both **LiPo & Li-Ion battery configurations**  

💡 **Best for:** Designing **custom battery packs** and **motor efficiency testing**.  

---

## **3. Advanced Simulation Software**
### ✅ **Matlab Simulink (Aerospace Blockset)**
🔗 **[https://www.mathworks.com/products/simulink.html](https://www.mathworks.com/products/simulink.html)**  
🛠 **Features:**  
- Simulates **battery drain under real-world conditions**  
- Models **drone dynamics, weight, aerodynamics, and battery usage**  
- Can simulate **GPS-guided flights & wind effects**  

💡 **Best for:** **Research & academic-level drone simulations**.  

---

### ✅ **PX4 SITL & Gazebo (Drone Hardware Simulation)**
🔗 **[https://dev.px4.io/v1.9.0/en/simulation/gazebo.html](https://dev.px4.io/v1.9.0/en/simulation/gazebo.html)**  
🛠 **Features:**  
- **Realistic flight physics & battery drain modeling**  
- Test **how different batteries affect flight time & stability**  
- Supports **DJI Phantom-like drones with custom battery integration**  

💡 **Best for:** **Testing custom battery packs in a simulated drone environment** before real-world deployment.  

---

## **Which One Should You Use?**
- If you **just need a quick estimation** ➝ **eCalc or Rotorgeeks Calculator**  
- If you’re **building a custom battery pack** ➝ **WebOCalc**  
- If you need **advanced flight simulation** ➝ **PX4 Gazebo or Matlab Simulink**  


---

### **Step-by-Step Guide to Using eCalc (DroneCalc) for Battery & Flight Time Testing**  
🔗 **Go to eCalc:** [https://www.ecalc.ch/xcoptercalc.php](https://www.ecalc.ch/xcoptercalc.php)  

---

## **Step 1: Select Drone Type & Configuration**  
- **Multicopter Type:** Choose **Quadcopter (4 motors)** (for a DJI Phantom equivalent).  
- **Battery Cells (LiPo):** Select **4S (14.8V)**.  
- **Battery Capacity:** Enter **6000mAh** (or your custom capacity).  

---

## **Step 2: Enter Battery Specifications**  
### **For LiPo (High Performance)**
- **Cell Type:** Select **LiPo**  
- **Battery Voltage:** **14.8V (nominal for 4S LiPo)**  
- **Battery Capacity:** **6000mAh**  
- **C-Rating (Discharge Rate):** **25C** (for high power output)  
- **Battery Weight:** **~500g (depends on your battery pack)**  

### **For Li-Ion (Long Flight Time)**
- **Cell Type:** Select **Li-Ion**  
- **Battery Voltage:** **14.8V (4S Li-Ion, nominal)**  
- **Battery Capacity:** **6000mAh (or your selected value)**  
- **C-Rating:** **8C to 15C**  
- **Battery Weight:** **~800-1000g**  

---

## **Step 3: Enter Drone Weight & Flight Specs**  
- **Total Takeoff Weight (including battery):** **1.3-1.5 kg** (for a DJI Phantom 4-like drone).  
- **Frame Size (Motor-to-Motor Distance):** **350-450mm** (for medium-sized drones).  

---

## **Step 4: Enter Motor & Propeller Details**  
- **Motor KV (RPM per Volt):** **800-1000KV**  
- **Motor Efficiency:** **~80% (if using a high-efficiency motor like DJI E310/E5000)**  
- **Propeller Size:** **9450 (9.4-inch, common for Phantom drones)**  

---

## **Step 5: Click "Calculate" and Analyze Results**  
✅ **Flight Time:** eCalc will estimate how long the drone will fly per charge.  
✅ **Power Consumption:** See if the **battery provides enough current for stable flight**.  
✅ **Efficiency:** Helps determine **if you need a bigger battery or lighter frame**.  

---


## **📌 Example Setup (DJI Phantom 4 Pro Equivalent)**
This setup closely resembles a **DJI Phantom 4 Pro** drone with a **custom LiPo or Li-Ion battery**.

### **1️⃣ General Setup**
| **Parameter**   | **Value (Example)** |
|----------------|------------------|
| **Multicopter Type** | **Quadcopter (4 motors)** |
| **Frame Size** | **350mm (DJI Phantom 4 size)** |
| **Total Weight (incl. battery)** | **1.4 kg (1400g)** |

---

### **2️⃣ Battery Setup**
| **Parameter**   | **Value for LiPo** | **Value for Li-Ion** |
|----------------|----------------|----------------|
| **Battery Type** | LiPo | Li-Ion |
| **Number of Cells** | **4S (14.8V nominal, 16.8V max)** | **4S (14.8V nominal, 16.8V max)** |
| **Battery Capacity** | **6000mAh** | **6000mAh** |
| **Discharge Rating (C-Rating)** | **25C (for high power needs)** | **10C (for endurance flight)** |
| **Battery Weight** | **500g** | **900g** |

---

### **3️⃣ Motor Setup**
| **Parameter**   | **Value (Example)** |
|----------------|------------------|
| **Motor KV (RPM per Volt)** | **900 KV** |
| **Motor Power per Unit** | **120W - 150W** |
| **Motor Efficiency** | **80%** |
| **Motor Max Current** | **20A (total 80A for 4 motors)** |

🔹 **Example Motors:** DJI 2312 960KV, T-Motor MN2212 920KV, or similar.

---

### **4️⃣ Propeller Setup**
| **Parameter**   | **Value (Example)** |
|----------------|------------------|
| **Propeller Size** | **9450 (9.4-inch, DJI Phantom standard)** |
| **Propeller Material** | **Carbon Fiber / Plastic** |
| **Pitch** | **4.5 inches** |

---

### **5️⃣ Running the Simulation on eCalc**
1️⃣ **Go to eCalc:** [https://www.ecalc.ch/xcoptercalc.php](https://www.ecalc.ch/xcoptercalc.php)  
2️⃣ **Enter values as per the example above**  
3️⃣ **Click "Calculate"**  

---

### **📊 Expected Results (Flight Time & Power Consumption)**
| **Parameter**   | **LiPo (4S, 6000mAh, 25C)** | **Li-Ion (4S, 6000mAh, 10C)** |
|----------------|----------------|----------------|
| **Hover Time** | **25-28 min** | **30-35 min** |
| **Full Throttle Time** | **10-12 min** | **12-15 min** |
| **Peak Current Draw** | **~60A** | **~30A** |

💡 **Key Takeaways:**
✅ **LiPo is better for high power & aggressive flight.**  
✅ **Li-Ion gives longer flight time but less burst power.**  

---

### **🚀 Guide to Using Rotorgeeks LiPo Flight Time Calculator**  
🔗 **Go to Rotorgeeks LiPo Calculator:** [https://rotorgeeks.com/lipo-calculator](https://rotorgeeks.com/lipo-calculator)  

---

## **📌 Step-by-Step Example Setup (DJI Phantom 4 Equivalent)**
We will use a **DJI Phantom 4-like quadcopter setup** as an example.

---

### **1️⃣ Input Battery Specifications**
| **Parameter**   | **Example Value** |
|----------------|------------------|
| **Battery Voltage (S Count)** | **4S (14.8V nominal, 16.8V max)** |
| **Battery Capacity** | **6000mAh** |
| **Battery C-Rating** | **25C** (for high power) |
| **Battery Weight** | **500g (LiPo) or 900g (Li-Ion)** |

---

### **2️⃣ Enter Drone Power Consumption**
| **Parameter**   | **Example Value** |
|----------------|------------------|
| **Amperage at Hover** | **12A** (for Phantom 4-sized drones) |
| **Amperage at Full Throttle** | **45A** |
| **Number of Motors** | **4** |

💡 **How to Find Amperage Values?**
- Use **motor datasheets** (e.g., **DJI 2312 960KV motors consume ~3A at hover**).
- Measure with an **amp meter or eCalc (previous guide)**.

---

### **3️⃣ Click "Calculate"**  
Once you input the values, press **Calculate** to get:  
✅ **Estimated Hover Time**  
✅ **Full Throttle Time**  
✅ **Battery Discharge Rate & Efficiency**  

---

### **📊 Expected Results for Phantom 4 Setup**
| **Battery Type** | **Hover Time** | **Full Throttle Time** |
|----------------|--------------|----------------|
| **4S 6000mAh LiPo (25C)** | **28-30 min** | **10-12 min** |
| **4S 6000mAh Li-Ion (10C)** | **35-40 min** | **12-15 min** |

📌 **Key Takeaways:**  
✅ **LiPo is best for high-power and aggressive flying.**  
✅ **Li-Ion gives longer flight time but lower discharge capacity.**  

---

### **🚀 Guide to Using WebOCalc - Open Source Drone Power Calculator**  
🔗 **Go to WebOCalc:** [https://www.miniquadtestbench.com/tools/webocalc.html](https://www.miniquadtestbench.com/tools/webocalc.html)  

---

## **📌 Step-by-Step Example Setup (DJI Phantom 4 Equivalent)**  
WebOCalc helps estimate **power consumption, battery endurance, and efficiency**. We will use a **DJI Phantom 4-like quadcopter setup** as an example.  

---

### **1️⃣ Enter General Drone Information**  
| **Parameter**   | **Example Value** |
|----------------|------------------|
| **Frame Type** | **Quadcopter** |
| **Frame Size** | **350mm (DJI Phantom size)** |
| **Total Weight (incl. battery)** | **1.4 kg (1400g)** |

---

### **2️⃣ Enter Battery Specifications**  
| **Parameter**   | **Example Value (LiPo)** | **Example Value (Li-Ion)** |
|----------------|----------------|----------------|
| **Battery Type** | LiPo | Li-Ion |
| **Battery Voltage (Nominal)** | **14.8V (4S)** | **14.8V (4S)** |
| **Battery Capacity** | **6000mAh** | **6000mAh** |
| **Battery C-Rating** | **25C** | **10C** |
| **Battery Weight** | **500g** | **900g** |

---

### **3️⃣ Enter Motor & Propeller Information**  
| **Parameter**   | **Example Value** |
|----------------|------------------|
| **Motor KV (RPM per Volt)** | **900KV** |
| **Motor Power (Each)** | **120W - 150W** |
| **Motor Max Current** | **20A (total 80A for 4 motors)** |
| **Propeller Size** | **9.4-inch (9450)** |
| **Propeller Pitch** | **4.5 inches** |

🔹 **Example Motors:** DJI 2312 960KV, T-Motor MN2212 920KV, or similar.  

---

### **4️⃣ Click "Calculate" to Get Results**  
Once you enter all values, **click "Calculate"** to get:  
✅ **Hover time** (How long the drone can stay in the air at hover)  
✅ **Full-throttle time** (Battery runtime at max throttle)  
✅ **Power consumption** (Amps drawn by motors at different speeds)  
✅ **Efficiency analysis** (Best battery-motor-propeller combo)  

---

### **📊 Expected Results for DJI Phantom 4 Setup**
| **Battery Type** | **Hover Time** | **Full Throttle Time** |
|----------------|--------------|----------------|
| **4S 6000mAh LiPo (25C)** | **28-30 min** | **10-12 min** |
| **4S 6000mAh Li-Ion (10C)** | **35-40 min** | **12-15 min** |

📌 **Key Takeaways:**  
✅ **LiPo is better for aggressive flights & high current draw.**  
✅ **Li-Ion gives longer flight time but has lower max current output.**  
✅ **The tool helps you optimize your drone for endurance or performance.**  

---

### **🚀 MATLAB Simulink (Aerospace Blockset) Guide for Drone Battery Simulation**  

This guide will walk you through **how to simulate a drone battery system using MATLAB Simulink and the Aerospace Blockset**. It covers:  
- Setting up the **battery model**  
- Simulating **power consumption & efficiency**  
- Integrating with **drone flight dynamics**  
- **References and learning resources**  

---

## **📌 1. Install Required MATLAB Toolboxes**
Before starting, make sure you have the following installed in MATLAB:  
✅ **Simulink** (Core simulation environment)  
✅ **Aerospace Blockset** (For drone dynamics & flight simulation)  
✅ **Simscape Electrical** (For modeling battery & electrical systems)  
✅ **Simscape Power Systems** (For energy efficiency & power electronics)  
✅ **Stateflow (Optional, for advanced logic control like Battery Management Systems - BMS)**  

🔗 **To install toolboxes:**  
- Open MATLAB, go to **Home → Add-Ons → Get Add-Ons**, and search for the above toolboxes.  

---

## **📌 2. Setting Up the Simulink Model**
1️⃣ **Open MATLAB and Create a New Simulink Model**  
- Type `simulink` in the MATLAB command window.  
- Click **"Blank Model"** and save it as **"Drone_Battery_Model.slx"**.  
- Open the **Simulink Library Browser** (`Ctrl+Shift+L`).  

---

## **📌 3. Modeling the Battery System**
### **🔋 3.1 Add & Configure a LiPo Battery Model**
1️⃣ **Go to**:  
   - `Simscape → Electrical → Specialized Power Systems → Sources`  
2️⃣ Drag and drop the **Battery** block.  
3️⃣ **Set Battery Parameters (Example: 4S LiPo, 6000mAh)**  
   - **Nominal Voltage:** `14.8V`  
   - **Capacity:** `6000mAh` (6Ah)  
   - **Internal Resistance:** `0.02 ohms`  
   - **Self-Discharge Rate:** `1% per month` (optional)  
   - **Charge Dynamics:** Enable for real-time discharge simulation  

4️⃣ **Monitor Battery Performance:**  
   - Add a **Voltage Sensor** (`Simscape → Electrical → Sensors & Measurements`)  
   - Add a **Current Sensor** to track current draw  

---

### **🔄 3.2 Model Load (Motors & ESCs)**
1️⃣ **Go to**:  
   - `Simscape → Electrical → Specialized Power Systems → Machines`  
2️⃣ Add a **DC Motor** block (or BLDC motor model).  
3️⃣ Set **Motor Parameters** for a drone motor (Example: DJI Phantom 4 Motor Equivalent):  
   - **Rated Voltage:** `14.8V`  
   - **Rated Power:** `150W per motor`  
   - **Number of Motors:** `4`  
   - **Efficiency:** `85%`  
4️⃣ Add an **ESC Model** (Electronic Speed Controller) using:  
   - `Simscape → Electrical → Power Electronics`  
5️⃣ Connect the **Battery → ESC → Motor**  

---

## **📌 4. Simulating Drone Dynamics (Aerospace Blockset)**
### **🚁 4.1 Add a Quadcopter Model**
1️⃣ **Go to**:  
   - `Aerospace Blockset → UAV → Vehicle Model`  
2️⃣ Drag and drop the **Quadcopter Model** block.  
3️⃣ Set Parameters:  
   - **Thrust-to-Weight Ratio** → `2.5`  
   - **Frame Size** → `350mm`  
   - **Payload Weight** → `200g`  
   - **Air Resistance** → Enabled  

### **📊 4.2 Simulating Flight Characteristics**
1️⃣ Connect **Battery → ESC → Motor → Drone Model**  
2️⃣ Set **Flight Conditions** (Hover, Cruise, or Max Thrust)  
3️⃣ Click **"Run Simulation"** to analyze:  
   - **Battery Voltage Drop Over Time**  
   - **Current Draw at Different Thrust Levels**  
   - **Estimated Flight Time**  

---

## **📌 5. Testing & Optimizing the Battery System**
### **⚡ 5.1 Flight Time Estimation**
1️⃣ Add a **Power Calculation Block**:  
   - `Simscape → Electrical → Sensors & Measurements → Power Sensor`  
2️⃣ Measure Power Draw = **Voltage × Current**  
3️⃣ Estimate Flight Time using:  
   \[
   \text{Flight Time} = \frac{\text{Battery Capacity (mAh)}}{\text{Average Current Draw (mA)}}
   \]

---

## **📌 6. Advanced Features (Optional)**
### **🔹 Battery Management System (BMS) using Stateflow**
- Use **Stateflow** to add logic for:
  ✅ **Overvoltage/Undervoltage Protection**  
  ✅ **Battery Cell Balancing**  
  ✅ **Temperature Monitoring**  

### **📡 Real-Time Monitoring with Simulink Dashboard**
- Use the **Simulink Dashboard** to display:
  ✅ Battery Voltage & Current  
  ✅ Drone Altitude & Speed  
  ✅ Power Consumption Graphs  

---

## **📌 7. References & Learning Resources**
### **📚 MATLAB Official Documentation**
🔗 [Simulink Getting Started Guide](https://www.mathworks.com/help/simulink/)  
🔗 [Aerospace Blockset Overview](https://www.mathworks.com/products/aerospace-blockset.html)  
🔗 [Battery Modeling with Simscape](https://www.mathworks.com/help/physmod/sps/ug/battery-model.html)  

### **🎥 Video Tutorials**
📺 [Simulink for UAV Simulation (YouTube)](https://www.youtube.com/watch?v=RuEQ3RUKmXE)  
📺 [Simscape Electrical for Power Systems](https://www.youtube.com/watch?v=Mu8JHlDZtv4)  

---

**MATLAB script** that sets up a **Simulink model** for drone battery simulation. You can run this script in MATLAB, and it will generate the `.slx` file for you.  

The script will:  
✅ **Create a LiPo battery model**  
✅ **Add motors & ESCs**  
✅ **Include a quadcopter flight model**  
✅ **Simulate power consumption & flight time**  

---

### **📌 Steps to Use This Script**
1. **Open MATLAB**  
2. **Copy & Paste the Script** into the MATLAB Editor  
3. **Run the Script**  
4. **Open the Generated Simulink Model (`Drone_Battery_Model.slx`)**  

---

### **🚀 MATLAB Script to Create Simulink Model**

```matlab
% MATLAB Script to Create Simulink Model for Drone Battery Simulation

% Create a new Simulink model
modelName = 'Drone_Battery_Model';
new_system(modelName);
open_system(modelName);

% Add LiPo Battery Model
batteryBlock = 'simscape/Electrical/Specialized Power Systems/Sources/Battery';
add_block(batteryBlock, [modelName, '/LiPo Battery'], 'Position', [100, 100, 200, 200]);
set_param([modelName, '/LiPo Battery'], 'NominalVoltage', '14.8', 'Capacity', '6000', 'InternalResistance', '0.02');

% Add Voltage Sensor
voltageSensor = 'simscape/Electrical/Sensors & Measurements/Voltage Sensor';
add_block(voltageSensor, [modelName, '/Voltage Sensor'], 'Position', [250, 100, 350, 200]);

% Add Current Sensor
currentSensor = 'simscape/Electrical/Sensors & Measurements/Current Sensor';
add_block(currentSensor, [modelName, '/Current Sensor'], 'Position', [250, 250, 350, 350]);

% Add DC Motor Model
motorBlock = 'simscape/Electrical/Specialized Power Systems/Machines/DC Motor';
add_block(motorBlock, [modelName, '/Drone Motor'], 'Position', [400, 150, 500, 250]);
set_param([modelName, '/Drone Motor'], 'NominalVoltage', '14.8', 'RatedPower', '150', 'Efficiency', '85');

% Add Aerospace Quadcopter Model
quadBlock = 'aerospace/UAV/Vehicle Model/Quadcopter';
add_block(quadBlock, [modelName, '/Quadcopter'], 'Position', [600, 100, 800, 300]);

% Connect Components
add_line(modelName, 'LiPo Battery/1', 'Voltage Sensor/1');
add_line(modelName, 'Voltage Sensor/1', 'Drone Motor/1');
add_line(modelName, 'Drone Motor/1', 'Quadcopter/1');
add_line(modelName, 'LiPo Battery/1', 'Current Sensor/1');
add_line(modelName, 'Current Sensor/1', 'Quadcopter/1');

% Save and open the model
save_system(modelName);
open_system(modelName);
disp('Drone Battery Simulation Model Created Successfully!');
```



This MATLAB script will:  
✅ **Create a Simulink model (`Drone_Battery_Model.slx`)**  
✅ **Add a LiPo battery, sensors, motors, and a quadcopter model**  
✅ **Automatically connect components**  

### **📌 Steps to Run**
1. **Copy & paste** the script into MATLAB.  
2. **Run** the script (`Ctrl + Enter`).  
3. **Open Simulink** to visualize the model.  
4. **Simulate** and analyze battery performance.  

---

# PX4 SITL & Gazebo: Drone Hardware Simulation Guide

## **Overview**
This guide provides step-by-step instructions to set up and run **PX4 Software-in-the-Loop (SITL) with Gazebo** for drone hardware simulation. PX4 SITL allows testing of **flight controllers, sensors, and autonomous behavior** in a realistic simulation environment.

## **Features**
✅ Full PX4 SITL setup with Gazebo 3D simulation
✅ MAVLink integration for real-time telemetry
✅ QGroundControl support for mission planning
✅ Customizable drone parameters (Battery, GPS, Flight Modes, etc.)
✅ Different drone models: Quadcopter, Fixed-wing, VTOL

---

## **📌 System Requirements**
- **Ubuntu 20.04 or 22.04** (Preferred OS)
- **At least 8GB RAM and a dedicated GPU**

---

## **🔧 Step 1: Install Prerequisites**
### **Install Required Packages**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install git wget zip cmake ninja-build exiftool \
  python3-pip python3-pyserial python3-dev python3-setuptools \
  python3-pyulog python3-toml python3-numpy python3-pandas python3-jinja2 \
  x11-xserver-utils xterm gdb valgrind \
  build-essential gnupg flex bison gperf \
  autoconf automake texinfo libtool \
  libftdi-dev libgmp-dev libmpc-dev libmpfr-dev libncurses5-dev \
  libusb-1.0-0-dev python3-venv
```

### **Install PX4 Firmware**
```bash
cd ~
git clone --recursive https://github.com/PX4/PX4-Autopilot.git
cd PX4-Autopilot
bash ./Tools/setup/ubuntu.sh
```
🔄 **Restart your terminal** after installation.

---

## **🚀 Step 2: Run PX4 SITL with Gazebo**
Run the standard **quadcopter simulation**:
```bash
cd ~/PX4-Autopilot
make px4_sitl gazebo
```
This will start:
- **PX4 SITL firmware**
- **Gazebo Simulator with the Quadcopter model**
- **MAVLink Communication for telemetry**

---

## **🎮 Step 3: Connect QGroundControl (Optional)**
QGroundControl (QGC) is a GUI-based mission planner for PX4.

### **Install QGroundControl**
```bash
wget https://d176tv9ibo4jno.cloudfront.net/latest/QGroundControl.AppImage
chmod +x QGroundControl.AppImage
./QGroundControl.AppImage
```
✅ **Click ‘Add New Vehicle’ → Connect via UDP (Port: 14550)**

---

## **📡 Step 4: Simulating Different Drone Models**
To change the drone model:
```bash
make px4_sitl gazebo_iris  # Standard quadcopter
make px4_sitl gazebo_plane  # Fixed-wing aircraft
make px4_sitl gazebo_tiltrotor  # VTOL tiltrotor
make px4_sitl gazebo_standard_vtol  # VTOL drone
```

---

## **🔬 Step 5: Customize Drone Parameters**
You can modify PX4 parameters for **battery, GPS, flight modes, etc.**

### **Modify PX4 Parameter File**
```bash
nano ~/PX4-Autopilot/ROMFS/px4fmu_common/init.d-posix/rcS
```
Modify values such as:
```bash
param set BAT_CAPACITY 3000  # Battery Capacity (mAh)
param set GPS_USE 1  # Enable GPS
param set MPC_XY_CRUISE 5.0  # Set horizontal cruise speed
```
🔹 Save the file (`Ctrl+X`, then `Y`, then `Enter`) and restart SITL.

---

## **📊 Step 6: Analyzing Flight Logs**
Flight logs are stored in:
```bash
~/.ros/log/latest
```
To visualize flight data:
```bash
pyulog ~/path-to-log.ulg
```
Or upload logs to **[Flight Review](https://logs.px4.io/)** for analysis.

---

## **🎯 Advanced Topics**
🔹 **ROS2 Integration:** Use PX4 with ROS for **autonomous navigation**
🔹 **Real Hardware Testing:** Flash PX4 firmware to **Pixhawk flight controllers**
🔹 **GPS & LiDAR Integration:** Test **GPS waypoint missions** and **obstacle avoidance** in Gazebo

---



