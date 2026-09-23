import itertools
P_bigram = {
    "em": {"học": 0.52, "đi": 0.48},
    "học": {"bài": 0.40, "toán": 0.35, "vẽ": 0.25},
    "đi": {"chợ": 0.58, "bơi": 0.22, "ngủ": 0.20}
}
def exhaustive_lm():
    sentences = []
    for w2, p2 in P_bigram["em"].items():
        for w3, p3 in P_bigram[w2].items():
            sentences.append((f"em {w2} {w3}", 1.0 * p2 * p3))
    sentences.sort(key=lambda x: x[1], reverse=True)
    return sentences
def beam_search_lm(k):
    beam = [("em", 1.0)]
    for step in range(2): 
        next_beam = []
        for seq, prob in beam:
            last_word = seq.split()[-1]
            if last_word in P_bigram:
                for next_word, p in P_bigram[last_word].items():
                    next_beam.append((f"{seq} {next_word}", prob * p))
        next_beam.sort(key=lambda x: x[1], reverse=True)
        beam = next_beam[:k]
    return beam[0]
tags = ['N', 'V']
words = ["em", "học", "bài", "toán"]
pi = {'N': 0.6, 'V': 0.4}
A = {'N': {'N': 0.35, 'V': 0.65}, 'V': {'N': 0.70, 'V': 0.30}}
B = {
    'N': {'em': 0.35, 'học': 0.10, 'bài': 0.40, 'toán': 0.30},
    'V': {'em': 0.05, 'học': 0.45, 'bài': 0.05, 'toán': 0.02}
}
def viterbi_decode():
    f = [{}]
    backptr = [{}]
    for t in tags:
        f[0][t] = pi[t] * B[t][words[0]]
        backptr[0][t] = None
    for i in range(1, len(words)):
        f.append({})
        backptr.append({})
        for t in tags:
            max_prob = -1
            best_prev = None
            for prev_t in tags:
                prob = f[i-1][prev_t] * A[prev_t][t] * B[t][words[i]]
                if prob > max_prob:
                    max_prob = prob
                    best_prev = prev_t
            f[i][t] = max_prob
            backptr[i][t] = best_prev
    best_last_tag = max(tags, key=lambda t: f[-1][t])
    best_prob = f[-1][best_last_tag]
    sequence = [best_last_tag]
    for i in range(len(words)-1, 0, -1):
        sequence.insert(0, backptr[i][sequence[0]])
    return f, backptr, sequence, best_prob
def exhaustive_viterbi():
    best_seq = None
    max_prob = -1
    for seq in itertools.product(tags, repeat=4):
        prob = pi[seq[0]] * B[seq[0]][words[0]]
        for i in range(1, 4):
            prob *= A[seq[i-1]][seq[i]] * B[seq[i]][words[i]]
        if prob > max_prob:
            max_prob = prob
            best_seq = seq
    return best_seq, max_prob
def run_all():
    print("MÔ HÌNH NGÔN NGỮ")
    all_sentences = exhaustive_lm()
    print(f"[Vét cạn] Câu tốt nhất: '{all_sentences[0][0]}' (P = {all_sentences[0][1]:.6f})")
    greedy = beam_search_lm(1)
    print(f"Giải mã tham lam (k=1): '{greedy[0]}' (P = {greedy[1]:.6f})")
    for k in [1, 2, 3]:
        beam = beam_search_lm(k)
        print(f"Giải mã theo chùm k={k}: '{beam[0]}' (P = {beam[1]:.6f})")   
    print("\n MÔ HÌNH VITERBI ")
    f, backptr, seq, best_prob = viterbi_decode()
    print(f"{'i':<3} | {'Từ':<6} | {'f[i][N]':<10} | {'f[i][V]':<10} | {'Tr.của N':<10} | {'Tr.của V':<10}")
    print("-" * 65)
    for i in range(4):
        fn = f"{f[i]['N']:.6f}"
        fv = f"{f[i]['V']:.6f}"
        pn = backptr[i]['N'] if backptr[i]['N'] else "-"
        pv = backptr[i]['V'] if backptr[i]['V'] else "-"
        print(f"{i+1:<3} | {words[i]:<6} | {fn:<10} | {fv:<10} | {pn:<10} | {pv:<10}")
    print(f"\n[Viterbi] Dãy nhãn: {' - '.join(seq)} (P = {best_prob:.6f})")
    ex_seq, ex_prob = exhaustive_viterbi()
    print(f"[Vét cạn 16 TH] Dãy: {' - '.join(ex_seq)} (P = {ex_prob:.6f})")
    if seq == list(ex_seq):
        print("=> Viterbi đã tìm đúng dãy nhãn tối ưu toàn cục!")
if __name__ == "__main__":
    run_all()