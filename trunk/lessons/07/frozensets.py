codes=(12,13,45,67,81,90,92,12,45,81)  # alcuni elementi sono duplicati
print(codes)
unique_codes=frozenset(codes)   # i duplicati vengono rimossi
print(unique_codes)
duplicates=len(codes)-len(unique_codes)
print('I valori duplicati sono %d.' % duplicates)

