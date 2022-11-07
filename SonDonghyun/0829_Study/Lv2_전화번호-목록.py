### solution

solution = lambda l: False if {w[:(j + 1)] for w in l for j in range(len(w) - 1)} & set(l) else True


###