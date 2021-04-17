# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
counter=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    x1=line.find('0')
    total = float(line[x1:]) + total
    counter=counter+1
average = float(total/counter)
print("Average spam confidence:", average)
