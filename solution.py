import csv
import sys

def solve_mwr(cash_flows, final_market_value):
    """
    Solves for x in the equation:
    sum_{i=0}^{n-2} cash_flow[i] * (1 + x)^(n-1-i) = final_market_value
    """
    n = len(cash_flows) + 1
    
    def f(x):
        res = 0
        for i, cf in enumerate(cash_flows):
            # i=0 corresponds to year 0, i=1 to year 1, etc.
            # Exponent for year i is (n-1) - i
            res += cf * (1 + x)**(n - 1 - i)
        return res - final_market_value

    def df(x):
        res = 0
        for i, cf in enumerate(cash_flows):
            power = n - 1 - i
            if power > 0:
                res += cf * power * (1 + x)**(power - 1)
        return res

    # Newton-Raphson method
    x = 0.1  # Initial guess of 10%
    for _ in range(100):
        val_f = f(x)
        val_df = df(x)
        
        if abs(val_df) < 1e-12:
            # If derivative is too small, try a small step or bisection
            break
            
        x_new = x - val_f / val_df
        if abs(x_new - x) < 1e-10:
            return x_new
        x = x_new
    
    return x

def main():
    filename = 'test.csv'
    cash_flows = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
            if not rows:
                print("Error: Empty CSV file.")
                return

            # cash_flows for all years up to n-2
            # final market value is in the last row (year n-1)
            for i in range(len(rows) - 1):
                cash_flows.append(float(rows[i]['cash_flow']))
            
            final_market_value = float(rows[-1]['market_value'])
            
            mwr = solve_mwr(cash_flows, final_market_value)
            # Output rounded to 3 decimal places as per requirement (within 0.001)
            print(f"{mwr:.3f}")
            
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
