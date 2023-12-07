import unittest
from apply_discount import apply_discount

class TestApplyDiscount(unittest.TestCase):
    def test_apply_discount_1(self):
        self.assertEqual(
            extract_data("User details: Name:John. He is very active. He is also quite tall, standing at Height:181cm. He is Age:30, and spends his time as an Occupation:Engineer. End of data."),
            [("Name", "John"), ("Height", "181cm"), ("Age", "30"), ("Occupation", "Engineer")]
        )

    def test_apply_discount_2(self):
        self.assertEqual(
            extract_data("Product ID:12345, in the Category:Electronics department, priced at Price:299. All rights reserved."),
            [("ID", "12345"), ("Category", "Electronics"), ("Price", "299")]
        )

    def test_apply_discount_3(self):
        self.assertEqual(
            extract_data("Emergency Contacts: Police:911, Fire:999, Medical:112. Stay safe."),
            [("Police", "911"), ("Fire", "999"), ("Medical", "112")]
        )

if __name__ == '__main__':
    unittest.main()