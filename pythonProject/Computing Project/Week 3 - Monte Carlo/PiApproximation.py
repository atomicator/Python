# Monte Carlo method to calculate pi
import math
import random
import matplotlib . pyplot as plt

N = 10000
print ( " Parameter : N = " , str ( N ) )
# Array of iterations.
iterations = []
# Array of results.
results = []

count_in = 0
for i in range(N):
    # random.random returns a random double in range 0-1.
    x = random.random()
    y = random.random()
# Condition checks if the random point falls in the inscribed circle.
    cond = x **2 + y **2
    outcome = 1 if cond <= 1 else 0
    count_in += outcome
# Percentage of how many times it did fall into the circle.
# Analitically, this equals Ac/As = pi/4.
    fraction_in = count_in /( i +1)

# Store the results into the array.
    results . append (4.0 * fraction_in )
# Store iteration into the array.
    iterations . append ( i +1)

# Print the results - the last printed number should converge to pi.
    print("Location :" + str(outcome) + "\t" + str(x)
          + "\t" + str(y) + "\t" + str(count_in) + "\t"
          + str(i) + "\t" + str(4.0 * fraction_in))

# Plot the results using pyplot
fig = plt.figure ()
plt.plot(iterations, results, "k", label="numerical pi")
plt.plot([0, iterations[-1]], [math.pi, math.pi],
        "r-" , label="pi")

plt.grid(True)
plt.legend()
plt.ylabel(" Result [ -] ")
plt.xlabel(" Iteration [ -] ")
# plt.savefig("piConvergence.pdf")
plt.show()
