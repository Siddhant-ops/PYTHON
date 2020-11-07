import unittest
import cap


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = "python"
        result = cap.cap_text(text)
        return result
        self.assertEqual(result, "Python")

    def test_multiple_word(self):
        text = "python coders"
        result = cap.title_text(text)
        return result
        self.assertEqual(result, "Python Coders")


if __name__ == "__main__":
    unittest.main()
