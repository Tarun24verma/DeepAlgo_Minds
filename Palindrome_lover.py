T=int(input())
for _ in range(T):
    N=int(input())
    numbers=list(map(int, input().split()))

    for i in range(N):
        numbers[i] = numbers[i] % 2
    
    
    counts = {}

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    if N%2==0:
        if all(value % 2 == 0 for value in counts.values()):
            print(1)
        else:
            print(0)
    else:
        odd_count = sum(1 for value in counts.values() if value % 2 == 1)
        if odd_count == 1:
            print(1)
        else:
            print(0)