print('------------------')

def get_stat(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers)/len(numbers)

    return (minimum, maximum, average)

print(get_stat([1, 2, 3, 4, 5]))
print(get_stat([7]))

print('------------------')

# def message():
#     print('Это рекурсивная функция')
#     message()

# message()

print('------------------')

def message(times):
    if times > 0:
        print('Это рекурсивная функция')
        message(times - 1)

message(5)

print('------------------')

def message(times):
    if times > 0:
        print('Это рекурсивная функция.')
        message(times - 1)
        print(times)

message(5)

print('------------------')

def message(times):
    if times > 0:
        print('Это рекурсивная функция.', times)
        message(times - 1)
        print(times)

message(5)

print('------------------')