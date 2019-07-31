import unittest
from soundly.features.temporal import get_max


class TestTemporalFeatures(unittest.TestCase):
    def test_max(self):
        arr = [1, 2, 3, 4, 20, 5]
        self.assertEqual(get_max(arr), 20)


if __name__ == "__main__":
    unittest.main()
