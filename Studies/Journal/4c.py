def compare_lists(l1, l2):
    common_l = []
    for i in l1:
        for j in l2:
            if i == j:
                common_l.append(i)

    if len(common_l) == 0:
        print(f"{l1} and {l2} have nothing in common")
    else:
        print(f"{common_l} are the common elements in both lists")


l1 = [25, 687, 523, "light", "cap", "horn"]
l2 = [2524, 687, 5243, "show", "cap", "face"]
l3 = [598, 852, 880, "minimum", "embark", "king"]
l4 = [781, 993, 518, "persist", "understanding", "tough"]

compare_lists(l1, l2)

print("\n==================================================\n")

compare_lists(l3, l4)
