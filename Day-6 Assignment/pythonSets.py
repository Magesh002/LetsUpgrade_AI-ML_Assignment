
setData = {"Car", "Bike", "Train", "Bus"}
print(setData)

print("Bike" in setData)
for s in setData:
    print(s)

setData.add("Flight")
print(setData)

setData.update(["Cycle", "Metro", "Van"])
print(setData)

print(len(setData))

setData.discard("Metro")
print(setData)

print(setData.pop())
print(setData)

print("Clearing the data from set")
setData.clear()
print(setData)

print("Deleting the set variable")
del setData
# print(setData)

setData1 = {"Car", "Bike", "Train", "Bus"}
setData2 = {1, 2, 3}

setData3 = setData1.union(setData2)
print(setData3)

setData1.update(setData2)
print(setData1)

setData = set(("Car", "Bike", "Train", "Bus"))
print(setData)