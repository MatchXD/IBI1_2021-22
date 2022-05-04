import re
seq = open('cut_genes.fa')
fname = input('please write a filename as the new fasta file to be written to: ')
output = open(fname,'w')
for line in seq:
    if  line.startswith('Y'):
        list = re.findall(r'(.+?)\s', line)
        gene = list[0]
    else:
        count = 1
        DNA = line
        number = re.findall('GAATTC', line)
        count += len(number)
        line1 = gene + '     ' + str(count) + '\n'
        line2 = DNA
        output.write(line1)
        output.write(line2)
output.close()
seq.close()


