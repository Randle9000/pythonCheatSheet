import matplotlib.pyplot as plt
import random

def splitter(additional_information=''):
    print('\n\n####### {0} #########\n'.format(additional_information))

""""The following format string characters are accepted to control the line style or marker:

=============================================
character       description
=============================================
'-'             solid line style
'--'            dashed line style
'-.'            dash-dot line style
':'             dotted line style
'.'             point marker
','             pixel marker
'o'             circle marker
'v'             triangle_down marker
'^'             triangle_up marker
'<'             triangle_left marker
'>'             triangle_right marker
'1'             tri_down marker
'2'             tri_up marker
'3'             tri_left marker
'4'             tri_right marker
's'             square marker
'p'             pentagon marker
'*'             star marker
'h'             hexagon1 marker
'H'             hexagon2 marker
'+'             plus marker
'x'             x marker
'D'             diamond marker
'd'             thin_diamond marker
'|'             vline marker
'_'             hline marker
===============================================


The following color abbreviations are supported:

==================
character   color
==================
'b'         blue
'g'         green
'r'         red
'c'         cyan
'm'         magenta
'y'         yellow
'k'         black
'w'         white
=================="""

# simple plot
splitter('simple plot')
values = [random.randint(-4, 5) for x in range(0, 6)]
plt.plot(values)
#plt.show()

plt.plot(values, 'ob')
#plt.show()


## hierarchy and important terms
splitter('hierarchy and important terms')
plt.close()

x = [i for i in range(0, 5)]
y = [random.randint(-22, 0) for i in range(0, 5)]
fig, ax = plt.subplots()
ax.plot(x, y)


##lables on axes
splitter('lables on axes')
ax.set(xlabel='Day',
       ylabel='temperature',
       title='temperature per day')
plt.show()




