from analyzer import analyze_results

def score_number(num, freq, position):

    score = 0

    for i,d in enumerate(num):

        if freq[d] >= 3:
            score += 2

        if position[f"p{i+1}"][d] >= 2:
            score += 3

    odd = sum(int(x)%2 for x in num)

    if odd >= len(num)//2:
        score += 2

    big = sum(int(x)>=5 for x in num)

    if big >= len(num)//2:
        score += 2

    return score


def predict(results, candidates):

    freq,position = analyze_results(results)

    scored = []

    for n in candidates:

        s = score_number(n,freq,position)

        scored.append((n,s))

    scored.sort(key=lambda x:x[1],reverse=True)

    return scored[:20]
