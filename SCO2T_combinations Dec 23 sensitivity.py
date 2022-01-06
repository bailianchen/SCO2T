# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 08:53:50 2021

@author: 347484
"""

# import openpyxl
import pandas as pd
# import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from pyDOE import *
from functions import random_list

# from functions import ROM_A_Pressure_Injection_30yr  
# from functions import ROM_B_Pressure_Injection_30yr  
# from functions import ROM_C_Pressure_Injection_30yr  
# from functions import ROM_D_Pressure_Injection_30yr  
# from functions import ROM_E_Pressure_Injection_30yr  
# from functions import ROM_F_Pressure_Injection_30yr  
# from functions import ROM_G_Pressure_Injection_30yr  
  
# from functions import ROM_0_Pressure_LogInjection_30yr
# from functions import ROM_1_Pressure_LogInjection_30yr
# from functions import ROM_2_Pressure_LogInjection_30yr
# from functions import ROM_3_Pressure_LogInjection_30yr
# from functions import ROM_4_Pressure_LogInjection_30yr
# from functions import ROM_5_Pressure_LogInjection_30yr
# from functions import ROM_6_Pressure_LogInjection_30yr
# from functions import ROM_7_Pressure_LogInjection_30yr
  
# from functions import ROM_1_Pressure_LogArea_30yr    
# from functions import ROM_2_Pressure_LogArea_30yr    
# from functions import ROM_3_Pressure_LogArea_30yr    
# from functions import ROM_4_Pressure_LogArea_30yr  

from functions import ROM_1_LogMCO2_5yr
from functions import ROM_2_LogMCO2_5yr
from functions import ROM_3_LogMCO2_5yr
from functions import ROM_4_LogMCO2_5yr
from functions import ROM_5_LogMCO2_5yr
from functions import ROM_6_LogMCO2_5yr
from functions import ROM_7_LogMCO2_5yr

from functions import ROM_1_LogMCO2_10yr
from functions import ROM_2_LogMCO2_10yr
from functions import ROM_3_LogMCO2_10yr
from functions import ROM_4_LogMCO2_10yr
from functions import ROM_5_LogMCO2_10yr
from functions import ROM_6_LogMCO2_10yr
from functions import ROM_7_LogMCO2_10yr

from functions import ROM_1_LogMCO2_15yr
from functions import ROM_2_LogMCO2_15yr
from functions import ROM_3_LogMCO2_15yr
from functions import ROM_4_LogMCO2_15yr
from functions import ROM_5_LogMCO2_15yr
from functions import ROM_6_LogMCO2_15yr
from functions import ROM_7_LogMCO2_15yr

from functions import ROM_1_LogMCO2_20yr
from functions import ROM_2_LogMCO2_20yr
from functions import ROM_3_LogMCO2_20yr
from functions import ROM_4_LogMCO2_20yr
from functions import ROM_5_LogMCO2_20yr
from functions import ROM_6_LogMCO2_20yr
from functions import ROM_7_LogMCO2_20yr

from functions import ROM_1_LogMCO2_25yr
from functions import ROM_2_LogMCO2_25yr
from functions import ROM_3_LogMCO2_25yr
from functions import ROM_4_LogMCO2_25yr
from functions import ROM_5_LogMCO2_25yr
from functions import ROM_6_LogMCO2_25yr
from functions import ROM_7_LogMCO2_25yr

from functions import ROM_1_LogMCO2_30yr
from functions import ROM_2_LogMCO2_30yr
from functions import ROM_3_LogMCO2_30yr
from functions import ROM_4_LogMCO2_30yr
from functions import ROM_5_LogMCO2_30yr
from functions import ROM_6_LogMCO2_30yr
from functions import ROM_7_LogMCO2_30yr

from functions import ROM_1_LogMCO2_35yr
from functions import ROM_2_LogMCO2_35yr
from functions import ROM_3_LogMCO2_35yr
from functions import ROM_4_LogMCO2_35yr
from functions import ROM_5_LogMCO2_35yr
from functions import ROM_6_LogMCO2_35yr
from functions import ROM_7_LogMCO2_35yr

from functions import ROM_1_LogMCO2_40yr
from functions import ROM_2_LogMCO2_40yr
from functions import ROM_3_LogMCO2_40yr
from functions import ROM_4_LogMCO2_40yr
from functions import ROM_5_LogMCO2_40yr
from functions import ROM_6_LogMCO2_40yr
from functions import ROM_7_LogMCO2_40yr

from functions import ROM_1_LogMCO2_45yr
from functions import ROM_2_LogMCO2_45yr
from functions import ROM_3_LogMCO2_45yr
from functions import ROM_4_LogMCO2_45yr
from functions import ROM_5_LogMCO2_45yr
from functions import ROM_6_LogMCO2_45yr
from functions import ROM_7_LogMCO2_45yr

from functions import ROM_1_LogMCO2_50yr
from functions import ROM_2_LogMCO2_50yr
from functions import ROM_3_LogMCO2_50yr
from functions import ROM_4_LogMCO2_50yr
from functions import ROM_5_LogMCO2_50yr
from functions import ROM_6_LogMCO2_50yr
from functions import ROM_7_LogMCO2_50yr

from functions import ROM_1_LogArea_5yr
from functions import ROM_2_LogArea_5yr
from functions import ROM_3_LogArea_5yr
from functions import ROM_4_LogArea_5yr
from functions import ROM_5_LogArea_5yr
from functions import ROM_6_LogArea_5yr
from functions import ROM_7_LogArea_5yr

from functions import ROM_1_LogArea_10yr
from functions import ROM_2_LogArea_10yr
from functions import ROM_3_LogArea_10yr
from functions import ROM_4_LogArea_10yr
from functions import ROM_5_LogArea_10yr
from functions import ROM_6_LogArea_10yr
from functions import ROM_7_LogArea_10yr

from functions import ROM_1_LogArea_15yr
from functions import ROM_2_LogArea_15yr
from functions import ROM_3_LogArea_15yr
from functions import ROM_4_LogArea_15yr
from functions import ROM_5_LogArea_15yr
from functions import ROM_6_LogArea_15yr
from functions import ROM_7_LogArea_15yr

from functions import ROM_1_LogArea_20yr
from functions import ROM_2_LogArea_20yr
from functions import ROM_3_LogArea_20yr
from functions import ROM_4_LogArea_20yr
from functions import ROM_5_LogArea_20yr
from functions import ROM_6_LogArea_20yr
from functions import ROM_7_LogArea_20yr

from functions import ROM_1_LogArea_25yr
from functions import ROM_2_LogArea_25yr
from functions import ROM_3_LogArea_25yr
from functions import ROM_4_LogArea_25yr
from functions import ROM_5_LogArea_25yr
from functions import ROM_6_LogArea_25yr
from functions import ROM_7_LogArea_25yr

from functions import ROM_1_LogArea_30yr
from functions import ROM_2_LogArea_30yr
from functions import ROM_3_LogArea_30yr
from functions import ROM_4_LogArea_30yr
from functions import ROM_5_LogArea_30yr
from functions import ROM_6_LogArea_30yr
from functions import ROM_7_LogArea_30yr

from functions import ROM_1_LogArea_35yr
from functions import ROM_2_LogArea_35yr
from functions import ROM_3_LogArea_35yr
from functions import ROM_4_LogArea_35yr
from functions import ROM_5_LogArea_35yr
from functions import ROM_6_LogArea_35yr
from functions import ROM_7_LogArea_35yr

from functions import ROM_1_LogArea_40yr
from functions import ROM_2_LogArea_40yr
from functions import ROM_3_LogArea_40yr
from functions import ROM_4_LogArea_40yr
from functions import ROM_5_LogArea_40yr
from functions import ROM_6_LogArea_40yr
from functions import ROM_7_LogArea_40yr

from functions import ROM_1_LogArea_45yr
from functions import ROM_2_LogArea_45yr
from functions import ROM_3_LogArea_45yr
from functions import ROM_4_LogArea_45yr
from functions import ROM_5_LogArea_45yr
from functions import ROM_6_LogArea_45yr
from functions import ROM_7_LogArea_45yr

from functions import ROM_1_LogArea_50yr
from functions import ROM_2_LogArea_50yr
from functions import ROM_3_LogArea_50yr
from functions import ROM_4_LogArea_50yr
from functions import ROM_5_LogArea_50yr
from functions import ROM_6_LogArea_50yr
from functions import ROM_7_LogArea_50yr

# Read the input data. The whole format needs to be the same. 

xls=pd.ExcelFile('Input file US data - final.xlsx')
df1=pd.read_excel(xls,'Main cell')
df2=pd.read_excel(xls,'ReservoirData', skiprows = 2)
df3=pd.read_excel(xls,'Range of input parameters', skiprows = 2)

xls2=pd.ExcelFile('LookupTables.xlsx')
xls3=pd.ExcelFile('LookupPolynomials.xlsx')
xls4=pd.ExcelFile('EPA Report_2017.xlsx')

df4=pd.read_excel(xls2,'Sheet1', skiprows = 1)
df5=pd.read_excel(xls3,'Sheet1', skiprows = 1)
df6=pd.read_excel(xls4,'Sheet1')

array1=df1.to_numpy(dtype=None, copy=False)
array2=df2.to_numpy(dtype=None, copy=False)
array3=df3.to_numpy(dtype=None, copy=False)

array4=df4.to_numpy(dtype=None, copy=False)
array5=df5.to_numpy(dtype=None, copy=False)
array6=df6.to_numpy(dtype=None, copy=False)

# Define the range of different input parameters here. 




# The following are input from excel
Method=array1[1,1]
Volumetric_efficiency=array1[8,5]
Interest_Rate=array1[9,5]
Financing_period=array1[10,5]
Capital_charge_factor=array1[11,5]
Water_treatment=array1[12,5]
Water_production_wells=array1[13,5]
Pump_per_well=array1[14,5]
Only_integer=array1[15,5]
Square_Hexagonal=array1[16,5]
Allowable_overlap=array1[17,5]
Plume_ROM=array1[18,5]
Polynomial=array1[19,5]
residualWater=0
pi=3.1415926
Temperature_surface=11
sample_number=int(array3[11,5])
nParams=8
# number=lhs(nParams, samples=sample_number)

if Method == 'Y':
    name=array2[:,1]
    x_lo=array2[:,2]
    y_lo=array2[:,3]   
    Depth=array2[:,4]
    Hydro_P=Depth*9.80665/1000
    Thick=array2[:,6]
    Permeability=array2[:,7]
    Porosity=array2[:,8]
    Geothermal_gradient=array2[:,9]
    Temperature=Geothermal_gradient*Depth/1000+Temperature_surface
    Area=array2[:,11]
    Max_pressure=array2[:,12]
    Max_rate=array2[:,13]
    Injection_period=array2[:,14]
elif Method == 'N':
    x_lo=np.zeros(sample_number*10,dtype=np.float)
    y_lo=np.zeros(sample_number*10,dtype=np.float)
    Depth=np.zeros(sample_number*10,dtype=np.float)
    Hydro_P=np.zeros(sample_number*10,dtype=np.float)
    Thick=np.zeros(sample_number*10,dtype=np.float)
    Permeability=np.zeros(sample_number*10,dtype=np.float)
    Porosity=np.zeros(sample_number*10,dtype=np.float)
    Geothermal_gradient=np.zeros(sample_number*10,dtype=np.float)
    Temperature=np.zeros(sample_number*10,dtype=np.float)
    Area=np.zeros(sample_number*10,dtype=np.float)
    Max_pressure=np.zeros(sample_number*10,dtype=np.float)
    Max_rate=np.zeros(sample_number*10,dtype=np.float)
    lhs_samples = np.zeros((sample_number*10,nParams))
    Depth_min=array3[0,5]
    Depth_max=array3[0,6]
    Hydro_P_min=Depth_min*9.80665/1000
    Hydro_P_max=Depth_max*9.80665/1000
    Thick_min=array3[2,5]
    Thick_max=array3[2,6]
    Permeability_min=array3[3,5]
    Permeability_max=array3[3,6]
    Porosity_min=array3[4,5]
    Porosity_max=array3[4,6]
    Geothermal_gradient_min=array3[5,5]
    Geothermal_gradient_max=array3[5,6]
    Temperature_min=Geothermal_gradient_min*Depth_min/1000+Temperature_surface
    Temperature_max=Geothermal_gradient_max*Depth_min/1000+Temperature_surface
    Area_min=array3[7,5]
    Area_max=array3[7,6]
    Max_pressure_min=array3[8,5]
    Max_pressure_max=array3[8,6]
    Max_rate_min=array3[9,5]
    Max_rate_max=array3[9,6]
    var_min=[Depth_min, Thick_min, Permeability_min, Porosity_min, Geothermal_gradient_min, Area_min,Max_pressure_min, Max_rate_min]
    var_max=[Depth_max, Thick_max, Permeability_max, Porosity_max, Geothermal_gradient_max, Area_max,Max_pressure_max, Max_rate_max]

    for i in range(0, sample_number):
        for j in range(0, nParams):
            lhs_samples_scaled = lhs(nParams, samples=sample_number)
            lhs_samples[i][j] = lhs_samples_scaled[i][j]*(var_max[j]-var_min[j]) + var_min[j]
    
    Injection_period=np.zeros(sample_number*10,dtype=np.float)
    
    for j in range(10):
        for i in range(0, sample_number):
            x_lo[i+j*sample_number]=i
            y_lo[i+j*sample_number]=i   
            Depth[i+j*sample_number]=lhs_samples[i][0]
            Hydro_P[i+j*sample_number]=lhs_samples[i][0]*9.80665/1000
            Thick[i+j*sample_number]=lhs_samples[i][1]
            Permeability[i+j*sample_number]=lhs_samples[i][2]
            Porosity[i+j*sample_number]=lhs_samples[i][3]
            Geothermal_gradient[i+j*sample_number]=lhs_samples[i][4]
            Temperature[i+j*sample_number]=Geothermal_gradient[i]*Depth[i]/1000+Temperature_surface
            Area[i+j*sample_number]=lhs_samples[i][5]
            Max_pressure[i+j*sample_number]=lhs_samples[i][6]
            Max_rate[i+j*sample_number]=lhs_samples[i][7]
            Injection_period[i+j*sample_number]=5+5*j

else:
    print('The inputs in the Input file is improper, please choose Y or N in the main cell of input file. xlsx')


TemperatureLow = (Temperature * 2).astype(int) / 2 
TemperatureHigh = (Temperature * 2+ 1).astype(int) / 2 
PressureLow = (Hydro_P * 4).astype(int) / 4
PressureHigh = (Hydro_P * 4+1).astype(int) / 4
col_1=(TemperatureLow/0.5).astype(int)
col_2=(TemperatureHigh/0.5).astype(int)
row_1=(PressureLow/0.25).astype(int)
row_2=(PressureHigh/0.25).astype(int)

Geothermal_gradient=Geothermal_gradient/1000
Permeability=Permeability*9.86923299999996E-16
   
for i in range (Permeability.shape[0]):
    Permeability[i]=math.log(Permeability[i])/math.log(10)


if (Polynomial == 'N'):
    double1 = array4[row_1, col_1 + 1]      #Lower value 
    double2 = array4[row_1, col_2 + 1]      #Upper value
    splitDouble = (Temperature-TemperatureLow) * 2                    #Weight
    value1 = (double1*(1-splitDouble))+(double2*splitDouble)  #Weighted average value
    #Upper pressure
    double1 = array4[row_2, col_1 + 1]                #Lower value
    double2 = array4[row_2, col_2 + 1]                #Upper value                          
    value2 = (double1 * (1 - splitDouble)) + (double2 * splitDouble)    #Weighted average value
    #Weight the two values across pressure
    splitDouble = (Hydro_P - PressureLow) * 4                      #Weight
    densityCO2 = (value1 * (1 - splitDouble)) + (value2 * splitDouble)    #Weighted average value  
    
    double1 = array4[row_1+244, col_1 + 1]      #Lower value 
    double2 = array4[row_1+244, col_2 + 1]      #Upper value
    splitDouble = (Temperature-TemperatureLow) * 2                    #Weight
    value1 = (double1*(1-splitDouble))+(double2*splitDouble)  #Weighted average value
    #Upper pressure
    double1 = array4[row_2+244, col_1 + 1]                #Lower value
    double2 = array4[row_2+244, col_2 + 1]                #Upper value                          
    value2 = (double1 * (1 - splitDouble)) + (double2 * splitDouble)    #Weighted average value
    #Weight the two values across pressure
    splitDouble = (Hydro_P - PressureLow) * 4                      #Weight
    viscosityCO2 = (value1 * (1 - splitDouble)) + (value2 * splitDouble)    #Weighted average value  
    
    double1 = array4[row_1+488, col_1 + 1]      #Lower value 
    double2 = array4[row_1+488, col_2 + 1]      #Upper value
    splitDouble = (Temperature-TemperatureLow) * 2                    #Weight
    value1 = (double1*(1-splitDouble))+(double2*splitDouble)  #Weighted average value
    #Upper pressure
    double1 = array4[row_2+488, col_1 + 1]                #Lower value
    double2 = array4[row_2+488, col_2 + 1]                #Upper value                          
    value2 = (double1 * (1 - splitDouble)) + (double2 * splitDouble)    #Weighted average value
    #Weight the two values across pressure
    splitDouble = (Hydro_P - PressureLow) * 4                      #Weight
    densityH20 = (value1 * (1 - splitDouble)) + (value2 * splitDouble)    #Weighted average value  
    
    double1 = array4[row_1+732, col_1 + 1]      #Lower value 
    double2 = array4[row_1+732, col_2 + 1]      #Upper value
    splitDouble = (Temperature-TemperatureLow) * 2                    #Weight
    value1 = (double1*(1-splitDouble))+(double2*splitDouble)  #Weighted average value
    #Upper pressure
    double1 = array4[row_2+732, col_1 + 1]                #Lower value
    double2 = array4[row_2+732, col_2 + 1]                #Upper value                          
    value2 = (double1 * (1 - splitDouble)) + (double2 * splitDouble)    #Weighted average value
    #Weight the two values across pressure
    splitDouble = (Hydro_P - PressureLow) * 4                      #Weight
    viscosityH20 = (value1 * (1 - splitDouble)) + (value2 * splitDouble)    #Weighted average value  
    
elif (Polynomial == 'Y'):
    rowNearest = row_1
    polyText=array5[rowNearest, col_1 + 1]
    x=' '.join(map(str, polyText))
    y=x.split(" ")
    A = [float(x) for x in y]
    A=np.asarray(A)
    A=np.reshape(A,[-1,6])  # reshape to x rows, 6 columns.
    pA = A[:,3]
    pB = A[:,4]
    pC = A[:,5]
    value1 = (pA * Hydro_P * Hydro_P) + (pB * Hydro_P) + (pC)
    polyText=array5[rowNearest, col_2 + 1]
    x=' '.join(map(str, polyText))
    y=x.split(" ")
    A = [float(x) for x in y]
    A=np.asarray(A)
    A=np.reshape(A,[-1,6])  # reshape to x rows, 6 columns.
    pA = A[:,3]
    pB = A[:,4]
    pC = A[:,5]
    value2 = (pA * Hydro_P * Hydro_P) + (pB * Hydro_P) + (pC)    
    splitDouble = (Temperature - TemperatureLow) * 2 
    densityCO2 = (value1 * (1 - splitDouble)) + (value2 * splitDouble) 
    
    polyText=array5[rowNearest+244, col_1 + 1]
    x=' '.join(map(str, polyText))
    y=x.split(" ")
    A = [float(x) for x in y]
    A=np.asarray(A)
    A=np.reshape(A,[-1,6])  # reshape to x rows, 6 columns.
    pA = A[:,3]
    pB = A[:,4]
    pC = A[:,5]
    value1 = (pA * Hydro_P * Hydro_P) + (pB * Hydro_P) + (pC)
    polyText=array5[rowNearest+244, col_2 + 1]
    x=' '.join(map(str, polyText))
    y=x.split(" ")
    A = [float(x) for x in y]
    A=np.asarray(A)
    A=np.reshape(A,[-1,6])  # reshape to x rows, 6 columns.
    pA = A[:,3]
    pB = A[:,4]
    pC = A[:,5]
    value2 = (pA * Hydro_P * Hydro_P) + (pB * Hydro_P) + (pC)    
    splitDouble = (Temperature - TemperatureLow) * 2 
    viscosityCO2 = (value1 * (1 - splitDouble)) + (value2 * splitDouble)   
    
    polyText=array5[rowNearest+488, col_1 + 1]
    x=' '.join(map(str, polyText))
    y=x.split(" ")
    A = [float(x) for x in y]
    A=np.asarray(A)
    A=np.reshape(A,[-1,6])  # reshape to x rows, 6 columns.
    pA = A[:,3]
    pB = A[:,4]
    pC = A[:,5]
    value1 = (pA * Hydro_P * Hydro_P) + (pB * Hydro_P) + (pC)
    polyText=array5[rowNearest+488, col_2 + 1]
    x=' '.join(map(str, polyText))
    y=x.split(" ")
    A = [float(x) for x in y]
    A=np.asarray(A)
    A=np.reshape(A,[-1,6])  # reshape to x rows, 6 columns.
    pA = A[:,3]
    pB = A[:,4]
    pC = A[:,5]
    value2 = (pA * Hydro_P * Hydro_P) + (pB * Hydro_P) + (pC)    
    splitDouble = (Temperature - TemperatureLow) * 2 
    densityH20 = (value1 * (1 - splitDouble)) + (value2 * splitDouble)
    
    polyText=array5[rowNearest+732, col_1 + 1]
    x=' '.join(map(str, polyText))
    y=x.split(" ")
    A = [float(x) for x in y]
    A=np.asarray(A)
    A=np.reshape(A,[-1,6])  # reshape to x rows, 6 columns.
    pA = A[:,3]
    pB = A[:,4]
    pC = A[:,5]
    value1 = (pA * Hydro_P * Hydro_P) + (pB * Hydro_P) + (pC)
    polyText=array5[rowNearest+732, col_2 + 1]
    x=' '.join(map(str, polyText))
    y=x.split(" ")
    A = [float(x) for x in y]
    A=np.asarray(A)
    A=np.reshape(A,[-1,6])  # reshape to x rows, 6 columns.
    pA = A[:,3]
    pB = A[:,4]
    pC = A[:,5]
    value2 = (pA * Hydro_P * Hydro_P) + (pB * Hydro_P) + (pC)    
    splitDouble = (Temperature - TemperatureLow) * 2 
    viscosityH20 = (value1 * (1 - splitDouble)) + (value2 * splitDouble)     
    
  

# Main calculation





cutoffROMa = 0.1    #Move to next ROM if above this value (0 to 0.1 MtCO2/yr ROM)
cutoffROMb = 0.5    #Move to next ROM if above this value (0.05 to 0.5 MtCO2/yr ROM)
cutoffROMc = 1      #Move to next ROM if above this value (0.1 to 1 MtCO2/yr ROM)
cutoffROMd = 5      #Move to next ROM if above this value (0.5 to 5 MtCO2/yr ROM)
cutoffROMe = 10     #Move to next ROM if above this value (1 to 10 MtCO2/yr ROM)
cutoffROMf = 50     #Move to next ROM if above this value (5 to 50 MtCO2/yr ROM)
cutoffROMg = -1     #Move to next ROM if above this value (10 to Max MtCO2/yr ROM)

arrayLowerBound = np.zeros(7,dtype=np.float)
arrayLowerBound[0] = 0
arrayLowerBound[1] = 0.05
arrayLowerBound[2] = 0.1
arrayLowerBound[3] = 0.5
arrayLowerBound[4] = 1
arrayLowerBound[5] = 5
arrayLowerBound[6] = 10

arrayUpperBound = np.zeros(7,dtype=np.float)
arrayUpperBound[0] = 0.05
arrayUpperBound[1] = 0.1
arrayUpperBound[2] = 0.5
arrayUpperBound[3] = 1
arrayUpperBound[4] = 5
arrayUpperBound[5] = 10
arrayUpperBound[6] = 10000000000# '"Infinite" upper bound

transitionFraction = 0.5   # Smooth x% betwen new and previous ROM

depth=Depth
thick=Thick
perm=Permeability
poro=Porosity
geoGrad=Geothermal_gradient

injectionNew = np.zeros(Depth.shape[0],dtype=np.float)
injectionA = np.zeros(Depth.shape[0],dtype=np.float)
injectionB = np.zeros(Depth.shape[0],dtype=np.float)
injectionC = np.zeros(Depth.shape[0],dtype=np.float)
injectionD = np.zeros(Depth.shape[0],dtype=np.float)
injectionE = np.zeros(Depth.shape[0],dtype=np.float)
injectionF = np.zeros(Depth.shape[0],dtype=np.float)
injectionG = np.zeros(Depth.shape[0],dtype=np.float)
condition_1 = np.zeros(Depth.shape[0],dtype=np.float)
condition_2 = np.zeros(Depth.shape[0],dtype=np.float)
condition_3 = np.zeros(Depth.shape[0],dtype=np.float)
condition_4 = np.zeros(Depth.shape[0],dtype=np.float)
condition_5 = np.zeros(Depth.shape[0],dtype=np.float)
condition_6 = np.zeros(Depth.shape[0],dtype=np.float)
injection1 = np.zeros(Depth.shape[0],dtype=np.float)
injection2 = np.zeros(Depth.shape[0],dtype=np.float)
weight1 = np.zeros(Depth.shape[0],dtype=np.float)
weight2 = np.zeros(Depth.shape[0],dtype=np.float)
ROM_new = np.zeros(Depth.shape[0],dtype=np.float)
radiusNew = np.zeros(Depth.shape[0],dtype=np.float)
radiusA = np.zeros(Depth.shape[0],dtype=np.float)
radiusB = np.zeros(Depth.shape[0],dtype=np.float)   
ratioROM = np.zeros(Depth.shape[0],dtype=np.float)
radius1 = np.zeros(Depth.shape[0],dtype=np.float)   
radius2 = np.zeros(Depth.shape[0],dtype=np.float) 
numberOfWells= np.zeros(Depth.shape[0],dtype=np.float) 



for j in range (Depth.shape[0]):        
    for i in range (7):
        if i ==0:
            if Injection_period[j]==5:
                injectionNew[j]=ROM_1_LogMCO2_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==10:
                injectionNew[j]=ROM_1_LogMCO2_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==15:
                injectionNew[j]=ROM_1_LogMCO2_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==20:
                injectionNew[j]=ROM_1_LogMCO2_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==25:
                injectionNew[j]=ROM_1_LogMCO2_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==30:
                injectionNew[j]=ROM_1_LogMCO2_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==35:
                injectionNew[j]=ROM_1_LogMCO2_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==40:
                injectionNew[j]=ROM_1_LogMCO2_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==45:
                injectionNew[j]=ROM_1_LogMCO2_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==50:
                injectionNew[j]=ROM_1_LogMCO2_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
        if i ==1:
            if Injection_period[j]==5:
                injectionNew[j]=ROM_2_LogMCO2_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==10:
                injectionNew[j]=ROM_2_LogMCO2_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==15:
                injectionNew[j]=ROM_2_LogMCO2_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==20:
                injectionNew[j]=ROM_2_LogMCO2_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==25:
                injectionNew[j]=ROM_2_LogMCO2_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==30:
                injectionNew[j]=ROM_2_LogMCO2_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==35:
                injectionNew[j]=ROM_2_LogMCO2_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==40:
                injectionNew[j]=ROM_2_LogMCO2_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==45:
                injectionNew[j]=ROM_2_LogMCO2_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==50:
                injectionNew[j]=ROM_2_LogMCO2_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
        if i ==2:
            if Injection_period[j]==5:
                injectionNew[j]=ROM_3_LogMCO2_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==10:
                injectionNew[j]=ROM_3_LogMCO2_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==15:
                injectionNew[j]=ROM_3_LogMCO2_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==20:
                injectionNew[j]=ROM_3_LogMCO2_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==25:
                injectionNew[j]=ROM_3_LogMCO2_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==30:
                injectionNew[j]=ROM_3_LogMCO2_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==35:
                injectionNew[j]=ROM_3_LogMCO2_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==40:
                injectionNew[j]=ROM_3_LogMCO2_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==45:
                injectionNew[j]=ROM_3_LogMCO2_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==50:
                injectionNew[j]=ROM_3_LogMCO2_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
        if i ==3:
            if Injection_period[j]==5:
                injectionNew[j]=ROM_4_LogMCO2_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==10:
                injectionNew[j]=ROM_4_LogMCO2_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==15:
                injectionNew[j]=ROM_4_LogMCO2_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==20:
                injectionNew[j]=ROM_4_LogMCO2_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==25:
                injectionNew[j]=ROM_4_LogMCO2_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==30:
                injectionNew[j]=ROM_4_LogMCO2_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==35:
                injectionNew[j]=ROM_4_LogMCO2_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==40:
                injectionNew[j]=ROM_4_LogMCO2_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==45:
                injectionNew[j]=ROM_4_LogMCO2_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==50:
                injectionNew[j]=ROM_4_LogMCO2_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
        if i ==4:
            if Injection_period[j]==5:
                injectionNew[j]=ROM_5_LogMCO2_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==10:
                injectionNew[j]=ROM_5_LogMCO2_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==15:
                injectionNew[j]=ROM_5_LogMCO2_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==20:
                injectionNew[j]=ROM_5_LogMCO2_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==25:
                injectionNew[j]=ROM_5_LogMCO2_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==30:
                injectionNew[j]=ROM_5_LogMCO2_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==35:
                injectionNew[j]=ROM_5_LogMCO2_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==40:
                injectionNew[j]=ROM_5_LogMCO2_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==45:
                injectionNew[j]=ROM_5_LogMCO2_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==50:
                injectionNew[j]=ROM_5_LogMCO2_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
        if i ==5:
            if Injection_period[j]==5:
                injectionNew[j]=ROM_6_LogMCO2_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==10:
                injectionNew[j]=ROM_6_LogMCO2_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==15:
                injectionNew[j]=ROM_6_LogMCO2_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==20:
                injectionNew[j]=ROM_6_LogMCO2_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==25:
                injectionNew[j]=ROM_6_LogMCO2_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==30:
                injectionNew[j]=ROM_6_LogMCO2_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==35:
                injectionNew[j]=ROM_6_LogMCO2_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==40:
                injectionNew[j]=ROM_6_LogMCO2_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==45:
                injectionNew[j]=ROM_6_LogMCO2_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==50:
                injectionNew[j]=ROM_6_LogMCO2_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
        if i ==6:
            if Injection_period[j]==5:
                injectionNew[j]=ROM_7_LogMCO2_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==10:
                injectionNew[j]=ROM_7_LogMCO2_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==15:
                injectionNew[j]=ROM_7_LogMCO2_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==20:
                injectionNew[j]=ROM_7_LogMCO2_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==25:
                injectionNew[j]=ROM_7_LogMCO2_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==30:
                injectionNew[j]=ROM_7_LogMCO2_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==35:
                injectionNew[j]=ROM_7_LogMCO2_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==40:
                injectionNew[j]=ROM_7_LogMCO2_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==45:
                injectionNew[j]=ROM_7_LogMCO2_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            elif Injection_period[j]==50:
                injectionNew[j]=ROM_7_LogMCO2_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
        

        if i==0 and injectionNew[j]<arrayUpperBound[0]:
            injection1[j]=injectionNew[j]
            ROM_new[j]=i+1
            injectionPrevious=injectionNew[j]
            break
        if injectionNew[j] < arrayUpperBound[i]:
            transitionValue = transitionFraction * arrayUpperBound[i-1]
            weight1[j] = (injectionNew[j] - arrayUpperBound[i-1]) / transitionValue
            if weight1[j] >1:
                injection1[j]=injectionNew[j]
                ROM_new[j]=i+1
                break
            elif weight1[j]<0:
                injection1[j]=injectionPrevious
                ROM_new[j]=i
                break
            else:
                weight2[j]=1-weight1[j]
                injection1[j]=(weight2[j]*injectionPrevious)+(weight1[j]*injectionNew[j])
                ROM_new[j]=(i)*10+i+1
                break
        injectionPrevious=injectionNew[j]
            
if Plume_ROM == 'N' :
        injectionVolume = injection1 * Injection_period * 1000000 * 1000 / densityCO2 
        viscosityRatio = viscosityH20 / viscosityCO2
        areaNordbotten1 = viscosityRatio * injectionVolume / (Porosity * Thick * (1 - residualWater)) 
        radiusNordbotten1 = (areaNordbotten1 / pi) ^ 0.5 / 1000 
        areaNordbotten1 = pi * radiusNordbotten1 ^ 2 
        radius1 = radiusNordbotten1
else:

    for j in range (Depth.shape[0]):        
        for i in range (7):
            if i ==0:
                if Injection_period[j]==5:
                    radiusNew[j]=ROM_1_LogArea_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==10:
                    radiusNew[j]=ROM_1_LogArea_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==15:
                    radiusNew[j]=ROM_1_LogArea_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==20:
                    radiusNew[j]=ROM_1_LogArea_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==25:
                    radiusNew[j]=ROM_1_LogArea_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==30:
                    radiusNew[j]=ROM_1_LogArea_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==35:
                    radiusNew[j]=ROM_1_LogArea_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==40:
                    radiusNew[j]=ROM_1_LogArea_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==45:
                    radiusNew[j]=ROM_1_LogArea_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==50:
                    radiusNew[j]=ROM_1_LogArea_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            if i ==1:
                if Injection_period[j]==5:
                    radiusNew[j]=ROM_2_LogArea_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==10:
                    radiusNew[j]=ROM_2_LogArea_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==15:
                    radiusNew[j]=ROM_2_LogArea_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==20:
                    radiusNew[j]=ROM_2_LogArea_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==25:
                    radiusNew[j]=ROM_2_LogArea_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==30:
                    radiusNew[j]=ROM_2_LogArea_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==35:
                    radiusNew[j]=ROM_2_LogArea_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==40:
                    radiusNew[j]=ROM_2_LogArea_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==45:
                    radiusNew[j]=ROM_2_LogArea_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==50:
                    radiusNew[j]=ROM_2_LogArea_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            if i ==2:
                if Injection_period[j]==5:
                    radiusNew[j]=ROM_3_LogArea_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==10:
                    radiusNew[j]=ROM_3_LogArea_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==15:
                    radiusNew[j]=ROM_3_LogArea_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==20:
                    radiusNew[j]=ROM_3_LogArea_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==25:
                    radiusNew[j]=ROM_3_LogArea_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==30:
                    radiusNew[j]=ROM_3_LogArea_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==35:
                    radiusNew[j]=ROM_3_LogArea_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==40:
                    radiusNew[j]=ROM_3_LogArea_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==45:
                    radiusNew[j]=ROM_3_LogArea_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==50:
                    radiusNew[j]=ROM_3_LogArea_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            if i ==3:
                if Injection_period[j]==5:
                    radiusNew[j]=ROM_4_LogArea_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==10:
                    radiusNew[j]=ROM_4_LogArea_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==15:
                    radiusNew[j]=ROM_4_LogArea_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==20:
                    radiusNew[j]=ROM_4_LogArea_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==25:
                    radiusNew[j]=ROM_4_LogArea_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==30:
                    radiusNew[j]=ROM_4_LogArea_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==35:
                    radiusNew[j]=ROM_4_LogArea_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==40:
                    radiusNew[j]=ROM_4_LogArea_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==45:
                    radiusNew[j]=ROM_4_LogArea_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==50:
                    radiusNew[j]=ROM_4_LogArea_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            if i ==4:
                if Injection_period[j]==5:
                    radiusNew[j]=ROM_5_LogArea_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==10:
                    radiusNew[j]=ROM_5_LogArea_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==15:
                    radiusNew[j]=ROM_5_LogArea_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==20:
                    radiusNew[j]=ROM_5_LogArea_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==25:
                    radiusNew[j]=ROM_5_LogArea_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==30:
                    radiusNew[j]=ROM_5_LogArea_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==35:
                    radiusNew[j]=ROM_5_LogArea_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==40:
                    radiusNew[j]=ROM_5_LogArea_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==45:
                    radiusNew[j]=ROM_5_LogArea_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==50:
                    radiusNew[j]=ROM_5_LogArea_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            if i ==5:
                if Injection_period[j]==5:
                    radiusNew[j]=ROM_6_LogArea_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==10:
                    radiusNew[j]=ROM_6_LogArea_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==15:
                    radiusNew[j]=ROM_6_LogArea_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==20:
                    radiusNew[j]=ROM_6_LogArea_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==25:
                    radiusNew[j]=ROM_6_LogArea_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==30:
                    radiusNew[j]=ROM_6_LogArea_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==35:
                    radiusNew[j]=ROM_6_LogArea_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==40:
                    radiusNew[j]=ROM_6_LogArea_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==45:
                    radiusNew[j]=ROM_6_LogArea_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==50:
                    radiusNew[j]=ROM_6_LogArea_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            if i ==6:
                if Injection_period[j]==5:
                    radiusNew[j]=ROM_7_LogArea_5yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==10:
                    radiusNew[j]=ROM_7_LogArea_10yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==15:
                    radiusNew[j]=ROM_7_LogArea_15yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==20:
                    radiusNew[j]=ROM_7_LogArea_20yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==25:
                    radiusNew[j]=ROM_7_LogArea_25yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==30:
                    radiusNew[j]=ROM_7_LogArea_30yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==35:
                    radiusNew[j]=ROM_7_LogArea_35yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==40:
                    radiusNew[j]=ROM_7_LogArea_40yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==45:
                    radiusNew[j]=ROM_7_LogArea_45yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
                elif Injection_period[j]==50:
                    radiusNew[j]=ROM_7_LogArea_50yr(Depth[j], Thick[j], Permeability[j], Porosity[j], Geothermal_gradient[j])
            
    
            if i==0 and injection1[j]<arrayUpperBound[0]:
                radius1[j]=radiusNew[j]
                ROM_new[j]=i+1
                radiusPrevious=radiusNew[j]
                break
            if np.greater_equal(injection1[j],arrayUpperBound[i]):
                radiusPrevious=radiusNew[j]
            if injection1[j] < arrayUpperBound[i]:
                transitionValue = transitionFraction * arrayUpperBound[i-1]
                weight1[j] = (injection1[j] - arrayUpperBound[i-1]) / transitionValue
                if weight1[j] >1:
                    radius1[j]=radiusNew[j]
                    ROM_new[j]=i+1
                    break
                elif weight1[j]<0:
                    radius1[j]=radiusPrevious
                    ROM_new[j]=i
                    break
                else:
                    weight2[j]=1-weight1[j]
                    radius1[j]=(weight2[j]*radiusPrevious)+(weight1[j]*radiusNew[j])
                    ROM_new[j]=(i)*10+i+1
                    break
            radiusPrevious=radiusNew[j]



if Plume_ROM == 'Y':
    for i in range (radius1.shape[0]):        
        if radius1[i] < 0:
            radius1[i] = 0 - ((abs(radius1[i]) / pi) ** 0.5 / 1000)   #Convert to radius in km (keep it negative)
        else:
            radius1[i] = (radius1[i] / pi) ** 0.5 / 1000   #Convert to radius in km
    
for i in range (Depth.shape[0]):
    if injection1[i]>1:
        injection2[i] = 1 
        if injection1[i]<=2.5:
            ratioROM[i] = 0.9977 * injection1[i] ** 0.3589
            radius2[i] = radius1[i] / ratioROM[i]
        elif injection1[i]<=10:
            ratioROM[i] = 0.9524 * injection1[i] ** 0.4096 #Ratio between uncontrolled and rate-controlled plume radii
            radius2[i] = radius1[i] / ratioROM[i]
        else:
            ratioROM[i] = 0.935 * injection1[i] ** 0.4284 
            radius2[i] = radius1[i] / ratioROM[i]
    else:
        injection2[i] = injection1[i]
        radius2[i] = radius1[i]

area1 = pi * radius1 ** 2
area2 = pi * radius2 ** 2 

# for i in range (area1.shape[0]):
#     if area1[i]==0:
#         area1[i]=area1[i-1]
# for i in range (area2.shape[0]):
#     if area2[i]==0:
#         area2[i]=area2[i-1]        
        

if Square_Hexagonal=='H':
    wellUnusedArea = 1 - 0.107300918
    area3 = area2
    radius3 = radius2 
    decimalWells = (Area * wellUnusedArea) / area3
elif Square_Hexagonal=='S':
    if Allowable_overlap == 0:
        wellUnusedArea = 3.14 / 4
        area3 = area2
        radius3 = radius2
    else:
        radiusOverlap = 0.7185 * Allowable_overlap ^ 0.671
        radius3 = (1 - (radiusOverlap / 2)) * radius2
        uniquePlumeArea = -0.5 * Allowable_overlap + 1
        uniquePlumeArea = uniquePlumeArea * area2
        area3 = uniquePlumeArea 
        plumeBox = (radius3 * 2) ** 2
        wellUnusedArea = uniquePlumeArea / plumeBox
    decimalWells = (Area * wellUnusedArea) / area3
else:
    print('The well pattern input has error')

if Only_integer=='Y':
    for i in range (Depth.shape[0]):
        numberOfWells[i] = int(decimalWells[i] + 0.999)
else:
    numberOfWells = decimalWells

# Calculate if we will reduce the plume radius if assuming integer number of wells
wellReduction = decimalWells / numberOfWells    #Reduction factor
injection3 = injection2 * wellReduction         #Reduce injection rate (if using integer wells)
injectionEconomics = injection3                 #Make this variable available to the Economics module
radius3 = radius2 * (wellReduction ** 0.5)       #Reduce plume radius
plumeEconomics = radius3                        #Make this variable available to the Economics module
area3 = area3 * wellReduction                   #Reduce plume area

#Calculate plume volumes
volume1 = injection1 * Injection_period * 1000 / densityCO2
volume3 = injection3 * Injection_period * 1000 / densityCO2

#Calculate the volume of water from CO2 density and using the water density too (assumes an equivalent volume of water will be removed)
volumeWater = densityH20 / densityCO2

# Calculate and print the reservoir storage capacity (plume area in in m2 and reservoir area is in km2)
Static_reservoir_storage_capacity=poro*thick*Area*1000000*Volumetric_efficiency/100*densityCO2/1000/1000000
Dynamic_reservoir_storage_capacity=injection3 * numberOfWells * Injection_period 
Dynamic_efficiency_factor=Dynamic_reservoir_storage_capacity/(Static_reservoir_storage_capacity/Volumetric_efficiency*100)

print ('The injection rate are',injection1)
print ('The plume radius are', radius1)
print ('The plume volume are', volume1)
print ('The extracted water are', 1000 / densityCO2)
print ('The selected ROM are', ROM_new)
print ('The storage potential of plume are',(injection1 * Injection_period) / area1)
print ('Plume radius for one well (decimal or integer) are',injection3)
print ('Plume radius for one well when taking into account pressure and site area restrictions are',radius2)
print ('Plume volume are',volume3)
print ('Extracted water (m3 per tCO2) are',1000/densityCO2)
print ('Number of wells or the site are',numberOfWells)
print ('Static reservoir storage capacity for the site are',Static_reservoir_storage_capacity)
print ('Dynamic reservoir storage capacity for the site are',Dynamic_reservoir_storage_capacity)
print ('Dynamic efficiency factor for the site are',Dynamic_reservoir_storage_capacity)
# Economcs part

actualInjectionRate=Dynamic_reservoir_storage_capacity / Injection_period

if Financing_period<=0:
    Financing_period=Injection_period
if Capital_charge_factor<=0:
    Financing_period = ((Interest_Rate) * (((Interest_Rate) + 1) ** Financing_period/ ((((Interest_Rate) + 1) ** Financing_period - 1))))

siteFixed=array6[6, 7]+array6[8, 7]+array6[9, 7]+array6[10, 7]+array6[11, 7]+array6[12, 7]+array6[13, 7]+array6[14, 7] \
    +array6[15, 7]+array6[19, 7]+array6[25, 7]+array6[58, 7]+array6[65, 7]+array6[68, 7]+array6[69, 7]+array6[83, 7] \
    +array6[84, 7]++array6[86, 7]+array6[87, 7]+array6[94, 7]
siteFixedPerSqMile=array6[7, 9]+array6[9, 9]+array6[16, 9]+array6[18, 9]+array6[67, 9]+array6[68, 9]+array6[86, 9]+array6[100, 9]
siteFixedPerSqMile=siteFixedPerSqMile*Area/2.5899881103
siteFixedCost = (siteFixed + siteFixedPerSqMile) / 1000000

wellFixed=   array6[23, 11]+ array6[30, 11]+ array6[31, 11]+ array6[58, 11]+ array6[65, 11]+ array6[66, 11]+ array6[69, 11] \
    + array6[77, 11]+ array6[83, 11]+ array6[84, 11]+ array6[87, 11]+ array6[88, 11]+ array6[95, 11]+ array6[96, 11]+ array6[97, 11]
wellFixedPerFoot=array6[12, 12]+array6[30, 12]+array6[70, 12]+array6[72, 12]+array6[73, 12]+array6[75, 12]
wellFixedPerFoot = wellFixedPerFoot * (Depth + Thick) * 3.280839895

wellFixedPerCO2capacity=0+array6[77, 13]*Capital_charge_factor
wellFixedPerCO2capacity=wellFixedPerCO2capacity*injectionEconomics* 1000000
wellFixedPerCO2capacity=wellFixedPerCO2capacity*Pump_per_well

wellWaterCost=array6[70, 12]+array6[72, 12]+array6[73, 12]+array6[75, 12]
wellWaterCost=wellWaterCost*Water_production_wells*(Depth+Thick)*3.280839895

wellFixedCost= (wellFixed + wellFixedPerFoot + wellFixedPerCO2capacity + wellWaterCost) / 1000000

wellFixedPerYear=array6[99, 14]+array6[109, 14]+array6[110, 14]+array6[113, 14]

wellFixedCO2Year=array6[99, 16]+array6[110, 16]+array6[113, 16]
wellFixedCO2Year=wellFixedCO2Year*(Depth+Thick)*3.280839895

wellFixedOM = (wellFixedPerYear + wellFixedCO2Year) / 1000000

wellVariableOM=0
if Pump_per_well >0:
    wellVariableOM=array6[98, 15]
    
wellVariableOM=wellVariableOM+array6[101,15]+array6[103,15]+(Water_treatment * volumeWater)

d1 = actualInjectionRate    # Sitewide injection rate
d2 = injectionEconomics     # Well injection rate
d3 = plumeEconomics * 2      # Distance between wells


# for i in range (d1.shape[0]):    
#     d1[i]=round(d1[i])
#     if d1[i] < 1:
#         d1[i] = 1
#     if d1[i] > 20: 
#         d1[i] = 20  
#     d2[i]=d2[i]*20
#     d2[i]=round(d2[i])    
#     if d2[i] < 1:
#         d2[i] = 1
#     if d2[i] > 20: 
#         d2[i] = 20
#     d3[i]=d3[i]/1000
#     d3[i]=round(d3[i])
#     if d3[i] < 1:
#         d3[i] = 1
#     if d3[i] > 20: 
#         d3[i] = 20

# dRow = ((d1 - 1) * 400) + ((d2 - 1) * 20) + d3 + 1
# for i in range(d1.shape[0]):
#     distributionPipelineCost=array6[dRow[i], 4]

distributionPipelineCost=0  
wellVariableOM = wellVariableOM + distributionPipelineCost

siteFixedOM= np.zeros(Depth.shape[0],dtype=np.float)

totalCost = (siteFixedCost * Capital_charge_factor) + siteFixedOM +(wellFixedCost * Capital_charge_factor * numberOfWells) + (wellFixedOM * numberOfWells) + \
            (wellVariableOM * actualInjectionRate)
totalCost=totalCost/actualInjectionRate



# print ('Total cost ($/tCO2) are',totalCost)
# print ('Fixed site-wide costs ($M) are', siteFixedCost)
# print ('Fixed O&M costs for managin the site are', siteFixedOM)
# print ('Fixed captial cost for one well are', wellFixedCost)
# print ('Fixed O&M cost for a well are', wellFixedOM)
# print ('Variable O&M cost for a well are', wellVariableOM)



# import pandas as pd
# title = ['injection rate', 'plume radius', 'plume volume', 'extracted water',
#           'selected ROM', 'The storage potential of plume', 'Plume radius for one well (decimal or integer)','Plume radius for one well when taking into account pressure and site area restrictions',
#           'Plume volume', 'Extracted water (m3 per tCO2)', 'Number of wells or the site','Total storage capacity for the site','Storage potential for the rate-controlled plume',
#           ]
# import csv
# with open("Results_combination_full"  + ".csv", "w") as out_file:
#     writer = csv.DictWriter(out_file, fieldnames = ["ID", "Name", "x","y","Depth","Pressure","Thickness","Permeability","Porosity","Geothermal_gradient","Temperature","Area","Max_pressure","Max_rate","Injection period","CO2 density","CO2 viscosity","Injection_rate","Plume radius","Plume volume","Extracted water","ROM","Dynamic reservoir capability","Well injection rate","Plume radius","Plume volume","Extracted water","Number of Wells","Static reservoir capability","Dynamic reservoir capability","Dynamic efficiency factor","Total cost", 'SiteFixedCost','SiteVarOM','WellFixedCost','WellFixedOM','WellVarOM'])
#     writer.writeheader()
#     for i in range(Depth.shape[0]):
#         out_string = ""
#         out_string += str(i+1)
#         out_string += "," + str(name[i])
#         out_string += "," + str(x_lo[i])
#         out_string += "," + str(y_lo[i]) 
#         out_string += "," + str(Depth[i]) 
#         out_string += "," + str(Hydro_P[i]) 
#         out_string += "," + str(Thick[i]) 
#         out_string += "," + str(10**Permeability[i]/9.86923299999996E-16) 
#         out_string += "," + str(Porosity[i]) 
#         out_string += "," + str(Geothermal_gradient[i]) 
#         out_string += "," + str(Temperature[i]) 
#         out_string += "," + str(Area[i]) 
#         out_string += "," + str(Max_pressure[i]) 
#         out_string += "," + str(Max_rate[i]) 
#         out_string += "," + str(Injection_period[i]) 
#         out_string += "," + str(densityCO2[i]) 
#         out_string += "," + str(viscosityCO2[i])  
#         out_string += "," +str(injection1[i])
#         out_string += "," +str(radius1[i])
#         out_string += "," +str(volume1[i])
#         out_string += "," +str(1000/densityCO2[i])
#         out_string += "," +str(ROM_new[i])
#         out_string += "," +str(Dynamic_reservoir_storage_capacity[i])
#         out_string += "," +str(injection3[i])
#         out_string += "," +str(radius2[i])
#         out_string += "," +str(volume3[i])
#         out_string += "," +str(1000/densityCO2[i])
#         out_string += "," +str(numberOfWells[i])
#         out_string += "," +str(Dynamic_reservoir_storage_capacity[i])
#         out_string += "," + str(Static_reservoir_storage_capacity[i])
#         out_string += "," + str(Dynamic_efficiency_factor[i])        
#         out_string += "," + str(totalCost[i])
#         out_string += "," + str(siteFixedCost[i])
#         out_string += "," + str(siteFixedOM[i]) 
#         out_string += "," + str(wellFixedCost[i])        
#         out_string += "," + str(wellFixedOM[i])
#         out_string += "," + str(wellVariableOM[i]) 
#         out_string += "\n"
#         out_file.write(out_string) 
     

# with open("Results_plot"  + ".csv", "w") as out_file:
#     writer = csv.DictWriter(out_file, fieldnames = ["ID", "Name", "SinkCapacity", 'SinkFixedCost','SinkVarOM','WellInjectivity','WellFixedCost','WellFixedOM','WellVarOM','N/A','xLON','yLON'])
#     writer.writeheader()
#     for i in range(Depth.shape[0]):
#         out_string = ""
#         out_string += str(i)
#         out_string += "," +str(i)
#         out_string += "," + str(reservoirStorageCapacity[i])
#         out_string += "," + str(siteFixedCost[i])
#         out_string += "," + str(siteFixedOM[i])
#         out_string += "," + str(injection3[i]) 
#         out_string += "," + str(wellFixedCost[i])        
#         out_string += "," + str(wellFixedOM[i])
#         out_string += "," + str(wellVariableOM[i])
#         out_string += "," + str('N/A') 
#         out_string += "," + str(x_lo[i])
#         out_string += "," + str(y_lo[i])       
#         out_string += "\n"
#         out_file.write(out_string) 



# plot geothermal gradient versus reservoir storage capacity


# 10**Permeability/9.86923299999996E-16  Permeability (mD)
# geoGrad   Geo-thermal gradient (°C/km)





#############################################################
fig = plt.figure(figsize=(15,7))
ax1 = fig.add_subplot(231)
ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, injection3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, injection3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, injection3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, injection3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, injection3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, injection3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, injection3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, injection3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, injection3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, injection3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Injection rate (MtCO2/yr)',color='k', fontsize=12);
ax1.set_xlabel('Permeability (mD)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(232)
ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, radius2[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, radius2[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, radius2[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, radius2[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, radius2[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, radius2[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, radius2[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, radius2[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, radius2[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, radius2[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Plume radius (km)',color='k', fontsize=12);
ax1.set_xlabel('Permeability (mD)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(233)
ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, volume3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, volume3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, volume3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, volume3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, volume3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, volume3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, volume3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, volume3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, volume3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, volume3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Plume volume (Mm3)',color='k', fontsize=12);
ax1.set_xlabel('Permeability (mD)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(234)
ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, numberOfWells[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, numberOfWells[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, numberOfWells[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, numberOfWells[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, numberOfWells[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, numberOfWells[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, numberOfWells[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, numberOfWells[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, numberOfWells[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, numberOfWells[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Number of wells',color='k', fontsize=12);
ax1.set_xlabel('Permeability (mD)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(235)
ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =1,label = "5 year")
ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1,label = "10 year")
ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1,label = "15 year")
ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1,label = "20 year")
ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1,label = "25 year")
ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1,label = "30 year")
ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1,label = "35 year")
ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1,label = "40 year")
ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1,label = "45 year")
ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1,label = "50 year")
ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
ax1.set_xlabel('Permeability (mD)', fontsize=12)
ax1.legend(loc=1,ncol=2,fontsize=12.0)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(236)

# ax2.set_xlim([145, 175]);
# ax2.set_ylim([0, 5]);
ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, Dynamic_reservoir_storage_capacity[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, Dynamic_reservoir_storage_capacity[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, Dynamic_reservoir_storage_capacity[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, Dynamic_reservoir_storage_capacity[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, Dynamic_reservoir_storage_capacity[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, Dynamic_reservoir_storage_capacity[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, Dynamic_reservoir_storage_capacity[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, Dynamic_reservoir_storage_capacity[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, Dynamic_reservoir_storage_capacity[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, Dynamic_reservoir_storage_capacity[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Dynamic reservoir capacity (MtCO2)',color='blue', fontsize=12);
ax1.set_xlabel('Permeability (mD)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='blue')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='k')

ax2 = ax1.twinx() # this is the important function
ax2.scatter(10**Permeability/9.86923299999996E-16, Static_reservoir_storage_capacity, color='k',s=1.5)
ax2.set_ylabel('Static reservoir capacity (MtCO2)',color='k',fontsize=12.0);
ax2.yaxis.set_tick_params(labelsize=12.0,colors='k')
ax2.spines['right'].set_color('k')
ax2.spines['left'].set_color('blue')




# fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(111)
# ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =4,label = "5 year")
# ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =4,label = "10 year")
# ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =4,label = "15 year")
# ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =4,label = "20 year")
# ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =4,label = "25 year")
# ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =4,label = "30 year")
# ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =4,label = "35 year")
# ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =4,label = "40 year")
# ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =4,label = "45 year")
# ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =4,label = "50 year")
# ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Permeability (mD)', fontsize=12)
# ax1.legend(loc=1,ncol=2,fontsize=14.0)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


###########################################################

fig = plt.figure(figsize=(15,7))
ax1 = fig.add_subplot(231)
ax1.plot(Depth[:sample_number], injection3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number:sample_number*2], injection3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*2:sample_number*3], injection3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*3:sample_number*4], injection3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*4:sample_number*5], injection3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*5:sample_number*6], injection3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*6:sample_number*7], injection3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*7:sample_number*8], injection3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*8:sample_number*9], injection3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*9:sample_number*10], injection3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Injection rate (MtCO2/yr)',color='k', fontsize=12);
ax1.set_xlabel('Depth (m)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(232)
ax1.plot(Depth[:sample_number], radius2[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number:sample_number*2], radius2[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*2:sample_number*3], radius2[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*3:sample_number*4], radius2[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*4:sample_number*5], radius2[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*5:sample_number*6], radius2[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*6:sample_number*7], radius2[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*7:sample_number*8], radius2[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*8:sample_number*9], radius2[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*9:sample_number*10], radius2[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Plume radius (km)',color='k', fontsize=12);
ax1.set_xlabel('Depth (m)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(233)
ax1.plot(Depth[:sample_number], volume3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number:sample_number*2], volume3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*2:sample_number*3], volume3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*3:sample_number*4], volume3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*4:sample_number*5], volume3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*5:sample_number*6], volume3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*6:sample_number*7], volume3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*7:sample_number*8], volume3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*8:sample_number*9], volume3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*9:sample_number*10], volume3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Plume volume (Mm3)',color='k', fontsize=12);
ax1.set_xlabel('Depth (m)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(234)
ax1.plot(Depth[:sample_number], numberOfWells[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number:sample_number*2], numberOfWells[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*2:sample_number*3], numberOfWells[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*3:sample_number*4], numberOfWells[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*4:sample_number*5], numberOfWells[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*5:sample_number*6], numberOfWells[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*6:sample_number*7], numberOfWells[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*7:sample_number*8], numberOfWells[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*8:sample_number*9], numberOfWells[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*9:sample_number*10], numberOfWells[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Number of wells',color='k', fontsize=12);
ax1.set_xlabel('Depth (m)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


ax1 = fig.add_subplot(235)
ax1.plot(Depth[:sample_number], totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =1,label = "5 year")
ax1.plot(Depth[sample_number:sample_number*2], totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1,label = "10 year")
ax1.plot(Depth[sample_number*2:sample_number*3], totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1,label = "15 year")
ax1.plot(Depth[sample_number*3:sample_number*4], totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1,label = "20 year")
ax1.plot(Depth[sample_number*4:sample_number*5], totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1,label = "25 year")
ax1.plot(Depth[sample_number*5:sample_number*6], totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1,label = "30 year")
ax1.plot(Depth[sample_number*6:sample_number*7], totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1,label = "35 year")
ax1.plot(Depth[sample_number*7:sample_number*8], totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1,label = "40 year")
ax1.plot(Depth[sample_number*8:sample_number*9], totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1,label = "45 year")
ax1.plot(Depth[sample_number*9:sample_number*10], totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1,label = "50 year")
ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
ax1.set_xlabel('Depth (m)', fontsize=12)
ax1.set_ylim([5,14])
ax1.legend(loc=1,ncol=2,fontsize=12.0)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(236)

# ax2.set_xlim([145, 175]);
# ax2.set_ylim([0, 5]);
ax1.plot(Depth[:sample_number], Dynamic_reservoir_storage_capacity[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number:sample_number*2], Dynamic_reservoir_storage_capacity[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*2:sample_number*3], Dynamic_reservoir_storage_capacity[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*3:sample_number*4], Dynamic_reservoir_storage_capacity[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*4:sample_number*5], Dynamic_reservoir_storage_capacity[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*5:sample_number*6], Dynamic_reservoir_storage_capacity[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*6:sample_number*7], Dynamic_reservoir_storage_capacity[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*7:sample_number*8], Dynamic_reservoir_storage_capacity[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*8:sample_number*9], Dynamic_reservoir_storage_capacity[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Depth[sample_number*9:sample_number*10], Dynamic_reservoir_storage_capacity[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Dynamic reservoir capacity (MtCO2)',color='blue', fontsize=12);
ax1.set_xlabel('Depth (m)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='blue')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='k')

ax2 = ax1.twinx() # this is the important function
ax2.scatter(Depth, Static_reservoir_storage_capacity, color='k',s=1.5)
ax2.set_ylabel('Static reservoir capacity (MtCO2)',color='k',fontsize=12.0);
ax2.yaxis.set_tick_params(labelsize=12.0,colors='k')
ax2.spines['right'].set_color('k')
ax2.spines['left'].set_color('blue')



fig = plt.figure(figsize=(15,7))
ax1 = fig.add_subplot(231)
ax1.plot(Geothermal_gradient[:sample_number], injection3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number:sample_number*2], injection3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], injection3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], injection3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], injection3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], injection3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], injection3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], injection3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], injection3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], injection3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Injection rate (MtCO2/yr)',color='k', fontsize=12);
ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(232)
ax1.plot(Geothermal_gradient[:sample_number], radius2[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number:sample_number*2], radius2[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], radius2[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], radius2[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], radius2[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], radius2[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], radius2[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], radius2[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], radius2[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], radius2[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Plume radius (km)',color='k', fontsize=12);
ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(233)
ax1.plot(Geothermal_gradient[:sample_number], volume3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number:sample_number*2], volume3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], volume3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], volume3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], volume3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], volume3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], volume3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], volume3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], volume3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], volume3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Plume volume (Mm3)',color='k', fontsize=12);
ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(234)
ax1.plot(Geothermal_gradient[:sample_number], numberOfWells[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number:sample_number*2], numberOfWells[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], numberOfWells[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], numberOfWells[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], numberOfWells[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], numberOfWells[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], numberOfWells[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], numberOfWells[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], numberOfWells[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], numberOfWells[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylim([4,15])
ax1.set_ylabel('Number of wells',color='k', fontsize=12);
ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


ax1 = fig.add_subplot(235)
ax1.plot(Geothermal_gradient[:sample_number], totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =1,label = "5 year")
ax1.plot(Geothermal_gradient[sample_number:sample_number*2], totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1,label = "10 year")
ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1,label = "15 year")
ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1,label = "20 year")
ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1,label = "25 year")
ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1,label = "30 year")
ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1,label = "35 year")
ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1,label = "40 year")
ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1,label = "45 year")
ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1,label = "50 year")
ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
ax1.legend(loc=1,ncol=2,fontsize=12.0)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

ax1 = fig.add_subplot(236)

# ax2.set_xlim([145, 175]);
# ax2.set_ylim([0, 5]);
ax1.plot(Geothermal_gradient[:sample_number], Dynamic_reservoir_storage_capacity[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number:sample_number*2], Dynamic_reservoir_storage_capacity[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], Dynamic_reservoir_storage_capacity[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], Dynamic_reservoir_storage_capacity[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], Dynamic_reservoir_storage_capacity[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], Dynamic_reservoir_storage_capacity[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], Dynamic_reservoir_storage_capacity[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], Dynamic_reservoir_storage_capacity[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], Dynamic_reservoir_storage_capacity[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], Dynamic_reservoir_storage_capacity[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Dynamic reservoir capacity (MtCO2)',color='blue', fontsize=12);
ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='blue')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='k')

ax2 = ax1.twinx() # this is the important function
ax2.scatter(Geothermal_gradient, Static_reservoir_storage_capacity, color='k',s=1.5)
ax2.set_ylabel('Static reservoir capacity (MtCO2)',color='k',fontsize=12.0);
ax2.yaxis.set_tick_params(labelsize=12.0,colors='k')
ax2.spines['right'].set_color('k')
ax2.spines['left'].set_color('blue')



fig = plt.figure(figsize=(15,7))
ax1 = fig.add_subplot(231)
ax1.plot(poro[:sample_number], injection3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number:sample_number*2], injection3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*2:sample_number*3], injection3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*3:sample_number*4], injection3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*4:sample_number*5], injection3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*5:sample_number*6], injection3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*6:sample_number*7], injection3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*7:sample_number*8], injection3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*8:sample_number*9], injection3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*9:sample_number*10], injection3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Injection rate (MtCO2/yr)',color='k', fontsize=12);
ax1.set_xlabel('Porosity', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(232)
ax1.plot(poro[:sample_number], radius2[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number:sample_number*2], radius2[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*2:sample_number*3], radius2[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*3:sample_number*4], radius2[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*4:sample_number*5], radius2[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*5:sample_number*6], radius2[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*6:sample_number*7], radius2[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*7:sample_number*8], radius2[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*8:sample_number*9], radius2[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*9:sample_number*10], radius2[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Plume radius (km)',color='k', fontsize=12);
ax1.set_xlabel('Porosity', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(233)
ax1.plot(poro[:sample_number], volume3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number:sample_number*2], volume3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*2:sample_number*3], volume3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*3:sample_number*4], volume3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*4:sample_number*5], volume3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*5:sample_number*6], volume3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*6:sample_number*7], volume3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*7:sample_number*8], volume3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*8:sample_number*9], volume3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*9:sample_number*10], volume3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Plume volume (Mm3)',color='k', fontsize=12);
ax1.set_xlabel('Porosity', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(234)
ax1.plot(poro[:sample_number], numberOfWells[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number:sample_number*2], numberOfWells[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*2:sample_number*3], numberOfWells[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*3:sample_number*4], numberOfWells[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*4:sample_number*5], numberOfWells[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*5:sample_number*6], numberOfWells[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*6:sample_number*7], numberOfWells[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*7:sample_number*8], numberOfWells[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*8:sample_number*9], numberOfWells[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*9:sample_number*10], numberOfWells[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Number of wells',color='k', fontsize=12);
ax1.set_xlabel('Porosity', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(235)
ax1.plot(poro[:sample_number], totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =1,label = "5 year")
ax1.plot(poro[sample_number:sample_number*2], totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1,label = "10 year")
ax1.plot(poro[sample_number*2:sample_number*3], totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1,label = "15 year")
ax1.plot(poro[sample_number*3:sample_number*4], totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1,label = "20 year")
ax1.plot(poro[sample_number*4:sample_number*5], totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1,label = "25 year")
ax1.plot(poro[sample_number*5:sample_number*6], totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1,label = "30 year")
ax1.plot(poro[sample_number*6:sample_number*7], totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1,label = "35 year")
ax1.plot(poro[sample_number*7:sample_number*8], totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1,label = "40 year")
ax1.plot(poro[sample_number*8:sample_number*9], totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1,label = "45 year")
ax1.plot(poro[sample_number*9:sample_number*10], totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1,label = "50 year")
ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
ax1.set_xlabel('Porosity', fontsize=12)
ax1.set_ylim([4, 40]);
ax1.legend(loc=1,ncol=2,fontsize=12.0)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(236)

# ax2.set_xlim([145, 175]);
# ax2.set_ylim([0, 5]);
ax1.plot(poro[:sample_number], Dynamic_reservoir_storage_capacity[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number:sample_number*2], Dynamic_reservoir_storage_capacity[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*2:sample_number*3], Dynamic_reservoir_storage_capacity[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*3:sample_number*4], Dynamic_reservoir_storage_capacity[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*4:sample_number*5], Dynamic_reservoir_storage_capacity[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*5:sample_number*6], Dynamic_reservoir_storage_capacity[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*6:sample_number*7], Dynamic_reservoir_storage_capacity[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*7:sample_number*8], Dynamic_reservoir_storage_capacity[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*8:sample_number*9], Dynamic_reservoir_storage_capacity[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(poro[sample_number*9:sample_number*10], Dynamic_reservoir_storage_capacity[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Dynamic reservoir capacity (MtCO2)',color='blue', fontsize=12);
ax1.set_xlabel('Porosity', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='blue')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='k')

ax2 = ax1.twinx() # this is the important function
ax2.scatter(poro, Static_reservoir_storage_capacity, color='k',s=1.5)
ax2.set_ylabel('Static reservoir capacity (MtCO2)',color='k',fontsize=12.0);
ax2.yaxis.set_tick_params(labelsize=12.0,colors='k')
ax2.spines['right'].set_color('k')
ax2.spines['left'].set_color('blue')




fig = plt.figure(figsize=(15,7))
ax1 = fig.add_subplot(231)
ax1.plot(Thick[:sample_number], injection3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number:sample_number*2], injection3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*2:sample_number*3], injection3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*3:sample_number*4], injection3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*4:sample_number*5], injection3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*5:sample_number*6], injection3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*6:sample_number*7], injection3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*7:sample_number*8], injection3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*8:sample_number*9], injection3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*9:sample_number*10], injection3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Injection rate (MtCO2/yr)',color='k', fontsize=12);
ax1.set_xlabel('Thickness (m)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(232)
ax1.plot(Thick[:sample_number], radius2[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number:sample_number*2], radius2[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*2:sample_number*3], radius2[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*3:sample_number*4], radius2[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*4:sample_number*5], radius2[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*5:sample_number*6], radius2[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*6:sample_number*7], radius2[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*7:sample_number*8], radius2[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*8:sample_number*9], radius2[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*9:sample_number*10], radius2[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Plume radius (km)',color='k', fontsize=12);
ax1.set_xlabel('Thickness (m)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(233)
ax1.plot(Thick[:sample_number], volume3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number:sample_number*2], volume3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*2:sample_number*3], volume3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*3:sample_number*4], volume3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*4:sample_number*5], volume3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*5:sample_number*6], volume3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*6:sample_number*7], volume3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*7:sample_number*8], volume3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*8:sample_number*9], volume3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*9:sample_number*10], volume3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Plume volume (Mm3)',color='k', fontsize=12);
ax1.set_xlabel('Thickness (m)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(234)
ax1.plot(Thick[:sample_number], numberOfWells[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number:sample_number*2], numberOfWells[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*2:sample_number*3], numberOfWells[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*3:sample_number*4], numberOfWells[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*4:sample_number*5], numberOfWells[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*5:sample_number*6], numberOfWells[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*6:sample_number*7], numberOfWells[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*7:sample_number*8], numberOfWells[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*8:sample_number*9], numberOfWells[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*9:sample_number*10], numberOfWells[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Number of wells',color='k', fontsize=12);
ax1.set_xlabel('Thickness (m)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(235)
ax1.plot(Thick[:sample_number], totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =1,label = "5 year")
ax1.plot(Thick[sample_number:sample_number*2], totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1,label = "10 year")
ax1.plot(Thick[sample_number*2:sample_number*3], totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1,label = "15 year")
ax1.plot(Thick[sample_number*3:sample_number*4], totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1,label = "20 year")
ax1.plot(Thick[sample_number*4:sample_number*5], totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1,label = "25 year")
ax1.plot(Thick[sample_number*5:sample_number*6], totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1,label = "30 year")
ax1.plot(Thick[sample_number*6:sample_number*7], totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1,label = "35 year")
ax1.plot(Thick[sample_number*7:sample_number*8], totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1,label = "40 year")
ax1.plot(Thick[sample_number*8:sample_number*9], totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1,label = "45 year")
ax1.plot(Thick[sample_number*9:sample_number*10], totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1,label = "50 year")
ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
ax1.set_xlabel('Thickness (m)', fontsize=12)
ax1.legend(loc=1,ncol=2,fontsize=12.0)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(236)

# ax2.set_xlim([145, 175]);
# ax2.set_ylim([0, 5]);
ax1.plot(Thick[:sample_number], Dynamic_reservoir_storage_capacity[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number:sample_number*2], Dynamic_reservoir_storage_capacity[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*2:sample_number*3], Dynamic_reservoir_storage_capacity[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*3:sample_number*4], Dynamic_reservoir_storage_capacity[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*4:sample_number*5], Dynamic_reservoir_storage_capacity[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*5:sample_number*6], Dynamic_reservoir_storage_capacity[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*6:sample_number*7], Dynamic_reservoir_storage_capacity[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*7:sample_number*8], Dynamic_reservoir_storage_capacity[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*8:sample_number*9], Dynamic_reservoir_storage_capacity[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
ax1.plot(Thick[sample_number*9:sample_number*10], Dynamic_reservoir_storage_capacity[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
ax1.set_ylabel('Dynamic reservoir capacity (MtCO2)',color='blue', fontsize=12);
ax1.set_xlabel('Thickness (m)', fontsize=12)
ax1.yaxis.set_tick_params(labelsize=12.0,colors='blue')
ax1.xaxis.set_tick_params(labelsize=12.0,colors='k')

ax2 = ax1.twinx() # this is the important function
ax2.scatter(Thick, Static_reservoir_storage_capacity, color='k',s=1.5)
ax2.set_ylabel('Static reservoir capacity (MtCO2)',color='k',fontsize=12.0);
ax2.yaxis.set_tick_params(labelsize=12.0,colors='k')
ax2.spines['right'].set_color('k')
ax2.spines['left'].set_color('blue')






# fig = plt.figure(figsize=(15,7))
# ax1 = fig.add_subplot(341)
# ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, injection3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, injection3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, injection3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, injection3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, injection3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, injection3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, injection3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, injection3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, injection3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, injection3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Well injection rate (MtCO2/yr)',color='k', fontsize=12);
# ax1.set_xlabel('Permeability (mD)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(342)
# ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, radius2[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, radius2[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, radius2[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, radius2[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, radius2[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, radius2[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, radius2[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, radius2[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, radius2[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, radius2[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Plume radius (km)',color='k', fontsize=12);
# ax1.set_xlabel('Permeability (mD)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(343)
# ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, volume3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, volume3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, volume3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, volume3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, volume3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, volume3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, volume3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, volume3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, volume3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, volume3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Plume volume (Mm3)',color='k', fontsize=12);
# ax1.set_xlabel('Permeability (mD)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(344)
# ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, numberOfWells[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, numberOfWells[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, numberOfWells[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, numberOfWells[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, numberOfWells[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, numberOfWells[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, numberOfWells[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, numberOfWells[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, numberOfWells[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, numberOfWells[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Number of wells',color='k', fontsize=12);
# ax1.set_xlabel('Permeability (mD)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(345)
# ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, reservoirStorageCapacity[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, reservoirStorageCapacity[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, reservoirStorageCapacity[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, reservoirStorageCapacity[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, reservoirStorageCapacity[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, reservoirStorageCapacity[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, reservoirStorageCapacity[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, reservoirStorageCapacity[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, reservoirStorageCapacity[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, reservoirStorageCapacity[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Total injection (MtCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Permeability (mD)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(346)
# ax1.plot(10**Permeability[:sample_number]/9.86923299999996E-16, totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =1,label = "5 year")
# ax1.plot(10**Permeability[sample_number:sample_number*2]/9.86923299999996E-16, totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1,label = "10 year")
# ax1.plot(10**Permeability[sample_number*2:sample_number*3]/9.86923299999996E-16, totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1,label = "15 year")
# ax1.plot(10**Permeability[sample_number*3:sample_number*4]/9.86923299999996E-16, totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1,label = "20 year")
# ax1.plot(10**Permeability[sample_number*4:sample_number*5]/9.86923299999996E-16, totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1,label = "25 year")
# ax1.plot(10**Permeability[sample_number*5:sample_number*6]/9.86923299999996E-16, totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1,label = "30 year")
# ax1.plot(10**Permeability[sample_number*6:sample_number*7]/9.86923299999996E-16, totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1,label = "35 year")
# ax1.plot(10**Permeability[sample_number*7:sample_number*8]/9.86923299999996E-16, totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1,label = "40 year")
# ax1.plot(10**Permeability[sample_number*8:sample_number*9]/9.86923299999996E-16, totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1,label = "45 year")
# ax1.plot(10**Permeability[sample_number*9:sample_number*10]/9.86923299999996E-16, totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1,label = "50 year")
# ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Permeability (mD)', fontsize=12)
# # ax1.legend(loc=1,ncol=2,fontsize=10.0)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# ax1 = fig.add_subplot(347)
# ax1.plot(poro[:sample_number], injection3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number:sample_number*2], injection3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*2:sample_number*3], injection3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*3:sample_number*4], injection3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*4:sample_number*5], injection3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*5:sample_number*6], injection3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*6:sample_number*7], injection3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*7:sample_number*8], injection3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*8:sample_number*9], injection3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*9:sample_number*10], injection3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Well injection rate (MtCO2/yr)',color='k', fontsize=12);
# ax1.set_xlabel('Porosity', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(348)
# ax1.plot(poro[:sample_number], radius2[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number:sample_number*2], radius2[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*2:sample_number*3], radius2[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*3:sample_number*4], radius2[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*4:sample_number*5], radius2[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*5:sample_number*6], radius2[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*6:sample_number*7], radius2[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*7:sample_number*8], radius2[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*8:sample_number*9], radius2[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*9:sample_number*10], radius2[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Plume radius (km)',color='k', fontsize=12);
# ax1.set_xlabel('Porosity', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(349)
# ax1.plot(poro[:sample_number], volume3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number:sample_number*2], volume3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*2:sample_number*3], volume3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*3:sample_number*4], volume3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*4:sample_number*5], volume3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*5:sample_number*6], volume3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*6:sample_number*7], volume3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*7:sample_number*8], volume3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*8:sample_number*9], volume3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*9:sample_number*10], volume3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Plume volume (Mm3)',color='k', fontsize=12);
# ax1.set_xlabel('Porosity', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(3,4,10)
# ax1.plot(poro[:sample_number], numberOfWells[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number:sample_number*2], numberOfWells[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*2:sample_number*3], numberOfWells[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*3:sample_number*4], numberOfWells[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*4:sample_number*5], numberOfWells[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*5:sample_number*6], numberOfWells[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*6:sample_number*7], numberOfWells[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*7:sample_number*8], numberOfWells[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*8:sample_number*9], numberOfWells[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*9:sample_number*10], numberOfWells[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Number of wells',color='k', fontsize=12);
# ax1.set_xlabel('Porosity', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(3,4,11)
# ax1.plot(poro[:sample_number], reservoirStorageCapacity[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number:sample_number*2], reservoirStorageCapacity[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*2:sample_number*3], reservoirStorageCapacity[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*3:sample_number*4], reservoirStorageCapacity[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*4:sample_number*5], reservoirStorageCapacity[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*5:sample_number*6], reservoirStorageCapacity[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*6:sample_number*7], reservoirStorageCapacity[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*7:sample_number*8], reservoirStorageCapacity[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*8:sample_number*9], reservoirStorageCapacity[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(poro[sample_number*9:sample_number*10], reservoirStorageCapacity[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Total injection (MtCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Porosity', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(3,4,12)
# ax1.plot(poro[:sample_number], totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =1,label = "5 year")
# ax1.plot(poro[sample_number:sample_number*2], totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1,label = "10 year")
# ax1.plot(poro[sample_number*2:sample_number*3], totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1,label = "15 year")
# ax1.plot(poro[sample_number*3:sample_number*4], totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1,label = "20 year")
# ax1.plot(poro[sample_number*4:sample_number*5], totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1,label = "25 year")
# ax1.plot(poro[sample_number*5:sample_number*6], totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1,label = "30 year")
# ax1.plot(poro[sample_number*6:sample_number*7], totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1,label = "35 year")
# ax1.plot(poro[sample_number*7:sample_number*8], totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1,label = "40 year")
# ax1.plot(poro[sample_number*8:sample_number*9], totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1,label = "45 year")
# ax1.plot(poro[sample_number*9:sample_number*10], totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1,label = "50 year")
# ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Porosity', fontsize=12)
# # ax1.legend(loc=1,ncol=2,fontsize=10.0)
# ax1.set_ylim([0, 40]);
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')



# fig = plt.figure(figsize=(15,7))
# ax1 = fig.add_subplot(341)
# ax1.plot(Geothermal_gradient[:sample_number], injection3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number:sample_number*2], injection3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], injection3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], injection3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], injection3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], injection3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], injection3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], injection3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], injection3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], injection3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Well injection rate (MtCO2/yr)',color='k', fontsize=12);
# ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(342)
# ax1.plot(Geothermal_gradient[:sample_number], radius2[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number:sample_number*2], radius2[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], radius2[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], radius2[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], radius2[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], radius2[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], radius2[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], radius2[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], radius2[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], radius2[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Plume radius (km)',color='k', fontsize=12);
# ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(343)
# ax1.plot(Geothermal_gradient[:sample_number], volume3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number:sample_number*2], volume3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], volume3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], volume3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], volume3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], volume3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], volume3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], volume3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], volume3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], volume3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Plume volume (Mm3)',color='k', fontsize=12);
# ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(344)
# ax1.plot(Geothermal_gradient[:sample_number], numberOfWells[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number:sample_number*2], numberOfWells[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], numberOfWells[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], numberOfWells[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], numberOfWells[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], numberOfWells[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], numberOfWells[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], numberOfWells[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], numberOfWells[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], numberOfWells[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Number of wells',color='k', fontsize=12);
# ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(345)
# ax1.plot(Geothermal_gradient[:sample_number], reservoirStorageCapacity[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number:sample_number*2], reservoirStorageCapacity[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], reservoirStorageCapacity[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], reservoirStorageCapacity[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], reservoirStorageCapacity[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], reservoirStorageCapacity[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], reservoirStorageCapacity[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], reservoirStorageCapacity[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], reservoirStorageCapacity[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], reservoirStorageCapacity[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Total injection (MtCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(346)
# ax1.plot(Geothermal_gradient[:sample_number], totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =1,label = "5 year")
# ax1.plot(Geothermal_gradient[sample_number:sample_number*2], totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1,label = "10 year")
# ax1.plot(Geothermal_gradient[sample_number*2:sample_number*3], totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1,label = "15 year")
# ax1.plot(Geothermal_gradient[sample_number*3:sample_number*4], totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1,label = "20 year")
# ax1.plot(Geothermal_gradient[sample_number*4:sample_number*5], totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1,label = "25 year")
# ax1.plot(Geothermal_gradient[sample_number*5:sample_number*6], totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1,label = "30 year")
# ax1.plot(Geothermal_gradient[sample_number*6:sample_number*7], totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1,label = "35 year")
# ax1.plot(Geothermal_gradient[sample_number*7:sample_number*8], totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1,label = "40 year")
# ax1.plot(Geothermal_gradient[sample_number*8:sample_number*9], totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1,label = "45 year")
# ax1.plot(Geothermal_gradient[sample_number*9:sample_number*10], totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1,label = "50 year")
# ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Geothermal gradient (°C/km)', fontsize=12)
# # ax1.legend(loc=1,ncol=2,fontsize=10.0)
# ax1.set_ylim([4, 15]);
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# ax1 = fig.add_subplot(347)
# ax1.plot(Depth[:sample_number], injection3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number:sample_number*2], injection3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*2:sample_number*3], injection3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*3:sample_number*4], injection3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*4:sample_number*5], injection3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*5:sample_number*6], injection3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*6:sample_number*7], injection3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*7:sample_number*8], injection3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*8:sample_number*9], injection3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*9:sample_number*10], injection3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Well injection rate (MtCO2/yr)',color='k', fontsize=12);
# ax1.set_xlabel('Depth (m)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(348)
# ax1.plot(Depth[:sample_number], radius2[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number:sample_number*2], radius2[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*2:sample_number*3], radius2[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*3:sample_number*4], radius2[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*4:sample_number*5], radius2[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*5:sample_number*6], radius2[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*6:sample_number*7], radius2[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*7:sample_number*8], radius2[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*8:sample_number*9], radius2[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*9:sample_number*10], radius2[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Plume radius (km)',color='k', fontsize=12);
# ax1.set_xlabel('Depth (m)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(349)
# ax1.plot(Depth[:sample_number], volume3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number:sample_number*2], volume3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*2:sample_number*3], volume3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*3:sample_number*4], volume3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*4:sample_number*5], volume3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*5:sample_number*6], volume3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*6:sample_number*7], volume3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*7:sample_number*8], volume3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*8:sample_number*9], volume3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*9:sample_number*10], volume3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Plume volume (Mm3)',color='k', fontsize=12);
# ax1.set_xlabel('Depth (m)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(3,4,10)
# ax1.plot(Depth[:sample_number], numberOfWells[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number:sample_number*2], numberOfWells[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*2:sample_number*3], numberOfWells[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*3:sample_number*4], numberOfWells[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*4:sample_number*5], numberOfWells[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*5:sample_number*6], numberOfWells[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*6:sample_number*7], numberOfWells[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*7:sample_number*8], numberOfWells[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*8:sample_number*9], numberOfWells[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*9:sample_number*10], numberOfWells[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Number of wells',color='k', fontsize=12);
# ax1.set_xlabel('Depth (m)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(3,4,11)
# ax1.plot(Depth[:sample_number], reservoirStorageCapacity[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number:sample_number*2], reservoirStorageCapacity[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*2:sample_number*3], reservoirStorageCapacity[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*3:sample_number*4], reservoirStorageCapacity[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*4:sample_number*5], reservoirStorageCapacity[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*5:sample_number*6], reservoirStorageCapacity[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*6:sample_number*7], reservoirStorageCapacity[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*7:sample_number*8], reservoirStorageCapacity[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*8:sample_number*9], reservoirStorageCapacity[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Depth[sample_number*9:sample_number*10], reservoirStorageCapacity[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Total injection (MtCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Depth (m)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(3,4,12)
# ax1.plot(Depth[:sample_number], totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =1,label = "5 year")
# ax1.plot(Depth[sample_number:sample_number*2], totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1,label = "10 year")
# ax1.plot(Depth[sample_number*2:sample_number*3], totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1,label = "15 year")
# ax1.plot(Depth[sample_number*3:sample_number*4], totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1,label = "20 year")
# ax1.plot(Depth[sample_number*4:sample_number*5], totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1,label = "25 year")
# ax1.plot(Depth[sample_number*5:sample_number*6], totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1,label = "30 year")
# ax1.plot(Depth[sample_number*6:sample_number*7], totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1,label = "35 year")
# ax1.plot(Depth[sample_number*7:sample_number*8], totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1,label = "40 year")
# ax1.plot(Depth[sample_number*8:sample_number*9], totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1,label = "45 year")
# ax1.plot(Depth[sample_number*9:sample_number*10], totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1,label = "50 year")
# ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Depth (m)', fontsize=12)
# # ax1.legend(loc=1,ncol=2,fontsize=10.0)
# ax1.set_ylim([4, 12]);
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


# fig = plt.figure(figsize=(15,7))
# ax1 = fig.add_subplot(341)
# ax1.plot(Thick[:sample_number], injection3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number:sample_number*2], injection3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*2:sample_number*3], injection3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*3:sample_number*4], injection3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*4:sample_number*5], injection3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*5:sample_number*6], injection3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*6:sample_number*7], injection3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*7:sample_number*8], injection3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*8:sample_number*9], injection3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*9:sample_number*10], injection3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Well injection rate (MtCO2/yr)',color='k', fontsize=12);
# ax1.set_xlabel('Thickness (m)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(342)
# ax1.plot(Thick[:sample_number], radius2[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number:sample_number*2], radius2[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*2:sample_number*3], radius2[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*3:sample_number*4], radius2[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*4:sample_number*5], radius2[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*5:sample_number*6], radius2[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*6:sample_number*7], radius2[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*7:sample_number*8], radius2[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*8:sample_number*9], radius2[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*9:sample_number*10], radius2[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Plume radius (km)',color='k', fontsize=12);
# ax1.set_xlabel('Thickness (m)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(343)
# ax1.plot(Thick[:sample_number], volume3[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number:sample_number*2], volume3[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*2:sample_number*3], volume3[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*3:sample_number*4], volume3[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*4:sample_number*5], volume3[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*5:sample_number*6], volume3[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*6:sample_number*7], volume3[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*7:sample_number*8], volume3[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*8:sample_number*9], volume3[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*9:sample_number*10], volume3[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Plume volume (Mm3)',color='k', fontsize=12);
# ax1.set_xlabel('Thickness (m)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(344)
# ax1.plot(Thick[:sample_number], numberOfWells[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number:sample_number*2], numberOfWells[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*2:sample_number*3], numberOfWells[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*3:sample_number*4], numberOfWells[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*4:sample_number*5], numberOfWells[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*5:sample_number*6], numberOfWells[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*6:sample_number*7], numberOfWells[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*7:sample_number*8], numberOfWells[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*8:sample_number*9], numberOfWells[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*9:sample_number*10], numberOfWells[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Number of wells',color='k', fontsize=12);
# ax1.set_xlabel('Thickness (m)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')


# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(345)
# ax1.plot(Thick[:sample_number], reservoirStorageCapacity[:sample_number], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number:sample_number*2], reservoirStorageCapacity[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*2:sample_number*3], reservoirStorageCapacity[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*3:sample_number*4], reservoirStorageCapacity[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*4:sample_number*5], reservoirStorageCapacity[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*5:sample_number*6], reservoirStorageCapacity[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*6:sample_number*7], reservoirStorageCapacity[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*7:sample_number*8], reservoirStorageCapacity[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*8:sample_number*9], reservoirStorageCapacity[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1)
# ax1.plot(Thick[sample_number*9:sample_number*10], reservoirStorageCapacity[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1)
# # ax1.set_xlabel('Geo-thermal gradient (°C/km)', fontsize=12)
# ax1.set_ylabel('Total injection (MtCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Thickness (m)', fontsize=12)
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

# # fig = plt.figure(figsize=(9,6))
# ax1 = fig.add_subplot(346)
# ax1.plot(Thick[:sample_number], totalCost[:sample_number], 'o',markerfacecolor='none',MarkerSize =1,label = "5 year")
# ax1.plot(Thick[sample_number:sample_number*2], totalCost[sample_number:sample_number*2], 'o',markerfacecolor='none',MarkerSize =1,label = "10 year")
# ax1.plot(Thick[sample_number*2:sample_number*3], totalCost[sample_number*2:sample_number*3], 'o',markerfacecolor='none',MarkerSize =1,label = "15 year")
# ax1.plot(Thick[sample_number*3:sample_number*4], totalCost[sample_number*3:sample_number*4], 'o',markerfacecolor='none',MarkerSize =1,label = "20 year")
# ax1.plot(Thick[sample_number*4:sample_number*5], totalCost[sample_number*4:sample_number*5], 'o',markerfacecolor='none',MarkerSize =1,label = "25 year")
# ax1.plot(Thick[sample_number*5:sample_number*6], totalCost[sample_number*5:sample_number*6], 'o',markerfacecolor='none',MarkerSize =1,label = "30 year")
# ax1.plot(Thick[sample_number*6:sample_number*7], totalCost[sample_number*6:sample_number*7], 'o',markerfacecolor='none',MarkerSize =1,label = "35 year")
# ax1.plot(Thick[sample_number*7:sample_number*8], totalCost[sample_number*7:sample_number*8], 'o',markerfacecolor='none',MarkerSize =1,label = "40 year")
# ax1.plot(Thick[sample_number*8:sample_number*9], totalCost[sample_number*8:sample_number*9], 'o',markerfacecolor='none',MarkerSize =1,label = "45 year")
# ax1.plot(Thick[sample_number*9:sample_number*10], totalCost[sample_number*9:sample_number*10], 'o',markerfacecolor='none',MarkerSize =1,label = "50 year")
# ax1.set_ylabel('Total cost ($/tCO2)',color='k', fontsize=12);
# ax1.set_xlabel('Thickness (m)', fontsize=12)
# ax1.legend(loc=1,ncol=2,fontsize=10.0)
# # ax1.set_ylim([4, 15]);
# ax1.yaxis.set_tick_params(labelsize=12.0,colors='black')
# ax1.xaxis.set_tick_params(labelsize=12.0,colors='black')

import matplotlib.pyplot as plt
fig, axe = plt.subplots(figsize = (8, 5))
axe.hist(totalCost,bins=1000)
axe.set_xlabel('Total cost ($/tCO2)',color='k', fontsize=16);
axe.set_ylabel('Count', fontsize=16)
axe.set_xlim([4, 15]);
plt.show()