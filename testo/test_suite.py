import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solution import solve_mwr

class TestMWR(unittest.TestCase):
    def test_example_1_to_2(self):
        # (1 + x)^2 = 1.21 => x = 0.1
        # Equivalent to: cf_0 = 1000, cf_1 = 0, mv_2 = 1210
        # 1000 * (1+x)^2 + 0 * (1+x)^1 = 1210
        cash_flows = [1000, 0]
        mv = 1210
        result = solve_mwr(cash_flows, mv)
        self.assertAlmostEqual(result, 0.1, places=3)

    def test_example_3(self):
        # Example 3 from README
        # 1000 * (1 + x) ^ 5 + 1500 * (1 + x) ^ 4 = 3806.66
        cash_flows = [1000, 1500, 0, 0, 0]
        mv = 3806.66
        result = solve_mwr(cash_flows, mv)
        self.assertAlmostEqual(result, 0.1, places=3)

    def test_withdrawal(self):
        # 1000 deposit, 500 withdrawal after 1 year, final value 600 after 2 years
        # 1000 * (1+x)^2 - 500 * (1+x) = 600
        # 1000(1 + 2x + x^2) - 500 - 500x = 600
        # 1000x^2 + 1500x - 100 = 0
        # x = [-1500 + sqrt(1500^2 - 4*1000*-100)] / 2000
        # x = [-1500 + sqrt(2,250,000 + 400,000)] / 2000
        # x = [-1500 + sqrt(2,650,000)] / 2000
        # x = [-1500 + 1627.882] / 2000 = 0.06394
        cash_flows = [1000, -500]
        mv = 600
        result = solve_mwr(cash_flows, mv)
        self.assertAlmostEqual(result, 0.06394, places=4)

if __name__ == '__main__':
    unittest.main()
