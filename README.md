# Multi-Module Engineering Calculator Suite

A console-driven electrical engineering tool written in pure Python. This comprehensive software package provides instant numerical solvers and step-by-step transient derivations for fundamental circuit engineering principles including Ohm's Law, voltage division, RC time-constants, and multi-variable Joule power states.

## 🚀 Key Tool Modules
* **Ohm's Law Solver:** Dynamically determines missing parameters across $V$, $I$, or $R$ using algebraic exception constraints.
* **Voltage Divider Analytical Network:** Evaluates circuit loop current, total power loop boundaries, and specific output voltage parameters ($V_{\text{out}}$) across a standard dual-resistor node.
* **RC Time Constant ($\tau$) Tracker:** Computes exact time parameters in seconds while outputting dynamic numerical step models tracing the $e^{-t/\tau}$ charging state behavior up to steady-state boundary conditions ($5\tau$).
* **Joule's Law Power Matrix Engine:** Uses algebraic deduction combinations to resolve complete operational electrical parameters from any two known metrics across Power ($W$), Voltage ($V$), Current ($A$), or Resistance ($\Omega$).

---

## 🛠️ Tech Stack & Philosophy
* **Core Language:** Python 3 (Pure Standard Library)
* **Dependency Overhead:** Zero (`0`) external package installations needed. Designed to compile seamlessly out of the box on any native Python kernel shell.

---

## 📐 Governing Analytical Equations

### Ohm's Law
$$V = I \cdot R$$

### Voltage Divider Network
$$V_{\text{out}} = V_{\text{in}} \cdot \left(\frac{R_2}{R_1 + R_2}\right)$$

### RC Circuit Dynamics
$$\tau = R \cdot C \quad \Big| \quad V_c(t) = V_s \cdot \left(1 - e^{-\frac{t}{\tau}}\right)$$

### Power Equivalencies Matrix
$$P = V \cdot I = I^2 \cdot R = \frac{V^2}{R}$$

---

## 📋 Operational Installation Guide

1. Clone this utility folder locally:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/engineering-calculators.git](https://github.com/YOUR-USERNAME/engineering-calculators.git)
   cd engineering-calculators
