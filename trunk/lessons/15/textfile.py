print('== Lettura, primo approccio ==')

file_in = open('loremipsum.txt')
while True:
    line = file_in.readline()
    if line == '':
        break
    print(line, end='')
file_in.close()

#alternativa:
file_in = open('loremipsum.txt')
jobdone=False
while not jobdone:
    line = file_in.readline()
    if line == '':
        jobdone=True
    else:
        print(line, end='')
file_in.close()

print('== Scrittura ==')

lines = (
    'Aenean non nulla ut neque pharetra faucibus feugiat sit amet erat.',
    'Nullam sed elit ante.',
    'Praesent aliquet dictum mauris, non pretium leo luctus eu.'
    )

file_out = open('aenannon.txt', 'w')
for line in lines:
    file_out.write(line+'\n')

file_out.close()


print('== Aggiunta ==')

newlines = (
    'Vestibulum viverra molestie nulla, sed aliquet urna malesuada in.',
    'Etiam porttitor quam ut massa rutrum vitae volutpat erat interdum.',
    'Etiam lorem purus, sollicitudin ac pretium in, pellentesque ac magna.',
    'Nam laoreet, turpis nec feugiat mollis, metus augue sollicitudin augue, in dictum nulla dolor ac nulla.'
    )

file_out = open('aenannon.txt', 'a')
for line in newlines:
    file_out.write(line+'\n')
file_out.close()


print('== Lettura, secondo approccio ==')

file_written = open('aenannon.txt')

for line in file_written:
    print(line, end='')
file_written.close()

print('== Lettura, terzo approccio ==')
with open('aenannon.txt') as f:
    lines = f.readlines()
for line in lines:
    print(line, end='')
