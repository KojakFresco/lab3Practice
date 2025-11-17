# Counting sort 1
def countingSort(a):
    cnt = [0]*100

    for i in range(len(a)):
        cnt[a[i]] += 1
    return cnt

# Counting sort 2
def countingSort(a):
    # Write your code here
    cnt = [0]*100

    for i in range(len(a)):
        cnt[a[i]] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]

    res = [0]*len(a)
    for i in a:
        cnt[i] -= 1
        res[cnt[i]] = i

    return res



# Counting sort 3

def counting_sort(a):
    cnt = [0]*100

    for i in range(len(a)):
        cnt[a[i]] += 1
    for i in range(1, 100):
        cnt[i] += cnt[i - 1]

    return cnt
    
n = int(input())
arr = []

for _ in range(n):
    i, str = input().split()
    arr.append(int(i))
for i in counting_sort(arr):
    print(i, end=" ")
