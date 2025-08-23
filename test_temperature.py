import unittest
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit_typical(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6)
        self.assertAlmostEqual(celsius_to_fahrenheit(20), 68)
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67, places=2)  # Absolute zero

    def test_fahrenheit_to_celsius_typical(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(68), 20)
        self.assertAlmostEqual(fahrenheit_to_celsius(-459.67), -273.15, places=2)  # Absolute zero

    def test_celsius_to_fahrenheit_extremes(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(1000), 1832)
        self.assertAlmostEqual(celsius_to_fahrenheit(-1000), -1768)

    def test_fahrenheit_to_celsius_extremes(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(1000), 537.78, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(-1000), -573.33, places=2)

    def test_celsius_to_fahrenheit_float(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0.5), 32.9)
        self.assertAlmostEqual(celsius_to_fahrenheit(-0.5), 31.1)

    def test_fahrenheit_to_celsius_float(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32.9), 0.5, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(31.1), -0.5, places=2)

if __name__ == '__main__':
    unittest.main()