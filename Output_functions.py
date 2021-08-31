from numpy import array,sin,cos,tan,arcsin,arccos,arctan,sqrt,pi


alpha=17.5*pi/180
L_1=0.14
L_2=0.5
L_3=0.5246808715635702
d=0.2
D=1.6
m_2=1.12
m_r=1.17
I_1=0.7761601605732
I_2=0.024676 


def F(x, y, z, w):
    return (array([[(-1/2*L_1*L_2*m_2*sin(alpha + x + y) - L_1*L_2*m_r*sin(y)*cos(alpha + x))*sin(alpha + x)/(-L_2*sin(y)*sin(alpha + x) + L_2*cos(y)*cos(alpha + x)) + (I_1 + L_1**2*m_2 + L_1**2*m_r*cos(alpha + x)**2)*cos(y)/(-L_1*sin(y)*sin(alpha + x) + L_1*cos(y)*cos(alpha + x)), (I_2 + (1/4)*L_2**2*m_2 + L_2**2*m_r*sin(y)**2)*sin(alpha + x)/(-L_2*sin(y)*sin(alpha + x) + L_2*cos(y)*cos(alpha + x)) + (-1/2*L_1*L_2*m_2*sin(alpha + x + y) - L_1*L_2*m_r*sin(y)*cos(alpha + x))*cos(y)/(-L_1*sin(y)*sin(alpha + x) + L_1*cos(y)*cos(alpha + x)), -L_1**2*m_r*sin(alpha + x)*cos(y)*cos(alpha + x)/(-L_1*sin(y)*sin(alpha + x) + L_1*cos(y)*cos(alpha + x)) + (-1/2*L_1*L_2*m_2*cos(alpha + x + y) + L_1*L_2*m_r*sin(y)*sin(alpha + x))*sin(alpha + x)/(-L_2*sin(y)*sin(alpha + x) + L_2*cos(y)*cos(alpha + x)), L_2**2*m_r*sin(y)*sin(alpha + x)*cos(y)/(-L_2*sin(y)*sin(alpha + x) + L_2*cos(y)*cos(alpha + x)) + (-1/2*L_1*L_2*m_2*cos(alpha + x + y) - L_1*L_2*m_r*cos(y)*cos(alpha + x))*cos(y)/(-L_1*sin(y)*sin(alpha + x) + L_1*cos(y)*cos(alpha + x)), (1/2)*L_1*L_2*m_2*sin(alpha - z)*sin(-alpha + w + z)/(-L_2*sin(w)*sin(alpha - z) + L_2*cos(w)*cos(alpha - z)) + (I_1 + L_1**2*m_2)*cos(w)/(-L_1*sin(w)*sin(alpha - z) + L_1*cos(w)*cos(alpha - z)), -1/2*L_1*L_2*m_2*sin(-alpha + w + z)*cos(w)/(-L_1*sin(w)*sin(alpha - z) + L_1*cos(w)*cos(alpha - z)) - (I_2 + (1/4)*L_2**2*m_2)*sin(alpha - z)/(-L_2*sin(w)*sin(alpha - z) + L_2*cos(w)*cos(alpha - z)), (1/2)*L_1*L_2*m_2*sin(alpha - z)*cos(-alpha + w + z)/(-L_2*sin(w)*sin(alpha - z) + L_2*cos(w)*cos(alpha - z)), -1/2*L_1*L_2*m_2*cos(w)*cos(-alpha + w + z)/(-L_1*sin(w)*sin(alpha - z) + L_1*cos(w)*cos(alpha - z)), -cos(y)/(-L_1*sin(y)*sin(alpha + x) + L_1*cos(y)*cos(alpha + x)), -cos(w)/(-L_1*sin(w)*sin(alpha - z) + L_1*cos(w)*cos(alpha - z))]]))



def Xdd(x, y, z, w):
    return (array([[-2*L_1*(I_2 + (1/4)*L_2**2*m_2 + L_2**2*m_r*sin(y)**2)*sin(alpha + x)/(2*I_1*L_2*cos(y) - L_1**2*L_2*m_2*sin(alpha + x)*sin(alpha + x + y) + 2*L_1**2*L_2*m_2*cos(y) - 2*L_1**2*L_2*m_r*sin(y)*sin(alpha + x)*cos(alpha + x) + 2*L_1**2*L_2*m_r*cos(y)*cos(alpha + x)**2) - 2*(-1/2*L_1*L_2*m_2*sin(alpha + x + y) - L_1*L_2*m_r*sin(y)*cos(alpha + x))*cos(y)/(2*I_1*cos(y) - L_1**2*m_2*sin(alpha + x)*sin(alpha + x + y) + 2*L_1**2*m_2*cos(y) - 2*L_1**2*m_r*sin(y)*sin(alpha + x)*cos(alpha + x) + 2*L_1**2*m_r*cos(y)*cos(alpha + x)**2), 2*L_1**2*m_r*sin(alpha + x)*cos(y)*cos(alpha + x)/(2*I_1*cos(y) - L_1**2*m_2*sin(alpha + x)*sin(alpha + x + y) + 2*L_1**2*m_2*cos(y) - 2*L_1**2*m_r*sin(y)*sin(alpha + x)*cos(alpha + x) + 2*L_1**2*m_r*cos(y)*cos(alpha + x)**2) - 2*L_1*(-1/2*L_1*L_2*m_2*cos(alpha + x + y) + L_1*L_2*m_r*sin(y)*sin(alpha + x))*sin(alpha + x)/(2*I_1*L_2*cos(y) - L_1**2*L_2*m_2*sin(alpha + x)*sin(alpha + x + y) + 2*L_1**2*L_2*m_2*cos(y) - 2*L_1**2*L_2*m_r*sin(y)*sin(alpha + x)*cos(alpha + x) + 2*L_1**2*L_2*m_r*cos(y)*cos(alpha + x)**2), -2*L_1*L_2**2*m_r*sin(y)*sin(alpha + x)*cos(y)/(2*I_1*L_2*cos(y) - L_1**2*L_2*m_2*sin(alpha + x)*sin(alpha + x + y) + 2*L_1**2*L_2*m_2*cos(y) - 2*L_1**2*L_2*m_r*sin(y)*sin(alpha + x)*cos(alpha + x) + 2*L_1**2*L_2*m_r*cos(y)*cos(alpha + x)**2) - 2*(-1/2*L_1*L_2*m_2*cos(alpha + x + y) - L_1*L_2*m_r*cos(y)*cos(alpha + x))*cos(y)/(2*I_1*cos(y) - L_1**2*m_2*sin(alpha + x)*sin(alpha + x + y) + 2*L_1**2*m_2*cos(y) - 2*L_1**2*m_r*sin(y)*sin(alpha + x)*cos(alpha + x) + 2*L_1**2*m_r*cos(y)*cos(alpha + x)**2), -1/2*L_1*L_2*m_2*(-2*L_1*sin(y)*sin(alpha + x)*sin(alpha - z) + 2*L_1*sin(alpha - z)*cos(y)*cos(alpha + x))*sin(-alpha + w + z)/(-2*I_1*L_2*sin(w)*sin(alpha - z)*cos(y) + 2*I_1*L_2*cos(w)*cos(y)*cos(alpha - z) + L_1**2*L_2*m_2*sin(w)*sin(alpha + x)*sin(alpha - z)*sin(alpha + x + y) - 2*L_1**2*L_2*m_2*sin(w)*sin(alpha - z)*cos(y) - L_1**2*L_2*m_2*sin(alpha + x)*sin(alpha + x + y)*cos(w)*cos(alpha - z) + 2*L_1**2*L_2*m_2*cos(w)*cos(y)*cos(alpha - z) + 2*L_1**2*L_2*m_r*sin(w)*sin(y)*sin(alpha + x)*sin(alpha - z)*cos(alpha + x) - 2*L_1**2*L_2*m_r*sin(w)*sin(alpha - z)*cos(y)*cos(alpha + x)**2 - 2*L_1**2*L_2*m_r*sin(y)*sin(alpha + x)*cos(w)*cos(alpha + x)*cos(alpha - z) + 2*L_1**2*L_2*m_r*cos(w)*cos(y)*cos(alpha + x)**2*cos(alpha - z)) + (I_1 + L_1**2*m_2)*(2*sin(y)*sin(alpha + x)*cos(w) - 2*cos(w)*cos(y)*cos(alpha + x))/(-2*I_1*sin(w)*sin(alpha - z)*cos(y) + 2*I_1*cos(w)*cos(y)*cos(alpha - z) + L_1**2*m_2*sin(w)*sin(alpha + x)*sin(alpha - z)*sin(alpha + x + y) - 2*L_1**2*m_2*sin(w)*sin(alpha - z)*cos(y) - L_1**2*m_2*sin(alpha + x)*sin(alpha + x + y)*cos(w)*cos(alpha - z) + 2*L_1**2*m_2*cos(w)*cos(y)*cos(alpha - z) + 2*L_1**2*m_r*sin(w)*sin(y)*sin(alpha + x)*sin(alpha - z)*cos(alpha + x) - 2*L_1**2*m_r*sin(w)*sin(alpha - z)*cos(y)*cos(alpha + x)**2 - 2*L_1**2*m_r*sin(y)*sin(alpha + x)*cos(w)*cos(alpha + x)*cos(alpha - z) + 2*L_1**2*m_r*cos(w)*cos(y)*cos(alpha + x)**2*cos(alpha - z)), -1/2*L_1*L_2*m_2*(2*sin(y)*sin(alpha + x)*cos(w) - 2*cos(w)*cos(y)*cos(alpha + x))*sin(-alpha + w + z)/(-2*I_1*sin(w)*sin(alpha - z)*cos(y) + 2*I_1*cos(w)*cos(y)*cos(alpha - z) + L_1**2*m_2*sin(w)*sin(alpha + x)*sin(alpha - z)*sin(alpha + x + y) - 2*L_1**2*m_2*sin(w)*sin(alpha - z)*cos(y) - L_1**2*m_2*sin(alpha + x)*sin(alpha + x + y)*cos(w)*cos(alpha - z) + 2*L_1**2*m_2*cos(w)*cos(y)*cos(alpha - z) + 2*L_1**2*m_r*sin(w)*sin(y)*sin(alpha + x)*sin(alpha - z)*cos(alpha + x) - 2*L_1**2*m_r*sin(w)*sin(alpha - z)*cos(y)*cos(alpha + x)**2 - 2*L_1**2*m_r*sin(y)*sin(alpha + x)*cos(w)*cos(alpha + x)*cos(alpha - z) + 2*L_1**2*m_r*cos(w)*cos(y)*cos(alpha + x)**2*cos(alpha - z)) + (I_2 + (1/4)*L_2**2*m_2)*(-2*L_1*sin(y)*sin(alpha + x)*sin(alpha - z) + 2*L_1*sin(alpha - z)*cos(y)*cos(alpha + x))/(-2*I_1*L_2*sin(w)*sin(alpha - z)*cos(y) + 2*I_1*L_2*cos(w)*cos(y)*cos(alpha - z) + L_1**2*L_2*m_2*sin(w)*sin(alpha + x)*sin(alpha - z)*sin(alpha + x + y) - 2*L_1**2*L_2*m_2*sin(w)*sin(alpha - z)*cos(y) - L_1**2*L_2*m_2*sin(alpha + x)*sin(alpha + x + y)*cos(w)*cos(alpha - z) + 2*L_1**2*L_2*m_2*cos(w)*cos(y)*cos(alpha - z) + 2*L_1**2*L_2*m_r*sin(w)*sin(y)*sin(alpha + x)*sin(alpha - z)*cos(alpha + x) - 2*L_1**2*L_2*m_r*sin(w)*sin(alpha - z)*cos(y)*cos(alpha + x)**2 - 2*L_1**2*L_2*m_r*sin(y)*sin(alpha + x)*cos(w)*cos(alpha + x)*cos(alpha - z) + 2*L_1**2*L_2*m_r*cos(w)*cos(y)*cos(alpha + x)**2*cos(alpha - z)), -1/2*L_1*L_2*m_2*(-2*L_1*sin(y)*sin(alpha + x)*sin(alpha - z) + 2*L_1*sin(alpha - z)*cos(y)*cos(alpha + x))*cos(-alpha + w + z)/(-2*I_1*L_2*sin(w)*sin(alpha - z)*cos(y) + 2*I_1*L_2*cos(w)*cos(y)*cos(alpha - z) + L_1**2*L_2*m_2*sin(w)*sin(alpha + x)*sin(alpha - z)*sin(alpha + x + y) - 2*L_1**2*L_2*m_2*sin(w)*sin(alpha - z)*cos(y) - L_1**2*L_2*m_2*sin(alpha + x)*sin(alpha + x + y)*cos(w)*cos(alpha - z) + 2*L_1**2*L_2*m_2*cos(w)*cos(y)*cos(alpha - z) + 2*L_1**2*L_2*m_r*sin(w)*sin(y)*sin(alpha + x)*sin(alpha - z)*cos(alpha + x) - 2*L_1**2*L_2*m_r*sin(w)*sin(alpha - z)*cos(y)*cos(alpha + x)**2 - 2*L_1**2*L_2*m_r*sin(y)*sin(alpha + x)*cos(w)*cos(alpha + x)*cos(alpha - z) + 2*L_1**2*L_2*m_r*cos(w)*cos(y)*cos(alpha + x)**2*cos(alpha - z)), -1/2*L_1*L_2*m_2*(2*sin(y)*sin(alpha + x)*cos(w) - 2*cos(w)*cos(y)*cos(alpha + x))*cos(-alpha + w + z)/(-2*I_1*sin(w)*sin(alpha - z)*cos(y) + 2*I_1*cos(w)*cos(y)*cos(alpha - z) + L_1**2*m_2*sin(w)*sin(alpha + x)*sin(alpha - z)*sin(alpha + x + y) - 2*L_1**2*m_2*sin(w)*sin(alpha - z)*cos(y) - L_1**2*m_2*sin(alpha + x)*sin(alpha + x + y)*cos(w)*cos(alpha - z) + 2*L_1**2*m_2*cos(w)*cos(y)*cos(alpha - z) + 2*L_1**2*m_r*sin(w)*sin(y)*sin(alpha + x)*sin(alpha - z)*cos(alpha + x) - 2*L_1**2*m_r*sin(w)*sin(alpha - z)*cos(y)*cos(alpha + x)**2 - 2*L_1**2*m_r*sin(y)*sin(alpha + x)*cos(w)*cos(alpha + x)*cos(alpha - z) + 2*L_1**2*m_r*cos(w)*cos(y)*cos(alpha + x)**2*cos(alpha - z)), 2*cos(y)/(2*I_1*cos(y) - L_1**2*m_2*sin(alpha + x)*sin(alpha + x + y) + 2*L_1**2*m_2*cos(y) - 2*L_1**2*m_r*sin(y)*sin(alpha + x)*cos(alpha + x) + 2*L_1**2*m_r*cos(y)*cos(alpha + x)**2), -(2*sin(y)*sin(alpha + x)*cos(w) - 2*cos(w)*cos(y)*cos(alpha + x))/(-2*I_1*sin(w)*sin(alpha - z)*cos(y) + 2*I_1*cos(w)*cos(y)*cos(alpha - z) + L_1**2*m_2*sin(w)*sin(alpha + x)*sin(alpha - z)*sin(alpha + x + y) - 2*L_1**2*m_2*sin(w)*sin(alpha - z)*cos(y) - L_1**2*m_2*sin(alpha + x)*sin(alpha + x + y)*cos(w)*cos(alpha - z) + 2*L_1**2*m_2*cos(w)*cos(y)*cos(alpha - z) + 2*L_1**2*m_r*sin(w)*sin(y)*sin(alpha + x)*sin(alpha - z)*cos(alpha + x) - 2*L_1**2*m_r*sin(w)*sin(alpha - z)*cos(y)*cos(alpha + x)**2 - 2*L_1**2*m_r*sin(y)*sin(alpha + x)*cos(w)*cos(alpha + x)*cos(alpha - z) + 2*L_1**2*m_r*cos(w)*cos(y)*cos(alpha + x)**2*cos(alpha - z)), -2*L_1*L_2*sin(y)*sin(alpha + x)/(2*I_1*L_2*cos(y) - L_1**2*L_2*m_2*sin(alpha + x)*sin(alpha + x + y) + 2*L_1**2*L_2*m_2*cos(y) - 2*L_1**2*L_2*m_r*sin(y)*sin(alpha + x)*cos(alpha + x) + 2*L_1**2*L_2*m_r*cos(y)*cos(alpha + x)**2) + 2*L_1*cos(y)*cos(alpha + x)/(2*I_1*cos(y) - L_1**2*m_2*sin(alpha + x)*sin(alpha + x + y) + 2*L_1**2*m_2*cos(y) - 2*L_1**2*m_r*sin(y)*sin(alpha + x)*cos(alpha + x) + 2*L_1**2*m_r*cos(y)*cos(alpha + x)**2)]]))



def Y(x):
    return (-arcsin((L_1*cos(alpha + x) - d)/L_2))



def Z(x, y, w):
    return (alpha + arcsin((-D + L_1*sin(alpha + x) + L_2*cos(w) + L_2*cos(y) + L_3)/L_1))



def W(x, y):
    return (2*arctan((2*L_2*d - sqrt(-L_1**4 + 2*L_1**2*L_2**2 + 2*L_1**2*d**2 + 2*L_1**2*(-D + L_1*sin(alpha + x) + L_2*cos(y) + L_3)**2 - L_2**4 + 2*L_2**2*d**2 + 2*L_2**2*(-D + L_1*sin(alpha + x) + L_2*cos(y) + L_3)**2 - d**4 - 2*d**2*(-D + L_1*sin(alpha + x) + L_2*cos(y) + L_3)**2 - (-D + L_1*sin(alpha + x) + L_2*cos(y) + L_3)**4))/(-L_1**2 + L_2**2 - 2*L_2*(-D + L_1*sin(alpha + x) + L_2*cos(y) + L_3) + d**2 + (-D + L_1*sin(alpha + x) + L_2*cos(y) + L_3)**2)))



def Yd(x, xd, y):
    return (L_1*xd*sin(alpha + x)/(L_2*cos(y)))



def Zd(x, xd, y, yd, z, w):
    return ((L_1*xd*cos(alpha + x) - L_2*yd*sin(y))*cos(w)/(L_1*cos(alpha + w - z)))



def Wd(x, xd, y, yd, z, w):
    return (-(L_1*xd*cos(alpha + x) - L_2*yd*sin(y))*sin(alpha - z)/(L_2*cos(alpha + w - z)))



def Ydd(x, xd, xdd, y, yd):
    return ((L_1*(xd**2*cos(alpha + x) + xdd*sin(alpha + x)) + L_2*yd**2*sin(y))/(L_2*cos(y)))



def Zdd(x, xd, xdd, y, yd, ydd, z, zdd, w, wd):
    return ((-L_1*xd**2*sin(alpha + x)*cos(w) + L_1*xdd*cos(w)*cos(alpha + x) - L_1*zdd**2*sin(alpha + w - z) - L_2*wd**2 - L_2*yd**2*cos(w)*cos(y) - L_2*ydd*sin(y)*cos(w))/(L_1*cos(alpha + w - z)))



def Wdd(x, xd, xdd, y, yd, ydd, z, zdd, w, wd):
    return ((L_1*xd**2*sin(alpha + x)*sin(alpha - z) - L_1*xdd*sin(alpha - z)*cos(alpha + x) + L_1*zdd**2 + L_2*wd**2*sin(alpha + w - z) + L_2*yd**2*sin(alpha - z)*cos(y) + L_2*ydd*sin(y)*sin(alpha - z))/(L_2*cos(alpha + w - z)))



def dr_to_x_0(dr, y):
    return (-alpha + arcsin(((1/2)*D - L_2*cos(y) - 1/2*L_3 + dr)/L_1))



def dr_to_x_1(drd, x, y, yd):
    return ((L_2*yd*sin(y) + drd)/(L_1*cos(alpha + x)))



def dr_to_x_2(drdd, x, xd, y, yd, ydd):
    return ((L_1*xd**2*sin(alpha + x) + L_2*yd**2*cos(y) + L_2*ydd*sin(y) + drdd)/(L_1*cos(alpha + x)))



def x_to_dr(x, xd, xdd, y, yd, ydd):
    return (array([[-1/2*D + L_1*sin(alpha + x) + L_2*cos(y) + (1/2)*L_3], [L_1*xd*cos(alpha + x) - L_2*yd*sin(y)], [-L_1*xd**2*sin(alpha + x) + L_1*xdd*cos(alpha + x) - L_2*yd**2*cos(y) - L_2*ydd*sin(y)]]))



