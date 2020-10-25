import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
import scipy as sp
import scipy.ndimage
import csv

def ReadQMatricesFile(path): #i take a yield function file and i put it into a matrix
    file_object  = open(path, "r")
    file_data = []
    for val in file_object.readlines():
        file_data.append(val)
    file_object.close()
    depth=file_data[3].split(",")[1:]
    depth[-1]=depth[-1][:-1] #eliminate last /n from last depth    
    depth = np.array(depth)    
    depth = depth.astype(np.float)
    
    phi=[]
    row=len(file_data)-3
    columns=len(depth)
    output = [[0 for x in range(columns)] for y in range(row)]

    for data in file_data[4:]:
        temp=data.split(",")
        phi.append(float(temp[0]))
        for Y in temp[1:]:
            output[file_data[3:].index(data)][temp[1:].index(Y)]=float(Y.replace("\n",""))
    return [phi,depth,output]

#### you can play with this variables ####

root_path="/home/monacoarpa/Desktop/Monaco_Poluianov"
Q_root_path=root_path+"/production/matrices"

flag_write=1 # 1 save smoothed output file, 0 don't save it

which_plot=1  #0 no smooth, 1 smoothed, 2 difference between no smooth and smoothed
sigmay=1
sigmax=1.5

#specify here which q matrix to read
radius="10cm"
category="H"
Q_root_path+="/"+category
q_path=Q_root_path+"/Q_VosAndPotgieter_10cm_"+category+".csv"
Q_Data=ReadQMatricesFile(q_path)


#### here it's the plotting code

save_path=q_path
phi=Q_Data[0]
depths=Q_Data[1]
q_matrix=Q_Data[2][1:]
titolo="Q PRODUCTION MATRIX "+category+" "+radius

X_matrix=[depths for x in range(len(phi))]
Y_matrix=[phi for x in range(len(depths))]
X_matrix=np.matrix(X_matrix)
Y_matrix=np.matrix(Y_matrix)
q_matrix=np.matrix(q_matrix)


sigma = [sigmay, sigmax]
q_matrix_smoothed = sp.ndimage.filters.gaussian_filter(q_matrix, sigma, mode='reflect') #where the effective smoothing is done

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
if which_plot==1:
    output_matrix=q_matrix_smoothed
    titolo += " SMOOTHED"   
    suffix = "_smoothed"                    
elif which_plot==0:
    output_matrix=q_matrix    
    titolo += " NOT SMOOTHED"
    suffix = "_original"
elif which_plot==2:
    output_matrix=q_matrix-q_matrix_smoothed #ad numpy matrices, i can just make the difference like this 
    titolo += " DIFFERENCE NO SMOOTH-SMOOTHED"
    suffix = "_difference"

surf = ax.plot_surface(X_matrix, Y_matrix.T, output_matrix, cmap=cm.coolwarm, linewidth=0, antialiased=False)   

ax.set_xlabel('depth [g/cm2]')
ax.set_ylabel('phi [MV]')
ax.set_zlabel('production value')

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.subplots_adjust(bottom=0, left=0, top=1, right=1)
plt.title(titolo)

plt.show()

if flag_write==1 and which_plot==1:  #i suppose we need to write only the smoothed yf, not the original one or the difference between the 2
    import datetime
    save_path+=suffix
    file_object  = open(save_path, "w")
    file_object.write("Production rate of Ti-44 by GCR (all) in meteoroid "+radius+".\n")
    file_object.write("Notes: LIS_VosPotgieter 2015\n")
    file_object.write("Values=Production rates [atoms/gs], X=phi [MV], Y=depth [g/cm2]\n")    
    strToWrite="phi/depths "
    for h in depths:
        if h<6:
            h=int(h)
        strToWrite+=str(h)+" "
    strToWrite=strToWrite[:-1]
    strToWrite+="\n"
    file_object.write(strToWrite)
    for i in range(0,len(phi)):
        strToWrite=str(phi[i]) + " "            
        for h in range(0,len(depths)):
            strToWrite+=str("%1.5E"% (output_matrix[i][h]))+" "
        strToWrite=strToWrite[:-1]
        strToWrite+="\n"
        file_object.write(strToWrite)
    file_object.close()    