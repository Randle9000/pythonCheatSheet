

import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
fig, (ax1, ax2)  = plt.subplots(1, 2,
                                sharey='row')
ax1.text(0.5, 0.5,
              "left",
              color="green",
              fontsize=18,
              ha='center')

ax2.text(0.5, 0.5,
              "right",
              color="green",
              fontsize=18,
              ha='center')

plt.show()

