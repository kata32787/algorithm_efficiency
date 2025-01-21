class HashTable:
    def __init__(self, capacity=10):
        """Initialize the hash table with a default capacity and empty buckets."""
        self.capacity = capacity  # Number of buckets
        self.table = [[] for _ in range(capacity)]  # Create an array of empty lists (buckets)
        self.size = 0  # Number of elements in the hash table

    def _hash_function(self, key):
        """Hash function to map keys to bucket indices."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash_function(key)
        # Check if the key already exists; update if it does
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, add the new key-value pair
        self.table[index].append([key, value])
        self.size += 1

    def search(self, key):
        """Search for a value associated with a key."""
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                self.size -= 1
                return True
        return False  # Key not found

    def __str__(self):
        """Return a string representation of the hash table."""
        return "\n".join(f"Bucket {i}: {bucket}" for i, bucket in enumerate(self.table))


if __name__ == "__main__":
    # Example usage
    hash_table = HashTable()

    # Insert key-value pairs
    hash_table.insert("apple", 5)
    hash_table.insert("banana", 10)
    hash_table.insert("orange", 15)

    # Search for a key
    print("Search for 'apple':", hash_table.search("apple"))

    # Delete a key
    hash_table.delete("banana")
    print("After deleting 'banana':")
    print(hash_table)
    def _resize(self):
        """Resize the hash table when the load factor exceeds 0.7."""
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]
        for bucket in self.table:
            for key, value in bucket:
                new_index = hash(key) % new_capacity
                new_table[new_index].append([key, value])
        self.table = new_table
        self.capacity = new_capacity

    def insert(self, key, value):
        """Insert a key-value pair and resize if load factor exceeds 0.7."""
        if self.size / self.capacity > 0.7:
            self._resize()
        super().insert(key, value)
