import random

import matplotlib.pyplot as plt
import numpy as np

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


index = ["0", "0.7", "2.1", "2.8", "4.9", "7.0", "9.1", "11.2", "13.3", "14.0"]

for i in index:

    
    arrayTDM = np.loadtxt("withBar/50_3_459_20/TDM_t="+i+".txt")
    arrayB = np.loadtxt("withBar/50_3_459_20/B_t="+i+".txt")
    arrayT = np.loadtxt("withBar/50_3_459_20/T_t="+i+".txt")


    plt.plot(arrayTDM[:, 2], arrayTDM[:, 6], label="total DM"+i)
    plt.plot(arrayB[:, 2], arrayB[:, 6], label="baryon"+i)
    plt.plot(arrayT[:, 2], arrayT[:, 6], label="total"+i)

    # plt.ylabel("total average density (Mo / kpc^3)")
    plt.ylabel("average density (Mo / kpc^3)")
    plt.xlabel("radius kpc")
    plt.yscale("log")
    plt.xscale("log")
    plt.legend()
    plt.show()