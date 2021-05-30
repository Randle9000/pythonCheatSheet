
import matplotlib.pyplot as plt
python_course_green = "#476042"
python_course_orange = "#f17c0b"
python_course_green_light = "#6a9662"
# plt.figure(figsize=(6, 4))
fig, ax = plt.subplots(2, 2,
                       figsize=(6, 4),
                       facecolor=python_course_green_light)


ax[0, 0].text(0.5, # x-Koordinate, 0 ganz links, 1 ganz rechts
              0.5, # y-Koordinate, 0 ganz oben, 1 ganz unten
              'ax[0, 0]', # der Text der ausgegeben wird
              horizontalalignment='center', # abgekürzt 'ha'
              verticalalignment='center', # abgekürzt 'va'
              fontsize=20,
              alpha=.5 )

ax[0, 0].set_facecolor('xkcd:salmon')

ax[1 ,1].text(0.5, 0.5,
             'ax[1, 1]',
             ha='center', va='center',
             fontsize=20,
             color="y")
ax[1, 0].set_facecolor((0.8, 0.6, 0.5))
ax[0, 1].set_facecolor((1, 1, 0.5))
ax[1, 1].set_facecolor(python_course_green)
plt.show()

