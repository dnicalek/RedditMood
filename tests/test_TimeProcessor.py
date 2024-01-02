import unittest
from datetime import datetime
from TimeProcessor import TimeProcessor


class TestTimeProcessor(unittest.TestCase):

    def test_get_current_timestamp(self):
        # Arrange
        expected_timestamp = datetime.now().timestamp()

        # Act
        actual_timestamp = TimeProcessor.get_current_timestamp()

        # Assert
        self.assertAlmostEqual(actual_timestamp, expected_timestamp, delta=1)

    def test_delay(self):
        # Arrange
        start_time = datetime.now()

        # Act
        TimeProcessor.delay()

        # Assert
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        self.assertGreaterEqual(elapsed_time.seconds, 30)


if __name__ == '__main__':
    unittest.main()
