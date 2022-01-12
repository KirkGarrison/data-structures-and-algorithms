class HashTable():

    def __init__(self) -> None:
        self.length = 599
        self.table = [[]] * self.length

    def string_to_int(self, string):
        ascii_value = [ord(letter) for letter in string]
        return sum(ascii_value)

    def hash(self, key) -> int:
        if type(key) is str:
            hasher = self.string_to_int(key)
        elif type(key) is int:
            hasher = key

        index_position = (hasher * 6917) % self.length
        return index_position

    def add(self, key, value) -> None:
        hash_key = self.hash(key)

        list_index = self.table[hash_key]

        list_index.append((key, value))

    def get(self, key) -> any:
        hash_key = self.hash(key)

        index_list = self.table[hash_key]

        if len(index_list) == 0:
            return None
        else:
            for match in index_list:
                if match[0] == key:
                    return match[1]
        return None

    def contains(self, key):
        return bool(self.get(key))
