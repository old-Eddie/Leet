
def maximumEnergy(energy, k) -> int:
    last_k = energy[-k:][::-1]
    for idx in range(len(energy) - k - 1, -1, -1):
        last_k.append(last_k[-k] + energy[idx])
    return max(last_k)
