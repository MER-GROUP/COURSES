print('------------------')

# import sys

# for line in sys.stdin:
#     print(line.strip('\n'))

print('------------------')

# import sys

# data = [line.strip() for line in sys.stdin]

print('------------------')

# import sys

# data = list(map(str.strip, sys.stdin))

print('------------------')

# name, surname = input(), input()

print('------------------')

# import sys

# data = sys.stdin.readlines()

print('------------------')

# import sys

# data = sys.stdin.read()

print('------------------')

import sys

print('Hello')
sys.stdout.write('world!')
print('from')
sys.stdout.write('python\n')
print('Bye-bye')

print('------------------')

# import sys

# sys.stdout.write(17)

print('------------------')

import sys

# преобразуем данные в строку
sys.stdout.write(str(17))     

print('------------------')

import sys

# store original stdout object for later
temp = sys.stdout    
# redirect all prints to this log file             
sys.stdout = open('log.txt', 'w') 
# nothing appears at interactive prompt
print('testing123')   
# again nothing appears. it's written to log file instead            
print('another line') 
# ordinary file object            
sys.stdout.close()  
# restore print commands to interactive prompt              
sys.stdout = temp       
# this shows up in the interactive prompt          
print('back to normal')           

print('------------------')

import sys

for line in sys.stdin:
    if '\n' == line:
        break
    print(line.strip('\n'))

print('------------------')