"""Challenge02."""

file = open('challenge02.dat', 'r')
data = file.read()
file.close()

# print type(data)

freqs = {}
for x in data:
    if x in freqs.keys():
        freqs[x] += 1
    else:
        freqs[x] = 1

print type(freqs), freqs
