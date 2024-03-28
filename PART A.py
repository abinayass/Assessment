#How many total combinations are possible? Show the math along with the code!
num = 6
tot_combos = num_sides * num
print("Total combinations:", tot_combos)

#Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together. Show the math along with the code!
import numpy as np

distr = np.empty((6, 6), dtype=object)
for i in range(1, 7):
    for j in range(1, 7):
        distr[i-1][j-1] = (i, j)

print("Distribution of all possible combinations:")
for row in distr:
    print(row)

#Calculate the Probability of all Possible Sums occurring among the num of combinations from (2).
import numpy as np

distr_sum = np.empty((6, 6), dtype=int)
for i in range(1, 7):
    for j in range(1, 7):
        distr_sum[i-1][j-1] = i + j

print("Probability of all possible sums:")
for i in range(2, 13):
    count = 0
    for row in distr_sum:
        for value in row:
            if i == value:
                count += 1
    probability = count / tot_combos
    print("P(Sum = {}) = {} / {} or {:.4f}".format(i, count, tot_combos, probability))
