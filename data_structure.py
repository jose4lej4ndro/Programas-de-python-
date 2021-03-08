# Use the file name mbox-short.txt as the file name

# acumulador
sum = 0

fh = open('words.txt')
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        sld = line[20:26]
        sld = float(sld)

        # Hace la suma de los nuevos números que se van leyendo
        # desde el archivo
        sum = sum + sld
        print(sum)
print('Average is:', sum)

# Cuando se trabajan con archivos siempre cerrarlo al final de usarlo
fh.close()
