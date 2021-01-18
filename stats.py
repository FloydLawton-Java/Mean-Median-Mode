import csv
from collections import Counter
with open("C:/Users/v0788/Desktop/Python/Project_Mean_median_mode/Height Weight.csv", newline='')as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
#print(fileData)
#shorting data to get the height of people
newData=[]
for i in range(len(fileData)):
    num=fileData[i][2]
    newData.append(float(num))
#getting the mean
n=len(newData)
total=0
for x in newData:
    total=total+x
mean=total/n
print("Mean is " + str(mean))
#median
n=len(newData)
newData.sort()
if n%2==0:
    median1=float(newData[n//2])
    median2=float(newData[n//2-1])
    median=(median1+median2)/2
else:
    median=newData[n//2]
    print(n)
print("Median is" + str(median))
#mode now
data=Counter(newData)
modeDataforrange={
    "50-60":0, 
    "60-70":0,
    "70-80":0,
}
for height, occurence in data.items():
    if 50<float(height)<60:
        modeDataforrange["50-60"]+=occurence
    elif 60<float(height)<70:
        modeDataforrange["60-70"]+=occurence
    elif 70<float(height)<80:
        modeDataforrange["70-80"]+=occurence
modeRange, modeoccurence=0,0
for range, occurence in modeDataforrange.items(): 
    if occurence > modeoccurence: 
        modeRange, modeoccurence = [int(range.split("-")[0]), int(range.split("-")[1])],occurence 
mode = float((modeRange[0] + modeRange[1]) / 2) 
print(f"Mode is -> {mode:2f}")