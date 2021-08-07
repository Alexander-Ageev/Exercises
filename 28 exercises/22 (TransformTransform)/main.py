def s_function(A):
    B = []
    N = len(A)
    for i in range(N):
        for j in range(N - i):
            k = i + j
            m = max(A[j: k + 1])
            B.append(m)
    return B[::-1]

def TransformTransform(A, N):
    B = s_function(s_function(A))
    if sum(B) % 2 == 0:
        return True
    else:
        return False