import random
import math

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc

Mo = 1.98847e30  # kg
kpc = 3.08567758128e19  # m

G = 6.67430e-11 / (kpc**3) * Mo
h = 0.6727

# index = ["0", "0.7", "1.4", "2.1", "2.8", "3.5", "4.2", "4.9", "5.6", "6.3", "7.0", "7.7", "8.4", "9.1", "9.8", "10.5", "11.2", "11.9", "12.6", "13.3", "14.0"]
# index = ["0", "2.1", "2.8", "4.9", "7.0", "9.1", "11.2", "13.3"]

# for i in index: 
#     # red = random.random()
#     # blue = random.random()
#     # green = random.random()
#     # color = (red, green, blue)

#     array1 = np.loadtxt("M_t=" + i + ".txt")
#     # plt.plot(array1[:,2], array1[:,4], label="M_t="+i)

#     array2 = np.loadtxt("D_t=" + i + ".txt")
#     # plt.plot(array2[:,2], array2[:,4], label="D_t="+i, linestyle="dashdot")

#     mumLen = array1.shape[0]
#     plt.plot(array1[:mumLen,2], array1[:mumLen,4] + array2[:mumLen,4], label="Total_t="+i)

# plt.yscale("log")
# plt.xscale("log")
# plt.xlabel("Radius (kpc)")
# plt.ylabel("Density (M$_o$ kpc$^{-3}$)")

# plt.legend()
# plt.show()

# i = "0"
# arrayB = np.loadtxt("B_t=" + i + ".txt")
# plt.plot(arrayB[:,2], arrayB[:,4], label="B_t="+i)

# plt.yscale("log")
# plt.xscale("log")
# plt.xlabel("Radius (kpc)")
# plt.ylabel("Density (M$_o$ kpc$^{-3}$)")

# plt.legend()
# plt.show()

# array100000 = np.loadtxt("verify_NFW_GPE_100000.txt")
# array100 = np.loadtxt("verify_NFW_GPE_100.txt")
# array10 = np.loadtxt("verify_NFW_GPE_10.txt")
# array5 = np.loadtxt("verify_NFW_GPE_5.txt")

# # plt.plot(array5[:, 0], array5[:, 1], label="numerical_5")
# # plt.plot(array10[:, 0], array10[:, 1], label="numerical_10")
# # plt.plot(array100[:, 0], array100[:, 1], label="numerical_100")
# # plt.plot(array100000[:, 0], array100000[:, 1], label="numerical_100000")
# # plt.plot(array100[:, 0], array100[:, 2], label="analytical")
# plt.plot(array100[:, 0], abs(array100[:, 1] - array100[:, 2]), label="diff")


# plt.yscale("symlog")
# # plt.xscale("log")
# plt.xlabel("Radius (kpc)")
# plt.ylabel("G potential")

# plt.legend()
# plt.show()


# array = np.loadtxt("NFW_potentialProfile.txt")

# # plt.plot(array5[:, 0], array5[:, 1], label="numerical_5")
# # plt.plot(array10[:, 0], array10[:, 1], label="numerical_10")
# # plt.plot(array100[:, 0], array100[:, 1], label="numerical_100")
# # plt.plot(array100000[:, 0], array100000[:, 1], label="numerical_100000")
# # plt.plot(array100[:, 0], array100[:, 2], label="analytical")
# plt.plot(array[:, 0], array[:, 1], label="potentialProfile")


# # plt.yscale("symlog")
# # plt.xscale("log")
# plt.xlabel("Radius (kpc)")
# plt.ylabel("Effective potential")

# plt.legend()
# plt.show()

# array50M = np.loadtxt("50/M_t=14.0.txt")
# array50D = np.loadtxt("50/D_t=14.0.txt")
# array100M = np.loadtxt("100/M_t=14.0.txt")
# array100D = np.loadtxt("100/D_t=14.0.txt")
# array500M = np.loadtxt("500/M_t=14.0.txt")
# array500D = np.loadtxt("500/D_t=14.0.txt")
# array1000M = np.loadtxt("1000/M_t=14.0.txt")
# array1000D = np.loadtxt("1000/D_t=14.0.txt")
# array2000M = np.loadtxt("2000/M_t=14.0.txt")
# array2000D = np.loadtxt("2000/D_t=14.0.txt")

# def arrayTotal(arrayM, arrayD):
#     a = np.amin([arrayM.shape[0], arrayD.shape[0]])
#     b = np.amax([arrayM.shape[0], arrayD.shape[0]])
    
#     arrayT = np.zeros((b, 7))
#     arrayT[:a, 3:5] = arrayM[:a, 3:5] + arrayD[:a, 3:5]
#     arrayT[a:b, 3:5] = arrayD[a:b, 3:5]
#     arrayT[:, 0:3] = arrayD[:, 0:3]

#     return arrayT

# def averageDen(arrayT):
#     for i in np.arange(arrayT.shape[0]):
#         arrayT[i, 5] = np.sum(arrayT[0:i+1, 3])
    
#     arrayT[:, 6] = arrayT[:, 5] / (4 / 3 * np.pi * (arrayT[:, 1]**3))

#     return arrayT

# # plt.plot(array50M[:, 2], array50M[:, 4], label="50M")
# # plt.plot(array100M[:, 2], array100M[:, 4], label="100M")
# # plt.plot(array500M[:, 2], array500M[:, 4], label="500M")
# # plt.plot(array1000M[:, 2], array1000M[:, 4], label="1000M")
# # plt.plot(array2000M[:, 2], array2000M[:, 4], label="2000M")

# # plt.plot(array50D[:, 2], array50D[:, 4], label="50D")
# # plt.plot(array100D[:, 2], array100D[:, 4], label="100D")
# # plt.plot(array500D[:, 2], array500D[:, 4], label="500D")
# # plt.plot(array1000D[:, 2], array1000D[:, 4], label="1000D")
# # plt.plot(array2000D[:, 2], array2000D[:, 4], label="2000D")

# array50T = averageDen(arrayTotal(array50M, array50D))
# array100T = averageDen(arrayTotal(array100M, array100D))
# array500T = averageDen(arrayTotal(array500M, array500D))
# array1000T = averageDen(arrayTotal(array1000M, array1000D))
# array2000T = averageDen(arrayTotal(array2000M, array2000D))
# plt.plot(array50T[:, 2], array50T[:, 6], label="50T")
# plt.plot(array100T[:, 2], array100T[:, 6], label="100T")
# plt.plot(array500T[:, 2], array500T[:, 6], label="500T")
# plt.plot(array1000T[:, 2], array1000T[:, 6], label="1000T")
# plt.plot(array2000T[:, 2], array2000T[:, 6], label="2000T")

# plt.xlabel("Radius (kpc)")
# plt.ylabel("Average density (M$_o$ kpc$^{-3}$)")

# plt.legend()
# plt.show()


# array999D_beforeAdia = np.loadtxt("999/D_beforeAdia_t=0.7.txt")
# array999D = np.loadtxt("999/D_t=0.7.txt")
# array499D_beforeAdia = np.loadtxt("499/D_beforeAdia_t=0.7.txt")
# array499D = np.loadtxt("499/D_t=0.7.txt")
# array49D_beforeAdia = np.loadtxt("49/D_beforeAdia_t=0.7.txt")
# array49D = np.loadtxt("49/D_t=0.7.txt")

# array501D_beforeAdia = np.loadtxt("501/D_beforeAdia_t=0.7.txt")
# array501D = np.loadtxt("501/D_t=0.7.txt")

# array1501D_beforeAdia = np.loadtxt("1501/D_beforeAdia_t=0.7.txt")
# array1501D = np.loadtxt("1501/D_t=0.7.txt")

# # plt.plot(array999D_beforeAdia[:, 2], array999D_beforeAdia[:, 4], label="999_beforeAdia")
# # #plt.plot(array999D[:, 2], array999D[:, 4], label="999")
# plt.plot(array499D_beforeAdia[:, 2], array499D_beforeAdia[:, 4], label="499_beforeAdia")
# #plt.plot(array499D[:, 2], array499D[:, 4], label="499")
# # plt.plot(array49D_beforeAdia[:, 2], array49D_beforeAdia[:, 4], label="49_beforeAdia")
# # #plt.plot(array49D[:, 2], array49D[:, 4], label="49")

# plt.plot(array501D_beforeAdia[:, 2], array501D_beforeAdia[:, 4], label="501_beforeAdia")
# #plt.plot(array501D[:, 2], array501D[:, 4], label="501")
# plt.plot(array1501D_beforeAdia[:, 2], array1501D_beforeAdia[:, 4], label="1501_beforeAdia")
# #plt.plot(array501D[:, 2], array501D[:, 4], label="501")

# plt.xlabel("Radius (kpc)")
# plt.ylabel("Density (M$_o$ kpc$^{-3}$)")

# plt.yscale("log")
# plt.xscale("log")

# plt.legend()
# plt.show()


# index = ["0", "2.1", "2.8", "4.9", "7.0", "9.1", "11.2", "13.3"]
# X = "D"

# for i in index:
#     array500 = np.loadtxt("500/" + X + "_t=" + i + ".txt")
#     array501 = np.loadtxt("501/" + X + "_t=" + i + ".txt")

#     plt.plot(array500[:, 2], array500[:, 4], label="500"+X+"_"+i)
#     plt.plot(array501[:, 2], array501[:, 4], label="501"+X+"_"+i)

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# array = np.loadtxt("verify_NFW_GPE_682.txt")
# plt.plot(array[:, 0], array[:, 1] - array[:, 2])
# # plt.plot(array[:, 0], array[:, 1])
# # plt.plot(array[:, 0], array[:, 2])

# # plt.yscale("log")
# # plt.xscale("log")
# plt.show()

# arrayNFW_20 = np.loadtxt("1544_20/M_t=0.txt")
# arrayNFW_90 = np.loadtxt("1544_90/M_t=0.txt")
# plt.plot(arrayNFW_20[:, 2], arrayNFW_20[:, 4])
# plt.plot(arrayNFW_90[:, 2], arrayNFW_90[:, 4])

# arrayNFW_den = np.loadtxt("NFW_density.txt")
# array1544_20M = np.loadtxt("1544_20/M_t=0.txt")

# plt.plot(arrayNFW_den[:, 0], arrayNFW_den[:, 1])
# plt.plot(array1544_20M[:, 2], array1544_20M[:, 4])

# plt.show()

####################################################################

# array1544_20M_0 = np.loadtxt("1544_20/M_t=0.txt")  # NFW

# array1544_20M = np.loadtxt("1544_20/M_t=14.0.txt")
# array1544_20D = np.loadtxt("1544_20/D_t=14.0.txt")
# array1544_20T = np.loadtxt("1544_20/T_t=14.0.txt")

# array1544_50M = np.loadtxt("1544_50/M_t=14.0.txt")
# array1544_50D = np.loadtxt("1544_50/D_t=14.0.txt")
# array1544_50T = np.loadtxt("1544_50/T_t=14.0.txt")

# array1544_90M = np.loadtxt("1544_90/M_t=14.0.txt")
# array1544_90D = np.loadtxt("1544_90/D_t=14.0.txt")
# array1544_90T = np.loadtxt("1544_90/T_t=14.0.txt")

# array1544_140T = np.loadtxt("1544_140/T_t=14.0.txt")

# plt.plot(array1544_20M_0[:, 2], array1544_20M_0[:, 6], label="NFW")
# plt.plot(array1544_20T[:, 2], array1544_20T[:, 6], label="1544_20")
# plt.plot(array1544_50T[:, 2], array1544_50T[:, 6], label="1544_50")
# plt.plot(array1544_90T[:, 2], array1544_90T[:, 6], label="1544_90")
# plt.plot(array1544_140T[:, 2], array1544_140T[:, 6], label="1544_140")

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# ##################################################################################

# index = ["0.7", "2.1", "2.8", "4.9", "7.0", "9.1", "11.2", "13.3", "14.0"]

# for i in index:
#     array1544_20M_0 = np.loadtxt("1544_20/M_t=0.txt")  # NFW

#     array1544_20M_b = np.loadtxt("1544_20/M_beforeAdia_t="+i+".txt")
#     array1544_20M = np.loadtxt("1544_20/M_t="+i+".txt")

#     array1544_20D_b = np.loadtxt("1544_20/D_beforeAdia_t="+i+".txt")
#     array1544_20D = np.loadtxt("1544_20/D_t="+i+".txt")

#     plt.plot(array1544_20M_0[:, 2], array1544_20M_0[:, 6], label="NFW")
#     plt.plot(array1544_20M_b[:, 2], array1544_20M_b[:, 6], label="before")
#     plt.plot(array1544_20M[:, 2], array1544_20M[:, 6], label="after")

#     plt.yscale("log")
#     plt.xscale("log")
#     plt.legend()
#     plt.show()

#     plt.plot(array1544_20D_b[:, 2], array1544_20D_b[:, 6], label="before")
#     plt.plot(array1544_20D[:, 2], array1544_20D[:, 6], label="after")

#     plt.yscale("log")
#     plt.xscale("log")
#     plt.legend()
#     plt.show()

#     arrayT = np.loadtxt("1544_20/T_t="+i+".txt")
#     plt.plot(arrayT[:, 2], arrayT[:, 4], label=i)

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

##################################################################################

# array1544_20M_0 = np.loadtxt("1544_20/M_t=0.txt")  # NFW

# array250_20T = np.loadtxt("250_20/T_t=14.0.txt")
# array459_20T = np.loadtxt("459_20/T_t=14.0.txt")
# array844_20T = np.loadtxt("844_20/T_t=14.0.txt")
# array1544_20T = np.loadtxt("1544_20/T_t=14.0.txt")
# array1873_20T = np.loadtxt("1873_20/T_t=14.0.txt")

# plt.plot(array1544_20M_0[:, 2], array1544_20M_0[:, 6], label="NFW") 

# plt.plot(array250_20T[:, 2], array250_20T[:, 6], label="250_20")
# plt.plot(array459_20T[:, 2], array459_20T[:, 6], label="459_20")
# plt.plot(array844_20T[:, 2], array844_20T[:, 6], label="844_20")
# plt.plot(array1544_20T[:, 2], array1544_20T[:, 6], label="1544_20")
# plt.plot(array1873_20T[:, 2], array1873_20T[:, 6], label="1873_20")

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# arrayBp = np.loadtxt("459_20/B.txt")

# arrayB = np.loadtxt("459_20/B_t=0.txt")
# arrayM = np.loadtxt("459_20/M_t=0.txt")

# # plt.plot(arrayB[:, 2], arrayB[:, 3], label="B")
# # plt.plot(arrayM[:, 2], arrayM[:, 3], label="M")
# plt.plot(arrayBp[:, 0], arrayBp[:, 2], label="B")

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# plt.plot(arrayBp[:, 0], arrayBp[:, 3], label="B")

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# plt.plot(arrayBp[:, 0], arrayBp[:, 4], label="B")

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# plt.plot(arrayBp[:, 0], arrayBp[:, 5], label="B")

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# arrayB = np.loadtxt("576_20/B_t=0.txt")

# plt.plot(arrayB[:, 2], arrayB[:, 4], label="b")

# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()

################################################################################

# index = ["0.7", "2.1", "2.8", "4.9", "7.0", "9.1", "11.2", "13.3", "14.0"]

# for i in index:

#     arrayNFW = np.loadtxt("dmOnly/30_3_459_20/T_t=0.txt")
    
#     arrayn = np.loadtxt("dmOnly/30_3_459_20/T_t="+i+".txt")

#     #arrayyb = np.loadtxt("dmOnly1/30_3_459_20/T_beforeAdia_t="+i+".txt")
#     arrayy = np.loadtxt("dmOnly1/30_3_459_20/T_t="+i+".txt")



#     plt.plot(arrayNFW[:, 2], arrayNFW[:, 5], label="NFW")
    
#     plt.plot(arrayn[:, 2], arrayn[:, 5], label="w/o daughter expansion"+i+"")
    
#     # plt.plot(arrayyb[:, 2], arrayyb[:, 6], label="yb"+i+"")
#     plt.plot(arrayy[:, 2], arrayy[:, 5], label="w/ daughter expansion"+i+"")



#     # plt.ylabel("total average density (Mo / kpc^3)")
#     plt.ylabel("enclosed mass (Mo)")
#     plt.xlabel("radius kpc")
#     plt.yscale("log")
#     plt.xscale("log")
#     plt.legend()
#     plt.show()

# index = ["0.7", "2.1", "2.8", "4.9", "7.0", "9.1", "11.2", "13.3", "14.0"]
# index = ["0.7", "2.8", "9.1", "14.0"]

# arrayNFW = np.loadtxt("dmOnly/30_3_459_20/GPE_t=0.txt")
# plt.plot(arrayNFW[:, 2], arrayNFW[:, 3], label="NFW")

# for i in index:


    
#     arrayn = np.loadtxt("dmOnly/30_3_459_20/GPE_t="+i+".txt")

#     #arrayyb = np.loadtxt("dmOnly1/30_3_459_20/T_beforeAdia_t="+i+".txt")
#     arrayy = np.loadtxt("dmOnly1/30_3_459_20/GPE_t="+i+".txt")




    
#     plt.plot(arrayn[:, 2], arrayn[:, 3], label="w/o daughter expansion"+i+"")
    
#     # plt.plot(arrayyb[:, 2], arrayyb[:, 6], label="yb"+i+"")
#     plt.plot(arrayy[:, 2], arrayy[:, 3], label="w/ daughter expansion"+i+"")


# plt.ylabel("GPE per mass")
# plt.xlabel("radius kpc")
# # plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()


# index = ["0", "0.7", "2.1", "2.8", "4.9", "7.0", "9.1", "11.2", "13.3", "14.0"]

# for i in index:

    
#     arrayTDM = np.loadtxt("withBar/50_3_459_20/TDM_t="+i+".txt")
#     arrayB = np.loadtxt("withBar/50_3_459_20/B_t="+i+".txt")
#     arrayT = np.loadtxt("withBar/50_3_459_20/T_t="+i+".txt")


#     plt.plot(arrayTDM[:, 2], arrayTDM[:, 6], label="total DM"+i)
#     plt.plot(arrayB[:, 2], arrayB[:, 6], label="baryon"+i)
#     plt.plot(arrayT[:, 2], arrayT[:, 6], label="total"+i)

#     # plt.ylabel("total average density (Mo / kpc^3)")
#     plt.ylabel("average density (Mo / kpc^3)")
#     plt.xlabel("radius kpc")
#     plt.yscale("log")
#     plt.xscale("log")
#     plt.legend()
#     plt.show()


# arrayNFW = np.loadtxt("dmOnly_check/0.01_3_1307_20/T_t=0.txt")
# array0 = np.loadtxt("dmOnly_check/0_3_1307_20/T_result.txt")
# array0001 = np.loadtxt("dmOnly_check/0.001_3_1307_20/T_result.txt")
# array001 = np.loadtxt("dmOnly_check/0.01_3_1307_20/T_result.txt")
# array01 = np.loadtxt("dmOnly_check/0.1_3_1307_20/T_result.txt")
# array1 = np.loadtxt("dmOnly_check/1_3_1307_20/T_result.txt")
# array10 = np.loadtxt("dmOnly_check/10_3_1307_20/T_result.txt")


# plt.plot(arrayNFW[:, 2], arrayNFW[:, 6], label="NFW")
# plt.plot(array0[:, 2], array0[:, 6], label="v_k = 0 km/s")
# plt.plot(array0001[:, 2], array0001[:, 6], label="v_k = 0.001 km/s")
# plt.plot(array001[:, 2], array001[:, 6], label="v_k = 0.01 km/s")
# plt.plot(array01[:, 2], array01[:, 6], label="v_k = 0.1 km/s")
# plt.plot(array1[:, 2], array1[:, 6], label="v_k = 1 km/s")
# plt.plot(array10[:, 2], array10[:, 6], label="v_k = 10 km/s")



# plt.ylabel("total average density (Mo / kpc^3)")
# plt.title("tau = 3 Gyr; results at t = 14 Gyr\nno daughter expansion")
# plt.xlabel("radius kpc")
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()



###########################################################################

# Mo = 1.98847e30
# kpc = 3.08567758128e19
# H = 70 * 1000 / 1000 / kpc
# G = 6.67430e-11 / kpc**3 * Mo

# rho_c = 3 * H**2 / (8 * math.pi * G)
# c = 23.6  # Concentration parameter
# M_vir = 0.505e10  # Mo
# rho_avg = 103.4 * rho_c

# R_vir = (3 * M_vir / (4 * math.pi * rho_avg))**(1 / 3)
# R_s = R_vir / c
# rho_0 = M_vir / (4 * math.pi * (R_s**3)) / (math.log(1 + c) - c / (1 + c))

# # index = ["0", "0.7", "2.1", "2.8", "4.9", "7.0", "9.1", "11.2", "13.3", "14.0"]
# # indexNum = [0, 0.7, 2.1, 2.8, 4.9, 7.0, 9.1, 11.2, 13.3, 14.0]

# index = ["0", "2.1", "4.9", "9.1", "14.0"]
# indexNum = [0, 2.1, 4.9, 9.1, 14.0]

# tau = 3
# for j in np.arange(len(index)):
#     i = index[j]
#     t = indexNum[j]
#     f = 1 - math.exp(math.log(0.5) * t / tau)


#     #array = np.loadtxt("dmOnly_check/10000_3_459_20/T_t="+i+".txt")
#     array = np.loadtxt("dmOnly_check_inf/1.0e50_3_459_40/T_t="+i+".txt")
#     plt.plot(array[:, 2], array[:, 4], label="semicore(459): t = "+i+" Gyr")  
#     # plt.plot(array[:, 1], array[:, 5], label="semicore(459): t = "+i+" Gyr")  

#     array = np.loadtxt("dmOnly_check_inf/1.0e50_3_692_40/T_t="+i+".txt")
#     plt.plot(array[:, 2], array[:, 4], label="semicore(692): t = "+i+" Gyr") 
#     # plt.plot(array[:, 1], array[:, 5], label="semicore(692): t = "+i+" Gyr") 
    
#     theoryDen = ((1 - f)**4) * rho_0 / ((1 - f) * array[:, 2] / R_s) / ((1 + (1 - f) * array[:, 2] / R_s)**2)
#     theoryEncMass = 4 * np.pi * (((1 - f)**4) * rho_0) * ((R_s / (1 - f))**3) * (np.log(1 + array[:, 1] / (R_s / (1 - f))) - array[:, 1] / (R_s / (1 - f) + array[:, 1]))

#     plt.plot(array[:, 2], theoryDen, label="theory: t = "+i+" Gyr", linestyle="dashed")
#     # plt.plot(array[:, 1], theoryEncMass, label="theory: t = "+i+" Gyr", linestyle="dashed")


# plt.ylabel("shell density of total DM (Mo / kpc^3)")
# # plt.ylabel("enclosed mass of total DM (Mo / kpc^3)")
# plt.title("v_k = inf (1e50) km / s, tau = 3 Gyr\nno daughter expansion\nlabel = time (from 0 to 14 Gyr)")
# plt.xlabel("radius (kpc)")
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

###########################################################################


# array227 = np.loadtxt("dmOnly_check_spatialCon/20_3_227_20/T_result.txt")
# array343 = np.loadtxt("dmOnly_check_spatialCon/20_3_343_20/T_result.txt")
# array459 = np.loadtxt("dmOnly_check_spatialCon/20_3_459_20/T_result.txt")
# array576 = np.loadtxt("dmOnly_check_spatialCon/20_3_576_20/T_result.txt")

# plt.plot(array227[:, 2], array227[:, 6], label="227")
# plt.plot(array343[:, 2], array343[:, 6], label="343")
# plt.plot(array459[:, 2], array459[:, 6], label="459")
# plt.plot(array576[:, 2], array576[:, 6], label="576")

# plt.ylabel("average density of total DM (Mo / kpc^3)")
# plt.title("v_k = 20 km / s, tau = 3 Gyr\nno daughter expansion\nlabel = initNumOf_M_Shells")
# plt.xlabel("radius (kpc)")
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()


# array5 = np.loadtxt("dmOnly_check_temporalCon/20_3_459_5/T_result.txt")
# array10 = np.loadtxt("dmOnly_check_temporalCon/20_3_459_10/T_result.txt")
# array20 = np.loadtxt("dmOnly_check_temporalCon/20_3_459_20/T_result.txt")
# array40 = np.loadtxt("dmOnly_check_temporalCon/20_3_459_40/T_result.txt")
# array60 = np.loadtxt("dmOnly_check_temporalCon/20_3_459_60/T_result.txt")
# array100 = np.loadtxt("dmOnly_check_temporalCon/20_3_459_100/T_result.txt")


# plt.plot(array5[:, 2], array5[:, 6], label="5")
# plt.plot(array10[:, 2], array10[:, 6], label="10")
# plt.plot(array20[:, 2], array20[:, 6], label="20")
# plt.plot(array40[:, 2], array40[:, 6], label="40")
# plt.plot(array60[:, 2], array60[:, 6], label="60")
# plt.plot(array100[:, 2], array100[:, 6], label="100")


# plt.ylabel("average density of total DM (Mo / kpc^3)")
# plt.title("v_k = 20 km / s, tau = 3 Gyr\nno daughter expansion\nlabel = number of time steps")
# plt.xlabel("radius (kpc)")
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# array = np.loadtxt("dmOnly_check_0/0_3_459_40/M_t=0.txt")
# plt.plot(array[:, 1], array[:, 6], label="NFW")

# array = np.loadtxt("dmOnly_check_0/0_3_459_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="0")

# array = np.loadtxt("dmOnly_check_0/0.1_3_459_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="0.1")

# array = np.loadtxt("dmOnly_check_0/1_3_459_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="1")

# array = np.loadtxt("dmOnly_check_0/5_3_459_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="5")

# plt.ylabel("average density of total DM (Mo / kpc^3)")
# plt.title("tau = 3 Gyr\nno daughter expansion\nlabel = v_k (km / s), at t = 14 Gyr")
# plt.xlabel("radius (kpc)")
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()



# # array = np.loadtxt("semicoredata/ddm_halo-structure_vk20.00_tau3.00.txt")
# # plt.plot(array[:, 0]/h, array[:, 3]/(4/3*np.pi*(array[:, 0]**3))*(10**10)*(h**2), label="xx: vk20 tau3")

# # array = np.loadtxt("dmOnly_check_xx/20_3_459_40/T_t=14.0.txt")
# # plt.plot(array[:, 1], array[:, 6], label="jy: vk20 tau3", linestyle="dashed")

# # array = np.loadtxt("semicoredata/ddm_halo-structure_vk20.00_tau6.93.txt")
# # plt.plot(array[:, 0]/h, array[:, 3]/(4/3*np.pi*(array[:, 0]**3))*(10**10)*(h**2), label="xx: vk20 tau6.93")

# # array = np.loadtxt("dmOnly_check_xx/20_6.93_459_40/T_t=14.0.txt")
# # plt.plot(array[:, 1], array[:, 6], label="jy: vk20 tau6.93", linestyle="dashed")

# # array = np.loadtxt("semicoredata/ddm_halo-structure_vk20.00_tau14.00.txt")
# # plt.plot(array[:, 0]/h, array[:, 3]/(4/3*np.pi*(array[:, 0]**3))*(10**10)*(h**2), label="xx: vk20 tau14")

# # array = np.loadtxt("dmOnly_check_xx/20_14_459_40/T_t=14.0.txt")
# # plt.plot(array[:, 1], array[:, 6], label="jy: vk20 tau14", linestyle="dashed")

# array = np.loadtxt("semicoredata_xx/ddm_halo-structure_vk30.00_tau3.00.txt")
# plt.plot(array[:, 0]/h, array[:, 3]/(4/3*np.pi*(array[:, 0]**3))*(10**10)*(h**2), label="xx: vk30 tau3")

# array = np.loadtxt("dmOnly_check_xx/30_3_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="jy: vk30 tau3", linestyle="dashed")

# array = np.loadtxt("semicoredata_xx/ddm_halo-structure_vk30.00_tau6.93.txt")
# plt.plot(array[:, 0]/h, array[:, 3]/(4/3*np.pi*(array[:, 0]**3))*(10**10)*(h**2), label="xx: vk30 tau6.93")

# array = np.loadtxt("dmOnly_check_xx/30_6.93_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="jy: vk30 tau6.93", linestyle="dashed")

# array = np.loadtxt("semicoredata_xx/ddm_halo-structure_vk30.00_tau14.00.txt")
# plt.plot(array[:, 0]/h, array[:, 3]/(4/3*np.pi*(array[:, 0]**3))*(10**10)*(h**2), label="xx: vk30 tau14")

# array = np.loadtxt("dmOnly_check_xx/30_14_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="jy: vk30 tau14", linestyle="dashed")

# # # array = np.loadtxt("semicoredata/ddm_halo-structure_vk40.00_tau3.00.txt")
# # # plt.plot(array[:, 0]/h, array[:, 3]/(4/3*np.pi*(array[:, 0]**3))*(10**10)*(h**2), label="xx: vk40 tau3")

# # # array = np.loadtxt("dmOnly_check_xx/40_3_459_40/T_t=14.0.txt")
# # # plt.plot(array[:, 1], array[:, 6], label="jy: vk40 tau3", linestyle="dashed")

# # array = np.loadtxt("semicoredata/ddm_halo-structure_vk40.00_tau6.93.txt")
# # plt.plot(array[:, 0]/h, array[:, 3]/(4/3*np.pi*(array[:, 0]**3))*(10**10)*(h**2), label="xx: vk40 tau6.93")

# # array = np.loadtxt("dmOnly_check_xx/40_6.93_459_40/T_t=14.0.txt")
# # plt.plot(array[:, 1], array[:, 6], label="jy: vk40 tau6.93", linestyle="dashed")

# # array = np.loadtxt("semicoredata/ddm_halo-structure_vk40.00_tau14.00.txt")
# # plt.plot(array[:, 0]/h, array[:, 3]/(4/3*np.pi*(array[:, 0]**3))*(10**10)*(h**2), label="xx: vk40 tau14")

# # array = np.loadtxt("dmOnly_check_xx/40_14_459_40/T_t=14.0.txt")
# # plt.plot(array[:, 1], array[:, 6], label="jy: vk40 tau14", linestyle="dashed")




# plt.ylabel("average density of total DM (Mo / kpc^3)")
# plt.title("no daughter expansion\nat t = 14 Gyr")
# plt.xlabel("radius (kpc)")
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()






# array = np.loadtxt("dmOnly_check_xx/20_3_459_40/M_t=0.txt")
# plt.plot(array[:, 1], array[:, 6], label="NFW")

# array = np.loadtxt("dmOnly_check_xx/20_3_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="vk20 tau3")

# array = np.loadtxt("dmOnly_check_xx/20_6.93_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="vk20 tau6.93")

# array = np.loadtxt("dmOnly_check_xx/20_14_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="vk20 tau14")

# array = np.loadtxt("dmOnly_check_xx/30_3_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="vk30 tau3")

# array = np.loadtxt("dmOnly_check_xx/30_6.93_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="vk30 tau6.93")

# array = np.loadtxt("dmOnly_check_xx/30_14_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="vk30 tau14")

# # array = np.loadtxt("dmOnly_check_xx/40_3_459_40/T_t=14.0.txt")
# # plt.plot(array[:, 1], array[:, 6], label="vk40 tau3", linestyle="dashed")

# array = np.loadtxt("dmOnly_check_xx/40_6.93_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="vk40 tau6.93")

# array = np.loadtxt("dmOnly_check_xx/40_14_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="vk40 tau14")


# plt.ylabel("average density of total DM (Mo / kpc^3)")
# plt.title("no daughter expansion\nat t = 14 Gyr")
# plt.xlabel("radius (kpc)")
# plt.xlim(0.01, 10)
# plt.ylim(1e6, 1e10)
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()



# array = np.loadtxt("dmOnly_check_xx/20_3_459_40/M_t=0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="NFW")

# array = np.loadtxt("dmOnly_check_xx/20_3_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="vk20 tau3")

# array = np.loadtxt("dmOnly_check_xx/20_6.93_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="vk20 tau6.93")

# array = np.loadtxt("dmOnly_check_xx/20_14_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="vk20 tau14")

# array = np.loadtxt("dmOnly_check_xx/30_3_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="vk30 tau3")

# array = np.loadtxt("dmOnly_check_xx/30_6.93_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="vk30 tau6.93")

# array = np.loadtxt("dmOnly_check_xx/30_14_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="vk30 tau14")

# # array = np.loadtxt("dmOnly_check_xx/40_3_459_40/T_t=14.0.txt")
# # plt.plot(array[:, 1], array[:, 6], label="vk40 tau3", linestyle="dashed")

# array = np.loadtxt("dmOnly_check_xx/40_6.93_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="vk40 tau6.93")

# array = np.loadtxt("dmOnly_check_xx/40_14_459_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="vk40 tau14")


# # plt.ylabel("average density of total DM (Mo / kpc^3)")
# plt.ylabel("orbital velocity (km / s)")
# plt.title("orbital velocity\nno daughter expansion\nat t = 14 Gyr")
# plt.xlabel("radius (kpc)")
# # plt.xlim(0.01, 10)
# # plt.ylim(1e6, 1e10)
# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()


# array = np.loadtxt("dmOnly_compare_MDadia_DadiaOff/30_6.93_576_40/M_t=0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="NFW")

# array = np.loadtxt("dmOnly_compare_MDadia_DadiaOff/30_6.93_576_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="off")

# array = np.loadtxt("dmOnly_compare_MDadia_DadiaOn/30_6.93_576_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="on")

# # plt.ylabel("average density of total DM (Mo / kpc^3)")
# plt.ylabel("orbital velocity (km / s)")
# plt.title("daughter adiabatic expansion on/off\nresults at t = 14 Gyr")
# plt.xlabel("radius (kpc)")
# # plt.xlim(0.01, 10)
# # plt.ylim(1e6, 1e10)
# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()


# array = np.loadtxt("dmOnly_check_adiaCon/30_6.93_576_40/M_t=0.txt")
# plt.plot(array[:, 1], array[:, 6], label="NFW")

# for i in np.arange(6):
#     array = np.loadtxt("dmOnly_check_adiaCon/30_6.93_576_40/T_t=0.35.adiaCon="+str(i)+".txt")
#     plt.plot(array[:, 1], array[:, 6], label=i)


# plt.ylabel("average density of total DM (Mo / kpc^3)")
# plt.title("convergence test on adiabatic expansion\nresults at t = 14 Gyr")
# plt.xlabel("radius (kpc)")
# # plt.xlim(0.01, 10)
# # plt.ylim(1e6, 1e10)
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()


# aIndices = ["1.2", "1.5", "1.67", "1.6666666666666667"]
# aIndices = ["1.67"]
# for i in aIndices:

#     indexNum = [0, 0.7, 2.1, 2.8, 4.9, 7.0, 9.1, 11.2, 13.3, 14.0]
#     indexNum = [0, 14.0]

#     # array = np.loadtxt("withBar_test_aIndex_"+i+"/30_6.93_576_20/BhiRes_t=0.txt")
#     # # array = np.loadtxt("withBar_test_aIndex_"+i+"/30_6.93_576_20/B_t=0.txt")
#     # # plt.plot(array[:, 1], array[:, 6], label=i + ", init", linestyle="dashed")
#     # plt.plot(array[:, 0], array[:, 1], label=i + ", init", linestyle="dashed")

#     for j in indexNum:

#         # array = np.loadtxt("withBar_test_aIndex_"+i+"/30_6.93_576_20/BhiRes_t="+str(j)+".txt")
#         # # array = np.loadtxt("withBar_test_aIndex_"+i+"/30_6.93_576_20/B_result.txt")
#         # # plt.plot(array[:, 1], array[:, 6], label=i)
#         # plt.plot(array[:, 0], array[:, 1], label="t = "+str(j), linestyle="dashed")
        
#         array = np.loadtxt("withBar_test_aIndex_"+i+"_constK/30_6.93_576_20/BhiRes_t="+str(j)+".txt")
#         # array = np.loadtxt("withBar_test_aIndex_"+i+"/30_6.93_576_20/B_result.txt")
#         # plt.plot(array[:, 1], array[:, 6], label=i)
#         plt.plot(array[:, 0], array[:, 1], label="t = "+str(j)+" ", linestyle="dashed")

#         array = np.loadtxt("withBar_test_aIndex_"+i+"_constK_escaped/30_6.93_576_20/BhiRes_t="+str(j)+".txt")
#         # array = np.loadtxt("withBar_test_aIndex_"+i+"/30_6.93_576_20/B_result.txt")
#         # plt.plot(array[:, 1], array[:, 6], label=i)
#         plt.plot(array[:, 0], array[:, 1], label="t = "+str(j)+" (with escaped)")


# plt.ylabel("density of baryon (Mo / kpc^3)")
# plt.title("results at different times\nv_k = 30 km / s, tau = 6.93 Gyr")
# plt.xlabel("radius (kpc)")
# # plt.xlim(0.01, 10)
# # plt.ylim(1e6, 1e10)
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()


# ####################### baryon density
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_40/BhiRes_t=0.txt")
# plt.plot(array[:, 0], array[:, 1], label="t = 0 Gyr")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_40/BhiRes_t=14.0.txt")
# plt.plot(array[:, 0], array[:, 1], label="t = 14 Gyr")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK_withIter/30_6.93_576_40/BhiRes_t=14.0.txt")
# plt.plot(array[:, 0], array[:, 1], label="t = 14 Gyr (with iter)", linestyle="dashed")

# # array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_20/BhiRes_t=14.0.txt")
# # plt.plot(array[:, 0], array[:, 1], label="t = 14 Gyr (20)")

# plt.ylabel("shell density of baryon (Mo / kpc^3)")
# plt.title("v_k = 30 km / s, tau = 6.93 Gyr, initCoreT = 5e5 K, initBarRho_0 = 1e9 Mo / kpc^3")
# plt.xlabel("radius (kpc)")
# plt.xlim(0, 1.4)
# plt.ylim(0, 1.1e9)
# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()

# ######################## dm density
# array = np.loadtxt("dmOnly_compare_MDadia_DadiaOn/30_6.93_576_40/T_t=0.txt")
# plt.plot(array[:, 1], array[:, 6], label="NFW")

# array = np.loadtxt("dmOnly_compare_MDadia_DadiaOn/30_6.93_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="without baryon")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_40/TDM_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="with baryon")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK_withIter/30_6.93_576_40/TDM_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="with baryon (with iter)", linestyle="dashed")

# # array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_20/BhiRes_t=14.0.txt")
# # plt.plot(array[:, 0], array[:, 1], label="t = 14 Gyr (20)")

# plt.ylabel("average density of total DM (Mo / kpc^3)")
# plt.title("v_k = 30 km / s, tau = 6.93 Gyr, initCoreT = 5e5 K, initBarRho_0 = 1e9 Mo / kpc^3")
# plt.xlabel("radius (kpc)")
# # plt.xlim(0, 1.4)
# # plt.ylim(0, 1.1e9)
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()


# ######################## orbital v
# array = np.loadtxt("dmOnly_compare_MDadia_DadiaOn/30_6.93_576_40/T_t=0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="NFW")

# array = np.loadtxt("dmOnly_compare_MDadia_DadiaOn/30_6.93_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="without baryon")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="with baryon")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK_withIter/30_6.93_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="with baryon (with iter)", linestyle="dashed")

# # array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_20/BhiRes_t=14.0.txt")
# # plt.plot(array[:, 0], array[:, 1], label="t = 14 Gyr (20)")

# plt.ylabel("orbital velocity (km / s)")
# plt.title("v_k = 30 km / s, tau = 6.93 Gyr, initCoreT = 5e5 K, initBarRho_0 = 1e9 Mo / kpc^3")
# plt.xlabel("radius (kpc)")
# # plt.xlim(0, 1.4)
# # plt.ylim(0, 1.1e9)
# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()


# ####################### baryon density many
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_40/BhiRes_t=0.txt")
# plt.plot(array[:, 0], array[:, 1], label="t = 0 Gyr")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/20_3_576_40/BhiRes_t=14.0.txt")
# plt.plot(array[:, 0], array[:, 1], label="(20, 3)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/20_6.39_576_40/BhiRes_t=14.0.txt")
# plt.plot(array[:, 0], array[:, 1], label="(20, 6.93)")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_3_576_40/BhiRes_t=14.0.txt")
# plt.plot(array[:, 0], array[:, 1], label="(30, 3)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_40/BhiRes_t=14.0.txt")
# plt.plot(array[:, 0], array[:, 1], label="(30, 6.93)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_14_576_40/BhiRes_t=14.0.txt")
# plt.plot(array[:, 0], array[:, 1], label="(30, 14)")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/40_3_576_40/BhiRes_t=14.0.txt")
# plt.plot(array[:, 0], array[:, 1], label="(40, 3)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/40_6.93_576_40/BhiRes_t=14.0.txt")
# plt.plot(array[:, 0], array[:, 1], label="(40, 6.93)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/40_14_576_40/BhiRes_t=14.0.txt")
# plt.plot(array[:, 0], array[:, 1], label="(40, 14)")


# # array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_20/BhiRes_t=14.0.txt")
# # plt.plot(array[:, 0], array[:, 1], label="t = 14 Gyr (20)")

# plt.ylabel("shell density of baryon (Mo / kpc^3)")
# plt.title("(v_k in km / s, tau in Gyr) at t = 14 Gyr, initCoreT = 5e5 K, initBarRho_0 = 1e9 Mo / kpc^3")
# plt.xlabel("radius (kpc)")
# plt.xlim(0, 1.4)
# plt.ylim(0, 1.1e9)
# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()


# ######################## dm density many
# array = np.loadtxt("dmOnly_compare_MDadia_DadiaOn/30_6.93_576_40/T_t=0.txt")
# plt.plot(array[:, 1], array[:, 6], label="NFW")


# array = np.loadtxt("withBar_test_aIndex_1.67_constK/20_3_576_40/TDM_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="(20, 3)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/20_6.39_576_40/TDM_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="(20, 6.93)")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_3_576_40/TDM_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="(30, 3)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_40/TDM_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="(30, 6.93)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_14_576_40/TDM_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="(30, 14)")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/40_3_576_40/TDM_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="(40, 3)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/40_6.93_576_40/TDM_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="(40, 6.93)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/40_14_576_40/TDM_t=14.0.txt")
# plt.plot(array[:, 1], array[:, 6], label="(40, 14)")


# # array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_20/BhiRes_t=14.0.txt")
# # plt.plot(array[:, 0], array[:, 1], label="t = 14 Gyr (20)")

# plt.ylabel("average density of total DM (Mo / kpc^3)")
# plt.title("(v_k in km / s, tau in Gyr) at t = 14 Gyr with baryon, initCoreT = 5e5 K, initBarRho_0 = 1e9 Mo / kpc^3")
# plt.xlabel("radius (kpc)")
# # plt.xlim(0, 1.4)
# # plt.ylim(0, 1.1e9)
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()


# ######################## orbital v many
# array = np.loadtxt("dmOnly_compare_MDadia_DadiaOn/30_6.93_576_40/T_t=0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="NFW")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/20_3_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(20, 3)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/20_6.39_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(20, 6.93)")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_3_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(30, 3)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_6.93_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(30, 6.93)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/30_14_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(30, 14)")

# array = np.loadtxt("withBar_test_aIndex_1.67_constK/40_3_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(40, 3)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/40_6.93_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(40, 6.93)")
# array = np.loadtxt("withBar_test_aIndex_1.67_constK/40_14_576_40/T_t=14.0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(40, 14)")


# plt.ylabel("orbital velocity (km / s)")
# plt.title("(v_k in km / s, tau in Gyr) at t = 14 Gyr with baryon, initCoreT = 5e5 K, initBarRho_0 = 1e9 Mo / kpc^3")
# plt.xlabel("radius (kpc)")
# # plt.xlim(0, 1.4)
# # plt.ylim(0, 1.1e9)
# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()














# array = np.loadtxt("withBar_baryonEffectIter=0/30_6.93_576_40/BhiRes_t=0.txt")
# plt.plot(array[:, 0], array[:, 1], label="init", linestyle="dashed")

# array = np.loadtxt("withBar_baryonEffectIter=0/30_6.93_576_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="0")

# array = np.loadtxt("withBar_baryonEffectIter=1/30_6.93_576_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="1")

# array = np.loadtxt("withBar_baryonEffectIter=2/30_6.93_576_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="2")

# array = np.loadtxt("withBar_baryonEffectIter=5/30_6.93_576_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="5")

# array = np.loadtxt("withBar_baryonEffectIter=10/30_6.93_576_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="10")

# array = np.loadtxt("withBar_baryonEffectIter=20/30_6.93_576_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="20")

# plt.ylabel("shell density of baryon (Mo / kpc^3)")
# plt.title("v_k = 30 km / s, tau = 6.93 Gyr at t = 14 Gyr, initCoreT = 5e5 K, initBarRho_0 = 1e9 Mo / kpc^3")
# plt.xlabel("radius (kpc)")
# # plt.xlim(0, 1.4)
# # plt.ylim(0, 1.1e9)
# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()


# array = np.loadtxt("dmOnly_baryonEffectIter=dmOnlyControl/30_6.93_576_40/T_t=0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="NFW", linestyle="dashed")

# array = np.loadtxt("dmOnly_baryonEffectIter=dmOnlyControl/30_6.93_576_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="dmOnly", linestyle="dotted")

# array = np.loadtxt("withBar_baryonEffectIter=0/30_6.93_576_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="0")

# array = np.loadtxt("withBar_baryonEffectIter=1/30_6.93_576_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="1")

# array = np.loadtxt("withBar_baryonEffectIter=2/30_6.93_576_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="2")

# array = np.loadtxt("withBar_baryonEffectIter=5/30_6.93_576_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="5")

# array = np.loadtxt("withBar_baryonEffectIter=10/30_6.93_576_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="10")

# array = np.loadtxt("withBar_baryonEffectIter=20/30_6.93_576_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="20")

# plt.ylabel("orbital velocity (km / s)")
# plt.title("v_k = 30 km / s, tau = 6.93 Gyr at t = 14 Gyr, initCoreT = 5e5 K, initBarRho_0 = 1e9 Mo / kpc^3")
# plt.xlabel("radius (kpc)")
# plt.xlim(0, 50)
# plt.ylim(0, 70)
# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()


# array = np.loadtxt("dmOnly_baryonEffectIter=dmOnlyControl/30_6.93_576_40/T_t=0.txt")
# plt.plot(array[:, 1], array[:, 6], label="NFW", linestyle="dashed")

# array = np.loadtxt("dmOnly_baryonEffectIter=dmOnlyControl/30_6.93_576_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="dmOnly_1e-5", linestyle="dotted")

# array = np.loadtxt("dmOnly/30_6.93_116_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="dmOnly_lowRes_1e-1", linestyle="dotted")

# array = np.loadtxt("dmOnly/30_6.93_227_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="dmOnly_lowRes_1e-2", linestyle="dotted")

# array = np.loadtxt("dmOnly/30_6.93_343_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="dmOnly_lowRes_1e-3", linestyle="dotted")

# array = np.loadtxt("dmOnly/30_6.93_459_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="dmOnly_lowRes_1e-4", linestyle="dotted")

# array = np.loadtxt("withBar_baryonEffectIter=0/30_6.93_576_40/TDM_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="0")

# array = np.loadtxt("withBar_baryonEffectIter=1/30_6.93_576_40/TDM_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="1")

# array = np.loadtxt("withBar_baryonEffectIter=2/30_6.93_576_40/TDM_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="2")

# array = np.loadtxt("withBar_baryonEffectIter=5/30_6.93_576_40/TDM_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="5")

# array = np.loadtxt("withBar_baryonEffectIter=10/30_6.93_576_40/TDM_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="10")

# array = np.loadtxt("withBar_baryonEffectIter=20/30_6.93_576_40/TDM_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="20")

# plt.ylabel("average density of DM (Mo / kpc^3)")
# plt.title("v_k = 30 km / s, tau = 6.93 Gyr at t = 14 Gyr, initCoreT = 5e5 K, initBarRho_0 = 1e9 Mo / kpc^3")
# plt.xlabel("radius (kpc)")
# plt.xlim(1e-1, 50)
# plt.ylim(1e4, 1e9)
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()








# array = np.loadtxt("withBar_withoutIter/30_6.93_493_40/T_t=0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="withBar, t=0")
# array = np.loadtxt("withBar_withoutIter/30_6.93_493_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="withBar_withoutIter, t=14")
# array = np.loadtxt("withBar_withIter/30_6.93_493_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="withBar_withIter, t=14")

# array = np.loadtxt("withBar_withoutIter/30_6.93_493_40/TDM_t=0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="withoutBar, t=0 (NFW)")
# array = np.loadtxt("dmOnly/30_6.93_493_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="withoutBar, t=14")




# plt.ylabel("orbital velocity (km / s)")
# plt.title("v_k = 30 km / s, tau = 6.93 Gyr")
# plt.xlabel("radius (kpc)")
# # plt.xlim(1e-1, 50)
# # plt.ylim(1e4, 1e9)
# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()


# array = np.loadtxt("withBar_withoutIter/30_6.93_493_40/TDM_t=0.txt")
# plt.plot(array[:, 1], array[:, 6], label="withBar, t=0")
# array = np.loadtxt("withBar_withoutIter/30_6.93_493_40/TDM_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="withBar_withoutIter, t=14")
# array = np.loadtxt("withBar_withIter/30_6.93_493_40/TDM_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="withBar_withIter, t=14")

# array = np.loadtxt("withBar_withoutIter/30_6.93_493_40/TDM_t=0.txt")
# plt.plot(array[:, 1], array[:, 6], label="withoutBar, t=0 (NFW)")
# array = np.loadtxt("dmOnly/30_6.93_493_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="withoutBar, t=14")




# plt.ylabel("DM density (km / s)")
# plt.title("v_k = 30 km / s, tau = 6.93 Gyr")
# plt.xlabel("radius (kpc)")
# # plt.xlim(1e-1, 50)
# # plt.ylim(1e4, 1e9)
# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()


# array = np.loadtxt("withBar_withoutIter/30_6.93_493_40/GPE_t=0.txt")
# plt.plot(array[:, 2], (-array[:, 3] * 2)**0.5*kpc/1000, label="withBar, t=0")
# array = np.loadtxt("withBar_withoutIter/30_6.93_493_40/GPE_result.txt")
# plt.plot(array[:, 2], (-array[:, 3] * 2)**0.5*kpc/1000, label="withBar_withoutIter, t=14")
# array = np.loadtxt("withBar_withIter/30_6.93_493_40/GPE_result.txt")
# plt.plot(array[:, 2], (-array[:, 3] * 2)**0.5*kpc/1000, label="withBar_withIter, t=14")

# array = np.loadtxt("withBar_withoutIter/30_6.93_493_40/GPE_t=0.txt")
# plt.plot(array[:, 2], (-array[:, 3] * 2)**0.5*kpc/1000, label="withoutBar, t=0 (NFW)")
# array = np.loadtxt("dmOnly/30_6.93_493_40/GPE_result.txt")
# plt.plot(array[:, 2], (-array[:, 3] * 2)**0.5*kpc/1000, label="withoutBar, t=14")




# plt.ylabel("escape velocity (km / s)")
# plt.title("v_k = 30 km / s, tau = 6.93 Gyr")
# plt.xlabel("radius (kpc)")
# # plt.xlim(1e-1, 50)
# # plt.ylim(1e4, 1e9)
# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()


# array = np.loadtxt("dmOnly_DDO161/40_3_261_40/T_t=0.txt")
# plt.plot(array[:, 1], array[:, 6], label="NFW")

# array = np.loadtxt("dmOnly_DDO161/40_3_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(40, 3)")
# array = np.loadtxt("dmOnly_DDO161/40_7_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(40, 7)")
# array = np.loadtxt("dmOnly_DDO161/40_14_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(40, 14)")

# array = np.loadtxt("dmOnly_DDO161/60_3_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(60, 3)")
# array = np.loadtxt("dmOnly_DDO161/60_7_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(60, 14)")
# array = np.loadtxt("dmOnly_DDO161/60_14_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(60, 14)")

# array = np.loadtxt("dmOnly_DDO161/80_3_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(80, 3)")
# array = np.loadtxt("dmOnly_DDO161/80_7_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(80, 7)")
# array = np.loadtxt("dmOnly_DDO161/80_14_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(80, 14)")

# array = np.loadtxt("dmOnly_DDO161/200_3_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(200, 3)")
# array = np.loadtxt("dmOnly_DDO161/200_7_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(200, 7)")
# array = np.loadtxt("dmOnly_DDO161/200_14_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(200, 14)")

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# array = np.loadtxt("withBar_withoutIter_DDO161/40_3_261_40/T_t=0.txt")
# plt.plot(array[:, 1], array[:, 6], label="NFW")

# array = np.loadtxt("withBar_withoutIter_DDO161/40_3_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(40, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/40_7_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(40, 7)")
# array = np.loadtxt("withBar_withoutIter_DDO161/40_14_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(40, 14)")

# array = np.loadtxt("withBar_withoutIter_DDO161/60_3_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(60, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/60_7_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(60, 14)")
# array = np.loadtxt("withBar_withoutIter_DDO161/60_14_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(60, 14)")

# array = np.loadtxt("withBar_withoutIter_DDO161/80_3_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(80, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/80_7_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(80, 7)")
# array = np.loadtxt("withBar_withoutIter_DDO161/80_14_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(80, 14)")

# array = np.loadtxt("withBar_withoutIter_DDO161/200_3_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(200, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/200_7_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(200, 7)")
# array = np.loadtxt("withBar_withoutIter_DDO161/200_14_261_40/T_result.txt")
# plt.plot(array[:, 1], array[:, 6], label="(200, 14)")

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# array = np.loadtxt("withBar_withoutIter_DDO161/40_3_261_40/BhiRes_t=0.txt")
# plt.plot(array[:, 0], array[:, 1], label="NFW")

# array = np.loadtxt("withBar_withoutIter_DDO161/40_3_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(40, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/40_7_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(40, 7)")
# array = np.loadtxt("withBar_withoutIter_DDO161/40_14_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(40, 14)")

# array = np.loadtxt("withBar_withoutIter_DDO161/60_3_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(60, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/60_7_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(60, 14)")
# array = np.loadtxt("withBar_withoutIter_DDO161/60_14_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(60, 14)")

# array = np.loadtxt("withBar_withoutIter_DDO161/80_3_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(80, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/80_7_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(80, 7)")
# array = np.loadtxt("withBar_withoutIter_DDO161/80_14_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(80, 14)")

# array = np.loadtxt("withBar_withoutIter_DDO161/200_3_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(200, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/200_7_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(200, 7)")
# array = np.loadtxt("withBar_withoutIter_DDO161/200_14_261_40/BhiRes_result.txt")
# plt.plot(array[:, 0], array[:, 1], label="(200, 14)")

# plt.yscale("log")
# plt.xscale("log")
# plt.legend()
# plt.show()

# array = np.loadtxt("withBar_withoutIter_DDO161/40_3_261_40/T_t=0.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="NFW")

# array = np.loadtxt("withBar_withoutIter_DDO161/40_3_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(40, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/40_7_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(40, 7)")
# array = np.loadtxt("withBar_withoutIter_DDO161/40_14_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(40, 14)")

# array = np.loadtxt("withBar_withoutIter_DDO161/60_3_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(60, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/60_7_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(60, 14)")
# array = np.loadtxt("withBar_withoutIter_DDO161/60_14_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(60, 14)")

# array = np.loadtxt("withBar_withoutIter_DDO161/80_3_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(80, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/80_7_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(80, 7)")
# array = np.loadtxt("withBar_withoutIter_DDO161/80_14_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(80, 14)")

# array = np.loadtxt("withBar_withoutIter_DDO161/200_3_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(200, 3)")
# array = np.loadtxt("withBar_withoutIter_DDO161/200_7_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(200, 7)")
# array = np.loadtxt("withBar_withoutIter_DDO161/200_14_261_40/T_result.txt")
# plt.plot(array[:, 1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="(200, 14)")

# # plt.yscale("log")
# # plt.xscale("log")
# plt.legend()
# plt.show()






















# lw=1

# array = np.loadtxt("dmOnly_DDO161/30_3_377_20/T_t=0.txt")
# plt.plot(array[:,1], array[:,6], label="NFW", lw=lw)

# array = np.loadtxt("dmOnly_DDO161/30_3_377_20/T_result.txt")
# plt.plot(array[:,1], array[:,6], label="30, 3", lw=lw)

# array = np.loadtxt("withBar_DDO161/30_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="30, 3; with baryon", lw=lw)

# array = np.loadtxt("withBar_withIter_DDO161/30_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="30, 3; with baryon with iter", linestyle="dashed", lw=lw)

# array = np.loadtxt("dmOnly_DDO161/70_3_377_20/T_result.txt")
# plt.plot(array[:,1], array[:,6], label="70, 3", lw=lw)

# array = np.loadtxt("withBar_DDO161/70_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="70, 3; with baryon", lw=lw)

# array = np.loadtxt("withBar_withIter_DDO161/70_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="70, 3; with baryon with iter", linestyle="dashed", lw=lw)

# # array = np.loadtxt("dmOnly_DDO161/30_3_377_20/T_result.txt")
# # plt.plot(array[:,1], array[:,6], label="30, 3")

# # array = np.loadtxt("dmOnly_DDO161/40_3_377_20/T_result.txt")
# # plt.plot(array[:,1], array[:,6], label="40, 3")

# plt.yscale("log")
# plt.xscale("log")
# plt.xlim(0.5, 100)
# plt.ylim(1e4, 1e8)
# # plt.legend()
# plt.show()















# array = np.loadtxt("withBar_DDO161/50_3_377_20/BhiRes_t=0.txt")
# plt.plot(array[:,0], array[:,1]/10**6, label="Initial", lw=1, linestyle="dotted", color="blue")

# # array = np.loadtxt("withBar_DDO161/50_3_377_20/BhiRes_t=0.7.txt")
# # plt.plot(array[:,0], array[:,1]/10**6, label="t = 0.7 Gyr", lw=1, color="blue")
# # array = np.loadtxt("withBar_withIter_DDO161/50_3_377_20/BhiRes_t=0.7.txt")
# # plt.plot(array[:,0], array[:,1]/10**6, label="t = 0.7 Gyr (w/ iter.)", linestyle="dashed", lw=1, color="green")

# # array = np.loadtxt("withBar_DDO161/50_3_377_20/BhiRes_t=3.5.txt")
# # plt.plot(array[:,0], array[:,1]/10**6, label="t = 3.5 Gyr", lw=1.7, color="blue")
# # array = np.loadtxt("withBar_withIter_DDO161/50_3_377_20/BhiRes_t=3.5.txt")
# # plt.plot(array[:,0], array[:,1]/10**6, label="t = 3.5 Gyr (w/ iter.)", linestyle="dashed", lw=1.7, color="green")

# # array = np.loadtxt("withBar_DDO161/50_3_377_20/BhiRes_result.txt")
# # plt.plot(array[:,0], array[:,1]/10**6, label="t = 14 Gyr", lw=4, color="blue")
# # array = np.loadtxt("withBar_withIter_DDO161/50_3_377_20/BhiRes_result.txt")
# # plt.plot(array[:,0], array[:,1]/10**6, label="t = 14 Gyr (w/ iter.)", linestyle="dashed", lw=4, color="green")

# plt.ticklabel_format(axis='y', style="sci", scilimits=(0,0))


# plt.ylabel(r'Baryon density $\rho_B$ [10$^6$ M$_{\odot}$ kpc$^{-3}$]')
# plt.xlabel(r'Radius r [kpc]')
# plt.legend()
# plt.show()




# array = np.loadtxt("withBar_DDO161/50_3_377_20/TDM_t=0.txt")
# plt.plot(array[:,1], array[:,6], label="NFW", color="black", linestyle="dotted", lw=1.5)

# array = np.loadtxt("dmOnly_DDO161/50_3_377_20/T_result.txt")
# plt.plot(array[:,1], array[:,6], label="DM only", color="black", lw=1.5)

# array = np.loadtxt("withBar_DDO161/50_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="w/ baryons", color="blue", lw=1.5)

# array = np.loadtxt("withBar_withIter_DDO161/50_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="w/ baryons & iter.", color="green", linestyle="dashed", lw=1.5)

# plt.ylabel(r'DM density $\rho_{DM}$ [M$_{\odot}$ kpc$^{-3}$]')
# plt.xlabel(r'Radius r [kpc]')
# plt.xscale("log")
# plt.yscale("log")
# plt.ylim(1e4, 1e8)
# plt.xlim(0.5, 100)
# plt.legend()
# plt.show()








# array = np.loadtxt("withBar_DDO161/50_3_377_20/TDM_t=0.txt")
# plt.plot(array[:,1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="NFW (DM only)", linestyle="dotted", color="black")

# array = np.loadtxt("withBar_DDO161/50_3_377_20/T_t=0.txt")
# plt.plot(array[:,1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="w/ baryons (initial)", linestyle="dotted", color="blue")
# array = np.loadtxt("withBar_DDO161/50_3_377_20/B_t=0.txt")
# plt.plot(array[:,1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, linestyle="dotted", color="red")

# array = np.loadtxt("withBar_DDO161/50_3_377_20/T_result.txt")
# plt.plot(array[:,1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="w/ baryons (at 14 Gyr)", color="blue")
# array = np.loadtxt("withBar_DDO161/50_3_377_20/B_result.txt")
# plt.plot(array[:,1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, color="red")

# array = np.loadtxt("withBar_withIter_DDO161/50_3_377_20/T_result.txt")
# plt.plot(array[:,1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, label="w/ baryons & iter. (at 14 Gyr)", linestyle="dashed", color="green")
# array = np.loadtxt("withBar_withIter_DDO161/50_3_377_20/B_result.txt")
# plt.plot(array[:,1], ((G*array[:, 5]/array[:, 1])**(0.5))*kpc/1000, linestyle="dashed", color="red")

# plt.ylabel(r'Orbital velocity [km s$^{-1}$]')
# plt.xlabel(r'Radius r [kpc]')
# plt.ylim(0, 70)
# plt.xlim(0, 15)
# plt.legend()
# plt.show()



# array = np.loadtxt("withBar_DDO161/50_3_377_20/GPE_t=0.txt")
# plt.plot(array[:,1], array[:,3]/10**(-29), label="Initial", lw=1, linestyle="dotted", color="blue")

# # array = np.loadtxt("withBar_DDO161/50_3_377_20/GPE_t=0.7.txt")
# # plt.plot(array[:,1], array[:,3]/10**(-29), label="t = 0.7 Gyr", lw=1, color="blue")
# # array = np.loadtxt("withBar_withIter_DDO161/50_3_377_20/GPE_t=0.7.txt")
# # plt.plot(array[:,1], array[:,3]/10**(-29), label="t = 0.7 Gyr (w/ iter.)", linestyle="dashed", lw=1, color="green")

# array = np.loadtxt("withBar_DDO161/50_3_377_20/GPE_t=3.5.txt")
# plt.plot(array[:,1], array[:,3]/10**(-29), label="t = 3.5 Gyr", lw=1.7, color="blue")
# # array = np.loadtxt("withBar_withIter_DDO161/50_3_377_20/GPE_t=3.5.txt")
# # plt.plot(array[:,1], array[:,3]/10**(-29), label="t = 3.5 Gyr (w/ iter.)", linestyle="dashed", lw=1.7, color="green")

# # array = np.loadtxt("withBar_DDO161/50_3_377_20/GPE_result.txt")
# # plt.plot(array[:,1], array[:,3]/10**(-29), label="t = 14 Gyr", lw=4, color="blue")
# # array = np.loadtxt("withBar_withIter_DDO161/50_3_377_20/GPE_result.txt")
# # plt.plot(array[:,1], array[:,3]/10**(-29), label="t = 14 Gyr (w/ iter.)", linestyle="dashed", lw=4, color="green")

# # plt.ticklabel_format(axis='y', style="sci", scilimits=(0,0))


# plt.ylabel(r'Gravitational potential [10$^{-29}$ kpc$^2$ s$^{-2}$]')
# plt.xlabel(r'Radius r [kpc]')
# # plt.xscale("log")
# plt.xlim(5, 100)
# plt.ylim(-1.8, 0)
# plt.legend()
# plt.show()







# array = np.loadtxt("withBar_DDO161/50_3_377_20/TDM_t=0.txt")
# plt.plot(array[:,1], array[:,6], label="NFW", color="black", linestyle="dotted", lw=1.5)

# array = np.loadtxt("dmOnly_DDO161/50_3_377_20/T_result.txt")
# plt.plot(array[:,1], array[:,6], label="DM only", color="black", lw=1.5)

# array = np.loadtxt("withBar_DDO161/50_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="w/ baryons", color="blue", lw=1.5)

# array = np.loadtxt("withBar_withIter_DDO161/50_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="w/ baryons & iter.", color="green", linestyle="dashed", lw=1.5)

# plt.ylabel(r'DM density $\rho_{DM}$ [M$_{\odot}$ kpc$^{-3}$]')
# plt.xlabel(r'Radius r [kpc]')
# plt.xscale("log")
# plt.yscale("log")
# plt.ylim(1e4, 1e8)
# plt.xlim(0.5, 100)
# plt.legend()
# plt.show()







# array = np.loadtxt("withBar_DDO161/50_3_377_20/TDM_t=0.txt")
# plt.plot(array[:,1], array[:,6], label="NFW", color="black", linestyle="dotted", lw=1.5)

# array = np.loadtxt("dmOnly_DDO161/30_3_377_20/T_result.txt")
# plt.plot(array[:,1], array[:,6], label="DM only (30)", color="black", lw=1)

# array = np.loadtxt("withBar_DDO161/30_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="w/ baryons (30)", color="blue", lw=1)

# array = np.loadtxt("withBar_withIter_DDO161/30_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="w/ baryons & iter. (30)", color="green", linestyle="dashed", lw=1)

# array = np.loadtxt("dmOnly_DDO161/70_3_377_20/T_result.txt")
# plt.plot(array[:,1], array[:,6], label="DM only (70)", color="black", lw=2.5)

# array = np.loadtxt("withBar_DDO161/70_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="w/ baryons (70)", color="blue", lw=2.5)

# array = np.loadtxt("withBar_withIter_DDO161/70_3_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="w/ baryons & iter. (70)", color="green", linestyle="dashed", lw=2.5)

# plt.ylabel(r'DM density $\rho_{DM}$ [M$_{\odot}$ kpc$^{-3}$]')
# plt.xlabel(r'Radius r [kpc]')
# plt.xscale("log")
# plt.yscale("log")
# plt.ylim(1e4, 1e8)
# plt.xlim(0.5, 100)
# plt.legend()
# plt.show()





# array = np.loadtxt("withBar_DDO161/50_3_377_20/TDM_t=0.txt")
# plt.plot(array[:,1], array[:,6], label="NFW", color="black", linestyle="dotted", lw=1.5)

# array = np.loadtxt("dmOnly_DDO161/50_3_377_20/T_result.txt")
# plt.plot(array[:,1], array[:,6], label="DM only (50, 3)", color="black", lw=1.5)

# array = np.loadtxt("withBar_DDO161/56_2.9_377_20/TDM_result.txt")
# plt.plot(array[:,1], array[:,6], label="w/ baryons (56, 2.9)", color="blue", lw=1.5)

# plt.ylabel(r'DM density $\rho_{DM}$ [M$_{\odot}$ kpc$^{-3}$]')
# plt.xlabel(r'Radius r [kpc]')
# plt.xscale("log")
# plt.yscale("log")
# plt.ylim(1e4, 1e8)
# plt.xlim(0.5, 100)
# plt.legend()
# plt.show()




