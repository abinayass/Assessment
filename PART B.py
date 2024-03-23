Die_A = [1,2,3,4,5,6]
Die_B = [1,2,3,4,5,6]

print("Original Dice A =", Die_A)
print("Original Dice B =", Die_B)

tot_combos = len(Die_A) * len(Die_B)

org_sums = {}
for i in range(len(Die_A)):
    for j in range(len(Die_B)):
        temp = Die_A[i] + Die_B[j]
        val = org_sums.get(temp,0)+1
        org_sums[temp] = val

org_probs = {}
for key,val in org_sums.items():
    org_probs[key] = val/tot_combos

print("\nOriginal Probabilities: ")
for key,val in org_probs.items():
    print("P(Sum = {})   Probability = {}/{} or {}".format(key, org_sums[key],tot_combos, val))
print("\n")

new_dic = org_sums
diceA = []
diceB = []

def diceA_possibilities(num,temp):
    if num > 4:
        return
    if len(temp) > 6:
        return

    if len(temp) == 6:
        if temp not in diceA:
            diceA.append(temp)
        return

    for i in range(num,5):
        diceA_possibilities(i,temp.copy() + [i])

def diceB_possibilities(num,temp):
    if num > 11:
        return

    if len(temp) > 6:
        return

    if len(temp) == 6:
        if temp not in diceB:
            diceB.append(temp)
        return

    for i in range(num+1,13):
        diceB_possibilities(i,temp.copy()+[i])

def undoom_dice(Die_A,Die_B):
    Die_A = Die_B = [0]*6
    for i in range(1,5):
        diceA_possibilities(i,[i])
    for j in range(1,12):
        diceB_possibilities(j,[j])

    print("After Undooming ")
    for i in diceA:
        for j in diceB:
            temp_dict = {}
            for k in range(len(i)):
                for l in range(len(j)):
                    summation = i[k] + j[l]
                    val = temp_dict.get(summation, 0) + 1
                    temp_dict[summation] = val

            match_count = 0
            for key, val in temp_dict.items():
                original_val = org_sums.get(key, -1)
                if val == original_val:
                    match_count += 1
            if match_count == 11:
                return i, j, temp_dict

New_Die_A, New_Die_B, tdic = undoom_dice(Die_A, Die_B)

print("Modified Dice A :", New_Die_A)
print("Modified Dice B :", New_Die_B)

print("\n Modified Probabilities")
for key in sorted(tdic.keys()):
    val = tdic[key]
    print("P(Sum = {}) Probability = {}/{} or {}".format(key, val, tot_combos, val/tot_combos))
