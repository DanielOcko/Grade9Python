y = 0
print("string of DNA:")
strand1 = input()
print("copied string:")
strand2 = input()
for x in range(len(strand1)):
    if strand1[x] != strand2[x]:
        y+=1
print(f"The hamming range is {y}")
