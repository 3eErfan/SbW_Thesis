"""
Created on Mon Jun 21 19:33:45 2021

@author: Erfan
"""
import numpy as np
from numpy import matmul as mm

_A = np.array([[0,1],[-0.01057,-0.01195]])
_B = np.array([[0],[0.0101]])
_C = np.array([1,0])

_F = np.array([[1,0.01],[-0.000105698808443481,0.999880027678993]])
_G = np.array([[5.58035749778086e-07],[0.000100637829661796]])
_h = 0.01

# _F = np.array([[1,0.03],[-0.000317058104761794,	0.999636955695172]])
# _G = np.array([[4.69293855847824e-06],[0.000301876985861239]])
# _h = 0.03

# _F = np.array([[1,0.05],[-0.000528365572538411,0.999389715610535]])
# _G = np.array([[1.28521321883567e-05],[0.000503066771949311]])
# _h = 0.05

# _Q = np.diag([1000,1000])
_Cs = np.array([-10, -1])
_si = 10

class CONTROLLER:
    
    
    Hist = []
    
    dt = []
    F = []
    G = []
    C = []
    h = []
    
    Q = []
    Cs = []
    si = []

    
    delay=0
    delay2=0
    sensor_packet_lost = 0
    actuator_packet_lost = 0
    
    P_sensor_packet_lost = 0.1
    P_actuator_packet_lost = 0.1
    sample_instant = 0
    actuation_instant = 0
    
    alpha_bar = P_sensor_packet_lost

    d_hat_sens = 0
    xk =  np.array([[0.0],[0.0]])
    xk_1 =  np.array([[0.0],[0.0]])
    
    u = 0
    uk = 0
    
    dk_1 = 0
    dk_2 = 0
    
    rand = []
    randi = []

    def __init__(self,dt,N,F=_F,G=_G,C=_C,h=_h,Cs=_Cs,si=_si):
        
        np.random.seed(0)
        
        self.dt = dt
        self.F = F
        self.G = G
        self.C = C
        self.h = h
        
        # self.Q = Q
        self.Cs = Cs
        self.si = si
        
        self.tau_sc = 1/2
        self.zeta = self.tau_sc/(self.tau_sc+1)
        # self.gamma = self.zeta # I have one sensor so one sampling rate
        
        
        self.n = np.int(self.h//self.dt)
        self.i = 0
        
        N = int(N)
        self.rand = np.random.rand(2,N)
        self.randi = np.random.randint(0,int(self.n//2),(2,N))
        
        return
    
    def get_delays(self):
        return np.array([self.delay,self.delay2,self.sensor_packet_lost,self.actuator_packet_lost])
    
    
    def q(self,Sk):
        return self.si/(self.si+np.linalg.norm(Sk))
    
    
    def CONTROLLER(self,xk,xk_1):
        Sk = mm(self.Cs,xk)-self.zeta*mm(self.Cs,xk_1)
        

        H = (1-self.alpha_bar)*mm(self.Cs,self.F)
        I = self.zeta*(1-self.alpha_bar)*self.zeta*self.Cs
        J = 1 - self.q(Sk)
        K = self.alpha_bar*self.Cs
        L = self.zeta*self.alpha_bar*self.Cs
        

        uk = -(mm(H,xk) -mm(I,xk) +mm(K,xk) -mm(L,xk_1) -J ) / (mm(self.Cs,self.G)*(1-self.alpha_bar)) 
        
        return uk
    
    
    def step_controller(self,err,d_hat):
        
              
        if self.i==self.sample_instant:
        # sensor:
            self.sensor_packet_lost = 0
            if self.rand[0,self.i] > self.P_sensor_packet_lost:
                self.xk_1 = self.xk
                self.xk = err
                
                self.d_hat_sens = d_hat
            else:
                self.sensor_packet_lost = 1
            
            self.sample_instant -= self.delay
            self.delay = self.randi[0,self.i]
            self.sample_instant += self.n//2+self.delay
        
        if self.i%self.n == 0:
            self.uk = self.CONTROLLER(self.xk,self.xk_1)
            
        if self.i==self.actuation_instant:
            self.actuator_packet_lost = 0
            if self.rand[1,self.i] > self.P_actuator_packet_lost:
                self.u = self.uk
                # self.u += self.d_hat_sens
                self.u += d_hat
            else:
                self.actuator_packet_lost = 1
                
            self.actuation_instant -= self.delay2
            self.delay2 = self.randi[1,self.i]
            self.actuation_instant += self.n+self.delay2
            
        self.i+=1
        
        return self.u 
    
    



class SMO:
    
    dt = []
    
    A = []
    B = []
    C = []
    
    k=100
    beta = 5000
    eps = 10
    po = 13
    qo = 15
    
    z = 0
    d_hat = 0
    
    def __init__(self,dt,A=_A,B=_B,C=_C):
        
        self.dt = dt
        
        self.A = A
        self.B = B
        self.C = C
 
        return
    
    def SMO(self,z,xn,fx,gx,u):
        
        so = z - xn
        
        tmp = -self.k*so -self.eps*np.abs(so)**(self.po/self.qo)*np.sign(so) -self.beta*np.arctanh(so/10) -np.abs(fx)*np.arctanh(so)
        
        z_dot = tmp + gx*u
        d_hat = tmp - fx
        
        return z_dot,d_hat
    
    def step_obs(self,x,u):
        
        z_dot, d_hat = self.SMO(self.z,x[1],mm(self.A[1],x),self.B[1],u)
        self.z += z_dot*self.dt
   
        return d_hat/self.B[1]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    