import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def rotx(xc, yc, zc, xp, yp, zp, Rx, g):
    g[0] = xp+xc
    g[1] = yp*np.cos(Rx)-zp*np.sin(Rx)+yc
    g[2] = yp*np.sin(Rx)+zp*np.cos(Rx)+zc
    return [g]


def roty(xc, yc, zc, xp, yp, zp, Ry, g):
    g[0] = xp*np.cos(Ry)+zp*np.sin(Ry)+xc
    g[1] = yp+yc
    g[2] = -xp*np.sin(Ry)+zp*np.cos(Ry)+zc
    return [g]


def rotz(xc, yc, zc, xp, yp, zp, Rz, g):
    g[0] = xp*np.cos(Rz)-yp*np.sin(Rz)+xc
    g[1] = xp*np.sin(Rz)+yp*np.cos(Rz)+yc
    g[2] = zp+zc
    return [g]


def update_data(i):
    """Description:
    Draw a Sphere with center(xc, yc, zc) radius rs and rotation(Rx, Ry, Rz).
    with default center(80, 50, 0) rs 40 and Rotation(45, 45, 45).
    Return artist l1, l2.
    """
    global l1, l2
    g = [0]*3
    xc, yc, zc = 80, 50, 0
    rs = 40+0.01*i if 40+0.01*i < 55 else 55 - 0.01*i
    Rx, Ry, Rz = 45+0.01*i, 45-0.005*i, 45+0.01*i
    # Longitude and latitude parameters
    phi1 = np.radians(-90)  # latitude from -90 to 90
    phi2 = np.radians(90)
    dphi = np.radians(10)    # step
    alpha1 = np.radians(0)  # longitude
    alpha2 = np.radians(360)
    dalpha = np.radians(9)  # step
    plt.axis([0, 150, 100, 0])
    plt.axis("off")
    plt.grid(False)
    j = -1
    for alpha in np.arange(alpha1, alpha2, dalpha):
        for phi in np.arange(phi1, phi2, dphi):
            xp = rs*np.cos(phi)*np.cos(alpha)
            yp = rs*np.sin(phi)
            zp = -rs*np.cos(phi)*np.sin(alpha)
            rotx(xc, yc, zc, xp, yp, zp, Rx, g)
            xp = g[0]-xc
            yp = g[1]-yc
            zp = g[2]-zc
            roty(xc, yc, zc, xp, yp, zp, Ry, g)
            xp = g[0]-xc
            yp = g[1]-yc
            zp = g[2]-zc
            rotz(xc, yc, zc, xp, yp, zp, Rz, g)
            xpg = g[0]
            ypg = g[1]
            zpg = g[2]
            nz = zpg-zc
            if phi == phi1:
                xpglast = xpg
                ypglast = ypg
            if nz < 0:
                j += 1
                if i == -1:
                    t, = plt.plot([xpglast, xpg], [ypglast, ypg], lw=1, c="w")
                    l1.append(t)
                else:
                    l1[j].set_data([xpglast, xpg], [ypglast, ypg])
            ypglast = ypg
            xpglast = xpg
    j = -1
    for phi in np.arange(phi1, phi2, dphi):
        r = rs*np.cos(phi)
        for alpha in np.arange(alpha1, alpha2+dalpha, dalpha):
            xp = r*np.cos(alpha)
            yp = rs*np.sin(phi)
            zp = -rs*np.cos(phi)*np.sin(alpha)
            rotx(xc, yc, zc, xp, yp, zp, Rx, g)
            xp = g[0]-xc
            yp = g[1]-yc
            zp = g[2]-zc
            roty(xc, yc, zc, xp, yp, zp, Ry, g)
            xp = g[0]-xc
            yp = g[1]-yc
            zp = g[2]-zc
            rotz(xc, yc, zc, xp, yp, zp, Rz, g)
            xpg = g[0]
            ypg = g[1]
            zpg = g[2]
            nz = zpg-zc
            if alpha == alpha1:
                xpglast = xpg
                ypglast = ypg
            if nz < 0:
                j += 1
                if i == -1:
                    t, = plt.plot([xpglast, xpg], [ypglast, ypg], lw=1, c="w")
                    l2.append(t)
                else:
                    try:
                        l2[j].set_data([xpglast, xpg], [ypglast, ypg])
                    except:
                        t, = plt.plot([xpglast, xpg], [
                                      ypglast, ypg], lw=1, c="w")
                        l2.append(t)
            ypglast = ypg
            xpglast = xpg
    return l1+l2
# 问题：l1, l2都是一堆线，如何同步更新所有的线的数据


fig = plt.figure()
fig.patch.set_facecolor("black")
l1, l2 = [], []
update_data(-1)

ani = FuncAnimation(fig, update_data, interval=1, blit=True)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)
plt.show()
