# import Output_functions as f
from steering_sys import STEERING_SYSTEM
from numpy import sin,cos,pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# plt.style.use('default')
plt.style.use('bmh')


t_end = 10
dt = 10**-3
n = int(t_end/dt)+1

mySteer = STEERING_SYSTEM(dt)


def ref_dx(t):
    a = 25*pi/180/9.5
    dx = sin(6*t)*sin(t)
    dxd = 6*cos(6*t)*sin(t)+sin(6*t)*cos(t)
    dxdd = 12*cos(6*t)*cos(t) - 37*sin(6*t)*sin(t)
    return np.array([dx,dxd,dxdd])*a
    
def disturbance(t):
    a = 20
    M1 = cos(2*t)+cos(3*t)+sin(5*t)+sin(7*t)
    M2 = cos(10*t)+cos(4*t)+sin(6*t)
    return np.array([M1, M2])*a

hist = np.zeros([n,6])
for i in range(n):
    t = i*dt
    
    M = disturbance(t)
    mySteer.deltaX_to_x(ref_dx(t))
    
    force = mySteer.get_F(M)
    
    hist[i] = np.array([t,mySteer.x,mySteer.y,mySteer.z,mySteer.w,force])





    
fig = plt.figure(num=None, figsize=(10, 8), dpi=100)

plt.subplot("411")
plt.plot(hist[:,0],hist[:,1]*180/np.pi)
plt.plot(hist[:,0],hist[:,3]*180/np.pi)

plt.subplot("412")
plt.plot(hist[:,0],hist[:,2])
plt.plot(hist[:,0],hist[:,4])

plt.subplot("413")

f_by_sm = np.loadtxt(open("force_by_simmech.txt", "rb"), delimiter=",")

plt.plot(f_by_sm[0],f_by_sm[1])
plt.plot(hist[:,0],hist[:,5])

plt.subplot("414")
plt.plot(f_by_sm[0,5:],f_by_sm[1,5:]-hist[5:,5])


plt.show()





x0 = 17.5*np.pi/180
L1 =0.14
L2 =0.4
L3 =0.72692859863604331
d  =0.2
D  =1.6

fig = plt.figure(num=None, figsize=(8, 2), dpi=100)
ax = plt.axes()
ax.axis('scaled')
ax.set(xlim=(-1.8, 0.2), ylim=(-0.2, 0.3))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    i*=49
    x = np.array([0,-L1*cos(hist[i,1]),-L1*cos(hist[i,1])-L2*cos(hist[i,2]),-L1*cos(hist[i,1])-L2*cos(hist[i,2])-L3,L1*cos(hist[i,3])-D,-D])
    y = np.array([0, L1*sin(hist[i,1]),L1*sin(hist[i,1])+L2*sin(hist[i,2]),d,L1*sin(hist[i,3]),0])
    line.set_data(x, y)
    return line,



anim = FuncAnimation(fig, animate, init_func=init,
                                frames=200, interval=20, blit=True)


anim.save('sine_wave.gif', writer='imagemagick')








