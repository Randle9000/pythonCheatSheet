import matplotlib.pyplot as plt
fig, ax = plt.subplots()

xticks = ax.get_xticks()
xticklabels = ax.get_xticklabels()
print(xticks, xticklabels)
for i in range(6):
    print(xticklabels[i])

yticks = ax.get_yticks()
print(yticks)
# plt.show()

ax.set_xticks([7, 13, 19, 33, 42])
plt.show()
