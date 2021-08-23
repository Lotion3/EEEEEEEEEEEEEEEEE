import csv

with open("SOCR-HeightWeight.csv" ,newline="") as d:
    datafile=csv.reader(d)
    files=list(datafile)

files.pop(0)
amount=len(files)
print(amount)

new_data=[]

for i in range(len(files)):
    num=files[i][1]
    new_data.append(float(num))
   ## print(new_data)

n=len(new_data)
print(n)
total=0
for x in new_data:
    total += x

mean=total/n

new_data.sort()
print(new_data)
if n%2 == 0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2
else:
    median=new_data[n//2]

print("Mean " + str(mean))
print("Meidan " + str(median))