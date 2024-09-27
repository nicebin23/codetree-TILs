def check_beautiful_sequences(A, B):
    N = len(A)
    M = len(B)
    results = []

    min_B = min(B)
    max_B = max(B)

    for i in range(N - M + 1):
        window = A[i:i + M]
        window_set = set(window)

        for k in range(-max_B, max_B + 1):
            transformed_B = {b + k for b in B}
            if transformed_B.issubset(window_set):
                results.append(i)
                break

    return results


N = int(input())
A = [int(input()) for i in range(N)]

M = int(input())
B = [int(input()) for i in range(M)]

result = check_beautiful_sequences(A, B)
print(len(result))

for index in result :
    print(index+1)