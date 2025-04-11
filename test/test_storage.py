import unittest
from storage import Storage

class TestStorage(unittest.TestCase):
    
    def setUp(self):
        self.storage = Storage()

    def test_save_and_load_data(self):
        data = {"key": "value"}
        self.storage.save_data(data)
        loaded_data = self.storage.load_data()
        self.assertEqual(data, loaded_data)

if __name__ == "__main__":
    unittest.main()
