def linear_probing(size, keys):
    table = [-1]*size
    for key in keys:
        index = key % size
        while table[index] != -1:
            index = (index + 1) % size
        table[index] = key
    return table

size = int(input("Enter hash table size: "))
keys = list(map(int, input("Enter keys separated by space: ").split()))
hash_table = linear_probing(size, keys)
print("Hash Table:", hash_table)
