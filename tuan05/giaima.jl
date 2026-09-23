using Printf
P_bigram = Dict(
    "em" => Dict("học" => 0.52, "đi" => 0.48),
    "học" => Dict("bài" => 0.40, "toán" => 0.35, "vẽ" => 0.25),
    "đi" => Dict("chợ" => 0.58, "bơi" => 0.22, "ngủ" => 0.20)
)
function exhaustive_lm()
    sentences = []
    for (w2, p2) in P_bigram["em"]
        for (w3, p3) in P_bigram[w2]
            push!(sentences, ("em $w2 $w3", 1.0 * p2 * p3))
        end
    end
    sort!(sentences, by = x -> x[2], rev=true)
    return sentences
end
function beam_search_lm(k)
    beam = [("em", "em", 1.0)]
    for step in 1:2
        next_beam = []
        for (seq, last_w, prob) in beam
            if haskey(P_bigram, last_w)
                for (nw, p) in P_bigram[last_w]
                    push!(next_beam, ("$seq $nw", nw, prob * p))
                end
            end
        end
        sort!(next_beam, by = x -> x[3], rev=true)
        beam = next_beam[1:min(k, length(next_beam))]
    end
    return beam[1]
end
words = ["em", "học", "bài", "toán"]
tags = ["N", "V"]
pi_prob = Dict("N" => 0.6, "V" => 0.4)
A = Dict("N" => Dict("N" => 0.35, "V" => 0.65), "V" => Dict("N" => 0.70, "V" => 0.30))
B = Dict(
    "N" => Dict("em" => 0.35, "học" => 0.10, "bài" => 0.40, "toán" => 0.30),
    "V" => Dict("em" => 0.05, "học" => 0.45, "bài" => 0.05, "toán" => 0.02)
)
function run_all()
    println(" MO HINH NGON NGU ")
    ex_res = exhaustive_lm()
    @printf("[Vet can] Cau tot nhat: '%s' (P = %.6f)\n", ex_res[1][1], ex_res[1][2])
    
    greedy = beam_search_lm(1)
    @printf("Giai ma tham lam (k=1): '%s' (P = %.6f)\n", greedy[1], greedy[3])
    for k in 1:3
        beam = beam_search_lm(k)
        @printf("Giai ma theo chum k=%d: '%s' (P = %.6f)\n", k, beam[1], beam[3])
    end
    println("\n MO HINH VITERBI ")
    f = [Dict{String, Float64}() for _ in 1:4]
    bp = [Dict{String, String}() for _ in 1:4]
    for t in tags
        f[1][t] = pi_prob[t] * B[t][words[1]]
        bp[1][t] = "-"
    end
    for i in 2:4
        for t in tags
            max_p = -1.0; best_prev = ""
            for pt in tags
                p = f[i-1][pt] * A[pt][t] * B[t][words[i]]
                if p > max_p; max_p = p; best_prev = pt; end
            end
            f[i][t] = max_p; bp[i][t] = best_prev
        end
    end
    @printf("%-3s | %-6s | %-10s | %-10s | %-10s | %-10s\n", "i", "Tu", "f[i][N]", "f[i][V]", "Tr.cua N", "Tr.cua V")
    println("-"^65)
    for i in 1:4
        @printf("%-3d | %-6s | %-10.6f | %-10.6f | %-10s | %-10s\n", i, words[i], f[i]["N"], f[i]["V"], bp[i]["N"], bp[i]["V"])
    end
    best_last = f[4]["N"] > f[4]["V"] ? "N" : "V"
    best_p = f[4][best_last]
    seq = [best_last]
    for i in 4:-1:2
        insert!(seq, 1, bp[i][seq[1]])
    end
    @printf("\n[Viterbi] Day nhan: %s (P = %.6f)\n", join(seq, " - "), best_p)
    max_ex = -1.0; best_ex_seq = []
    for i in 0:15
        s = [tags[(i÷8)%2 + 1], tags[(i÷4)%2 + 1], tags[(i÷2)%2 + 1], tags[i%2 + 1]]
        p = pi_prob[s[1]] * B[s[1]][words[1]]
        for j in 2:4
            p *= A[s[j-1]][s[j]] * B[s[j]][words[j]]
        end
        if p > max_ex; max_ex = p; best_ex_seq = s; end
    end
    @printf("[Vet can 16 TH] Day: %s (P = %.6f)\n", join(best_ex_seq, " - "), max_ex)
    println("=> Viterbi da tim dung day nhan toi uu toan cuc!")
end
run_all()