print(1, 2, 3, sep=' | ')       # separation
for i in range(8):
    print(i, end=" | ")         # out without \n

print(f"{' 3 ':%^10}")          # Format center
print(f"{' 3 ':%<10}")          # Format left
print(f"{' 3 ':%>10}")          # Format right
