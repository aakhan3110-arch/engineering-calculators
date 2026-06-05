import math
import time

def clear_screen():
    print("\n" + "="*50 + "\n")

# ==========================================
# 1. CORE CALCULATOR MODULES
# ==========================================
def calculate_ohms_law():
    print("--- Ohm's Law Calculator ---")
    print("Leave the variable you want to solve for BLANK (press Enter).")
    
    v_in = input("Enter Voltage (V) [or Enter to solve]: ").strip()
    i_in = input("Enter Current (A) [or Enter to solve]: ").strip()
    r_in = input("Enter Resistance (Ω) [or Enter to solve]: ").strip()
    
    try:
        if not v_in and i_in and r_in:
            i, r = float(i_in), float(r_in)
            v = i * r
            print(f"\n[Result] Calculated Voltage (V) = {v:.4f} V")
        elif not i_in and v_in and r_in:
            v, r = float(v_in), float(r_in)
            if r == 0: raise ZeroDivisionError("Resistance cannot be zero.")
            i = v / r
            print(f"\n[Result] Calculated Current (I) = {i:.4f} A")
        elif not r_in and v_in and i_in:
            v, i = float(v_in), float(i_in)
            if i == 0: raise ZeroDivisionError("Current cannot be zero.")
            r = v / i
            print(f"\n[Result] Calculated Resistance (R) = {r:.4f} Ω")
        else:
            print("\n[Error] Invalid input combination! Leave exactly ONE field blank.")
    except ValueError:
        print("\n[Error] Please enter valid numeric values.")
    except ZeroDivisionError as e:
        print(f"\n[Error] {e}")

def calculate_voltage_divider():
    print("--- Voltage Divider Calculator ---")
    try:
        v_in = float(input("Enter Input Voltage (V_in): "))
        r1 = float(input("Enter Resistor R1 (Ω): "))
        r2 = float(input("Enter Resistor R2 (Ω): "))
        
        if (r1 + r2) == 0:
            raise ZeroDivisionError("Total series resistance cannot be zero.")
            
        v_out = v_in * (r2 / (r1 + r2))
        print(f"\n[Result] Output Voltage (V_out across R2) = {v_out:.4f} V")
        print(f"         Total Loop Resistance = {r1 + r2:.2f} Ω")
        print(f"         Circuit Current = {(v_in / (r1 + r2)):.4f} A")
    except ValueError:
        print("\n[Error] Please enter valid numeric values.")
    except ZeroDivisionError as e:
        print(f"\n[Error] {e}")

def calculate_rc_time_constant():
    print("--- RC Time Constant (τ) Calculator ---")
    try:
        r = float(input("Enter Resistance (Ω): "))
        c = float(input("Enter Capacitance (Farads or use exponents e.g., 10e-6 for 10μF): "))
        
        tau = r * c
        print(f"\n[Result] Time Constant (τ) = {tau:.6f} seconds")
        
        # Display transient charging timeline points
        print("\n--- Capacitor Transient Charging State Timeline ---")
        print(f" {'Time Step':<12} | {'% Charge':<10} | {'Status'}")
        print("-" * 45)
        for target_tau in range(1, 6):
            charge_pct = (1 - math.exp(-target_tau)) * 100
            status = "Steady State reached" if target_tau == 5 else "Transient state"
            print(f" {target_tau}τ ({target_tau*tau:.5f}s) | {charge_pct:.2f}%     | {status}")
            
    except ValueError:
        print("\n[Error] Please enter valid numeric values.")

def calculate_power():
    print("--- Joule's Law Power Calculator ---")
    print("Leave the TWO variables you want to evaluate BLANK (press Enter).")
    
    p_in = input("Enter Power (W): ").strip()
    v_in = input("Enter Voltage (V): ").strip()
    i_in = input("Enter Current (A): ").strip()
    r_in = input("Enter Resistance (Ω): ").strip()
    
    # Map out provided inputs
    inputs = {'P': p_in, 'V': v_in, 'I': i_in, 'R': r_in}
    knowns = {k: float(v) for k, v in inputs.items() if v}
    
    if len(knowns) != 2:
        print(f"\n[Error] Got {len(knowns)} inputs. You must provide exactly TWO parameters to map the electrical state.")
        return
        
    try:
        # Evaluate combinations
        if 'V' in knowns and 'I' in knowns:
            knowns['P'] = knowns['V'] * knowns['I']
            knowns['R'] = knowns['V'] / knowns['I'] if knowns['I'] != 0 else float('inf')
        elif 'I' in knowns and 'R' in knowns:
            knowns['P'] = (knowns['I'] ** 2) * knowns['R']
            knowns['V'] = knowns['I'] * knowns['R']
        elif 'V' in knowns and 'R' in knowns:
            if knowns['R'] == 0: raise ZeroDivisionError("Resistance cannot be zero.")
            knowns['P'] = (knowns['V'] ** 2) / knowns['R']
            knowns['I'] = knowns['V'] / knowns['R']
        elif 'P' in knowns and 'V' in knowns:
            if knowns['V'] == 0: raise ZeroDivisionError("Voltage cannot be zero.")
            knowns['I'] = knowns['P'] / knowns['V']
            knowns['R'] = (knowns['V'] ** 2) / knowns['P'] if knowns['P'] != 0 else float('inf')
        elif 'P' in knowns and 'I' in knowns:
            if knowns['I'] == 0: raise ZeroDivisionError("Current cannot be zero.")
            knowns['V'] = knowns['P'] / knowns['I']
            knowns['R'] = knowns['P'] / (knowns['I'] ** 2)
        elif 'P' in knowns and 'R' in knowns:
            if knowns['R'] <= 0 or knowns['P'] < 0: raise ValueError("Invalid physical state constants.")
            knowns['I'] = math.sqrt(knowns['P'] / knowns['R'])
            knowns['V'] = math.sqrt(knowns['P'] * knowns['R'])

        print("\n=== Evaluated Electrical Power State ===")
        for unit_key, unit_name, sym in [('P', 'Power', 'W'), ('V', 'Voltage', 'V'), ('I', 'Current', 'A'), ('R', 'Resistance', 'Ω')]:
            print(f" * {unit_name:<12} ({sym}) = {knowns[unit_key]:.4f}")
            
    except ValueError:
        print("\n[Error] Invalid math operation. Ensure values are mathematically feasible.")
    except ZeroDivisionError as e:
        print(f"\n[Error] {e}")

# ==========================================
# 2. RUNTIME USER INTERFACE
# ==========================================
def main_menu():
    while True:
        clear_screen()
        print("======== INDUSTRIAL ENGINEERING CALCULATORS ========")
        print("1. Ohm's Law Calculator (V, I, R)")
        print("2. Voltage Divider Circuit Solver")
        print("3. RC Time Constant Analyzer (τ)")
        print("4. Power & Joule's Law Engine (P, V, I, R)")
        print("5. Exit System")
        print("====================================================")
        
        choice = input("Select an engineering utility module [1-5]: ").strip()
        clear_screen()
        
        if choice == '1':
            calculate_ohms_law()
        elif choice == '2':
            calculate_voltage_divider()
        elif choice == '3':
            calculate_rc_time_constant()
        elif choice == '4':
            calculate_power()
        elif choice == '5':
            print("[*] Powering down engine cores. Goodbye.")
            break
        else:
            print("[Error] Unrecognized module option index. Please try again.")
            
        input("\nPress [Enter] to return to the main utility index...")

if __name__ == "__main__":
    main_menu()
