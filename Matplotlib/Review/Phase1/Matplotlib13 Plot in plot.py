import matplotlib.pyplot as plt


fig = plt.figure()
x = [x for x in range(1, 8)]
y = [1, 3, 4, 2, 5, 8, 6]

left, bottom, width, height = .1, .1, .8, .8  # 表格位置
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("title1")

left, bottom, width, height = .2, .6, .25, .25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x, y, 'b')
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("title inside")


plt.axes([.6, .2, .25, .25])
plt.plot(y[::-1], x, 'g')
plt.xlabel("x")
plt.ylabel("y")
plt.title("title inside2")


plt.show()
