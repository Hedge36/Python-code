import matplotlib.pyplot as plt
import numpy as np


a = np.array([0.3136, 0.3653, 0.4237,
              0.3654, 0.4396, 0.5251,
              0.4237, 0.5251, 0.6515]).reshape(3, 3)


plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
# 颜色条(shrink表示颜色条与图高度比)
plt.colorbar(shrink=.9)


plt.xticks(())
plt.yticks(())
plt.show()
