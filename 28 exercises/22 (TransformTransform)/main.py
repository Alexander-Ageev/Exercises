def s_function(source_sequence):
    transform_sequence = []
    N = len(source_sequence)
    for i in range(N):
        for j in range(N - i):
            k = i + j
            m = max(source_sequence[j: k + 1])
            transform_sequence.append(m)
    return transform_sequence[::-1]

def TransformTransform(source_sequence, N):
    transform_sequence = s_function(s_function(source_sequence))
    if sum(transform_sequence) % 2 == 0:
        double_transform_even = True
    else:
        double_transform_even = False
    return double_transform_even