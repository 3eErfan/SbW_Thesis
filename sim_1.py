"""
Created on Sun Apr 25 17:02:07 2021

@author: Erfan
"""
from steering_sys import STEERING_SYSTEM
from controller import CONTROLLER,SMO
import numpy as np
from numpy import sign, sin,cos
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
# =============================================================================
#                               Define Values
# =============================================================================

duration = 5
dt = 10**-3
h = 0.01
n = int(h/dt)
N = int(duration/dt)

mySteer = STEERING_SYSTEM(dt)
myController = CONTROLLER(dt)
myObs = SMO(dt)

def fault(x):
    return 1
    x *= 1000
    x = x%20

    return min(1,abs(x-10)+0.5)

def disturbance(t):
    a = 100
    M1 = cos(t**2)+cos(3*t)+sin(5*t)+sin(7*t)
    M2 = cos(10*t)+cos(4*t)+sin(6*t)
    return np.array([M1,M2])*a

def ref(t):
    f = np.pi*t/5
    a = 20*np.pi/180.0 /9.5
    x1 = a*np.sin(f*t)
    x2 = 2*a*f*np.cos(f*t)

    return np.array([[x1],[x2]])

np.random.seed(0)

History = np.zeros([N,13])
Time = np.zeros(N)
# =============================================================================
#                           Sim Loop
# =============================================================================
u=0
d_hat = 0
x = mySteer.get_delta_r()[:2]
for i in range(N):

    t = i*dt
    M = disturbance(t)
    mySteer.step_xdd(M,u*fault(x[0])) 
    x = mySteer.get_delta_r()[:2]
    tmp = myObs.step_obs(x,u)
    d_hat = d_hat*0.5 + 0.5*tmp
    
    err = ref(t) - x
    u = -myController.step_controller(err,0)
    u -= d_hat

    d_eq = (mySteer.xd*M[0] + mySteer.zd*M[1])/(x[1]+0.00000000000001*sign(x[1]))

    delays = myController.get_delays()
    History[i] = [x[0],ref(t)[0],x[1],ref(t)[1],u,delays[0],d_eq,0,0,delays[1],delays[2],delays[3],d_hat]
    Time[i] = t





fig = plt.figure(num=None, figsize=(10, 8), dpi=100)



host = host_subplot(411, axes_class=AA.Axes)
# plt.subplots_adjust(right=1)


par2 = host.twinx()

offset = 0
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))
par2.axis["right"].toggle(all=True)
par2.set_ylabel("Error")

p1, =host.plot(Time , 9.5*History[:,1]*180/np.pi,label='Ref')
host.plot(Time , 9.5*History[:,0]*180/np.pi,label='$x_1$')
host.legend()


p2, =par2.plot(Time, 9.5*(History[:,1]-History[:,0])*180/np.pi,label='Error' )
par2.set_ylim(-3, 3)


host.axis["left"].label.set_color(p1.get_color())
par2.axis["right"].label.set_color(p2.get_color())


# plt.ylim(-10,10)

plt.subplot(4,1,2)
plt.plot(Time , History[:,3],label='Ref')
plt.plot(Time , History[:,2],label='$x_2$')
plt.legend()

plt.subplot(4,1,3)
plt.plot(Time , History[:,4])

plt.subplot(4,1,4)
plt.plot(Time , History[:,6],label='d(t)')
plt.plot(Time , History[:,12],label="$\^d$")
plt.legend()

plt.draw()
plt.show()


fig = plt.figure(num=None, figsize=(10, 5), dpi=100)

plt.subplot(3,1,1)
plt.plot(Time , History[:,10],label='sensor packet loss')
plt.legend()
# plt.ylim(-10,10)

plt.subplot(3,1,2)
plt.plot(Time , History[:,11],label='actuator packet loss')
plt.legend()

plt.subplot(3,1,3)
plt.plot(Time , h*History[:,9]/n,label=r"$\tau_{ca}$")
plt.plot(Time , h*History[:,5]/n,label=r"$\tau_{sc}$",alpha=0.8)
plt.legend()

plt.show()














