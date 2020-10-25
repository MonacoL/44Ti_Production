import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
import scipy as sp
import scipy.ndimage

def ReadYieldFunctionFile(path): #i take a yield function file and i put it into a matrix
    file_object  = open(path, "r")
    file_data = []
    for val in file_object.readlines():
        file_data.append(val)
    file_object.close()

    depth=file_data[2].split(" ")[1:]
    depth[-1]=depth[-1][:-1] #eliminate last /n from last depth
    depth = np.array(depth)
    depth = depth.astype(np.float)

    energy=[]
    row=len(file_data)-3
    columns=len(depth)
    output = [[0 for x in range(columns)] for y in range(row)]

    for data in file_data[3:]:
        temp=data.split(" ")
        energy.append(float(temp[0]))
        for Y in temp[1:]:
            output[file_data[3:].index(data)][temp[1:].index(Y)]=float(Y.replace("\n",""))
    return [energy,depth,output]


#### you can play with this variables ####

root_path="/home/monacoarpa/Desktop/Monaco_Poluianov"
S_root_path=root_path+"/yield_functions/44Ti/H"

flag_write=1 # 1 save smoothed output file, 0 don't save it

toplot="alphas"   #protons or alphas
which_plot=1  #0 no smooth, 1 smoothed, 2 difference between no smooth and smoothed
sigmay=1
sigmax=1.5

#specify here which yf to read
radius="60cm"
alpha_path=S_root_path+"/"+radius+"/yf_Ti44_prim_alphas_2020y08m13g_17h59m48s.txt"
protons_path=S_root_path+"/"+radius+"/yf_Ti44_prim_protons_2020y08m13g_17h59m48s.txt"
Y_DataAlpha = ReadYieldFunctionFile(alpha_path)
Y_DataProtons = ReadYieldFunctionFile(protons_path)

#radius="20cm"
#Y_DataAlpha = ReadYieldFunctionFile(S_root_path+"/"+radius+"/yf_Ti44_prim_alphas_2020y09m07g_10h35m06s.txt")
#Y_DataProtons = ReadYieldFunctionFile(S_root_path+"/"+radius+"/yf_Ti44_prim_protons_2020y09m07g_10h35m06s.txt")


#### here it's the plotting code

if toplot=="alphas":
    save_path=alpha_path
    energies=Y_DataAlpha[0]
    depths=Y_DataAlpha[1]
    yieldf_matrix=Y_DataAlpha[2]
    titolo="ALPHA PARTICLES "+radius
else:
    save_path=protons_path
    energies=Y_DataProtons[0]
    depths=Y_DataProtons[1]
    yieldf_matrix=Y_DataProtons[2]
    titolo="PROTONS "+radius

X_matrix=[depths for x in range(len(energies))]
Y_matrix=[energies for x in range(len(depths))]
X_matrix=np.matrix(X_matrix)
Y_matrix=np.matrix(Y_matrix)
yieldf_matrix=np.matrix(yieldf_matrix)

sigma = [sigmay, sigmax]
yieldf_matrix_smoothed = sp.ndimage.filters.gaussian_filter(yieldf_matrix, sigma, mode='reflect') #where the effective smoothing is done

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
if which_plot==1:
    output_matrix=yieldf_matrix_smoothed
    titolo += " SMOOTHED"   
    suffix = "_smoothed"                    
elif which_plot==0:
    output_matrix=yieldf_matrix    
    titolo += " NOT SMOOTHED"
    suffix = "_original"
elif which_plot==2:
    output_matrix=yieldf_matrix-yieldf_matrix_smoothed #ad numpy matrices, i can just make the difference like this 
    titolo += " DIFFERENCE NO SMOOTH-SMOOTHED"
    suffix = "_difference"

surf = ax.plot_surface(X_matrix, Y_matrix.T, output_matrix, cmap=cm.coolwarm, linewidth=0, antialiased=False)   

ax.set_xlabel('depth [g/cm2]')
ax.set_ylabel('energy [GeV/nucl]')
ax.set_zlabel('yield function value')

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.subplots_adjust(bottom=0, left=0, top=1, right=1)
plt.title(titolo)

plt.show() #comment this not to show the plot

if flag_write==1 and which_plot==1:  #i suppose we need to write only the smoothed yf, not the original one or the difference between the 2
    import datetime
    save_path+=suffix
    file_object  = open(save_path, "w")
    file_object.write("Yield function of production of Ti44 by protons, neutrons, alphas, [(Ti44 atoms * cm2) / (g * prim. part. nucleon)] (computed with Geant4.10).\n")
    file_object.write("The primaries are "+toplot+".\n")
    strToWrite="Energy[GeV/nuc],depths[g/cm2]: "
    for h in depths:
        if h<6:
            h=int(h)
        strToWrite+=str(h)+" "
    strToWrite=strToWrite[:-1]
    strToWrite+="\n"
    file_object.write(strToWrite)
    for i in range(0,len(energies)):
        strToWrite=str(energies[i]) + " "            
        for h in range(0,len(depths)):
            strToWrite+=str("%1.5E"% (output_matrix[i][h]))+" "
        strToWrite=strToWrite[:-1]
        strToWrite+="\n"
        file_object.write(strToWrite)
    file_object.close()    