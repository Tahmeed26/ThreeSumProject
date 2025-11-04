# ---------------------------------------------------
# Version 1: Brute Force (No Checks for Duplicate Indices)
# ---------------------------------------------------
def sum_of_three_v1(nums, target):
    list_of_list = []
    num_itr = 0  # Counts total number of iterations

    for i, n in enumerate(nums):
        for j, o in enumerate(nums):
            for k, p in enumerate(nums):
                num_itr += 1
                if target == n + o + p:
                    list_of_list.append([i, j, k])

    return list_of_list, num_itr


# ---------------------------------------------------
# Version 2: Brute Force (Avoid Using Same Index Twice)
# ---------------------------------------------------
def sum_of_three_v2(nums, target):
    list_of_list = []
    num_itr = 0

    for i, n in enumerate(nums):
        for j, o in enumerate(nums):
            if i == j:
                continue
            for k, p in enumerate(nums):
                num_itr += 1
                if j == k or i == k:
                    continue
                if target == n + o + p:
                    list_of_list.append([i, j, k])

    return list_of_list, num_itr


# ---------------------------------------------------
# Version 3: Using a Hash Map for Pair Sums
# ---------------------------------------------------
def sum_of_three_v3(nums, target):
    list_of_list = []
    add_map = {}
    num_itr = 0

    # Step 1: Precompute all possible pair sums
    for i, n in enumerate(nums):
        for j, o in enumerate(nums):
            num_itr += 1
            add_res = n + o
            add_map[add_res] = [i, j]

    # Step 2: Check if remaining element completes the target
    for k, p in enumerate(nums):
        num_itr += 1
        diff = target - p
        if add_map.get(diff) is not None:
            index_list = add_map.get(diff)
            index_list.append(k)
            list_of_list.append(index_list)

    return list_of_list, num_itr


# ---------------------------------------------------
# Version 4: Optimized Hash Map Approach
# ---------------------------------------------------
def sum_of_three_v4(nums, target):
    list_of_list = []
    add_map = {}
    num_itr = 0

    for i, n in enumerate(nums):
        diff2 = target - n
        # Check if complement exists in the map
        if add_map.get(diff2) is not None:
            index_list = add_map.get(diff2)
            index_list.append(n)
            list_of_list.append(index_list)
        else:
            # Build hash map of pair sums
            for j, o in enumerate(nums):
                num_itr += 1
                key = o + n
                add_map[key] = [i, j]

    return list_of_list, num_itr


# ---------------------------------------------------
# Test and Compare All Approaches
# ---------------------------------------------------
if __name__ == "__main__":
    nums_list = [1, 2, 3, 4, 5]
    target_value = 10

    print("\n==============================")
    print("🔹 Version 1: Basic Brute Force")
    print("==============================")
    result, iters = sum_of_three_v1(nums_list, target_value)
    print("Results:", result)
    print("Total Iterations:", iters, "\n")

    print("==============================")
    print("🔹 Version 2: Improved Brute Force")
    print("==============================")
    result, iters = sum_of_three_v2(nums_list, target_value)
    print("Results:", result)
    print("Total Iterations:", iters, "\n")

    print("==============================")
    print("🔹 Version 3: Hash Map for Pair Sums")
    print("==============================")
    result, iters = sum_of_three_v3(nums_list, target_value)
    print("Results:", result)
    print("Total Iterations:", iters, "\n")

    print("==============================")
    print("🔹 Version 4: Optimized Hash Map")
    print("==============================")
    result, iters = sum_of_three_v4(nums_list, target_value)
    print("Results:", result)
    print("Total Iterations:", iters, "\n")

    print("✅ Comparison Complete")
