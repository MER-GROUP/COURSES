'''
file = open('file2_test.txt', 'w')
file.write('Hello')
file.write(' world')
file.write('\nRed\n')
lines = ['line1', 'line2', 'line3']
s = '\n'.join(lines)
file.write(s)
file.close()
'''

file2 = open('file2_test.txt', 'a')
file2.write('\nHello')

file2.close