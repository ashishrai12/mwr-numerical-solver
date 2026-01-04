# Testo - Testing and Visualization for MWR

This directory contains utility scripts to verify and visualize the Money Weighted Return (MWR) calculation.

## Contents

- `test_suite.py`: Unit tests for the MWR solver, covering examples from the main README and edge cases.
- `visualize.py`: Generates a plot of investment performance (Market Value vs. Time) and overlays cash flows.

## How to use

### Run Tests
```bash
python testo/test_suite.py
```

### Generate Plots
```bash
python testo/visualize.py
```
This will create an `investment_plot.png` in the root directory.
