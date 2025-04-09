Great point! To improve the accuracy and **safety** of your flight time estimations, you should **include a safety margin** in the formula to **avoid over-discharging the battery**.

---

### ✅ **Improved Formula with Safety Margin**

Let:

- \( C_{\text{nominal}} \) = nominal battery capacity (Ah)  
- \( M \) = safety margin (in decimal, e.g., 0.1 for 10%)  
- \( C_{\text{usable}} = (1 - M) \times C_{\text{nominal}} \)  
- \( I_{\text{stage}} \) = current draw during that stage (A)

Then the **stage time** becomes:

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

Would you like me to give a version of this formula in a form you can directly paste into your presentation or report (with symbols and definitions)?
