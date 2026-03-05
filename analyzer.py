from collections import Counter

def analyze_results(results):

    digits = "".join(results)
    freq = Counter(digits)

    # tentukan panjang digit dari result pertama
    length = len(results[0])

    # buat counter posisi otomatis
    position = {}

    for i in range(length):
        position[f"p{i+1}"] = Counter()

    # hitung frekuensi posisi
    for r in results:

        if len(r) != length:
            continue  # skip kalau digit tidak sama

        for i,d in enumerate(r):

            position[f"p{i+1}"][d] += 1

    return freq, position
