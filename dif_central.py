import numpy as np

def diferencia_central_gradiente(f,x):
    Dx=0.01
    xfinal=[]
    for i in range(len(x)):
        xcopy1=np.copy(x)
        xcopy2=np.copy(x)
        xcopy1[i]=x[i]+Dx*x[i]
        xcopy2[i]=x[i]-Dx*x[i]
        f1=f(xcopy1)
        f2=f(xcopy2)
        xfinal.append((f1-f2)/(2*Dx*x[i]))
    
    return xfinal

def diferencia_central_hesiana(f,x):
    Dx=0.01
    xfinal=[]
    for i in range(len(x)):
        xcopy1=np.copy(x)
        xcopy2=np.copy(x)
        for j in range(len(x)):
            xcopy1[j]=x[j]+Dx*x[j]
            xcopy2[j]=x[j]-Dx*x[j]
            fx=f(x)
            f1=f(xcopy1)
            f2=f(xcopy2)
            print((f1-fx+f2)/(Dx*x[j])**2)
            



def funcion_prueba(x):
    r = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2
    return r

xt=np.transpose(np.array([1.0,1.0]))


print(diferencia_central_gradiente(funcion_prueba,xt))
diferencia_central_hesiana(funcion_prueba,xt)