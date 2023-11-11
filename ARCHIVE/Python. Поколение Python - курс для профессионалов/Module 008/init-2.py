print('------------------')

def draw_rect(width, height, step):
    if step < height:
        print('*' * width)
        draw_rect(width, height, step + 1)

draw_rect(4, 3, 0)
print()
draw_rect(6, 6, 0)
print()
draw_rect(10, 2, 0)

print('------------------')

def draw_rect(width, height, step=0):
    if step < height:
        print('*' * width)
        draw_rect(width, height, step + 1)

draw_rect(4, 3)
print()
draw_rect(6, 6)
print()
draw_rect(10, 2)

print('------------------')

def draw_rect(width, height):
    def rec(step):
        if step < height:
            print('*' * width)
            rec(step + 1)
    rec(0)

draw_rect(4, 3)
print()
draw_rect(6, 6)
print()
draw_rect(10, 2)

print('------------------')

def print_numbers(start, end):
    def rec(num):
        if num <= end:
            print(num)
            rec(num + 1)
    rec(start)

print_numbers(0, 7)
print()
print_numbers(-3, 4)

print('------------------')