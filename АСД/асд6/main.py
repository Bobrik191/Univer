import random
import matplotlib.pyplot as plt


class HashTable:

    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def pjw_hash(self, key):
        high_bits = 0xFFFFFFFF << (32 - 4)

        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value << 4) + ord(key[i])
            test = hash_value & high_bits
            if test != 0:
                hash_value = ((hash_value ^ (test >> 24)) & (~high_bits))

        return hash_value % self.size

    def quadratic_hash(self, key, i):
        return (self.pjw_hash(key) + i * i) % self.size

    def insert(self, key, value):
        index = self.pjw_hash(key)
        first_index = index
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
        else:
            i = 1
            while True:
                index = self.quadratic_hash(key, i)
                if index == first_index:
                    self.resize(self.size * 2)
                if self.keys[index] is None:
                    self.keys[index] = key
                    self.values[index] = value
                    break
                i += 1
        return 1

    def resize(self, new_size):
        old_keys = self.keys
        old_values = self.values
        self.keys = [None] * new_size
        self.values = [None] * new_size
        self.size = new_size

        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.insert(old_keys[i], old_values[i])

    def search(self, key):
        index = self.pjw_hash(key)
        comparisons = 1
        if self.keys[index] == key:
            return self.values[index], comparisons
        else:
            i = 1
            while self.keys[index] is not None:
                comparisons += 1
                index = self.quadratic_hash(key, i)
                if self.keys[index] == key:
                    return self.values[index], comparisons
                i += 1
        return None, comparisons


def generate_data(size):
    data = []
    for i in range(size):
        key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 20)))
        value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 200)))
        data.append((key, value))
    return data


def main():
    sizes = int(input("Введіть кількість елементів: "))
    #sizes = [100, 1000, 5000, 10000, 20000]
    sizes_multipliers = int(input("Введіть кількість елементів: "))
    sizes_multipliers = [3, 5, 10]
    search_comparisons = [[], [], []]

    for j in range(3):
        for i in range(5):
            print(sizes[i], sizes_multipliers[j])
            hashtable = HashTable(sizes[i] * sizes_multipliers[j])
            data = generate_data(sizes[i])

            search_count = 0
            for key, value in data:
                hashtable.insert(key, value)

            for key, value in data:
                result, comparisons = hashtable.search(key)
                if result is not None:
                    search_count += comparisons

            print(data[len(data) - 1], hashtable.search(data[len(data) - 1][0]))

            search_comparisons[j].append(search_count)

    for i in range(3):
        print(f"1/{sizes_multipliers[i]}: {search_comparisons[i]}")

    fig, ax = plt.subplots()

    ax.plot(sizes, search_comparisons[0], color='red', label='33%')
    ax.plot(sizes, search_comparisons[1], color='blue', label='20%')
    ax.plot(sizes, search_comparisons[2], color='purple', label='10%')
    ax.plot(sizes, sizes, color='black', linestyle='--', label='y = x')

    ax.set_xlabel('Кількість порівнянь')
    ax.set_ylabel('Кількість елементів у таблиці')
    ax.set_title('Графік залежності кількості порівнянь')

    ax.legend()

    plt.show()


if __name__ == "__main__":
    main()
