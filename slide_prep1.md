When analyzing **battery power consumption** in drone flights, the total flight can be divided into several **distinct stages**, each with different power demands. Understanding these stages helps in optimizing battery life and drone performance.

---

### 🔋 **Stages of Flying a Drone (W.r.t Battery Power Consumption)**

1. ### **Pre-Flight (Idle/Standby Mode)**
   - **Description**: Drone is powered on, GPS acquiring, sensors initializing, motors idle.
   - **Power Usage**: Low
   - **Main Consumers**: Microcontroller, IMU, GPS module, telemetry systems, LEDs.

2. ### **Takeoff**
   - **Description**: Motors spin up to generate lift.
   - **Power Usage**: **Very High (Peak Consumption)**
   - **Main Consumers**: Motors and ESCs draw a sudden burst of current.
   - **Note**: Sudden inrush current can stress the battery if not designed properly.

3. ### **Hovering**
   - **Description**: Drone maintains altitude with minimal horizontal motion.
   - **Power Usage**: Moderate to High
   - **Main Consumers**: Motors (constant RPM to fight gravity)
   - **Factors**:
     - Payload weight
     - Wind conditions
     - Drone type (quadcopter vs fixed-wing)

4. ### **Cruise / Horizontal Flight**
   - **Description**: Drone moves laterally at a steady altitude and speed.
   - **Power Usage**: Lower than hovering (especially in **fixed-wing drones** which use lift)
   - **Main Consumers**: Motors (less thrust required than hover), control electronics.
   - **Optimization**: Efficient cruising saves power vs hovering.

5. ### **Maneuvers / Acceleration**
   - **Description**: Sharp turns, altitude changes, rapid acceleration/deceleration.
   - **Power Usage**: **High**
   - **Main Consumers**: Motors with varying loads.
   - **Note**: Power spikes can happen frequently in this phase.

6. ### **Loitering / Holding Pattern**
   - **Description**: Drone circles or hovers in one location.
   - **Power Usage**: Similar to hover, possibly slightly higher due to lateral adjustments.
   - **Use Case**: Surveillance or mapping missions.

7. ### **Return-to-Home (RTH) / Descent**
   - **Description**: Drone returns and begins to descend.
   - **Power Usage**: **Moderate to Low**
   - **Descent**: Gravity aids, motors throttle down.
   - **RTH Cruise**: Efficient, usually slower and optimized by autopilot for battery conservation.

8. ### **Landing**
   - **Description**: Drone gently descends and touches down.
   - **Power Usage**: Low (unless wind compensation needed)
   - **Note**: Must still keep sensors and stabilization active.

9. ### **Post-Flight (Telemetry/Shutdown)**
   - **Description**: Motors off, data transmitted, logs saved.
   - **Power Usage**: Very Low
   - **Main Consumers**: Electronics only (no propulsion).

---

###  Power Consumption Overview Table:

| Stage           | Power Usage   | Remarks |
|----------------|---------------|---------|
| Pre-Flight      | 🔋 Low         | Sensors, GPS initialization |
| Takeoff         | 🔋🔋🔋🔋 Very High | Highest burst of current |
| Hovering        | 🔋🔋🔋 High     | Sustained motor load |
| Cruise          | 🔋🔋 Moderate  | Efficient motion (esp. fixed-wing) |
| Maneuvering     | 🔋🔋🔋 High     | Power spikes during agility |
| Loitering       | 🔋🔋🔋 High     | Similar to hover |
| Descent / RTH   | 🔋🔋 Moderate  | Gravity helps, less throttle |
| Landing         | 🔋 Low         | Short duration |
| Post-Flight     | 🔋 Very Low    | Logging & shutdown |

---


1. **Battery specifications**, and  
2. **Current consumption (or power draw)** of the drone in each stage.

Let’s break this down in a clean, practical way.

---

## 🔋 **1. Key Battery Specifications Needed**

| Spec | Symbol | Unit | Description |
|------|--------|------|-------------|
| **Battery Capacity** | \( C \) | mAh or Ah | Total charge available |
| **Nominal Voltage** | \( V \) | Volts (V) | Average voltage during discharge (e.g., 11.1V for 3S LiPo) |
| **Max Discharge Rate** | \( D \) | C (C-rate) | Max safe discharge speed: \( D \times C \) = max current |
| **Internal Resistance** | \( R_{int} \) | Ohms (Ω) | Affects efficiency and heat loss |
| **Battery Type** | — | — | LiPo, Li-ion, etc. (LiPo preferred for high current) |

---

## ⏱️ **2. Estimating Flight Time per Stage**

We can use this basic formula for each stage:

\[
\text{Time}_{\text{stage}} = \frac{C_{\text{usable}}}{I_{\text{stage}}}
\]

Where:
- \( C_{\text{usable}} \) is usable capacity in Ah (usually 80–90% of full to prevent over-discharge)
- \( I_{\text{stage}} \) is current draw during that stage in Amperes (can be measured or estimated)

Or in power terms:

\[
\text{Time}_{\text{stage}} = \frac{V \times C_{\text{usable}}}{P_{\text{stage}}}
\]

Where \( P_{\text{stage}} \) is power draw in watts (W).

---

### 🔍 Example

Let’s assume:
- 3S LiPo battery: 2200 mAh = 2.2 Ah
- Nominal Voltage: 11.1 V
- Usable capacity: 90% → \( 0.9 \times 2.2 = 1.98 \, \text{Ah} \)
- Stage-wise current draw:

| Stage        | Est. Current Draw | Duration Formula |
|--------------|------------------|------------------|
| Pre-flight   | 0.5 A            | \( \frac{1.98}{0.5} = 3.96 \, \text{hrs} \) |
| Takeoff      | 25 A             | \( \frac{1.98}{25} = 0.079 \, \text{hrs} \approx 4.7 \, \text{min} \) |
| Hover        | 15 A             | \( \frac{1.98}{15} = 0.132 \, \text{hrs} \approx 7.9 \, \text{min} \) |
| Cruise       | 10 A             | \( \frac{1.98}{10} = 0.198 \, \text{hrs} \approx 11.9 \, \text{min} \) |
| Maneuvering  | 20 A             | \( \frac{1.98}{20} = 0.099 \, \text{hrs} \approx 6 \, \text{min} \) |
| RTH/Descent  | 8 A              | \( \frac{1.98}{8} = 0.247 \, \text{hrs} \approx 14.8 \, \text{min} \) |

👉 You’d use mission planning or telemetry logs to estimate how long each stage lasts and then calculate total energy use.

---

### 🔧 **Optional Enhancements**

- Include motor efficiency losses (~80–90%)
- Add power draw of electronics (~0.5–2W)
- Consider temperature derating of batteries
- Use **Coulomb counting** (with a current sensor) for real-time measurement

---

## ✅ Summary: To Calculate Stage-wise Flight Time

1. **Get battery specs**: \( C \), \( V \), \( D \)
2. **Estimate or measure** current draw \( I \) in each stage
3. Use:
   \[
   \text{Time}_{\text{stage}} = \frac{\text{Usable Capacity (Ah)}}{I_{\text{stage}}}
   \]
4. Add safety margin (leave 10–20% capacity unused)

---

Great point! To improve the accuracy and **safety** of your flight time estimations, you should **include a safety margin** in the formula to **avoid over-discharging the battery**.

---

### ✅ **Improved Formula with Safety Margin**

Let:

- \( C_{\text{nominal}} \) = nominal battery capacity (Ah)  
- \( M \) = safety margin (in decimal, e.g., 0.1 for 10%)  
- \( C_{\text{usable}} = (1 - M) \times C_{\text{nominal}} \)  
- \( I_{\text{stage}} \) = current draw during that stage (A)

**stage time** :

\[
\boxed{
\text{Time}_{\text{stage}} = \frac{(1 - M) \times C_{\text{nominal}}}{I_{\text{stage}}}
}
\]

---

### 🧮 **Example (with 10% safety margin)**

- Battery: 2200 mAh = 2.2 Ah  
- Safety Margin: 10% → \( M = 0.1 \)  
- Usable capacity: \( 2.2 \times (1 - 0.1) = 1.98 \, \text{Ah} \)  
- Hover current: 15 A

\[
\text{Time}_{\text{hover}} = \frac{1.98}{15} = 0.132 \, \text{hr} \approx \boxed{7.9 \text{ min}}
\]

---
