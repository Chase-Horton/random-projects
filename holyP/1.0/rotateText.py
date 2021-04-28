def rotateFile(file):
    columns = []
    with open(file, "r") as f:
        for line in f:
            columns.append(line.rstrip())
    i = 0
    lines = []
    longest = max(columns, key=len)
    longest = len(longest)
    for i in range(longest):
        lines.append('')
    while len(columns) > 0:
        for n in range(longest):
            if n >= len(columns[0]):
                lines[n] += ' '
            else:
                lines[n] += columns[0][n]
        columns.pop(0)
    return lines

def rotateText(text):
    pass
def write(filename, text):
    with open(filename, 'w') as f:
        for line in text:
            f.write(line+'\n')
        
#for line in rotateText('fib.txt'):
#    print(line)
#write('fib.txt',rotateText('fib.holyP'))
