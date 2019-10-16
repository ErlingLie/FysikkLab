import math

vals = [1.561, 1.533, 1.692, 1.543, 1.391, 1.526, 1.746, 1.580, 1.606, 1.654]
oving3 = [0.166, 0.154, 0.184, 0.187, 0.186, 0.179, 0.162, 0.161]

def mean(vals):
    total = 0;
    for i in vals:
        total += i

    total /= len(vals)
    return total




def standardDeviation(vals):
    meanValue = mean(vals)
    total = 0
    for i in vals:
       total += (i-meanValue)**2
    total /= (len(vals) - 1)

    return math.sqrt(total)


def standardError(vals):
    deviation = standardDeviation(vals)
    return deviation/math.sqrt(len(vals))
