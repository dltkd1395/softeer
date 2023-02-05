import sys


def getRank(items):
    l = 0
    rank = 1
    result = [0]*N

    for s, p in items:
        rank += l
        l=0
        for j in p:
            result[j] = rank
        l += len(p)
    return result

N=int(input())

total_score = [[i,0] for i in range(N)]
for i in range(3):
    score = list(map(int,input().split()))
    temp = {}
    for idx, s in enumerate(score):
        total_score[idx][1] += s
        if s not  in temp:
            temp[s] = [idx]
        else:
            temp[s].append(idx)
    items = list(temp.items())
    items.sort(reverse=True)
    print(*getRank(items))

total_score.sort(key=lambda x:-x[1])
score_dict = {}
for idx, s in total_score:
    if s not in score_dict:
        score_dict[s] = [idx]
    else:
        score_dict[s].append(idx)
items = score_dict.items()
print(*getRank(items))

