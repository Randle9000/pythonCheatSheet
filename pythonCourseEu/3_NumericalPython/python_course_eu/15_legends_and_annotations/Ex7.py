from polynomials.polynomials import Polynomial

import numpy as np
import matplotlib.pyplot as plt

p = Polynomial(1, 0, -12, 0)
p_der = p.derivative()

fig, ax = plt.subplots()
X = np.arange(-5, 5, 0.1)
F = p(X)

F_derivative = p_der(X)
ax.grid()

ax.annotate("local maximum",
            xy=(-2, p(-2)),
            xytext=(-1, p(-2)+35),
            arrowprops=dict(facecolor='orange'))
ax.annotate("local minimum",
            xy=(2, p(2)),
            xytext=(-2, p(2)-40),
            arrowprops=dict(facecolor='orange', shrink=0.05))
ax.annotate("inflection point",
            xy=(0, p(0)),
            xytext=(-3, -30),
            arrowprops=dict(facecolor='orange', shrink=0.05))


ax.plot(X, F, label="p")
ax.plot(X, F_derivative, label="derivation of p")

ax.legend(loc='best')
plt.show()

"""


We have to provide some informations to the parameters of annotate, we have used in our previous example.
Parameter 	Meaning
xy 	coordinates of the arrow tip
xytext 	coordinates of the text location

The xy and the xytext locations of our example are in data coordinates. There are other coordinate systems available we can choose. The coordinate system of xy and xytext can be specified string values assigned to xycoords and textcoords. The default value is 'data':
String Value 	Coordinate System
figure points 	points from the lower left corner of the figure
figure pixels 	pixels from the lower left corner of the figure
figure fraction 	0,0 is lower left of figure and 1,1 is upper right
axes points 	points from lower left corner of axes
axes pixels 	pixels from lower left corner of axes
axes fraction 	0,0 is lower left of axes and 1,1 is upper right
data 	use the axes data coordinate system

Additionally, we can also specify the properties of the arrow. To do so, we have to provide a dictionary of arrow properties to the parameter arrowprops:
arrowprops key 	description
width 	the width of the arrow in points
headlength 	The length of the arrow head in points
headwidth 	the width of the base of the arrow head in points
shrink 	move the tip and base some percent away from the annotated point and text
**kwargs 	any key for matplotlib.patches.Polygon, e.g., facecolor
"""