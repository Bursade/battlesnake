"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

    python src/tests.py -v

"""
import unittest

from src import logic


class AvoidNeckTest(unittest.TestCase):
    def test_avoid_neck_all(self):
        # Arrange
        test_head = {"x": 5, "y": 5}
        test_neck = {"x": 5, "y": 5}
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_head, test_neck, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 4)
        self.assertEqual(possible_moves, result_moves)

    def test_avoid_neck_left(self):
        # Arrange
        test_head = {"x": 5, "y": 5}
        test_neck = {"x": 4, "y": 5}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_head, test_neck, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_right(self):
        # Arrange
        test_head = {"x": 5, "y": 5}
        test_neck = {"x": 6, "y": 5}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left"]

        # Act
        result_moves = logic._avoid_my_neck(test_head, test_neck, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_up(self):
        # Arrange
        test_head = {"x": 5, "y": 5}
        test_neck = {"x": 5, "y": 6}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_head, test_neck, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_down(self):
        # Arrange
        test_head = {"x": 5, "y": 5}
        test_neck = {"x": 5, "y": 4}
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_head, test_neck, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)


class AvoidTheWallsTest(unittest.TestCase):
    def test_avoid_right_wall(self):
        # Arrange
        test_head = {"x": 5, "y": 3}
        test_height = 5
        test_width = 5
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left"]

        # Act
        result_moves = logic._avoid_the_walls(test_height, test_width, test_head, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_left_wall(self):
        # Arrange
        test_head = {"x": 0, "y": 3}
        test_height = 5
        test_width = 5
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "right"]

        # Act
        result_moves = logic._avoid_the_walls(test_height, test_width, test_head, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_top_wall(self):
        # Arrange
        test_head = {"x": 3, "y": 5}
        test_height = 5
        test_width = 5
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left", "right"]

        # Act
        result_moves = logic._avoid_the_walls(test_height, test_width, test_head, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_bottom_wall(self):
        # Arrange
        test_head = {"x": 3, "y": 0}
        test_height = 5
        test_width = 5
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left", "right"]

        # Act
        result_moves = logic._avoid_the_walls(test_height, test_width, test_head, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)
    
    def test_avoid_top_right_corner(self):
        # Arrange
        test_head = {"x": 5, "y": 5}
        test_height = 5
        test_width = 5
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left"]

        # Act
        result_moves = logic._avoid_the_walls(test_height, test_width, test_head, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 2)
        self.assertEqual(expected, result_moves)

    def test_avoid_bottom_right_corner(self):
        # Arrange
        test_head = {"x": 5, "y": 0}
        test_height = 5
        test_width = 5
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left"]

        # Act
        result_moves = logic._avoid_the_walls(test_height, test_width, test_head, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 2)
        self.assertEqual(expected, result_moves)

    def test_avoid_top_left_corner(self):
        # Arrange
        test_head = {"x": 0, "y": 5}
        test_height = 5
        test_width = 5
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "right"]

        # Act
        result_moves = logic._avoid_the_walls(test_height, test_width, test_head, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 2)
        self.assertEqual(expected, result_moves)


    def test_avoid_bottom_left_corner(self):
        # Arrange
        test_head = {"x": 0, "y": 0}
        test_height = 5
        test_width = 5
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "right"]

        # Act
        result_moves = logic._avoid_the_walls(test_height, test_width, test_head, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 2)
        self.assertEqual(expected, result_moves)


if __name__ == "__main__":
    unittest.main()
