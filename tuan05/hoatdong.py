import random
def get_overlaps(activities):
    overlaps = {act[0]: 0 for act in activities}
    for i in range(len(activities)):
        for j in range(i + 1, len(activities)):
            if not (activities[i][2] <= activities[j][1] or activities[j][2] <= activities[i][1]):
                overlaps[activities[i][0]] += 1
                overlaps[activities[j][0]] += 1
    return overlaps
def is_compatible(selected, new_act):
    for act in selected:
        if not (new_act[2] <= act[1] or act[2] <= new_act[1]):
            return False
    return True
def greedy_criteria(activities):
    acts_finish = sorted(activities, key=lambda x: (x[2], x[1]))
    res_finish = []
    last_finish = -1
    for act in acts_finish:
        if act[1] >= last_finish:
            res_finish.append(act)
            last_finish = act[2]
    acts_start = sorted(activities, key=lambda x: (x[1], x[2]))
    res_start = []
    last_finish_s = -1
    for act in acts_start:
        if act[1] >= last_finish_s:
            res_start.append(act)
            last_finish_s = act[2]
    acts_short = sorted(activities, key=lambda x: (x[2] - x[1], x[1]))
    res_short = []
    for act in acts_short:
        if is_compatible(res_short, act):
            res_short.append(act)
    overlaps = get_overlaps(activities)
    acts_overlap = sorted(activities, key=lambda x: (overlaps[x[0]], x[1]))
    res_overlap = []
    for act in acts_overlap:
        if is_compatible(res_overlap, act):
            res_overlap.append(act)  
    return res_finish, res_start, res_short, res_overlap
def dynamic_programming_max(activities):
    acts = sorted(activities, key=lambda x: x[2])
    n = len(acts)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if acts[j][2] <= acts[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) if n > 0 else 0
def run_tests():
    std_data = [
        ("H1", 1, 5), ("H2", 2, 5), ("H3", 2, 6), ("H4", 3, 4), ("H5", 4, 8),
        ("H6", 6, 9), ("H7", 8, 11), ("H8", 9, 14), ("H9", 11, 13), ("H10", 12, 15)
    ]
    rf, rs, rsh, ro = greedy_criteria(std_data)
    true_max = dynamic_programming_max(std_data)
    print(f"1. Kết thúc sớm nhất : {[a[0] for a in rf]} (Số HĐ: {len(rf)})")
    print(f"2. Bắt đầu sớm nhất  : {[a[0] for a in rs]} (Số HĐ: {len(rs)})")
    print(f"3. Ngắn nhất         : {[a[0] for a in rsh]} (Số HĐ: {len(rsh)})")
    print(f"4. Ít chồng lấn nhất : {[a[0] for a in ro]} (Số HĐ: {len(ro)})")
    print(f"=> Số nhiều nhất thật sự (DP): {true_max}")
    rand_data = []
    for i in range(1, 8):
        s = random.randint(1, 10)
        f = s + random.randint(1, 5)
        rand_data.append((f"R{i}", s, f))
    print("Dữ liệu test ngẫu nhiên:", [(a[0], a[1], a[2]) for a in rand_data])
    rf_rand, _, _, _ = greedy_criteria(rand_data)
    dp_max_rand = dynamic_programming_max(rand_data)
    print(f"Tham lam kết thúc sớm nhất: {len(rf_rand)}")
    print(f"Quy hoạch động (Tối ưu): {dp_max_rand}")
    if len(rf_rand) == dp_max_rand:
        print('=> Thuật toán tham lam "Kết thúc sớm nhất" cho kết quả tối ưu chính xác!')
if __name__ == "__main__":
    run_tests()