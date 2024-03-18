import unittest

def calculate_average_velocity(sprint_points):
    if not sprint_points:
        return 0
    return sum(sprint_points) / len(sprint_points)

class TestCalculateAverageVelocity(unittest.TestCase):
    def test_with_positive_numbers(self):
        """Test average velocity with positive integers."""
        self.assertEqual(calculate_average_velocity([30, 40, 50]), 40.0)

    

    def test_with_single_value(self):
        """Test average velocity with a single value."""
        self.assertEqual(calculate_average_velocity([50]), 50.0)

    def test_with_negative_numbers(self):
        """Test average velocity with negative integers."""
        self.assertEqual(calculate_average_velocity([-30, -40, -50]), -40.0)

    def test_with_mixed_sign_numbers(self):
        """Test average velocity with mixed positive and negative integers."""
        self.assertEqual(calculate_average_velocity([-10, 0, 10]), 0.0)

    def test_with_floating_point_numbers(self):
        """Test average velocity with floating point numbers."""
        self.assertAlmostEqual(calculate_average_velocity([25.5, 30.75, 50.25]), 35.5)

    def test_with_large_numbers(self):
        """Test average velocity with very large integers."""
        self.assertEqual(calculate_average_velocity([1000000, 2000000, 3000000]), 2000000.0)

   

   

   

if __name__ == '__main__':
    unittest.main()
