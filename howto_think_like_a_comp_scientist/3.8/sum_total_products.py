xs = [12,10,32,3,66,17,42,99,20]
total = 0
squared = 0
squared_sum = 0
total_product = 1

for x in xs:
    total = total + x
    squared = x**2
    squared_sum += squared
    total_product *= x
    print(str(x) + "\t" + str(squared) + "\t" + str(total_product))

for x in range(len(str(total))):
    print("-",end="")
print("\t", end="")

for x in range(len(str(squared_sum))):
    print("-",end="")
print("\t",end="")

for x in range(len(str(total_product))):
    print("-",end="")
print('')

print(str(total)+"\t"+str(squared_sum)+"\t"+str(total_product))
