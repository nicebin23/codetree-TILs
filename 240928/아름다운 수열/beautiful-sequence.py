def bSort(arr) :
  n = len(arr)
  for last in range(1, n) :
    for i in range(last, 0, -1) :
      if arr[i-1] > arr[i] :
        arr[i-1], arr[i] = arr[i], arr[i-1]
  return arr

def check_beautiful_sequences(A, B):
    N = len(A)
    M = len(B)
    results = []
    count = 0
    
    B_sorted = bSort(B)

    for i in range(N - M + 1):
        window = A[i:i + M]
        window_sorted = bSort(window)
        diff = [window_sorted[j] - B_sorted[j] for j in range(M)]
        if len(set(diff)) == 1:
            results.append(i + 1)
            count += 1
    return count, results

N = int(input())
A = [int(input()) for i in range(N)]
M = int(input())
B = [int(input()) for i in range(M)]

count, beautiful_indices = check_beautiful_sequences(A, B)

print(count)
for index in beautiful_indices:
    print(index)