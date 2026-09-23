#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <ctime>
using namespace std;
struct Activity {
    string name;
    int s, f;
};
bool is_compatible(const vector<Activity>& selected, const Activity& new_act) {
    for (const auto& act : selected) {
        if (!(new_act.f <= act.s || act.f <= new_act.s)) {
            return false;
        }
    }
    return true;
}
map<string, int> get_overlaps(const vector<Activity>& acts) {
    map<string, int> overlaps;
    for (const auto& act : acts) overlaps[act.name] = 0;
    for (size_t i = 0; i < acts.size(); ++i) {
        for (size_t j = i + 1; j < acts.size(); ++j) {
            if (!(acts[i].f <= acts[j].s || acts[j].f <= acts[i].s)) {
                overlaps[acts[i].name]++;
                overlaps[acts[j].name]++;
            }
        }
    }
    return overlaps;
}
int dynamic_programming_max(vector<Activity> acts) {
    sort(acts.begin(), acts.end(), [](const Activity& a, const Activity& b) {
        return a.f < b.f;
    });
    int n = acts.size();
    if (n == 0) return 0;
    vector<int> dp(n, 1);
    int max_acts = 1;
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (acts[j].f <= acts[i].s) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        max_acts = max(max_acts, dp[i]);
    }
    return max_acts;
}
void print_result(const string& criteria, const vector<Activity>& res) {
    cout << criteria << ": [";
    for(size_t i = 0; i < res.size(); ++i) {
        cout << res[i].name << (i + 1 == res.size() ? "" : ", ");
    }
    cout << "] (So HD: " << res.size() << ")\n";
}
int main() {
    srand(time(NULL));
    vector<Activity> std_data = {
        {"H1", 1, 5}, {"H2", 2, 5}, {"H3", 2, 6}, {"H4", 3, 4}, {"H5", 4, 8},
        {"H6", 6, 9}, {"H7", 8, 11}, {"H8", 9, 14}, {"H9", 11, 13}, {"H10", 12, 15}
    };
    vector<Activity> finish = std_data;
    sort(finish.begin(), finish.end(), [](const Activity& a, const Activity& b) {
        return a.f == b.f ? a.s < b.s : a.f < b.f;
    });
    vector<Activity> res_finish;
    int last_f = -1;
    for (const auto& act : finish) {
        if (act.s >= last_f) {
            res_finish.push_back(act);
            last_f = act.f;
        }
    }
    vector<Activity> start = std_data;
    sort(start.begin(), start.end(), [](const Activity& a, const Activity& b) {
        return a.s == b.s ? a.f < b.f : a.s < b.s;
    });
    vector<Activity> res_start;
    last_f = -1;
    for (const auto& act : start) {
        if (act.s >= last_f) {
            res_start.push_back(act);
            last_f = act.f;
        }
    }
    vector<Activity> short_acts = std_data;
    sort(short_acts.begin(), short_acts.end(), [](const Activity& a, const Activity& b) {
        int lenA = a.f - a.s; int lenB = b.f - b.s;
        return lenA == lenB ? a.s < b.s : lenA < lenB;
    });
    vector<Activity> res_short;
    for (const auto& act : short_acts) {
        if (is_compatible(res_short, act)) res_short.push_back(act);
    }
    map<string, int> overlaps = get_overlaps(std_data);
    vector<Activity> overlap_acts = std_data;
    sort(overlap_acts.begin(), overlap_acts.end(), [&overlaps](const Activity& a, const Activity& b) {
        return overlaps[a.name] == overlaps[b.name] ? a.s < b.s : overlaps[a.name] < overlaps[b.name];
    });
    vector<Activity> res_overlap;
    for (const auto& act : overlap_acts) {
        if (is_compatible(res_overlap, act)) res_overlap.push_back(act);
    }
    print_result("1. Ket thuc som nhat", res_finish);
    print_result("2. Bat dau som nhat ", res_start);
    print_result("3. Ngan nhat        ", res_short);
    print_result("4. It chong lan nhat", res_overlap);
    cout << "=> So nhieu nhat that su (DP): " << dynamic_programming_max(std_data) << "\n\n";
    vector<Activity> rand_data;
    for (int i = 1; i <= 7; ++i) {
        int s = rand() % 10 + 1;
        int f = s + rand() % 5 + 1;
        rand_data.push_back({"R" + to_string(i), s, f});
    }
    int dp_rand = dynamic_programming_max(rand_data);
    cout << "Da sinh test ngau nhien 7 hoat dong.\n";
    cout << "Quy hoach dong (Toi uu): " << dp_rand << "\n";
    return 0;
}