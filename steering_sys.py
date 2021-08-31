# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:25:10 2021

@author: Erfan
"""
import Output_functions as f
import numpy as np



class STEERING_SYSTEM:
    
    
    
    dt = []
    
    a = 17.5*np.pi/180
    L1 =0.14
    L2 =0.5
    L3 =0.5246808715635702
    d  =0.2
    D  =1.6
   
    
    lock_margin = 10*np.pi/180
    max_lock_angle = np.arccos(d/(L1+L2)) - lock_margin - a
    min_lock_angle = []
    
    x = []
    xd = []
    xdd = []
    y = []
    yd = []
    ydd = []
    z = []
    zd = []
    zdd = []
    w = []
    wd = []
    wdd = []
     
    def __init__(self,dt):
        
        self.dt = dt
        self.xd = 0
        self.xdd = 0
        
        self.x = self.max_lock_angle
        self.apply_constraints()
        self.min_lock_angle = -self.z
    
        self.x = 0
        self.apply_constraints()
        
    
    def apply_constraints(self):
        self.y = f.Y(self.x)
        
        # if not self.w:
        #     self.w = f.W(self.x,self.y)
        # else:
        #     self.inverse_kinematics()
        self.w = f.W(self.x,self.y)
        self.z = f.Z(self.x,self.y,self.w)
        
        self.yd   = f.Yd(self.x,self.xd,self.y)
        self.zd = f.Zd(self.x,self.xd,self.y,self.yd,self.z,self.w)
        self.wd = f.Wd(self.x,self.xd,self.y,self.yd,self.z,self.w)
    
        self.ydd = f.Ydd(self.x,self.xd,self.xdd,self.y,self.yd)
        self.zdd = f.Zdd(self.x,self.xd,self.xdd,self.y,self.yd,self.ydd,self.z,self.zd,self.w,self.wd)
        self.wdd = f.Wdd(self.x,self.xd,self.xdd,self.y,self.yd,self.ydd,self.z,self.zd,self.w,self.wd)
    
    def inverse_kinematics(self):
        C = self.D - (self.L1*np.sin(self.x)+self.L2*np.cos(self.y)+self.L3)
        gamma = np.arccos((self.L1**2+self.L2**2-self.d**2-C**2)/(2*self.L1*self.L2))
        
        for i in range(50):
            tmp = np.arcsin((self.d-self.L1*np.sin(gamma - self.w))/self.L2)
            if abs(tmp-self.w)<1e-10:
                self.w = tmp
                break
            self.w = tmp

    
    def get_delta_r(self):
        return f.x_to_dr(self.x,self.xd,self.xdd,self.y,self.yd,self.ydd)
    
    def deltaX_to_x(self,dX):
        self.x   = f.dr_to_x_0(dX[0],self.y)
        self.xd  = f.dr_to_x_1(dX[1],self.x,self.y,self.yd)
        self.xdd = f.dr_to_x_2(dX[2],self.x,self.xd,self.y,self.yd,self.ydd)
        
    
    def step_xdd(self,M,F):
        F += self.self_aligning_T()
        
        param = np.array([self.ydd,self.xd**2,self.yd**2,self.zdd,self.wdd,self.zd**2,self.wd**2,M[0],M[1],F],dtype=float)
        xdd = np.dot(f.Xdd(self.x,self.y,self.z,self.w).reshape([10,]),param)
        
        self.xdd = 0.5*self.xdd + 0.5*xdd
        
        self.xd += self.xdd*self.dt
        self.x  += 0.5*self.xdd*self.dt**2 + self.xd*self.dt
        
        
        self.lock()
        self.apply_constraints()
        
    def get_F(self,M):
       
        if (self.lock()):
            self.F = 0
            self.apply_constraints()
            return self.F
        
        self.apply_constraints()
        
        param = np.array([self.xdd,self.ydd,self.xd**2,self.yd**2,self.zdd,self.wdd,self.zd**2,self.wd**2,M[0],M[1]])
        self.F = np.dot(f.F(self.x,self.y,self.z,self.w),param)

        return self.F        
    
    
    def lock(self):
        if self.x <= self.min_lock_angle:
            self.xdd = 0
            self.xd = 0
            self.x = self.min_lock_angle
            return True
        if self.x >= self.max_lock_angle:
            self.xdd = 0
            self.xd = 0
            self.x = self.max_lock_angle
            return True
        return False
    
    
    def self_aligning_T(self):
        return 0
        return -1000*self.get_deltaX()[1]
        # return -2000*self.get_deltaX()[0] - 100*self.get_deltaX()[1]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    