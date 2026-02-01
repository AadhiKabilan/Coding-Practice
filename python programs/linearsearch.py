arr=[2,1,5,7,4,8,2,4]
target=8
n=len(arr)
for i in range(n):
    if target==arr[i]:
        print(arr[i]," found at ",i)
        break
    print("Checking ",i," and ", arr[i])