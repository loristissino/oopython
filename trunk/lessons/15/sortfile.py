print('== Lettura, ordinamento, riscrittura ==')
with open('unordered.txt') as f_in, open('ordered.txt', 'w') as f_out:
    lines=f_in.readlines()
    lines.sort()
    f_out.writelines(lines)

