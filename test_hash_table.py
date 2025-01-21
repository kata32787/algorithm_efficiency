import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):

    def test_insert_and_search(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        self.assertEqual(hash_table.search("key1"), "value1")
        self.assertEqual(hash_table.search("key2"), "value2")
        self.assertIsNone(hash_table.search("key3"))  # Non-existent key

    def test_update_value(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        hash_table.insert("key1", "updated_value1")
        self.assertEqual(hash_table.search("key1"), "updated_value1")

    def test_delete(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        self.assertTrue(hash_table.delete("key1"))
        self.assertIsNone(hash_table.search("key1"))
        self.assertFalse(hash_table.delete("key1"))  # Non-existent key

    def test_collision_handling(self):
        hash_table = HashTable(capacity=2)  # Small capacity to force collisions
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")  # Collides with key1
        self.assertEqual(hash_table.search("key1"), "value1")
        self.assertEqual(hash_table.search("key2"), "value2")

if __name__ == "__main__":
    unittest.main()
