def solution(total_lambs):
    # Your code here
    maxlist=[]
    i=0
    henchmen=0
    while i<= total_lambs:
        currentvalue=2**i
        maxlist.append(currentvalue)
        henchmen=henchmen + currentvalue
        if henchmen > total_lambs:
            break
        i=i+1

    lambs=[1,1]
    fibhenchmen=2
    y=2
    while y<= total_lambs:
        value=lambs[y-1] + lambs[y-2]
        lambs.append(value)
        fibhenchmen=fibhenchmen + int(lambs[y])
        if fibhenchmen > total_lambs:
            break
        y=y+1

    answer = len(lambs) - len(maxlist)

    return abs(answer)
