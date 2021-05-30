print("ART %5d, Price +%8.2f" % (999.55, 59.00222))
print("%10.3e"% (356.08977))
print("%10.3E"% (356.08977))
print("%10o"% (25))
print("%10.3o"% (25))
print("%10.5o"% (25))
print("%5x"% (47))
print("%5.4x"% (47))
print("%5.4X"% (47))
print("%#5X"% (47))
print("%5X"% (47))
print("%#5.4X"% (47))
print("%#5o"% (25))
print("%+d"% (42))
print("% d"% (42))
print("%+2d"% (42))
print("% 2d"% (42))
print("%2d"% (42))

dict_basic_info  = {1:{'open': 133.97, 'close': 136.9355, 'percent_change': 2.161688453954581, 'vol': 21441900},
                    2: {'open': 133.97, 'close': 136.9355, 'percent_change': -3.161688453954581, 'vol': 1221441900}}

for d in range(1, 3):


    print("{0}day : {1:7.2f} : {2:7.2f} : {4:5.2f} :{3:10}\n".format(d, dict_basic_info[d]["open"],
                                                          dict_basic_info[d]["close"],
                                                          dict_basic_info[d]["vol"],
                                                          dict_basic_info[d]["percent_change"]))