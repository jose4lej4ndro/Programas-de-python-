# Use the file name mbox-short.txt as the file name
fh = open("words.txt")
for line in fh:
    if  line.startswith("X-DSPAM-Confidence:"):
    	sld = line[20:26]
    	sld = float(sld)
    	res = sld + sld
    	print(res)
print("Average is:", res)
   