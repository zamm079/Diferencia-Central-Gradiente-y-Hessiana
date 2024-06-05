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
        subxfinal=[]
        xcopy1=np.copy(x)
        xcopy2=np.copy(x)
        for j in range(len(x)):
            xcopy1[i]=x[j]+Dx*x[j]
            xcopy2[i]=x[j]-Dx*x[j]
            f1=f(xcopy1)
            fx= 2*f(x)
            f2=f(xcopy2)

            t1=(np.array([x[i]+Dx*x[i],x[j]+Dx*x[j]]))
            t2=(np.array([x[i]+Dx*x[i],x[j]-Dx*x[j]]))
            t3=(np.array([x[i]-Dx*x[i],x[j]+Dx*x[j]]))
            t4=(np.array([x[i]-Dx*x[i],x[j]-Dx*x[j]]))
            ft1=f(t1)
            ft2=f(t2)
            ft3=f(t3)
            ft4=f(t4)
            div=4*(Dx*x[i]*Dx*x[j])
            a_fx=ft1-ft2-ft3+ft4
            a_fx=a_fx/div

            if j > i:
                sub11=((f1-fx+f2)/(Dx*x[i])**2)
                sub12=(a_fx)
            if j == i:
                sub21=(a_fx)
                sub22=((f1-fx+f2)/(Dx*x[i])**2)
        if i == 0:
            subxfinal.append(sub11)
            subxfinal.append(sub12)
            xfinal.append(subxfinal)
        if i == 1:
            subxfinal.append(sub21)
            subxfinal.append(sub22)
            xfinal.append(subxfinal)
    return xfinal

           
            



def funcion_prueba(x):
    r = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2
    return r

xt=np.transpose(np.array([1.0,1.0,1.0]))


print(diferencia_central_gradiente(funcion_prueba,xt))
print(diferencia_central_hesiana(funcion_prueba,xt))