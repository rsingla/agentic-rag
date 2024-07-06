def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        print(fib_sequence)
    return fib_sequence[:-1]


n = 5

print(fibonacci(n))


tuple_val = [2,4,5,7,8]

print(len(tuple_val))

new_dict = {"1":"value","key1": "value1", "key2": "value2"}

print(len(new_dict))

for key, value in new_dict.items():
    print(key)
    print(value)