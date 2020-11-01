myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}
for k, v in myData.items():
  print('key:', k, ', value:', v)
y = (myData)
limit = 100
for x in range(1, limit + 1):
    y.append(x)
print(y)
