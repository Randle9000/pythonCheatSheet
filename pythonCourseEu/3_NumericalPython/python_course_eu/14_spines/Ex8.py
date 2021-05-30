from datetime import datetime, timedelta as delta
import numpy as np
import matplotlib.pyplot as plt
import random

from pandas import DatetimeIndex




x = DatetimeIndex(['2020-05-11', '2020-05-12', '2020-05-13', '2020-05-14',
               '2020-05-15', '2020-05-18', '2020-05-19', '2020-05-20',
               '2020-05-21', '2020-05-22', '2020-05-26', '2020-05-27',
               '2020-05-28', '2020-05-29', '2020-06-01', '2020-06-02',
               '2020-06-03', '2020-06-04', '2020-06-05', '2020-06-08',
               '2020-06-09', '2020-06-10', '2020-06-11', '2020-06-12',
               '2020-06-15', '2020-06-16', '2020-06-17', '2020-06-18',
               '2020-06-19', '2020-06-22', '2020-06-23', '2020-06-24',
               '2020-06-25', '2020-06-26', '2020-06-29', '2020-06-30',
               '2020-07-01', '2020-07-02', '2020-07-06', '2020-07-07',
               '2020-07-08', '2020-07-09', '2020-07-10', '2020-07-13',
               '2020-07-14', '2020-07-15', '2020-07-16', '2020-07-17',
               '2020-07-20', '2020-07-21', '2020-07-22', '2020-07-23',
               '2020-07-24', '2020-07-27', '2020-07-28', '2020-07-29',
               '2020-07-30', '2020-07-31', '2020-08-03', '2020-08-04',
               '2020-08-05', '2020-08-06', '2020-08-07', '2020-08-10'],
              dtype='datetime64[ns]', name='Date', freq=None)

y = np.array([15803200, 21441900, 22508200, 12681800,  8232900,  8031600,
       13729700,  9777900,  5531800,  3318600,  4639100, 10083700,
        4995800,  7684500, 11557800,  6732900,  4649000,  7779600,
        4612000, 20318900, 13834100,  8852300,  9487200,  5693700,
        6470500,  4797600, 16130000,  6264300,  7732100,  5035000,
        7571100,  5063400, 13608800,  4284400, 10411300,  4915800,
       14713400,  4938800,  4625900,  4844600,  3049100,  4505200,
        5998300,  6980900,  3448100,  6835800,  5508600,  2693400,
        2487300,  5016000,  2716700,  3561600,  2700900,  2912200,
        2062400,  2110900,  2667600,  2964300,  5635000, 10277600,
       10613700,  3954000,  3473800,  3492174], dtype=np.int64)

rows = 2
fig, ax = plt.subplots(rows)
ax[0] = plt.plot(x, y)
ax[1] = plt.bar(x, y)
plt.show()