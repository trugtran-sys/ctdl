#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <iomanip>
using namespace std;
map<string, map<string, double>> P_bigram = {
    {"em", {{"hoc", 0.52}, {"di", 0.48}}},
    {"hoc", {{"bai", 0.40}, {"toan", 0.35}, {"ve", 0.25}}},
    {"di", {{"cho", 0.58}, {"boi", 0.22}, {"ngu", 0.20}}}
};
struct Beam { string seq; string last_word; double prob; };
bool compareBeam(const Beam& a, const Beam& b) { return a.prob > b.prob; }
void run_language_model() {
    cout << " MO HINH NGON NGU \n";
    vector<Beam> all_sentences;
    for(auto& w2 : P_bigram["em"]) {
        for(auto& w3 : P_bigram[w2.first]) {
            all_sentences.push_back({"em " + w2.first + " " + w3.first, w3.first, 1.0 * w2.second * w3.second});
        }
    }
    sort(all_sentences.begin(), all_sentences.end(), compareBeam);
    cout << "[Vet can] Cau tot nhat: '" << all_sentences[0].seq << "' (P = " << fixed << setprecision(6) << all_sentences[0].prob << ")\n";
    for (int k = 1; k <= 3; ++k) {
        vector<Beam> beam = {{"em", "em", 1.0}};
        for (int step = 0; step < 2; ++step) {
            vector<Beam> next_beam;
            for (auto& b : beam) {
                if (P_bigram.count(b.last_word)) {
                    for (auto& next_w : P_bigram[b.last_word]) {
                        next_beam.push_back({b.seq + " " + next_w.first, next_w.first, b.prob * next_w.second});
                    }
                }
            }
            sort(next_beam.begin(), next_beam.end(), compareBeam);
            beam.clear();
            for(int i = 0; i < min(k, (int)next_beam.size()); ++i) beam.push_back(next_beam[i]);
        }
        if(k==1) cout << "Giai ma tham lam (k=1): '" << beam[0].seq << "' (P = " << beam[0].prob << ")\n";
        cout << "Giai ma theo chum k=" << k << ": '" << beam[0].seq << "' (P = " << beam[0].prob << ")\n";
    }
}
string words[] = {"em", "hoc", "bai", "toan"};
string tags[] = {"N", "V"};
map<string, double> pi = {{"N", 0.6}, {"V", 0.4}};
map<string, map<string, double>> A = {{"N", {{"N", 0.35}, {"V", 0.65}}}, {"V", {{"N", 0.70}, {"V", 0.30}}}};
map<string, map<string, double>> B = {
    {"N", {{"em", 0.35}, {"hoc", 0.10}, {"bai", 0.40}, {"toan", 0.30}}},
    {"V", {{"em", 0.05}, {"hoc", 0.45}, {"bai", 0.05}, {"toan", 0.02}}}
};
void run_viterbi() {
    cout << "\n MO HINH VITERBI \n";
    double f[4][2]; string backptr[4][2];
    f[0][0] = pi["N"] * B["N"][words[0]]; backptr[0][0] = "-";
    f[0][1] = pi["V"] * B["V"][words[0]]; backptr[0][1] = "-";
    for (int i = 1; i < 4; ++i) {
        for (int t = 0; t < 2; ++t) {
            string curr_tag = tags[t];
            double max_p = -1; string best_prev = "";
            for (int pt = 0; pt < 2; ++pt) {
                string prev_tag = tags[pt];
                double p = f[i-1][pt] * A[prev_tag][curr_tag] * B[curr_tag][words[i]];
                if (p > max_p) { max_p = p; best_prev = prev_tag; }
            }
            f[i][t] = max_p; backptr[i][t] = best_prev;
        }
    }
    cout << left << setw(3) << "i" << " | " << setw(6) << "Tu" << " | " << setw(10) << "f[i][N]" << " | " << setw(10) << "f[i][V]" << " | " << setw(10) << "Tr.cua N" << " | " << setw(10) << "Tr.cua V\n";
    cout << string(65, '-') << "\n";
    for (int i = 0; i < 4; ++i) {
        cout << left << setw(3) << i+1 << " | " << setw(6) << words[i] << " | " << fixed << setprecision(6) << setw(10) << f[i][0] << " | " << setw(10) << f[i][1] << " | " << setw(10) << backptr[i][0] << " | " << setw(10) << backptr[i][1] << "\n";
    }
    int last_idx = f[3][0] > f[3][1] ? 0 : 1;
    double best_p = f[3][last_idx];
    vector<string> seq = {tags[last_idx]};
    for (int i = 3; i > 0; --i) {
        string prev = backptr[i][tags[0] == seq[0] ? 0 : 1];
        seq.insert(seq.begin(), prev);
    }
    cout << "\n[Viterbi] Day nhan: ";
    for(size_t i=0; i<seq.size(); ++i) cout << seq[i] << (i==seq.size()-1 ? "" : " - ");
    cout << " (P = " << best_p << ")\n";
    double max_ex = -1; vector<string> best_ex_seq;
    for(int i=0; i<16; ++i) { // 2^4
        vector<string> s = {tags[(i/8)%2], tags[(i/4)%2], tags[(i/2)%2], tags[i%2]};
        double p = pi[s[0]] * B[s[0]][words[0]];
        for(int j=1; j<4; ++j) p *= A[s[j-1]][s[j]] * B[s[j]][words[j]];
        if(p > max_ex) { max_ex = p; best_ex_seq = s; }
    }
    cout << "[Vet can 16 TH] Day: ";
    for(size_t i=0; i<best_ex_seq.size(); ++i) cout << best_ex_seq[i] << (i==best_ex_seq.size()-1 ? "" : " - ");
    cout << " (P = " << max_ex << ")\n";
    cout << "=> Viterbi da tim dung day nhan toi uu toan cuc!\n";
}
int main() {
    run_language_model();
    run_viterbi();
    return 0;
}