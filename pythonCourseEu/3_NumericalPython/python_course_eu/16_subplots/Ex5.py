import matplotlib.pyplot as plt

rows, cols = 2, 3
fig, ax = plt.subplots(rows, cols,
                       sharex='col',
                       sharey='row')

for row in range(2):
    for col in range(3):
        ax[row, col].text(0.5, 0.5,
                          str((row, col)),
                          color="green",
                          fontsize=18,
                          ha='center')

plt.show()