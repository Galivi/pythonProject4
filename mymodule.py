# import matplotlib.pyplot as plt
#
# months=['Jan', 'Feb', 'Mar', 'Apr', 'may', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# temp_fl=[15, 16, 18, 21, 24, 27, 28, 26, 23, 19, 16, 11]
# temp_ny=[2, 2, 4, 11, 16, 22, 25, 26, 24, 14, 12, 3]
#
# plt.plot (months, temp_fl, marker="*", color='red', linestyle='-', label='FL')
# plt.plot (months, temp_ny, marker="^", color='green', linestyle='-', label='NY')
# plt.xlabel('Month')
# plt.ylabel('Celcius Temperature')
# plt.title('Monthly Temperature in temp_fl')
# plt.show()





import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0, 4*np.pi,2000)
y= np.sin (x)


plt.plot(x, y, color='red', label='sine')
plt.ylim(-2, 2)
plt.xlabel ('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid(True)

plt.show()






