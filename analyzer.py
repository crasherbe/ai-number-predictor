from collections import Counter

def analyze_results(results):

    digits = "".join(results)

    freq = Counter(digits)

    position = {
        "p1": Counter(),
        "p2": Counter(),
        "p3": Counter(),
        "p4": Counter(),
        "p5": Counter()
    }

    for r in results:

        for i,d in enumerate(r):

            position[f"p{i+1}"][d] += 1

    return freq, position
