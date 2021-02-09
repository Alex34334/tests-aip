words = ["Alaska", "auto", "arc", "agenda", "arugula", "Caveman"]
q = []
u = set()
p = []
for i in range(len(words)):
    words[i].lower()
    words[i] = words[i].lower()
    y = int(words[i].count("a"))
    if y >= 2:
        q.append(y*y)
    if len(words[i]) >3:
        u.add(len(words[i]))
print(q, u)
