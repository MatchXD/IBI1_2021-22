import re
import pandas

seq = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
output = open('cut_genes.fa','w')
total_line = ''
for line in seq:
    line = line.rstrip()
    if '>' in line:
        if total_line != '':
            if 'GAATTC' in total_line:
                list1 = re.findall(r'.+gene:(.+?)\s', total_line)
                gene = list1[0]
                list2 = re.findall(r'.+](.+)',total_line)
                DNA = list2[0]
                num = len(DNA)
                line1 = gene + '      ' + str(num) + '\n'
                line2 = DNA + '\n'
                output.write(line1)
                output.write(line2)
        total_line = ''
    total_line += line.rstrip()
output.close()
seq.close()