import csv
import matplotlib.pyplot as plt
import sys
import os

# Add parent directory to path so we can import solution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solution import solve_mwr

def generate_plots(csv_file='test.csv'):
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    years = []
    cash_flows = []
    market_values = []

    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            years.append(int(row['year']))
            cash_flows.append(float(row['cash_flow']))
            market_values.append(float(row['market_value']))
    
    # Calculate MWR
    # cash_flows for all years up to n-2
    # final market value is in the last row (year n-1)
    mwr_cf = cash_flows[:-1]
    final_mv = market_values[-1]
    mwr = solve_mwr(mwr_cf, final_mv)
    
    # Set up the plot
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Plot Market Value (Line)
    color = 'tab:blue'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Market Value ($)', color=color)
    ax1.plot(years, market_values, color=color, marker='o', linewidth=2, label='Market Value')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, alpha=0.3)
    
    # Create a second y-axis for Cash Flows (Bars)
    ax2 = ax1.twinx()
    color = 'tab:green'
    ax2.set_ylabel('Cash Flow ($)', color=color)
    
    # Positive cash flows are deposits (green), negative are withdrawals (red)
    bar_colors = ['tab:green' if val >= 0 else 'tab:red' for val in cash_flows]
    ax2.bar(years, cash_flows, color=bar_colors, alpha=0.4, label='Cash Flow')
    ax2.tick_params(axis='y', labelcolor=color)
    
    # Title and layout
    plt.title(f'Investment Performance (Annualized MWR: {mwr:.2%})', fontsize=14)
    fig.tight_layout()
    
    # Save the plot
    output_path = 'investment_plot.png'
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    # Check if we are in the testo directory or parent
    if os.path.exists('test.csv'):
        generate_plots('test.csv')
    elif os.path.exists('../test.csv'):
        generate_plots('../test.csv')
    else:
        print("Could not find test.csv")
