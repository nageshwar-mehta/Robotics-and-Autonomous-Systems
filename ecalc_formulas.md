

# 🛠️ eCalc Motor Calculation - Reverse Engineering (README Format)

This document outlines how eCalc likely calculates various motor parameters (Hover, Optimum, Maximum) using a mix of formulas and pre-characterized database values.

---

## 📊 Sources of Data

| Source Type        | Used For                                                |
|--------------------|---------------------------------------------------------|
| 📑 Datasheet Values | Kv, Resistance, No-load Current, Motor Weight          |
| 🧪 Empirical Data   | Thrust, Torque, Temp rise, ESC losses, Prop behavior   |
| 📐 Formulas         | Electric/Mechanical power, RPM, Efficiency, etc.       |
| 📚 Look-Up Tables   | Pre-tested motor + prop combos interpolated for inputs |

---

## ⚡ Core Formulas Used

### 1. **Electric Power**
\[
P_{elec} = V \times I
\]

### 2. **RPM Estimate**
\[
\text{RPM} = K_v \times (V - I \times R)
\]

Where:
- \( K_v \): RPM per Volt (from motor spec)
- \( R \): Motor winding resistance

### 3. **Mechanical Power**
\[
P_{mech} = \tau \cdot \omega = \text{Torque} \times \frac{2\pi \cdot \text{RPM}}{60}
\]

Often, this is derived from empirical thrust-torque curves.

### 4. **Efficiency**
\[
\eta = \frac{P_{mech}}{P_{elec}} \times 100
\]

### 5. **Power-to-Weight Ratio**
\[
\text{PWR} = \frac{P_{mech}}{\text{Total Weight}}
\]

### 6. **Specific Thrust**
\[
\text{Specific Thrust} = \frac{\text{Thrust}}{P_{elec}}
\]

---

## 📦 Parameters: Source Breakdown

| Parameter             | Formula Based? | Data-Based? | Notes                                           |
|-----------------------|----------------|-------------|-------------------------------------------------|
| Voltage               | ✅              | —           | User input or regulated value                   |
| Current               | ✅              | ✅           | From test data or \( I = P/V \) approx.         |
| RPM                   | ✅              | ✅           | Formula + corrected from real-world data        |
| Electric Power        | ✅              | —           | \( P = V \cdot I \)                             |
| Mechanical Power      | ✅              | ✅           | From thrust curve or torque formula             |
| Efficiency            | ✅              | ✅           | Formula above, but includes losses              |
| Temperature Estimate  | —              | ✅           | Based on current draw, ambient temp, airflow    |
| Thrust                | ✅              | ✅           | From empirical prop+RPM data                    |
| Throttle % (Linear)   | ✅              | —           | From user throttle input (usually 0–100%)       |
| Throttle % (Log)      | ✅              | —           | Logarithmic scale to reflect real throttle feel |
| Specific Thrust       | ✅              | ✅           | Derived using thrust data and power             |
| Power-Weight Ratio    | ✅              | —           | Derived metric for drone performance            |

---

## 📈 Example Snapshots

### 🚁 Hover
- Input Throttle: 54%
- Current: 3.47 A
- RPM: 4876 rpm
- Electric Power: 38 W
- Mech. Power: 31 W
- Efficiency: 81.6%
- Specific Thrust: 8.12 g/W

### ⚙️ Max
- Current: 13.53 A
- RPM: 8488 rpm
- Electric Power: 142.9 W
- Mech. Power: 116 W
- Efficiency: 81.1%

### ✅ Optimum
- Current: 6.22 A
- RPM: 9659 rpm
- Electric Power: 67.5 W
- Mech. Power: 58.1 W
- Efficiency: 86.0%

---

## 📌 Notes

- Some values are approximations derived from **manufacturer test data**.
- Actual flight conditions (wind, pitch, load) can affect real-world behavior.
- eCalc applies **correction factors** for airflow, ESC losses, and heating.
- It also includes safety margins to prevent overheating beyond 80–100°C.

---

## 📚 References

- [eCalc Website](https://ecalc.ch)
- [RCGroups Motor Theory Threads](https://www.rcgroups.com/forums)
- [OpenMotorSim GitHub](https://github.com/shaun-edwards/openmotorcalc)
- Martin Simons – *Model Aircraft Aerodynamics*
- Manufacturer Test Sheets (e.g., T-Motor, EMAX)

---
