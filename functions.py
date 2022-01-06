# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 09:31:14 2021

@author: mengm
"""


# All Reduced Order Model (ROM) sub-routines are at the bottom of this module
# PRESSURE-CONTROLLED ROMs FOR PLUME AREA (normal-space values)

import numpy as np
import random 

def pmax (x1, x2):
    pmax=np.maximum(x1,x2)
    return pmax

def random_list(start, stop, length):
    start, stop = (start, stop) if start <= stop else (stop, start)
    length = abs (length) if length else 0
    random_list = []
    for i in range (length):
        random_list.append(random.uniform(start,stop))
    random_list=np.asarray(random_list)
    return random_list


# CO2 injection ROM trained on data with 0 to 0.1 MtCO2/yr injection rate, 30 years, based on PRESSURE input data (the only PRESSURE data that failed were ones with super-high injection rates)

def ROM_A_Pressure_Injection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_A_Pressure_Injection_30yr = 2772970000 + 15658600 * pmax(0, thick - 90) - 51516200 * pmax(0, 90 - thick) + 2491650 * pmax(0, depth - 1105.76) \
        - 3438880 * pmax(0, 1105.76 - depth) + 3920800000 * pmax(0, perm + 14.9223) - 4080960000 * pmax(0, -14.9223 - perm) + 2598970 * thick * pmax(0, 90 - thick) \
        + 1380.99 * pmax(0, depth - 1100.28) * thick * pmax(0, 90 - thick) - 6576270000 * pmax(0, 0.046341 - geoGrad) + 14263800 * pmax(0, perm + 13.9701) * thick * pmax(0, 90 - thick) \
        - 3872750 * pmax(0, -13.9701 - perm) * thick * pmax(0, 90 - thick) + 5017.16 * pmax(0, perm + 14.4797) * pmax(0, depth - 1100.28) * thick * pmax(0, 90 - thick) - 1821.53 * pmax(0, -14.4797 - perm) * pmax(0, depth - 1100.28) * thick * pmax(0, 90 - thick) \
        + 10413.8 * pmax(0, geoGrad - 0.0284601) * pmax(0, depth - 1100.28) * thick * pmax(0, 90 - thick) - 19869.5 * pmax(0, 0.0284601 - geoGrad) * pmax(0, depth - 1100.28) * thick * pmax(0, 90 - thick) \
        - 27392 * pmax(0, depth - 1655.41) * pmax(0, 90 - thick) + 29137.2 * pmax(0, 1655.41 - depth) * pmax(0, 90 - thick) - 34174200 * pmax(0, perm + 14.762) * pmax(0, 90 - thick) \
        + 91054700 * pmax(0, -14.762 - perm) * pmax(0, 90 - thick) - 5798760 * pmax(0, perm + 14.472) * pmax(0, -13.9701 - perm) * thick * pmax(0, 90 - thick) + 2586040 * pmax(0, -14.472 - perm) * pmax(0, -13.9701 - perm) * thick * pmax(0, 90 - thick) \
        - 1188420000 * geoGrad * pmax(0, -14.762 - perm) * pmax(0, 90 - thick) + 359373 * pmax(0, depth - 1575.51) * pmax(0, perm + 14.9223) - 807132 * pmax(0, 1575.51 - depth) * pmax(0, perm + 14.9223)\
        + 4145420 * pmax(0, geoGrad - 0.0300566) * thick * pmax(0, 90 - thick) - 23528100 * pmax(0, 0.0300566 - geoGrad) * thick * pmax(0, 90 - thick) - 4721480000 * pmax(0, perm + 14.788) * pmax(0, 0.046341 - geoGrad) \
        - 62995000000 * pmax(0, -14.788 - perm) * pmax(0, 0.046341 - geoGrad) + 0.036448 * pmax(0, depth - 3452.13) * pmax(0, depth - 1100.28) * thick * pmax(0, 90 - thick) - 0.0982414 * pmax(0, 3452.13 - depth) * pmax(0, depth - 1100.28) * thick * pmax(0, 90 - thick) \
        - 372584000 * pmax(0, perm + 13.9701) * pmax(0, 0.0300566 - geoGrad) * thick * pmax(0, 90 - thick) + 21378000 * pmax(0, -13.9701 - perm) * pmax(0, 0.0300566 - geoGrad) * thick * pmax(0, 90 - thick)
    ROM_A_Pressure_Injection_30yr = ROM_A_Pressure_Injection_30yr / 1000000000 / 30  
    return ROM_A_Pressure_Injection_30yr


# CO2 injection ROM trained on data with 0.05 to 0.5 MtCO2/yr injection rate, 30 years, based on PRESSURE input data (the only PRESSURE data that failed were ones with super-high injection rates)


def ROM_B_Pressure_Injection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_B_Pressure_Injection_30yr = 666118000000 + 45174300000 * perm + 423425000000 * thick \
        + 12084200 * pmax(0, depth - 3381.79) * thick - 62386200 * pmax(0, 3381.79 - depth) * thick \
        + 30185000000 * thick * perm + 839422 * pmax(0, depth - 3381.79) * thick * perm \
        - 4436400 * pmax(0, 3381.79 - depth) * thick * perm - 1244540000 * pmax(0, geoGrad - 0.0371514) * perm \
        - 1515670000 * pmax(0, 0.0371514 - geoGrad) * perm + 2989950000 * pmax(0, perm + 14.7285) * perm \
        - 2932320000 * pmax(0, -14.7285 - perm) * perm - 136281 * pmax(0, depth - 3774.14) * pmax(0, perm + 14.7285) * perm \
        + 91844 * pmax(0, 3774.14 - depth) * pmax(0, perm + 14.7285) * perm + 1901650000 * pmax(0, perm + 13.9893) * thick * perm \
        - 1877460000 * pmax(0, -13.9893 - perm) * thick * perm - 213702 * pmax(0, perm + 13.9561) * pmax(0, 3381.79 - depth) * thick * perm \
        + 232200 * pmax(0, -13.9561 - perm) * pmax(0, 3381.79 - depth) * thick * perm + 1422140 * pmax(0, depth - 1423.6) * pmax(0, 0.0371514 - geoGrad) * perm \
        - 5654920 * pmax(0, 1423.6 - depth) * pmax(0, 0.0371514 - geoGrad) * perm + 72621.1 * thick * pmax(0, depth - 1423.6) * pmax(0, 0.0371514 - geoGrad) * perm \
        + 8625040000 * pmax(0, perm + 14.4494) * pmax(0, 0.0371514 - geoGrad) * perm - 13.5332 * pmax(0, depth - 1490.66) * pmax(0, 3381.79 - depth) * thick \
        + 51.6152 * pmax(0, 1490.66 - depth) * pmax(0, 3381.79 - depth) * thick + 73958700000 * pmax(0, geoGrad - 0.027274) * thick \
        - 174393000000 * pmax(0, 0.027274 - geoGrad) * thick - 74317200 * pmax(0, perm + 14.9341) * pmax(0, -13.9893 - perm) * thick * perm \
        + 81837100 * pmax(0, -14.9341 - perm) * pmax(0, -13.9893 - perm) * thick * perm - 38124.1 * pmax(0, depth - 1461.17) * pmax(0, -13.9893 - perm) * thick * perm \
        + 45585.9 * pmax(0, 1461.17 - depth) * pmax(0, -13.9893 - perm) * thick * perm + 4880710000 * pmax(0, geoGrad - 0.027274) * thick * perm \
        - 11613200000 * pmax(0, 0.027274 - geoGrad) * thick * perm - 3218270 * pmax(0, depth - 2105.99) * pmax(0, -14.4494 - perm) * pmax(0, 0.0371514 - geoGrad) * perm \
        + 15285500 * pmax(0, 2105.99 - depth) * pmax(0, -14.4494 - perm) * pmax(0, 0.0371514 - geoGrad) * perm - 16590600 * pmax(0, geoGrad - 0.0263619) * pmax(0, 3381.79 - depth) * thick \
        + 55644900 * pmax(0, 0.0263619 - geoGrad) * pmax(0, 3381.79 - depth) * thick - 1070440 * pmax(0, geoGrad - 0.0263619) * pmax(0, 3381.79 - depth) * thick * perm \
        + 3686360 * pmax(0, 0.0263619 - geoGrad) * pmax(0, 3381.79 - depth) * thick * perm
    ROM_B_Pressure_Injection_30yr = ROM_B_Pressure_Injection_30yr / 1000000000 / 30
    return ROM_B_Pressure_Injection_30yr

# CO2 injection ROM trained on data with 0.1 to 1 MtCO2/yr injection rate, 30 years, based on PRESSURE input data (the only PRESSURE data that failed were ones with super-high injection rates)

def ROM_C_Pressure_Injection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_C_Pressure_Injection_30yr = 1764300000000 + 123234000000 * perm + 870751000 * thick - 68732.1 * pmax(0, depth - 2656.39) * perm \
        + 40444 * pmax(0, 2656.39 - depth) * perm - 7778180 * thick * thick + 84923.6 * thick * thick * thick - 1087620000 * pmax(0, geoGrad - 0.0282262) * perm \
        + 17873500000 * pmax(0, 0.0282262 - geoGrad) * perm - 329.542 * thick * thick * thick * thick - 190247 * pmax(0, -14.4473 - perm) * pmax(0, 2656.39 - depth) * perm \
        - 512939 * pmax(0, depth - 1251.72) * thick - 378362 * pmax(0, 1251.72 - depth) * thick + 1799160000 * pmax(0, perm + 13.5403) * thick \
        - 401927000 * pmax(0, -13.5403 - perm) * thick + 2359560 * pmax(0, perm + 14.1926) * pmax(0, depth - 1251.72) * thick - 1693440 * pmax(0, -14.1926 - perm) * pmax(0, depth - 1251.72) * thick \
        - 477908000 * pmax(0, perm + 14.8441) * pmax(0, -13.5403 - perm) * thick + 248038000 * pmax(0, -14.8441 - perm) * pmax(0, -13.5403 - perm) * thick + 8812520000 * pmax(0, perm + 14.3203) * perm \
        - 7849030000 * pmax(0, -14.3203 - perm) * perm + 2089440 * pmax(0, geoGrad - 0.0192943) * pmax(0, depth - 1251.72) * thick - 2757730 * pmax(0, 0.0192943 - geoGrad) * pmax(0, depth - 1251.72) * thick \
        + 12236900 * pmax(0, perm + 14.4202) * pmax(0, geoGrad - 0.0192943) * pmax(0, depth - 1251.72) * thick - 2704490 * pmax(0, -14.4202 - perm) * pmax(0, geoGrad - 0.0192943) * pmax(0, depth - 1251.72) * thick \
        + 1151550 * pmax(0, depth - 1263.09) * pmax(0, -13.5403 - perm) * thick + 177762 * pmax(0, 1263.09 - depth) * pmax(0, -13.5403 - perm) * thick - 1316010 * pmax(0, perm + 14.1723) * pmax(0, depth - 1263.09) * pmax(0, -13.5403 - perm) * thick \
        + 202418 * pmax(0, -14.1723 - perm) * pmax(0, depth - 1263.09) * pmax(0, -13.5403 - perm) * thick + 172755 * pmax(0, 1888.58 - depth) * pmax(0, perm + 14.8441) * pmax(0, -13.5403 - perm) * thick - 17502000000 * pmax(0, -13.6182 - perm) * pmax(0, 0.0282262 - geoGrad) * perm \
        - 122264000 * pmax(0, perm + 14.2822) * pmax(0, perm + 14.8441) * pmax(0, -13.5403 - perm) * thick + 329304000 * pmax(0, -14.2822 - perm) * pmax(0, perm + 14.8441) * pmax(0, -13.5403 - perm) * thick \
        - 111051 * pmax(0, depth - 1148.76) * pmax(0, perm + 14.3203) * perm + 1237830 * pmax(0, 1148.76 - depth) * pmax(0, perm + 14.3203) * perm - 1305630000 * pmax(0, 0.0335429 - geoGrad) * thick
    ROM_C_Pressure_Injection_30yr = ROM_C_Pressure_Injection_30yr / 1000000000 / 30
    return ROM_C_Pressure_Injection_30yr

# CO2 injection ROM trained on data with 0.5 to 5 MtCO2/yr injection rate, 30 years, based on PRESSURE input data (the only PRESSURE data that failed were ones with super-high injection rates)

def ROM_D_Pressure_Injection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_D_Pressure_Injection_30yr = -12213400000 + 36199900000 * pmax(0, perm + 13.9918) \
        - 9181900000 * pmax(0, -13.9918 - perm) + 6962000000 * thick + 43547000 * pmax(0, 2547.14 - depth) - 50406000 * thick * thick \
        + 378800 * thick * thick * thick - 1383.02 * thick * thick * thick * thick \
        + 28753400000 * pmax(0, perm + 12.9709) * thick - 3967010000 * pmax(0, -12.9709 - perm) * thick \
        + 4372130 * pmax(0, perm + 14.657) * pmax(0, depth - 2547.14) - 38175000 * pmax(0, -14.657 - perm) * pmax(0, depth - 2547.14) \
        + 998845 * thick * pmax(0, perm + 14.657) * pmax(0, depth - 2547.14) + 3101270 * pmax(0, perm + 13.6228) * thick * pmax(0, perm + 14.657) * pmax(0, depth - 2547.14) \
        - 865014 * pmax(0, -13.6228 - perm) * thick * pmax(0, perm + 14.657) * pmax(0, depth - 2547.14) \
        - 203868000 * pmax(0, perm + 12.9567) * thick * thick + 13672900 * pmax(0, -12.9567 - perm) * thick * thick \
        + 4903.05 * pmax(0, 1310.42 - depth) * pmax(0, 2547.14 - depth) + 2901740 * pmax(0, geoGrad - 0.038072) * thick * pmax(0, perm + 14.657) * pmax(0, depth - 2547.14) \
        - 14268800 * pmax(0, 0.038072 - geoGrad) * thick * pmax(0, perm + 14.657) * pmax(0, depth - 2547.14) \
        + 71728400 * pmax(0, perm + 13.421) * pmax(0, 2547.14 - depth) - 70698700 * pmax(0, -13.421 - perm) * pmax(0, 2547.14 - depth) \
        + 161022 * pmax(0, depth - 2603.24) * thick - 1563360 * pmax(0, 2603.24 - depth) * thick \
        - 2585240000 * pmax(0, perm + 14.2758) * pmax(0, -12.9709 - perm) * thick + 2183820000 * pmax(0, -14.2758 - perm) * pmax(0, -12.9709 - perm) * thick \
        - 9450500 * pmax(0, perm + 12.9847) * pmax(0, 2603.24 - depth) * thick + 1198600 * pmax(0, -12.9847 - perm) * pmax(0, 2603.24 - depth) * thick \
        - 26266300000 * pmax(0, 0.040658 - geoGrad) * pmax(0, perm + 14.2758) * pmax(0, -12.9709 - perm) * thick \
        - 4009650 * pmax(0, depth - 2496.86) * pmax(0, perm + 13.9918) - 102238000 * pmax(0, 2496.86 - depth) * pmax(0, perm + 13.9918) \
        + 818020000000 * pmax(0, geoGrad - 0.0223673) * pmax(0, perm + 13.9918) - 2048040000000 * pmax(0, 0.0223673 - geoGrad) * pmax(0, perm + 13.9918) \
        + 72675100000 * pmax(0, perm + 12.4828) * pmax(0, perm + 13.9918) - 23058800000 * pmax(0, -12.4828 - perm) * pmax(0, perm + 13.9918) \
        + 16700000 * pmax(0, perm + 13.9716) * pmax(0, -12.9567 - perm) * thick * thick - 9098310 * pmax(0, -13.9716 - perm) * pmax(0, -12.9567 - perm) * thick * thick \
        - 309027000 * pmax(0, geoGrad - 0.0234058) * pmax(0, 2547.14 - depth) + 1126180000 * pmax(0, 0.0234058 - geoGrad) * pmax(0, 2547.14 - depth) \
        - 8260690000 * pmax(0, poro - 0.168399) * pmax(0, perm + 13.9918) + 60615700000 * pmax(0, 0.168399 - poro) * pmax(0, perm + 13.9918) \
        + 3284010000 * pmax(0, geoGrad - 0.0240564) * thick - 9989180000 * pmax(0, 0.0240564 - geoGrad) * thick
    ROM_D_Pressure_Injection_30yr = ROM_D_Pressure_Injection_30yr / 1000000000 / 30
    return ROM_D_Pressure_Injection_30yr

# CO2 injection ROM trained on data with 1 to 10 MtCO2/yr injection rate, 30 years, based on PRESSURE input data (the only PRESSURE data that failed were ones with super-high injection rates)

def ROM_E_Pressure_Injection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_E_Pressure_Injection_30yr = -37418100000 + 62430600000 * pmax(0, perm + 13.7663) - 49588800000 * pmax(0, -13.7663 - perm) \
        + 4244020000 * thick + 10706500 * pmax(0, depth - 2752.37) - 15989800 * pmax(0, 2752.37 - depth) - 84366600 * thick * thick + 384547000000 * pmax(0, geoGrad - 0.0275567) \
        - 1168450000000 * pmax(0, 0.0275567 - geoGrad) + 816716 * thick * thick * thick - 2978.69 * thick * thick * thick * thick - 14390900 * pmax(0, perm + 13.3978) * pmax(0, 2752.37 - depth) \
        - 19572600 * pmax(0, -13.3978 - perm) * pmax(0, 2752.37 - depth) + 9245050000 * pmax(0, perm + 14.2393) * thick - 547510000 * pmax(0, -14.2393 - perm) * thick + 1909420 * pmax(0, depth - 2886.06) * pmax(0, perm + 14.2393) * thick \
        - 3806580 * pmax(0, 2886.06 - depth) * pmax(0, perm + 14.2393) * thick + 30616300000 * pmax(0, perm + 12.6807) * pmax(0, perm + 14.2393) * thick - 6897590000 * pmax(0, -12.6807 - perm) * pmax(0, perm + 14.2393) * thick \
        - 12512500 * pmax(0, perm + 12.6758) * pmax(0, 2886.06 - depth) * pmax(0, perm + 14.2393) * thick + 2677590 * pmax(0, -12.6758 - perm) * pmax(0, 2886.06 - depth) * pmax(0, perm + 14.2393) * thick \
        - 2464730000 * pmax(0, perm + 13.8227) * pmax(0, -12.6807 - perm) * pmax(0, perm + 14.2393) * thick + 3309200000 * pmax(0, -13.8227 - perm) * pmax(0, -12.6807 - perm) * pmax(0, perm + 14.2393) * thick \
        + 17203100000 * pmax(0, geoGrad - 0.0386452) * pmax(0, perm + 14.2393) * thick - 90065200000 * pmax(0, 0.0386452 - geoGrad) * pmax(0, perm + 14.2393) * thick - 33533800 * pmax(0, depth - 1630.3) * pmax(0, 0.0386452 - geoGrad) * pmax(0, perm + 14.2393) * thick \
        + 50375200 * pmax(0, 1630.3 - depth) * pmax(0, 0.0386452 - geoGrad) * pmax(0, perm + 14.2393) * thick + 3695010 * pmax(0, perm + 13.5665) * pmax(0, depth - 2886.06) * pmax(0, perm + 14.2393) * thick \
        - 1123810 * pmax(0, -13.5665 - perm) * pmax(0, depth - 2886.06) * pmax(0, perm + 14.2393) * thick + 791028000000 * pmax(0, perm + 12.2571) * pmax(0, 0.0386452 - geoGrad) * pmax(0, perm + 14.2393) * thick \
        + 62862800000 * pmax(0, -12.2571 - perm) * pmax(0, 0.0386452 - geoGrad) * pmax(0, perm + 14.2393) * thick - 44693000000 * pmax(0, poro - 0.152232) * pmax(0, perm + 13.7663) \
        + 200126000000 * pmax(0, 0.152232 - poro) * pmax(0, perm + 13.7663) + 3058.77 * pmax(0, depth - 1565.85) * thick * thick + 1843.77 * pmax(0, 1565.85 - depth) * thick * thick \
        + 1079050 * pmax(0, perm + 12.8918) * pmax(0, depth - 1565.85) * thick * thick - 1153.91 * pmax(0, -12.8918 - perm) * pmax(0, depth - 1565.85) * thick * thick \
        + 24228800000 * pmax(0, perm + 12.9253) * pmax(0, perm + 13.7663) - 55587000000 * pmax(0, -12.9253 - perm) * pmax(0, perm + 13.7663)
    ROM_E_Pressure_Injection_30yr = ROM_E_Pressure_Injection_30yr / 1000000000 / 30
    return ROM_E_Pressure_Injection_30yr

# CO2 injection ROM trained on data with 5 to 50 MtCO2/yr injection rate, 30 years, based on PRESSURE input data (the only PRESSURE data that failed were ones with super-high injection rates)

def ROM_F_Pressure_Injection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_F_Pressure_Injection_30yr = -143435000000 + 389622000000 * pmax(0, perm + 12.9374) - 453867000000 * pmax(0, -12.9374 - perm) + 21288800000 * thick + 91105700 * pmax(0, depth - 2404.97) \
        - 177036000 * pmax(0, 2404.97 - depth) - 362800000 * thick * thick + 1000900000000 * pmax(0, geoGrad - 0.0347305) - 4261530000000 * pmax(0, 0.0347305 - geoGrad) \
        + 3351680 * thick * thick * thick - 11804.5 * thick * thick * thick * thick - 71962700 * pmax(0, perm + 13.6145) * pmax(0, depth - 2404.97) \
        - 37789100 * pmax(0, -13.6145 - perm) * pmax(0, depth - 2404.97) + 5653030 * thick * pmax(0, perm + 13.6145) * pmax(0, depth - 2404.97) \
        + 2895030000 * pmax(0, perm + 13.308) * thick + 2652570 * pmax(0, depth - 1975.74) * pmax(0, perm + 13.308) * thick \
        - 9921130 * pmax(0, 1975.74 - depth) * pmax(0, perm + 13.308) * thick - 549373000 * pmax(0, geoGrad - 0.0256615) * pmax(0, depth - 1975.74) * pmax(0, perm + 13.308) * thick \
        + 317961000 * pmax(0, 0.0256615 - geoGrad) * pmax(0, depth - 1975.74) * pmax(0, perm + 13.308) * thick + 28151600 * pmax(0, perm + 12.6327) * pmax(0, depth - 1975.74) * pmax(0, perm + 13.308) * thick \
        - 11981300 * pmax(0, -12.6327 - perm) * pmax(0, depth - 1975.74) * pmax(0, perm + 13.308) * thick + 26716400000 * pmax(0, perm + 12.7617) * pmax(0, perm + 13.308) * thick \
        - 8050810000 * pmax(0, -12.7617 - perm) * pmax(0, perm + 13.308) * thick - 6866740000 * pmax(0, poro - 0.13216) * pmax(0, perm + 13.308) * thick \
        + 28834000000 * pmax(0, 0.13216 - poro) * pmax(0, perm + 13.308) * thick + 74852900000 * pmax(0, geoGrad - 0.0137038) * pmax(0, perm + 13.308) * thick \
        - 10803900 * pmax(0, perm + 12.202) * pmax(0, 1975.74 - depth) * pmax(0, perm + 13.308) * thick + 13163600 * pmax(0, -12.202 - perm) * pmax(0, 1975.74 - depth) * pmax(0, perm + 13.308) * thick \
        + 518304000 * pmax(0, depth - 1810.06) * pmax(0, geoGrad - 0.0137038) * pmax(0, perm + 13.308) * thick - 193013000 * pmax(0, 1810.06 - depth) * pmax(0, geoGrad - 0.0137038) * pmax(0, perm + 13.308) * thick \
        - 102035000 * pmax(0, perm + 12.7089) * thick * thick + 197759000000 * pmax(0, perm + 13.0614) * pmax(0, geoGrad - 0.0137038) * pmax(0, perm + 13.308) * thick \
        + 490695000000 * pmax(0, -13.0614 - perm) * pmax(0, geoGrad - 0.0137038) * pmax(0, perm + 13.308) * thick + 49039200 * pmax(0, geoGrad - 0.0347248) * thick * pmax(0, perm + 13.6145) * pmax(0, depth - 2404.97) \
        - 91842400 * pmax(0, 0.0347248 - geoGrad) * thick * pmax(0, perm + 13.6145) * pmax(0, depth - 2404.97)
    ROM_F_Pressure_Injection_30yr = ROM_F_Pressure_Injection_30yr / 1000000000 / 30
    return ROM_F_Pressure_Injection_30yr

# CO2 injection ROM trained on data with 10 to max MtCO2/yr injection rate, 30 years, based on PRESSURE input data (the only PRESSURE data that failed were ones with super-high injection rates)

def ROM_G_Pressure_Injection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_G_Pressure_Injection_30yr = 184441000000 - 1854040000000 * pmax(0, perm + 12.7203) - 979008000000 * pmax(0, -12.7203 - perm) \
        - 84979600 * pmax(0, 3118.57 - depth) * pmax(0, perm + 12.7203) + 124397000000 * thick * pmax(0, perm + 12.7203) + 40334700 * pmax(0, depth - 2165.37) * thick * pmax(0, perm + 12.7203) \
        - 24204600 * pmax(0, 2165.37 - depth) * thick * pmax(0, perm + 12.7203) - 296178 * thick * pmax(0, depth - 2165.37) * thick * pmax(0, perm + 12.7203) + 35309600 * pmax(0, depth - 2440.23) \
        - 380757000 * pmax(0, 2440.23 - depth) + 15316700000 * thick + 6362550000000 * pmax(0, geoGrad - 0.028452) - 22694500000000 * pmax(0, 0.028452 - geoGrad) \
        + 3012260000000 * pmax(0, perm + 12.6591) * pmax(0, perm + 12.7203) - 68284000 * thick * thick + 694197000 * pmax(0, geoGrad - 0.0205275) * pmax(0, depth - 2165.37) * thick * pmax(0, perm + 12.7203) \
        - 1383190000 * pmax(0, 0.0205275 - geoGrad) * pmax(0, depth - 2165.37) * thick * pmax(0, perm + 12.7203) - 20395000 * pmax(0, poro - 0.15296) * pmax(0, depth - 2165.37) * thick * pmax(0, perm + 12.7203) \
        + 76339800 * pmax(0, 0.15296 - poro) * pmax(0, depth - 2165.37) * thick * pmax(0, perm + 12.7203) + 2315120 * pmax(0, depth - 2440.23) * thick - 1048280 * pmax(0, 2440.23 - depth) * thick \
        + 11810500 * pmax(0, perm + 13.1855) * pmax(0, depth - 2440.23) * thick - 1595900 * pmax(0, -13.1855 - perm) * pmax(0, depth - 2440.23) * thick + 45091700 * pmax(0, perm + 12.0787) * pmax(0, depth - 2165.37) * thick * pmax(0, perm + 12.7203) \
        - 29459000 * pmax(0, -12.0787 - perm) * pmax(0, depth - 2165.37) * thick * pmax(0, perm + 12.7203) - 1571000000 * pmax(0, perm + 12.6834) * thick * thick - 11623000 * pmax(0, -12.6834 - perm) * thick * thick \
        + 7347920 * thick * pmax(0, perm + 12.6834) * thick * thick - 290364000000 * pmax(0, poro - 0.124595) + 1206420000000 * pmax(0, 0.124595 - poro)
    ROM_G_Pressure_Injection_30yr = ROM_G_Pressure_Injection_30yr / 1000000000 / 30
    return ROM_G_Pressure_Injection_30yr


# PRESSURE-CONTROLLED ROMs FOR PLUME AREA (log values)
# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 0 to Max MtCO2/yr

def ROM_0_Pressure_LogInjection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_0_Pressure_LogInjection_30yr = 10.7955 + 1.30612 * pmax(0, perm + 12.584) - 0.990253 * pmax(0, -12.584 - perm) + 0.0657643 * thick + 0.000180496 * pmax(0, depth - 2441.04) - 0.000280554 * pmax(0, 2441.04 - depth) - 0.00139314 * thick * thick + 0.0000137101 * thick * thick * thick + 4.63749 * pmax(0, geoGrad - 0.0267164) - 9.6099 * pmax(0, 0.0267164 - geoGrad) \
        - 0.0000000491835 * thick * thick * thick * thick - 0.0000817098 * pmax(0, perm + 12.6327) * thick * thick + 0.0000408885 * pmax(0, -12.6327 - perm) * thick * thick + 0.00000971813 * pmax(0, depth - 4245.39) * pmax(0, -12.584 - perm) - 0.00000241421 * pmax(0, 4245.39 - depth) * pmax(0, -12.584 - perm) - 0.000000131113 * pmax(0, 1861.76 - depth) * pmax(0, 2441.04 - depth) - 0.0000000216195 * pmax(0, depth - 4064.03) * pmax(0, depth - 2441.04) \
        + 0.0000000355813 * pmax(0, 4064.03 - depth) * pmax(0, depth - 2441.04) - 0.565969 * poro * pmax(0, perm + 12.584) - 0.0000121123 * pmax(0, perm + 14.0078) * pmax(0, 4245.39 - depth) * pmax(0, -12.584 - perm) + 0.00000221272 * pmax(0, -14.0078 - perm) * pmax(0, 4245.39 - depth) * pmax(0, -12.584 - perm) - 0.0000346914 * pmax(0, poro - 0.0791191) * pmax(0, perm + 14.0078) * pmax(0, 4245.39 - depth) * pmax(0, -12.584 - perm) \
        + 0.000422719 * pmax(0, 0.0791191 - poro) * pmax(0, perm + 14.0078) * pmax(0, 4245.39 - depth) * pmax(0, -12.584 - perm) - 0.000000336091 * thick * pmax(0, 4245.39 - depth) * pmax(0, -12.584 - perm) + 0.000737313 * pmax(0, perm + 12.981) * thick - 0.00215072 * pmax(0, -12.981 - perm) * thick + 0.000000534163 * pmax(0, perm + 12.5898) * thick * thick * thick - 0.000000205754 * pmax(0, -12.5898 - perm) * thick * thick * thick + 0.00573236 * pmax(0, 1801.31 - depth) * pmax(0, 0.0267164 - geoGrad) \
        - 0.102581 * pmax(0, perm + 13.2884) * pmax(0, -12.584 - perm) + 0.0200497 * pmax(0, -13.2884 - perm) * pmax(0, -12.584 - perm) - 0.00141468 * pmax(0, geoGrad - 0.0394397) * pmax(0, depth - 2441.04) - 0.000189541 * pmax(0, 0.0394397 - geoGrad) * pmax(0, depth - 2441.04) + 0.00116548 * pmax(0, 0.411007 - poro) * pmax(0, perm + 12.981) * thick - 0.00740018 * poro * pmax(0, 0.411007 - poro) * pmax(0, perm + 12.981) * thick \
        - 0.0426429 * pmax(0, poro - 0.220764) * pmax(0, -13.2884 - perm) * pmax(0, -12.584 - perm) + 0.0455365 * pmax(0, 0.220764 - poro) * pmax(0, -13.2884 - perm) * pmax(0, -12.584 - perm) - 0.108736 * pmax(0, poro - 0.166506) + 0.504414 * pmax(0, 0.166506 - poro) + 0.122445 * pmax(0, poro - 0.172188) * pmax(0, -12.584 - perm) - 0.353135 * pmax(0, 0.172188 - poro) * pmax(0, -12.584 - perm) \
        - 0.0000703989 * depth * pmax(0, perm + 12.584) + 0.000501759 * pmax(0, perm + 13.6585) * pmax(0, 0.0394397 - geoGrad) * pmax(0, depth - 2441.04) + 0.000149847 * depth * poro * pmax(0, perm + 12.584) + 0.00000000193705 * pmax(0, 4358.49 - depth) * pmax(0, -12.6327 - perm) * thick * thick
    ROM_0_Pressure_LogInjection_30yr = 10 ** ROM_0_Pressure_LogInjection_30yr / 1000000000 / 30
    return ROM_0_Pressure_LogInjection_30yr 
    
# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 0 to 0.1 MtCO2/yr
def ROM_1_Pressure_LogInjection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_1_Pressure_LogInjection_30yr = 8.59591 + 0.015587 * thick + 0.0000142795 * pmax(0, depth - 1754.41) * thick - 0.00000115625 * pmax(0, 1754.41 - depth) * thick + 0.947937 * pmax(0, perm + 14.5911) - 0.885917 * pmax(0, -14.5911 - perm) + 4.7154 * pmax(0, geoGrad - 0.0194368) - 8.42901 * pmax(0, 0.0194368 - geoGrad) + 0.00019654 * pmax(0, depth - 1826.12) \
        - 0.000452777 * pmax(0, 1826.12 - depth) - 0.0000878814 * pmax(0, thick - 90) * thick + 0.000644175 * pmax(0, 90 - thick) * thick - 0.0000149189 * thick * pmax(0, 90 - thick) * thick + 0.000000118253 * thick * thick * pmax(0, 90 - thick) * thick - 0.0000000265273 * pmax(0, depth - 2568.81) * pmax(0, depth - 1826.12) - 0.0000000850627 * pmax(0, 2568.81 - depth) * pmax(0, depth - 1826.12) - 0.00000000821374 * pmax(0, depth - 1754.41) * thick * pmax(0, 90 - thick) * thick \
        - 9.52831 * pmax(0, geoGrad - 0.0366303) * pmax(0, -14.5911 - perm) - 4.22929 * pmax(0, 0.0366303 - geoGrad) * pmax(0, -14.5911 - perm)
    ROM_1_Pressure_LogInjection_30yr = 10 ** ROM_1_Pressure_LogInjection_30yr / 1000000000 / 30
    return ROM_1_Pressure_LogInjection_30yr 

# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 0.05 to 0.5 MtCO2/yr
def ROM_2_Pressure_LogInjection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_2_Pressure_LogInjection_30yr = 22.6945 + 0.936802 * perm + 0.0635403 * thick - 0.0000257106 * pmax(0, depth - 2522.5) * perm + 0.000030864 * pmax(0, 2522.5 - depth) * perm \
        - 0.00140477 * thick * thick + 0.0000146724 * thick * thick * thick - 0.220429 * pmax(0, geoGrad - 0.0330801) * perm + 0.552063 * pmax(0, 0.0330801 - geoGrad) * perm \
        - 0.0000000554063 * thick * thick * thick * thick - 0.000111586 * pmax(0, depth - 1463.02) - 0.000119406 * pmax(0, 1463.02 - depth) - 0.0000000285215 * pmax(0, depth - 2625.36) * pmax(0, depth - 1463.02) \
        + 0.0000000599429 * pmax(0, 2625.36 - depth) * pmax(0, depth - 1463.02) - 0.000135224 * pmax(0, 2250.43 - depth) * pmax(0, 0.0330801 - geoGrad) * perm
    ROM_2_Pressure_LogInjection_30yr = 10 ** ROM_2_Pressure_LogInjection_30yr / 1000000000 / 30
    return ROM_2_Pressure_LogInjection_30yr 

# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 0.1 to 1 MtCO2/yr
def ROM_3_Pressure_LogInjection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_3_Pressure_LogInjection_30yr = 8.57673 + 0.984198 * pmax(0, perm + 14.9896) - 0.948761 * pmax(0, -14.9896 - perm) + 0.0614451 * thick + 0.000305034 * pmax(0, depth - 2668.3) - 0.000321293 * pmax(0, 2668.3 - depth) - 0.00131418 * thick * thick + 0.0000133997 * thick * thick * thick + 3.09624 * pmax(0, geoGrad - 0.0334528) - 7.52532 * pmax(0, 0.0334528 - geoGrad) \
        - 0.0000000496852 * thick * thick * thick * thick - 0.0000224321 * pmax(0, depth - 1450.43) * pmax(0, perm + 14.9896) + 0.0000000541804 * pmax(0, depth - 1706.53) * pmax(0, 2668.3 - depth) - 0.000000112084 * pmax(0, 1706.53 - depth) * pmax(0, 2668.3 - depth) - 0.000000025979 * depth * pmax(0, depth - 2668.3) - 0.0000393038 * pmax(0, perm + 13.836) * pmax(0, depth - 1450.43) * pmax(0, perm + 14.9896)
    ROM_3_Pressure_LogInjection_30yr = 10 ** ROM_3_Pressure_LogInjection_30yr / 1000000000 / 30
    return ROM_3_Pressure_LogInjection_30yr 

# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 0.5 to 5 MtCO2/yr
def ROM_4_Pressure_LogInjection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_4_Pressure_LogInjection_30yr = 9.19451 + 0.971363 * pmax(0, perm + 14.1939) - 0.949 * pmax(0, -14.1939 - perm) + 0.0628482 * thick + 0.000189699 * pmax(0, depth - 2383.1) \
        - 0.000255874 * pmax(0, 2383.1 - depth) - 0.00131262 * thick * thick + 4.46001 * pmax(0, geoGrad - 0.025134) - 10.1692 * pmax(0, 0.025134 - geoGrad) \
        + 0.0000130933 * thick * thick * thick - 0.0000000476059 * thick * thick * thick * thick - 0.000000269116 * pmax(0, 4047.09 - depth) * thick - 0.000000113634 * pmax(0, 2109.77 - depth) * pmax(0, 2383.1 - depth) \
        - 0.0000000191524 * pmax(0, depth - 3950.1) * pmax(0, depth - 2383.1) + 0.000000037298 * pmax(0, 3950.1 - depth) * pmax(0, depth - 2383.1)
    ROM_4_Pressure_LogInjection_30yr = 10 ** ROM_4_Pressure_LogInjection_30yr / 1000000000 / 30
    return ROM_4_Pressure_LogInjection_30yr 

# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 1 to 10 MtCO2/yr
def ROM_5_Pressure_LogInjection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_5_Pressure_LogInjection_30yr = 9.62783 + 1.04177 * pmax(0, perm + 13.8227) - 0.958923 * pmax(0, -13.8227 - perm) + 0.0628821 * thick + 0.000204775 * pmax(0, depth - 2626.68) - 0.00034 * pmax(0, 2626.68 - depth) - 0.00131846 * thick * thick + 4.25255 * pmax(0, geoGrad - 0.0274764) - 9.22856 * pmax(0, 0.0274764 - geoGrad) + 0.0000131497 * thick * thick * thick - 0.0000000477828 * thick * thick * thick * thick \
        - 0.00000215176 * pmax(0, 1532.13 - depth) * thick - 0.116271 * pmax(0, poro - 0.131861) * pmax(0, perm + 13.8227) + 0.586219 * pmax(0, 0.131861 - poro) * pmax(0, perm + 13.8227) - 0.0000000195266 * pmax(0, depth - 3053.9) * pmax(0, depth - 2626.68) - 0.000000305364 * pmax(0, 3053.9 - depth) * pmax(0, depth - 2626.68) - 0.0000272035 * pmax(0, depth - 1555.91) * pmax(0, perm + 13.8227) - 0.0000844071 * pmax(0, 1555.91 - depth) * pmax(0, perm + 13.8227)
    ROM_5_Pressure_LogInjection_30yr = 10 ** ROM_5_Pressure_LogInjection_30yr / 1000000000 / 30
    return ROM_5_Pressure_LogInjection_30yr 

# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 5 to 50 MtCO2/yr
def ROM_6_Pressure_LogInjection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_6_Pressure_LogInjection_30yr = 10.4006 + 0.995985 * pmax(0, perm + 13.0923) - 0.972968 * pmax(0, -13.0923 - perm) + 0.0592448 * thick + 0.000175889 * pmax(0, depth - 2457.9) \
        - 0.00026904 * pmax(0, 2457.9 - depth) - 0.00119045 * thick * thick + 2.95806 * pmax(0, geoGrad - 0.0328211) - 8.16887 * pmax(0, 0.0328211 - geoGrad) \
        + 0.000011503 * thick * thick * thick - 0.0000000408037 * thick * thick * thick * thick - 0.000000311001 * pmax(0, 4099.72 - depth) * thick \
        - 0.000000860943 * pmax(0, poro - 0.136387) * pmax(0, 4099.72 - depth) * thick + 0.00000337893 * pmax(0, 0.136387 - poro) * pmax(0, 4099.72 - depth) * thick \
        + 0.0000000544514 * pmax(0, depth - 1796.28) * pmax(0, 2457.9 - depth) - 0.000000119955 * pmax(0, 1796.28 - depth) * pmax(0, 2457.9 - depth) \
        - 0.0000000168045 * pmax(0, depth - 3762.6) * pmax(0, depth - 2457.9) + 0.0000000509724 * pmax(0, 3762.6 - depth) * pmax(0, depth - 2457.9)
    ROM_6_Pressure_LogInjection_30yr = 10 ** ROM_6_Pressure_LogInjection_30yr / 1000000000 / 30
    return ROM_6_Pressure_LogInjection_30yr 

# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 1 to 10 MtCO2/yr
def ROM_7_Pressure_LogInjection_30yr(depth, thick, perm, poro, geoGrad):
    ROM_7_Pressure_LogInjection_30yr = 10.4773 + 1.12844 * pmax(0, perm + 13.0493) - 1.13841 * pmax(0, -13.0493 - perm) + 0.000148313 * pmax(0, depth - 2832.97) - 0.000318076 * pmax(0, 2832.97 - depth) + 0.060381 * thick - 0.00124806 * thick * thick + 3.81313 * pmax(0, geoGrad - 0.0266459) - 9.37883 * pmax(0, 0.0266459 - geoGrad) + 0.0000119876 * thick * thick * thick \
        - 0.0000000423995 * thick * thick * thick * thick - 0.0801118 * pmax(0, poro - 0.157579) * pmax(0, perm + 13.0493) + 0.529548 * pmax(0, 0.157579 - poro) * pmax(0, perm + 13.0493) - 0.00263363 * pmax(0, perm + 12.2758) * thick + 0.00188026 * pmax(0, -12.2758 - perm) * thick - 0.0000290337 * pmax(0, depth - 1521.74) * pmax(0, perm + 13.0493) - 0.000256461 * pmax(0, 1521.74 - depth) * pmax(0, perm + 13.0493) - 0.0891983 * pmax(0, poro - 0.0855489) \
        + 0.773541 * pmax(0, 0.0855489 - poro)
    ROM_7_Pressure_LogInjection_30yr = 10 ** ROM_7_Pressure_LogInjection_30yr / 1000000000 / 30
    return ROM_7_Pressure_LogInjection_30yr 


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PRESSURE-CONTROLLED ROMs FOR PLUME AREA (log values)
# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 0 to max MtCO2/yr
def ROM_1_Pressure_LogArea_30yr(depth, thick, perm, poro, geoGrad):
    ROM_1_Pressure_LogArea_30yr = 9.0217 + 1.1726 * pmax(0, perm + 12.7347) - 1.0845 * pmax(0, -12.7347 - perm) - 2.43355 * pmax(0, poro - 0.147156) \
        + 4.93026 * pmax(0, 0.147156 - poro) + 0.0000831618 * pmax(0, depth - 2383.55) - 0.000143794 * pmax(0, 2383.55 - depth) \
        + 8.38554 * pmax(0, geoGrad - 0.0375871) - 7.19776 * pmax(0, 0.0375871 - geoGrad) - 0.17883 * pmax(0, perm + 13.8104) * pmax(0, poro - 0.147156) \
        - 0.132382 * pmax(0, -13.8104 - perm) * pmax(0, poro - 0.147156) - 0.000866848 * thick * pmax(0, perm + 12.7347) - 0.0544284 * pmax(0, perm + 13.4154) * pmax(0, -12.7347 - perm) \
        + 0.0760034 * pmax(0, -13.4154 - perm) * pmax(0, -12.7347 - perm) + 0.494409 * pmax(0, poro - 0.0618619) * pmax(0, -12.7347 - perm) - 1.44279 * pmax(0, 0.0618619 - poro) * pmax(0, -12.7347 - perm) \
        + 3.35855 * pmax(0, poro - 0.183483) * pmax(0, poro - 0.147156) - 24.4928 * pmax(0, 0.183483 - poro) * pmax(0, poro - 0.147156) \
        - 24.6859 * pmax(0, poro - 0.0641099) * pmax(0, 0.147156 - poro) + 53.1903 * pmax(0, 0.0641099 - poro) * pmax(0, 0.147156 - poro) \
        - 0.0000000969448 * pmax(0, 1971.85 - depth) * pmax(0, 2383.55 - depth) - 0.0000000124453 * pmax(0, depth - 4426.84) * pmax(0, depth - 2383.55) \
        + 0.0000000186833 * pmax(0, 4426.84 - depth) * pmax(0, depth - 2383.55) - 0.390312 * pmax(0, perm + 14.4645) * pmax(0, 0.0375871 - geoGrad) \
        - 0.00174513 * pmax(0, geoGrad - 0.0347666) * pmax(0, depth - 2383.55) + 0.000514721 * pmax(0, 0.0347666 - geoGrad) * pmax(0, depth - 2383.55) \
        - 0.000000555221 * depth * thick * pmax(0, perm + 12.7347) + 0.00237257 * thick * pmax(0, perm + 13.8104) * pmax(0, poro - 0.147156) \
        - 0.000041975 * thick * thick * pmax(0, perm + 13.8104) * pmax(0, poro - 0.147156) + 0.0039026 * pmax(0, poro - 0.294963) * thick * pmax(0, perm + 13.8104) * pmax(0, poro - 0.147156) \
        - 0.0425894 * pmax(0, 0.294963 - poro) * thick * pmax(0, perm + 13.8104) * pmax(0, poro - 0.147156) - 0.921133 * pmax(0, poro - 0.198002) * pmax(0, poro - 0.0618619) * pmax(0, -12.7347 - perm) \
        + 4.78136 * pmax(0, 0.198002 - poro) * pmax(0, poro - 0.0618619) * pmax(0, -12.7347 - perm) + 0.0000237651 * pmax(0, 1871.21 - depth) * pmax(0, -12.7347 - perm) \
        + 0.000386028 * pmax(0, geoGrad - 0.0269517) * pmax(0, depth - 1871.21) * pmax(0, -12.7347 - perm) - 0.000657527 * pmax(0, 0.0269517 - geoGrad) * pmax(0, depth - 1871.21) * pmax(0, -12.7347 - perm) \
        - 1.31628 * pmax(0, geoGrad - 0.0195184) * pmax(0, -12.7347 - perm) + 0.320756 * pmax(0, 0.0195184 - geoGrad) * pmax(0, -12.7347 - perm) \
        + 0.0063948 * thick * pmax(0, -13.8104 - perm) * pmax(0, poro - 0.147156) - 0.0000504452 * thick * thick * pmax(0, -13.8104 - perm) * pmax(0, poro - 0.147156) \
        - 15.6779 * poro * pmax(0, -14.4645 - perm) * pmax(0, 0.0375871 - geoGrad) - 5.79552 * pmax(0, poro - 0.389973) * pmax(0, perm + 14.4645) * pmax(0, 0.0375871 - geoGrad) \
        - 0.285296 * pmax(0, 0.389973 - poro) * pmax(0, perm + 14.4645) * pmax(0, 0.0375871 - geoGrad) - 0.0493448 * thick * pmax(0, 0.389973 - poro) * pmax(0, perm + 14.4645) * pmax(0, 0.0375871 - geoGrad) \
        + 0.0000000274033 * thick * pmax(0, depth - 1871.21) * pmax(0, -12.7347 - perm)
    ROM_1_Pressure_LogArea_30yr = 10 ** ROM_1_Pressure_LogArea_30yr
    return ROM_1_Pressure_LogArea_30yr 

# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 0 to 1 MtCO2/yr
def ROM_2_Pressure_LogArea_30yr(depth, thick, perm, poro, geoGrad):
    ROM_2_Pressure_LogArea_30yr = 7.74227 + 0.960104 * pmax(0, perm + 13.9173) - 0.839421 * pmax(0, -13.9173 - perm) - 1.73638 * pmax(0, poro - 0.143379) \
        + 6.7884 * pmax(0, 0.143379 - poro) + 0.0000640915 * pmax(0, depth - 2389.27) - 0.000182166 * pmax(0, 2389.27 - depth) + 5.98062 * pmax(0, geoGrad - 0.0221935) \
        - 7.02768 * pmax(0, 0.0221935 - geoGrad) - 93.6471 * pmax(0, poro - 0.0810211) * pmax(0, 0.143379 - poro) \
        + 106.431 * pmax(0, 0.0810211 - poro) * pmax(0, 0.143379 - poro) + 2.50803 * pmax(0, poro - 0.319748) * pmax(0, poro - 0.143379) \
        - 4.22037 * pmax(0, 0.319748 - poro) * pmax(0, poro - 0.143379) + 0.373923 * perm * pmax(0, 0.143379 - poro) \
        + 0.000000041123 * pmax(0, depth - 1559.87) * pmax(0, 2389.27 - depth) - 0.0000000799142 * pmax(0, 1559.87 - depth) * pmax(0, 2389.27 - depth) \
        + 0.000000186401 * pmax(0, depth - 5480.31) * pmax(0, depth - 2389.27) + 0.0000000147135 * pmax(0, 5480.31 - depth) * pmax(0, depth - 2389.27) + 0.00255451 * thick * pmax(0, poro - 0.143379) \
        - 0.0000068022 * thick * thick * pmax(0, poro - 0.143379) + 1.74031 * pmax(0, perm + 14.533) * pmax(0, geoGrad - 0.0221935) \
        + 1.66959 * pmax(0, -14.533 - perm) * pmax(0, geoGrad - 0.0221935) - 0.000652165 * pmax(0, geoGrad - 0.0303187) * pmax(0, depth - 2389.27) - 0.000360362 * pmax(0, 0.0303187 - geoGrad) * pmax(0, depth - 2389.27) \
        + 5.78904 * pmax(0, 0.0220609 - geoGrad) * thick * pmax(0, poro - 0.143379) - 0.257776 * pmax(0, perm + 13.9556) * pmax(0, geoGrad - 0.0220609) * thick * pmax(0, poro - 0.143379) - 0.0463053 * pmax(0, -13.9556 - perm) * pmax(0, geoGrad - 0.0220609) * thick * pmax(0, poro - 0.143379) \
        - 5.51088 * pmax(0, poro - 0.0523905) * perm * pmax(0, 0.143379 - poro) + 4.02571 * pmax(0, 0.0523905 - poro) * perm * pmax(0, 0.143379 - poro) - 0.000285179 * pmax(0, geoGrad - 0.0235267) * pmax(0, 2389.27 - depth) \
        + 0.00201109 * pmax(0, 0.0235267 - geoGrad) * pmax(0, 2389.27 - depth) - 0.000534446 * pmax(0, depth - 1215.83) * pmax(0, perm + 14.533) * pmax(0, geoGrad - 0.0221935) \
        - 0.00328046 * pmax(0, 1215.83 - depth) * pmax(0, perm + 14.533) * pmax(0, geoGrad - 0.0221935) - 0.206705 * poro * pmax(0, perm + 13.9173) - 103.236 * pmax(0, geoGrad - 0.0272079) * pmax(0, -14.533 - perm) * pmax(0, geoGrad - 0.0221935) \
        + 614.988 * pmax(0, 0.0272079 - geoGrad) * pmax(0, -14.533 - perm) * pmax(0, geoGrad - 0.0221935) - 0.0000233736 * pmax(0, perm + 14.5584) * thick * thick * pmax(0, poro - 0.143379) - 0.0000511631 * pmax(0, -14.5584 - perm) * thick * thick * pmax(0, poro - 0.143379) \
        + 0.000000996906 * thick * pmax(0, depth - 2389.27) - 0.0000000212408 * thick * thick * pmax(0, depth - 2389.27) + 0.000000000124633 * thick * thick * thick * pmax(0, depth - 2389.27) \
        + 0.0000609967 * pmax(0, perm + 13.2326) * pmax(0, 2389.27 - depth) + 0.00000959489 * pmax(0, -13.2326 - perm) * pmax(0, 2389.27 - depth) + 15.4629 * pmax(0, perm + 13.9636) * pmax(0, -13.9173 - perm) \
        + 0.00623768 * pmax(0, -13.9636 - perm) * pmax(0, -13.9173 - perm) - 0.0047152 * thick * pmax(0, 0.143379 - poro) + 0.000991631 * thick * pmax(0, -13.9636 - perm) * pmax(0, -13.9173 - perm) \
        - 0.0000070626 * thick * thick * pmax(0, -13.9636 - perm) * pmax(0, -13.9173 - perm) - 0.179283 * pmax(0, 0.263988 - poro) * pmax(0, -13.9173 - perm) + 0.413998 * perm * pmax(0, 0.0220609 - geoGrad) * thick * pmax(0, poro - 0.143379) \
        - 0.0649334 * pmax(0, perm + 14.6194) * pmax(0, geoGrad - 0.0220609) * thick * pmax(0, poro - 0.143379) + 0.327312 * pmax(0, -14.6194 - perm) * pmax(0, geoGrad - 0.0220609) * thick * pmax(0, poro - 0.143379) + 0.000000585279 * depth * thick * pmax(0, 0.143379 - poro)
    ROM_2_Pressure_LogArea_30yr = 10 ** ROM_2_Pressure_LogArea_30yr
    return ROM_2_Pressure_LogArea_30yr
 
# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 1 to 10 MtCO2/yr
def ROM_3_Pressure_LogArea_30yr(depth, thick, perm, poro, geoGrad):
    ROM_3_Pressure_LogArea_30yr = 8.56938 + 0.851044 * pmax(0, perm + 13.7386) - 0.932135 * pmax(0, -13.7386 - perm) - 18.6037 * pmax(0, poro - 0.134274) \
        + 20.5793 * pmax(0, 0.134274 - poro) + 0.000128773 * pmax(0, depth - 2279.91) - 0.000232379 * pmax(0, 2279.91 - depth) \
        + 6.11431 * pmax(0, geoGrad - 0.0327253) - 7.01032 * pmax(0, 0.0327253 - geoGrad) - 0.38454 * pmax(0, poro - 0.282005) * pmax(0, perm + 13.7386) \
        + 0.447102 * pmax(0, 0.282005 - poro) * pmax(0, perm + 13.7386) - 18.7021 * pmax(0, poro - 0.0826292) * pmax(0, 0.134274 - poro) \
        + 30.0385 * pmax(0, 0.0826292 - poro) * pmax(0, 0.134274 - poro) + 2.26223 * pmax(0, poro - 0.336977) * pmax(0, poro - 0.134274) \
        - 3.26314 * pmax(0, 0.336977 - poro) * pmax(0, poro - 0.134274) + 0.200201 * pmax(0, perm + 12.9742) * pmax(0, poro - 0.134274) - 0.257192 * pmax(0, -12.9742 - perm) * pmax(0, poro - 0.134274) \
        - 0.000505539 * pmax(0, depth - 1558) * pmax(0, geoGrad - 0.0327253) + 0.00952016 * pmax(0, 1558 - depth) * pmax(0, geoGrad - 0.0327253) - 0.0000000216748 * pmax(0, depth - 2872.89) * pmax(0, depth - 2279.91) \
        + 0.0000000274422 * pmax(0, 2872.89 - depth) * pmax(0, depth - 2279.91) - 0.00000766648 * pmax(0, depth - 1421.86) * pmax(0, perm + 13.7386) + 0.0000251569 * pmax(0, 1421.86 - depth) * pmax(0, perm + 13.7386) \
        + 0.474016 * pmax(0, poro - 0.122319) * pmax(0, -13.7386 - perm) - 1.00637 * pmax(0, 0.122319 - poro) * pmax(0, -13.7386 - perm) + 0.0976059 * pmax(0, perm + 13.3229) * pmax(0, perm + 13.7386) \
        - 0.0845148 * pmax(0, -13.3229 - perm) * pmax(0, perm + 13.7386) + 3.09586 * pmax(0, perm + 14.0279) * pmax(0, geoGrad - 0.0327253) - 0.305154 * pmax(0, -14.0279 - perm) * pmax(0, geoGrad - 0.0327253) \
        + 0.0000000818859 * pmax(0, depth - 982.217) * pmax(0, 2279.91 - depth) - 0.000000143042 * pmax(0, 982.217 - depth) * pmax(0, 2279.91 - depth) - 0.000200343 * pmax(0, geoGrad - 0.0353901) * pmax(0, depth - 1421.86) * pmax(0, perm + 13.7386) \
        - 0.000577721 * pmax(0, 0.0353901 - geoGrad) * pmax(0, depth - 1421.86) * pmax(0, perm + 13.7386) + 471.305 * pmax(0, 0.0559029 - poro) * pmax(0, 0.0826292 - poro) * pmax(0, 0.134274 - poro) \
        + 0.0700046 * pmax(0, -13.7422 - perm) * pmax(0, -13.7386 - perm) + 11.3953 * geoGrad * pmax(0, 0.282005 - poro) * pmax(0, perm + 13.7386) - 0.000000296006 * thick * pmax(0, 2279.91 - depth) \
        + 0.00000075935 * pmax(0, depth - 2185.44) * pmax(0, -12.9742 - perm) * pmax(0, poro - 0.134274) + 0.000402712 * pmax(0, 2185.44 - depth) * pmax(0, -12.9742 - perm) * pmax(0, poro - 0.134274) - 0.00157738 * pmax(0, depth - 1202.2) * geoGrad * pmax(0, 0.282005 - poro) * pmax(0, perm + 13.7386) \
        - 0.0249032 * pmax(0, 1202.2 - depth) * geoGrad * pmax(0, 0.282005 - poro) * pmax(0, perm + 13.7386) + 17.0894 * pmax(0, poro - 0.169081) - 16.6021 * pmax(0, 0.169081 - poro) \
        - 0.00768224 * geoGrad * pmax(0, 2185.44 - depth) * pmax(0, -12.9742 - perm) * pmax(0, poro - 0.134274) + 0.00000133595 * thick * pmax(0, depth - 1421.86) * pmax(0, perm + 13.7386) - 0.0000000164826 * thick * thick * pmax(0, depth - 1421.86) * pmax(0, perm + 13.7386) \
        + 3.31801E-12 * pmax(0, depth - 4631.45) * pmax(0, depth - 2872.89) * pmax(0, depth - 2279.91) - 5.15282E-12 * pmax(0, 4631.45 - depth) * pmax(0, depth - 2872.89) * pmax(0, depth - 2279.91) - 17.4579 * pmax(0, poro - 0.0528194) * geoGrad * pmax(0, 0.282005 - poro) * pmax(0, perm + 13.7386) \
        + 454.297 * pmax(0, 0.0528194 - poro) * geoGrad * pmax(0, 0.282005 - poro) * pmax(0, perm + 13.7386) - 0.00142432 * pmax(0, depth - 1558) * pmax(0, perm + 14.0279) * pmax(0, geoGrad - 0.0327253) \
        - 0.0126609 * pmax(0, 1558 - depth) * pmax(0, perm + 14.0279) * pmax(0, geoGrad - 0.0327253) + 0.00000213412 * pmax(0, perm + 13.1156) * thick * pmax(0, depth - 1421.86) * pmax(0, perm + 13.7386)
    ROM_3_Pressure_LogArea_30yr = 10 ** ROM_3_Pressure_LogArea_30yr
    return ROM_3_Pressure_LogArea_30yr

# Plume dimension ROM, 30 years, based on PRESSURE-controlled input data: 10 to max MtCO2/yr
def ROM_4_Pressure_LogArea_30yr(depth, thick, perm, poro, geoGrad):
    ROM_4_Pressure_LogArea_30yr = 9.42378 + 1.29518 * pmax(0, perm + 12.4406) - 1.2217 * pmax(0, -12.4406 - perm) - 2.94254 * pmax(0, poro - 0.155966) + 4.81165 * pmax(0, 0.155966 - poro) + 0.0000668318 * pmax(0, depth - 2949.99) \
        - 0.000123178 * pmax(0, 2949.99 - depth) + 6.2439 * pmax(0, geoGrad - 0.0411691) - 8.27408 * pmax(0, 0.0411691 - geoGrad) + 0.0023336 * thick - 0.00332709 * pmax(0, perm + 12.3391) * thick + 0.00283422 * pmax(0, -12.3391 - perm) * thick \
        + 4.74628 * pmax(0, poro - 0.189779) * pmax(0, poro - 0.155966) - 14.3159 * pmax(0, 0.189779 - poro) * pmax(0, poro - 0.155966) + 0.40252 * pmax(0, poro - 0.0750203) * pmax(0, -12.4406 - perm) - 1.37082 * pmax(0, 0.0750203 - poro) * pmax(0, -12.4406 - perm) \
        + 0.0000000388905 * pmax(0, depth - 1811.39) * pmax(0, 2949.99 - depth) - 0.0000000924857 * pmax(0, 1811.39 - depth) * pmax(0, 2949.99 - depth) - 0.00180334 * pmax(0, geoGrad - 0.0330142) * pmax(0, depth - 2949.99) + 0.000500428 * pmax(0, 0.0330142 - geoGrad) * pmax(0, depth - 2949.99) \
        + 0.0000224677 * pmax(0, depth - 4184.45) * pmax(0, poro - 0.0750203) * pmax(0, -12.4406 - perm) - 0.0000138588 * pmax(0, 4184.45 - depth) * pmax(0, poro - 0.0750203) * pmax(0, -12.4406 - perm) \
        - 18.1032 * pmax(0, poro - 0.0732944) * pmax(0, 0.155966 - poro) + 46.7563 * pmax(0, 0.0732944 - poro) * pmax(0, 0.155966 - poro) \
        + 0.00295422 * pmax(0, geoGrad - 0.0390234) * pmax(0, 2949.99 - depth) - 0.00119084 * pmax(0, 0.0390234 - geoGrad) * pmax(0, 2949.99 - depth) - 0.0000984202 * thick * thick - 0.0000000119237 * pmax(0, depth - 4185.93) * pmax(0, depth - 2949.99) \
        + 0.0000000188516 * pmax(0, 4185.93 - depth) * pmax(0, depth - 2949.99) + 0.000027272 * pmax(0, depth - 2460.34) * pmax(0, -12.4406 - perm) \
        - 0.0000566139 * pmax(0, 2460.34 - depth) * pmax(0, -12.4406 - perm) - 0.00000000313777 * pmax(0, depth - 1874.84) * thick * thick + 0.00000000684649 * pmax(0, 1874.84 - depth) * thick * thick \
        - 7.96102 * pmax(0, poro - 0.361987) * pmax(0, poro - 0.189779) * pmax(0, poro - 0.155966) + 11.1203 * pmax(0, 0.361987 - poro) * pmax(0, poro - 0.189779) * pmax(0, poro - 0.155966) \
        + 0.000000879089 * thick * thick * thick - 0.00555798 * pmax(0, geoGrad - 0.0320602) * pmax(0, 4184.45 - depth) * pmax(0, poro - 0.0750203) * pmax(0, -12.4406 - perm) \
        + 0.00243387 * pmax(0, 0.0320602 - geoGrad) * pmax(0, 4184.45 - depth) * pmax(0, poro - 0.0750203) * pmax(0, -12.4406 - perm) + 0.0000000226314 * pmax(0, perm + 12.854) * thick * thick * thick \
        - 0.0000000711469 * pmax(0, -12.854 - perm) * thick * thick * thick - 0.0000835825 * depth * pmax(0, 0.155966 - poro) + 0.000763754 * pmax(0, poro - 0.0398452) * thick + 0.031866 * pmax(0, 0.0398452 - poro) * thick \
        + 0.0000611 * pmax(0, depth - 1046.56) * pmax(0, poro - 0.155966) - 0.000593352 * pmax(0, 1046.56 - depth) * pmax(0, poro - 0.155966) - 0.00000000302942 * thick * thick * thick * thick - 0.03065 * pmax(0, geoGrad - 0.0338137) * pmax(0, poro - 0.0398452) * thick \
        + 0.0165905 * pmax(0, 0.0338137 - geoGrad) * pmax(0, poro - 0.0398452) * thick + 1.06841 * pmax(0, geoGrad - 0.0222961) * pmax(0, poro - 0.0750203) * pmax(0, -12.4406 - perm) \
        - 10.0263 * pmax(0, 0.0222961 - geoGrad) * pmax(0, poro - 0.0750203) * pmax(0, -12.4406 - perm) - 0.0000590248 * depth * pmax(0, perm + 12.4406) \
        + 0.0000063701 * pmax(0, depth - 2454.27) * pmax(0, 0.0338137 - geoGrad) * pmax(0, poro - 0.0398452) * thick + 0.0000497147 * pmax(0, 2454.27 - depth) * pmax(0, 0.0338137 - geoGrad) * pmax(0, poro - 0.0398452) * thick \
        + 0.105542 * pmax(0, perm + 12.7069) * pmax(0, geoGrad - 0.0338137) * pmax(0, poro - 0.0398452) * thick + 0.0356681 * pmax(0, -12.7069 - perm) * pmax(0, geoGrad - 0.0338137) * pmax(0, poro - 0.0398452) * thick \
        + 1.96929E-11 * pmax(0, depth - 1057.67) * thick * thick * thick - 0.000000000104645 * pmax(0, 1057.67 - depth) * thick * thick * thick - 0.0000646856 * pmax(0, perm + 12.1241) * pmax(0, depth - 1046.56) * pmax(0, poro - 0.155966) - 0.0000685336 * pmax(0, -12.1241 - perm) * pmax(0, depth - 1046.56) * pmax(0, poro - 0.155966) \
        - 0.018253 * pmax(0, geoGrad - 0.0232722) * pmax(0, 0.0390234 - geoGrad) * pmax(0, 2949.99 - depth) + 0.0424006 * pmax(0, 0.0232722 - geoGrad) * pmax(0, 0.0390234 - geoGrad) * pmax(0, 2949.99 - depth)
    ROM_4_Pressure_LogArea_30yr = 10 ** ROM_4_Pressure_LogArea_30yr
    return ROM_4_Pressure_LogArea_30yr
  









#################################################################################### 
# 5 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_MCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_1_MCO2_5yr = +3.66787e+07 +1.65976e+07  * Thick\
    +20239.6      * pmax(0, Depth-2178.43)*Thick -9467.19     * pmax(0, 2178.43-Depth)*Thick                                       \
    -1.09894e+08 * pmax(0, Perm+14.744)   -5.37639e+07 * pmax(0, -14.744-Perm)                                           \
    -5.29042e+08 * pmax(0, GeoGrad-0.0174088)  -2.56748e+09 * pmax(0, 0.0174088-GeoGrad)                                         \
    -1.91627e+07 * pmax(0, Perm+14.6726)*Thick  -2.84811e+07 * pmax(0, -14.6726-Perm)*Thick                                       \
    -30991.2     * pmax(0, Depth-1966.83)*pmax(0, -14.6726-Perm)*Thick                         \
    +14850.1      * pmax(0, 1966.83-Depth)*pmax(0, -14.6726-Perm)*Thick                         \
    +75003.7      * Depth*pmax(0, Perm+14.744)  +96859.7      * pmax(0, Perm+14.3109)*Depth*pmax(0, Perm+14.744)                            \
    -207743      * pmax(0, 0.0209519-GeoGrad)*pmax(0, Depth-2178.43)*Thick                        \
    +2.40276e+08  * pmax(0, GeoGrad-0.0139106)*Thick  -423054      * pmax(0, Depth-1377.3)*pmax(0, GeoGrad-0.0139106)*Thick                 \
    -251649      * pmax(0, 1377.3-Depth)*pmax(0, GeoGrad-0.0139106)*Thick                         
    +3.06716e+09  * pmax(0, Perm+14.6827)*pmax(0, GeoGrad-0.0174088)  +1.8921e+09   * pmax(0, -14.6827-Perm)*pmax(0, GeoGrad-0.0174088)                          \
    +48594.6      * Depth*pmax(0, Perm+14.6726)*Thick   +2.12655e+06  * pmax(0, Perm+14.9182)*pmax(0, Depth-1377.3)*pmax(0, GeoGrad-0.0139106)*Thick           \
    -1.42425e+06 * pmax(0, -14.9182-Perm)*pmax(0, Depth-1377.3)*pmax(0, GeoGrad-0.0139106)*Thick          \
    +3.76558e+08  * pmax(0, Perm+14.4294)*pmax(0, GeoGrad-0.0139106)*Thick   -3.14393e+08 * pmax(0, -14.4294-Perm)*pmax(0, GeoGrad-0.0139106)*Thick                       \
    +1.36073      * pmax(0, Depth-2686.31)*pmax(0, Depth-1966.83)*pmax(0, -14.6726-Perm)*Thick    +46.3522      * pmax(0, 2686.31-Depth)*pmax(0, Depth-1966.83)*pmax(0, -14.6726-Perm)*Thick                   \
    +1.9529e+07   * pmax(0, -14.7297-Perm)*pmax(0, -14.6726-Perm)*Thick   +68300.2      * pmax(0, Perm+14.1432)*Depth*pmax(0, Perm+14.6726)*Thick                       \
    -33334.8     * pmax(0, -14.1432-Perm)*Depth*pmax(0, Perm+14.6726)*Thick  +1.26513e+06  * pmax(0, Depth-1374.9)*pmax(0, -14.4294-Perm)*pmax(0, GeoGrad-0.0139106)*Thick          \
    +328198       * pmax(0, 1374.9-Depth)*pmax(0, -14.4294-Perm)*pmax(0, GeoGrad-0.0139106)*Thick      
    ROM_1_MCO2_5yr = ROM_1_MCO2_5yr / 1000000000 / 30       
    return ROM_1_MCO2_5yr
#############
# ROM: 0.05-0.5
############# 
def ROM_2_MCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_2_MCO2_5yr =+1.08539e+11  +7.36034e+09  * Perm +6.50156e+10  * Thick                                                       \
    +2.13097e+06  * pmax(0, Depth-3381.79)*Thick  -9.7707e+06  * pmax(0, 3381.79-Depth)*Thick                                         \
    +4.63371e+09  * Thick*Perm  +148042       * pmax(0, Depth-3381.79)*Thick*Perm                                      \
    -694519      * pmax(0, 3381.79-Depth)*Thick*Perm -1.88166e+08 * pmax(0, GeoGrad-0.0371514)*Perm                                                 \
    +4.78539e+08  * pmax(0, Perm+14.7285)*Perm -4.64881e+08 * pmax(0, -14.7285-Perm)*Perm                                        \
    -24444.4     * pmax(0, Depth-3774.14)*pmax(0, Perm+14.7285)*Perm +19420.6      * pmax(0, 3774.14-Depth)*pmax(0, Perm+14.7285)*Perm                           \
    +2.89934e+08  * pmax(0, Perm+13.9893)*Thick*Perm -2.85566e+08 * pmax(0, -13.9893-Perm)*Thick*Perm                                     \
    -33275.2     * pmax(0, Perm+13.9561)*pmax(0, 3381.79-Depth)*Thick*Perm +35410        * pmax(0, -13.9561-Perm)*pmax(0, 3381.79-Depth)*Thick*Perm                       \
    +320283       * pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm  -1.94049e+06 * pmax(0, 1423.6-Depth)*pmax(0, 0.0371514-GeoGrad)*Perm                          \
    +11350.3      * Thick*pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm +1.39739e+09  * pmax(0, Perm+14.4494)*pmax(0, 0.0371514-GeoGrad)*Perm                         \
    -8.43986e+08 * pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm -2.56948     * pmax(0, Depth-1490.66)*pmax(0, 3381.79-Depth)*Thick                           \
    +7.23019      * pmax(0, 1490.66-Depth)*pmax(0, 3381.79-Depth)*Thick +8.17167e+09  * pmax(0, GeoGrad-0.0270544)*Thick                                       \
    -1.41671e+10 * pmax(0, 0.0270544-GeoGrad)*Thick  -1.08045e+07 * pmax(0, Perm+14.9341)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +1.20005e+07  * pmax(0, -14.9341-Perm)*pmax(0, -13.9893-Perm)*Thick*Perm -6735.33     * pmax(0, Depth-1442.6)*pmax(0, -13.9893-Perm)*Thick*Perm                        \
    +7758.95      * pmax(0, 1442.6-Depth)*pmax(0, -13.9893-Perm)*Thick*Perm  +5.28942e+08  * pmax(0, GeoGrad-0.0270544)*Thick*Perm                                    \
    -9.22139e+08 * pmax(0, 0.0270544-GeoGrad)*Thick*Perm  -768421      * pmax(0, Depth-2105.99)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm          \
    +4.14462e+06  * pmax(0, 2105.99-Depth)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm  -152032      * pmax(0, GeoGrad-0.0268008)*pmax(0, 3381.79-Depth)*Thick                      \
    +252518       * pmax(0, 0.0268008-GeoGrad)*pmax(0, 3381.79-Depth)*Thick                         
    ROM_2_MCO2_5yr = ROM_2_MCO2_5yr / 1000000000 / 30       
    return ROM_2_MCO2_5yr
 
#############
# ROM: 0.1-1
############# 
def ROM_3_MCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_3_MCO2_5yr =+8.54014e+07   +202382       * Depth +62712.7      * Thick*Depth                                         \
    +366436       * pmax(0, Perm+13.9256)*Thick*Depth -69357.9     * pmax(0, -13.9256-Perm)*Thick*Depth                                   \
    +5.72194e+08  * pmax(0, -14.7142-Perm) -433625      * pmax(0, GeoGrad-0.0256195)*Thick*Depth                         \
    -608784      * pmax(0, 0.0256195-GeoGrad)*Thick*Depth  +2.69356e+06  * pmax(0, Perm+14.3343)*pmax(0, GeoGrad-0.0256195)*Thick*Depth           \
    -2.26024e+06 * pmax(0, -14.3343-Perm)*pmax(0, GeoGrad-0.0256195)*Thick*Depth  +997445       * pmax(0, Perm+13.4547)*Depth      \
    -142940      * pmax(0, -13.4547-Perm)*Depth +4.72846      * pmax(0, Depth-2202.83)*Thick*Depth                           \
    -5.72342     * pmax(0, 2202.83-Depth)*Thick*Depth   -53317.4     * pmax(0, Perm+14.6703)*pmax(0, -13.9256-Perm)*Thick*Depth            \
    +47567        * pmax(0, -14.6703-Perm)*pmax(0, -13.9256-Perm)*Thick*Depth -3.07368e+07 * Thick*pmax(0, Perm+14.7142)                              \
    +1.90718e+06  * pmax(0, GeoGrad-0.0255639)*pmax(0, -13.9256-Perm)*Thick*Depth    +411073       * pmax(0, 0.0255639-GeoGrad)*pmax(0, -13.9256-Perm)*Thick*Depth          \
    +768578       * pmax(0, Perm+12.9641)*pmax(0, Perm+13.9256)*Thick*Depth  -250835      * pmax(0, -12.9641-Perm)*pmax(0, Perm+13.9256)*Thick*Depth                    \
    -77.6737     * pmax(0, 3523.75-Depth)*pmax(0, GeoGrad-0.0256195)*Thick*Depth +50.0997      * pmax(0, Perm+13.9473)*pmax(0, Depth-2202.83)*Thick*Depth             \
    -3.581       * pmax(0, -13.9473-Perm)*pmax(0, Depth-2202.83)*Thick*Depth +2.96672e+06  * pmax(0, GeoGrad-0.0256195)*Depth                            \
    -1.7518e+07  * pmax(0, 0.0256195-GeoGrad)*Depth -2.80051e+06 * pmax(0, GeoGrad-0.0250539)*pmax(0, -13.4547-Perm)*Depth             \
    +1.29692e+07  * pmax(0, 0.0250539-GeoGrad)*pmax(0, -13.4547-Perm)*Depth -67.3052     * pmax(0, Perm+13.8431)*pmax(0, 2202.83-Depth)*Thick*Depth             \
    +4.07567      * pmax(0, -13.8431-Perm)*pmax(0, 2202.83-Depth)*Thick*Depth            
    ROM_3_MCO2_5yr = ROM_3_MCO2_5yr / 1000000000 / 30       
    return ROM_3_MCO2_5yr
 
#############
# ROM: 0.5-5
############# 
def ROM_4_MCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_4_MCO2_5yr =-2.50962e+09    +5.97516e+09  * pmax(0, Perm+13.9911)  -3.75289e+09 * pmax(0, -13.9911-Perm)                                           \
    +2.80255e+08  * Thick  +1.00801e+06  * pmax(0, Depth-2547.6)  -1.53343e+06 * pmax(0, 2547.6-Depth) -5.09309e+06 * Thick*Thick                                                   \
    +4.14144e+10  * pmax(0, GeoGrad-0.0253291) -1.11697e+11 * pmax(0, 0.0253291-GeoGrad)                                          \
    +48290.2      * Thick*Thick*Thick      -176.004     * Thick*Thick*Thick*Thick                                              \
    +1.63914e+08  * pmax(0, Perm+14.5929)*Thick -5.61565e+07 * pmax(0, -14.5929-Perm)*Thick                                        \
    +127181       * pmax(0, Depth-2872.52)*pmax(0, Perm+14.5929)*Thick -141377      * pmax(0, 2872.52-Depth)*pmax(0, Perm+14.5929)*Thick                           \
    +5.69813e+08  * pmax(0, Perm+14.0278)*pmax(0, Perm+14.5929)*Thick  -3.23314e+08 * pmax(0, -14.0278-Perm)*pmax(0, Perm+14.5929)*Thick                          \
    -6.15246e+06 * pmax(0, Perm+13.1614)*pmax(0, 2547.6-Depth)  -648476      * pmax(0, GeoGrad-0.0364025)*pmax(0, Depth-2872.52)*pmax(0, Perm+14.5929)*Thick                    \
    +1.09975e+09  * pmax(0, GeoGrad-0.0401399)*pmax(0, Perm+14.5929)*Thick -9.87504e+09 * pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick                         \
    -2.34743e+06 * pmax(0, Depth-3357.04)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick   +3.14071e+06  * pmax(0, 3357.04-Depth)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick           \
    +242567       * pmax(0, Depth-2496.86)*pmax(0, Perm+14.0278)*pmax(0, Perm+14.5929)*Thick  -46627       * pmax(0, 2496.86-Depth)*pmax(0, Perm+14.0278)*pmax(0, Perm+14.5929)*Thick             \
    +5.71504e+08  * pmax(0, Perm+12.8819)*pmax(0, Perm+14.0278)*pmax(0, Perm+14.5929)*Thick  -3.13727e+08 * pmax(0, -12.8819-Perm)*pmax(0, Perm+14.0278)*pmax(0, Perm+14.5929)*Thick            \
    -1.48413e+10 * pmax(0, Perm+12.8869)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick   +4.15956e+09  * pmax(0, -12.8869-Perm)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick          \
    +290.574      * pmax(0, Depth-1547.67)*Thick*Thick  +210.249      * pmax(0, 1547.67-Depth)*Thick*Thick                                      \
    +4.8403e+09   * pmax(0, Perm+12.8344)*pmax(0, Perm+13.9911) -3.76897e+09 * pmax(0, -12.8344-Perm)*pmax(0, Perm+13.9911)                             \
    -213956      * pmax(0, Perm+13.572)*pmax(0, 2872.52-Depth)*pmax(0, Perm+14.5929)*Thick  +93491.8      * pmax(0, -13.572-Perm)*pmax(0, 2872.52-Depth)*pmax(0, Perm+14.5929)*Thick             \
    +76165.8      * pmax(0, Perm+13.1385)*pmax(0, Depth-1547.67)*Thick*Thick -117.845     * pmax(0, -13.1385-Perm)*pmax(0, Depth-1547.67)*Thick*Thick                     
    ROM_4_MCO2_5yr = ROM_4_MCO2_5yr / 1000000000 / 30       
    return ROM_4_MCO2_5yr
     
#############
# ROM: 1-10
#############
def ROM_5_MCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_5_MCO2_5yr =-4.70419e+09 -4.86825e+09 * pmax(0, -13.7386-Perm) +1.95246e+06  * pmax(0, Depth-4489.41)                                            \
    +939791       * pmax(0, 4489.41-Depth)   +7.0577e+08   * Thick   -1.30872e+07 * Thick*Thick                                                    \
    +7.62645e+10  * pmax(0, GeoGrad-0.0275088)-4.27457e+10 * pmax(0, 0.0275088-GeoGrad)                                          \
    +131598       * Thick*Thick*Thick  -130.731     * pmax(0, Depth-1694.49)*pmax(0, 4489.41-Depth)                                       \
    -481.664     * Thick*Thick*Thick*Thick   +6.8172e+08   * pmax(0, Perm+14.3164)*Thick                                         \
    -1.56534e+08 * pmax(0, -14.3164-Perm)*Thick -1.27789e+06 * pmax(0, Depth-1946.93)*pmax(0, Perm+14.3164)*Thick                           \
    -463905      * pmax(0, 1946.93-Depth)*pmax(0, Perm+14.3164)*Thick  +3.16735e+06  * pmax(0, Perm+13.3459)*pmax(0, Depth-1946.93)*pmax(0, Perm+14.3164)*Thick             \
    -2.62932e+06 * pmax(0, -13.3459-Perm)*pmax(0, Depth-1946.93)*pmax(0, Perm+14.3164)*Thick            \
    +1.23832e+09  * pmax(0, Perm+12.6899)*pmax(0, Perm+14.3164)*Thick -6.43428e+08 * pmax(0, -12.6899-Perm)*pmax(0, Perm+14.3164)*Thick                          \
    +1.43626e+06  * pmax(0, GeoGrad-0.0269517)*pmax(0, Depth-1946.93)*pmax(0, Perm+14.3164)*Thick           \
    -5.00995e+06 * pmax(0, 0.0269517-GeoGrad)*pmax(0, Depth-1946.93)*pmax(0, Perm+14.3164)*Thick           \
    +3.9869e+06   * pmax(0, Depth-1742.79)*pmax(0, Perm+13.7386)-1.31158e+07 * pmax(0, 1742.79-Depth)*pmax(0, Perm+13.7386)                              \
    +1.89644e+09  * pmax(0, GeoGrad-0.0386452)*pmax(0, Perm+14.3164)*Thick-8.21646e+09 * pmax(0, 0.0386452-GeoGrad)*pmax(0, Perm+14.3164)*Thick                         \
    -1.67717e+11 * pmax(0, Perm+13.981)*pmax(0, 0.0275088-GeoGrad) -4.88517e+11 * pmax(0, -13.981-Perm)*pmax(0, 0.0275088-GeoGrad)                            \
    +5.59278e+06  * pmax(0, Perm+13.1236)*pmax(0, 4489.41-Depth)    -3.62935e+06 * pmax(0, -13.1236-Perm)*pmax(0, 4489.41-Depth)                             \
    +2.4629e+06   * pmax(0, Depth-1938.46)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.3164)*Thick +321017       * pmax(0, 1938.46-Depth)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.3164)*Thick            \
    -1.3476e+06  * pmax(0, Depth-2323.05)*pmax(0, 0.0386452-GeoGrad)*pmax(0, Perm+14.3164)*Thick  +5.49065e+06  * pmax(0, 2323.05-Depth)*pmax(0, 0.0386452-GeoGrad)*pmax(0, Perm+14.3164)*Thick           \
    -5.54774e+09 * pmax(0, Perm+13.1109)*pmax(0, 0.0386452-GeoGrad)*pmax(0, Perm+14.3164)*Thick  +7.32074e+09  * pmax(0, -13.1109-Perm)*pmax(0, 0.0386452-GeoGrad)*pmax(0, Perm+14.3164)*Thick          \
    -1.70238e+08 * pmax(0, Perm+13.8749)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.3164)*Thick  +2.85897e+08  * pmax(0, -13.8749-Perm)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.3164)*Thick         
    ROM_5_MCO2_5yr = ROM_5_MCO2_5yr / 1000000000 / 30       
    return ROM_5_MCO2_5yr
 
#############
# ROM: 5-50
############# 
def ROM_6_MCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_6_MCO2_5yr =-2.30345e+10 +8.78156e+10  * pmax(0, Perm+12.9445)  -7.30743e+10 * pmax(0, -12.9445-Perm)                                          \
    +1.44574e+07  * pmax(0, Depth-3260.4)  -2.06219e+07 * pmax(0, 3260.4-Depth)                                            \
    +4.29324e+09  * Thick  -7.62413e+07 * Thick*Thick    +1.81525e+11  * pmax(0, GeoGrad-0.0345342)                                         \
    -6.57095e+11 * pmax(0, 0.0345342-GeoGrad)   +714975       * Thick*Thick*Thick                                                       \
    +3900.01      * pmax(0, 1822.78-Depth)*pmax(0, 3260.4-Depth)  -2510.84     * Thick*Thick*Thick*Thick                                             \
    -1.40155e+07 * pmax(0, Perm+13.6336)*pmax(0, Depth-3260.4) +550561       * Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3260.4)                           \
    +2.06696e+06  * pmax(0, Perm+12.9279)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3260.4) +521734       * pmax(0, -12.9279-Perm)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3260.4)            \
    +4.26049e+10  * pmax(0, Perm+13.3654)*Thick   -2.17397e+08 * pmax(0, -13.3654-Perm)*Thick                                       \
    +9.52006e+06  * pmax(0, Depth-3336.52)*pmax(0, Perm+13.3654)*Thick -9.69479e+06 * pmax(0, 3336.52-Depth)*pmax(0, Perm+13.3654)*Thick                          \
    +2.07499e+09  * Perm*pmax(0, Perm+13.3654)*Thick    -1.78353e+07 * pmax(0, GeoGrad-0.0175175)*pmax(0, Depth-3336.52)*pmax(0, Perm+13.3654)*Thick                 \
    -3.8663e+07  * pmax(0, 1839.87-Depth)*pmax(0, Perm+12.9445)   -3.51449e+09 * pmax(0, GeoGrad-0.0256615)*Perm*pmax(0, Perm+13.3654)*Thick                     \
    +5.56792e+09  * pmax(0, 0.0256615-GeoGrad)*Perm*pmax(0, Perm+13.3654)*Thick  -1.79746e+07 * pmax(0, GeoGrad-0.0226121)*pmax(0, 3336.52-Depth)*pmax(0, Perm+13.3654)*Thick          \
    +2.9347e+07   * pmax(0, 0.0226121-GeoGrad)*pmax(0, 3336.52-Depth)*pmax(0, Perm+13.3654)*Thick +1.92766e+07  * pmax(0, GeoGrad-0.0217177)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3260.4)           \
    -5.01798e+07 * pmax(0, 0.0217177-GeoGrad)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3260.4)   +663690       * pmax(0, Depth-1692.34)*Perm*pmax(0, Perm+13.3654)*Thick                       \
    -695045      * pmax(0, 1692.34-Depth)*Perm*pmax(0, Perm+13.3654)*Thick                     
    ROM_6_MCO2_5yr = ROM_6_MCO2_5yr / 1000000000 / 30       
    return ROM_6_MCO2_5yr
 
###########
# ROM: 10-max
########### 
def ROM_7_MCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_7_MCO2_5yr =+1.70491e+10  -3.33135e+10 * pmax(0, Perm+12.8373)  -2.63283e+10 * pmax(0, -12.8373-Perm)                                          \
    -1.01142e+09 * pmax(0, Depth-5322.61)*pmax(0, Perm+12.8373)     +2.96e+07     * pmax(0, 5322.61-Depth)*pmax(0, Perm+12.8373)                             \
    -1.30994e+09 * Thick*pmax(0, Perm+12.8373)   +6.73103e+06  * pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)                          \
    -994583      * pmax(0, 2093.48-Depth)*Thick*pmax(0, Perm+12.8373)+6.11536e+06  * pmax(0, Depth-2962.7)                                            \
    -9.84196e+06 * pmax(0, 2962.7-Depth)   +5.96409e+09  * Thick    +1.40331e+10  * pmax(0, GeoGrad-0.028942)*Thick                                       \
    -3.89869e+10 * pmax(0, 0.028942-GeoGrad)*Thick  -47615.9     * Thick*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)                       \
    +1.86456e+10  * pmax(0, Perm+12.4319)*Thick  -7.15703e+09 * pmax(0, -12.4319-Perm)*Thick                                       \
    +6.95897e+07  * pmax(0, GeoGrad-0.0288039)*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)          \
    -1.21469e+08 * pmax(0, 0.0288039-GeoGrad)*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)          \
    +559909       * pmax(0, Depth-4670.83)*Thick -1.22165e+06 * pmax(0, 4670.83-Depth)*Thick                                        \
    -3.84767e+06 * pmax(0, Perm+12.4431)*pmax(0, 4670.83-Depth)*Thick +998604       * pmax(0, -12.4431-Perm)*pmax(0, 4670.83-Depth)*Thick                         \
    +5.23267e+10  * pmax(0, Perm+12.5412)*pmax(0, -12.4319-Perm)*Thick  +2.40998e+09  * pmax(0, -12.5412-Perm)*pmax(0, -12.4319-Perm)*Thick                        \
    +7281.26      * pmax(0, Depth-5322.61)*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)            \
    -374.895     * pmax(0, 5322.61-Depth)*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)            
    ROM_7_MCO2_5yr = ROM_7_MCO2_5yr / 1000000000 / 30       
    return ROM_7_MCO2_5yr 
                      
       
#################################################################################### 
# 10 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_MCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_1_MCO2_10yr =+4.9128e+07   +4.77263e+07  * Thick  +50767.2      * pmax(0, Depth-2130.1)*Thick                               \
    -39520.3     * pmax(0, 2130.1-Depth)*Thick  +2.61975e+08  * pmax(0, Perm+14.744)                                  \
    -1.91078e+08 * pmax(0, -14.744-Perm) +1.24491e+09  * pmax(0, GeoGrad-0.0174088)                                        \
    -1.39378e+08 * pmax(0, Perm+14.6726)*Thick  -5.96344e+07 * pmax(0, -14.6726-Perm)*Thick                             \
    -69005.5     * pmax(0, Depth-1966.83)*pmax(0, -14.6726-Perm)*Thick   +75351.7      * pmax(0, 1966.83-Depth)*pmax(0, -14.6726-Perm)*Thick               \
    +158707       * Depth*pmax(0, Perm+14.6726)*Thick+201645       * pmax(0, Perm+14.2094)*Depth*pmax(0, Perm+14.6726)*Thick             \
    -59291.9     * pmax(0, -14.2094-Perm)*Depth*pmax(0, Perm+14.6726)*Thick+13455.1      * pmax(0, Depth-2178.43)                                 \
    +35570.7      * pmax(0, 2178.43-Depth)+41517.8      * pmax(0, Perm+14.7858)*pmax(0, 2130.1-Depth)*Thick                 \
    -26872.1     * pmax(0, -14.7858-Perm)*pmax(0, 2130.1-Depth)*Thick+2.09016e+08  * pmax(0, GeoGrad-0.0300566)*Thick                            \
    +6.71953e+08  * pmax(0, 0.0300566-GeoGrad)*Thick-1.47203e+06 * Depth*pmax(0, 0.0300566-GeoGrad)*Thick                         \
    -5.26828e+06 * pmax(0, Perm+14.1759)*Depth*pmax(0, 0.0300566-GeoGrad)*Thick+1.43162e+06  * pmax(0, -14.1759-Perm)*Depth*pmax(0, 0.0300566-GeoGrad)*Thick          \
    +280677       * pmax(0, Depth-1318.6)*pmax(0, GeoGrad-0.0300566)*Thick-112493      * pmax(0, 1318.6-Depth)*pmax(0, GeoGrad-0.0300566)*Thick               \
    -3.93954e+08 * pmax(0, GeoGrad-0.0294556)*pmax(0, -14.6726-Perm)*Thick-1.41301e+09 * pmax(0, 0.0294556-GeoGrad)*pmax(0, -14.6726-Perm)*Thick                     \
    +4.65429      * pmax(0, 1992.15-Depth)*pmax(0, 2130.1-Depth)*Thick-177145      * pmax(0, Perm+15.0264)*pmax(0, 2178.43-Depth)                   \
    +2.11957e+06  * pmax(0, -15.0264-Perm)*pmax(0, 2178.43-Depth)-388.134     * Thick*pmax(0, Depth-2130.1)*Thick                          
    ROM_1_MCO2_10yr = ROM_1_MCO2_10yr / 1000000000 / 30       
    return ROM_1_MCO2_10yr
 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_MCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_2_MCO2_10yr =+2.18886e+11  +1.48423e+10  * Perm+1.33856e+11  * Thick                                                       \
    +4.26058e+06  * pmax(0, Depth-3381.79)*Thick-1.98935e+07 * pmax(0, 3381.79-Depth)*Thick                                         \
    +9.54094e+09  * Thick*Perm+296164       * pmax(0, Depth-3381.79)*Thick*Perm                                      \
    -1.41429e+06 * pmax(0, 3381.79-Depth)*Thick*Perm-3.53953e+08 * pmax(0, GeoGrad-0.0371514)*Perm                                                 \
    +9.68834e+08  * pmax(0, Perm+14.7285)*Perm-9.39235e+08 * pmax(0, -14.7285-Perm)*Perm                                        \
    -47425.3     * pmax(0, Depth-3774.14)*pmax(0, Perm+14.7285)*Perm+37032.7      * pmax(0, 3774.14-Depth)*pmax(0, Perm+14.7285)*Perm                           \
    +5.98545e+08  * pmax(0, Perm+13.9893)*Thick*Perm-5.89219e+08 * pmax(0, -13.9893-Perm)*Thick*Perm                                     \
    -67792.7     * pmax(0, Perm+13.9561)*pmax(0, 3381.79-Depth)*Thick*Perm+72365.4      * pmax(0, -13.9561-Perm)*pmax(0, 3381.79-Depth)*Thick*Perm                       \
    +609972       * pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm-3.7192e+06  * pmax(0, 1423.6-Depth)*pmax(0, 0.0371514-GeoGrad)*Perm                          \
    +21139.6      * Thick*pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm+2.70705e+09  * pmax(0, Perm+14.4494)*pmax(0, 0.0371514-GeoGrad)*Perm                         \
    -1.62158e+09 * pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm-5.05811     * pmax(0, Depth-1490.66)*pmax(0, 3381.79-Depth)*Thick                           \
    +14.5614      * pmax(0, 1490.66-Depth)*pmax(0, 3381.79-Depth)*Thick+1.60912e+10  * pmax(0, GeoGrad-0.0270544)*Thick                                       \
    -2.81541e+10 * pmax(0, 0.0270544-GeoGrad)*Thick-2.26603e+07 * pmax(0, Perm+14.9341)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +2.50741e+07  * pmax(0, -14.9341-Perm)*pmax(0, -13.9893-Perm)*Thick*Perm-13583.6     * pmax(0, Depth-1442.6)*pmax(0, -13.9893-Perm)*Thick*Perm                        \
    +15684.1      * pmax(0, 1442.6-Depth)*pmax(0, -13.9893-Perm)*Thick*Perm+1.04135e+09  * pmax(0, GeoGrad-0.0270544)*Thick*Perm                                    \
    -1.83224e+09 * pmax(0, 0.0270544-GeoGrad)*Thick*Perm-1.45956e+06 * pmax(0, Depth-2105.99)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm          \
    +8.13937e+06  * pmax(0, 2105.99-Depth)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm          \
    -305748      * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick+513776       * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick                         
    ROM_2_MCO2_10yr = ROM_2_MCO2_10yr / 1000000000 / 30       
    return ROM_2_MCO2_10yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_MCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_3_MCO2_10yr =+1.16025e+09   -4.2859e+09  * pmax(0, Perm+14.9851)+1.67777e+09  * pmax(0, -14.9851-Perm)                                          \
    +1.8728e+08   * Thick-493193      * pmax(0, Depth-2656.39)                                           \
    +1.03345e+06  * pmax(0, 2656.39-Depth)-898349      * Thick*Thick                                                   \
    +2.49582e+10  * pmax(0, GeoGrad-0.0251834)-2.19443e+10 * pmax(0, 0.0251834-GeoGrad)                                         \
    +16396.2      * Thick*Thick*Thick-41.7704     * Thick*Thick*Thick*Thick                                             \
    +96366        * pmax(0, Depth-1330.3)*Thick+14709.3      * pmax(0, 1330.3-Depth)*Thick                                         \
    +541976       * pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick-116961      * pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick                          \
    +4.34706e+08  * pmax(0, Perm+13.836)*Thick-2.23649e+08 * pmax(0, -13.836-Perm)*Thick                                        \
    +2.89735e+09  * pmax(0, Perm+14.4146)*pmax(0, Perm+14.9851)-3.99534e+09 * pmax(0, -14.4146-Perm)*pmax(0, Perm+14.9851)                            \
    +1.26436e+06  * pmax(0, Depth-1302.36)*pmax(0, Perm+14.9851)-6.12039e+06 * pmax(0, 1302.36-Depth)*pmax(0, Perm+14.9851)                             \
    +202311       * pmax(0, GeoGrad-0.0311258)*pmax(0, Depth-1330.3)*Thick-1.53224e+06 * pmax(0, 0.0311258-GeoGrad)*pmax(0, Depth-1330.3)*Thick                         \
    -1.00424e+07 * pmax(0, Perm+14.3174)*pmax(0, 0.0311258-GeoGrad)*pmax(0, Depth-1330.3)*Thick+1.96776e+06  * pmax(0, -14.3174-Perm)*pmax(0, 0.0311258-GeoGrad)*pmax(0, Depth-1330.3)*Thick          \
    -2.05769e+06 * pmax(0, Perm+14.4221)*Thick*Thick+2.26538e+06  * pmax(0, -14.4221-Perm)*Thick*Thick                                    \
    +1.35433e+06  * pmax(0, Perm+14.3618)*pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick+64867.8      * pmax(0, -14.3618-Perm)*pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick           \
    +1.9176e+07   * pmax(0, GeoGrad-0.0140863)*pmax(0, Perm+14.4221)*Thick*Thick+1.10332e+06  * pmax(0, Perm+13.4547)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick             \
    -391448      * pmax(0, -13.4547-Perm)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick-429638      * pmax(0, Depth-1801.57)*pmax(0, Perm+14.4146)*pmax(0, Perm+14.9851)               \
    +1.24744e+06  * pmax(0, 1801.57-Depth)*pmax(0, Perm+14.4146)*pmax(0, Perm+14.9851)-158.979     * pmax(0, Depth-1260.48)*Thick*Thick                                     \
    -432.69      * pmax(0, 1260.48-Depth)*Thick*Thick-83271.2     * pmax(0, Perm+13.7398)*Thick*Thick*Thick-8431.66     * pmax(0, -13.7398-Perm)*Thick*Thick*Thick                                 
    ROM_3_MCO2_10yr = ROM_3_MCO2_10yr / 1000000000 / 30       
    return ROM_3_MCO2_10yr 
#############
ROM: 0.5-5
#############
def ROM_4_MCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_MCO2_10yr =    -5.11718e+09   +1.21564e+10  * pmax(0, Perm+13.9911)-7.69951e+09 * pmax(0, -13.9911-Perm)                                           \
    +5.83072e+08  * Thick+1.97304e+06  * pmax(0, Depth-2547.6)-3.10268e+06 * pmax(0, 2547.6-Depth)                                             \
    -1.08313e+07 * Thick*Thick+7.85743e+10  * pmax(0, GeoGrad-0.0253291)                                          \
    -2.19435e+11 * pmax(0, 0.0253291-GeoGrad)+103609       * Thick*Thick*Thick                                                 \
    -378.895     * Thick*Thick*Thick*Thick+3.18127e+08  * pmax(0, Perm+14.5929)*Thick                                         \
    -1.03794e+08 * pmax(0, -14.5929-Perm)*Thick+246881       * pmax(0, Depth-2872.52)*pmax(0, Perm+14.5929)*Thick                           \
    -285565      * pmax(0, 2872.52-Depth)*pmax(0, Perm+14.5929)*Thick+1.16561e+09  * pmax(0, Perm+14.0278)*pmax(0, Perm+14.5929)*Thick                           \
    -6.4545e+08  * pmax(0, -14.0278-Perm)*pmax(0, Perm+14.5929)*Thick-1.22698e+07 * pmax(0, Perm+13.1614)*pmax(0, 2547.6-Depth)                                        \
    -1.40292e+06 * pmax(0, GeoGrad-0.0364025)*pmax(0, Depth-2872.52)*pmax(0, Perm+14.5929)*Thick                    \
    +2.19105e+09  * pmax(0, GeoGrad-0.0401399)*pmax(0, Perm+14.5929)*Thick-1.99567e+10 * pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick                         \
    -4.46761e+06 * pmax(0, Depth-3422.25)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick+6.1145e+06   * pmax(0, 3422.25-Depth)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick           \
    +483795       * pmax(0, Depth-2531.8)*pmax(0, Perm+14.0278)*pmax(0, Perm+14.5929)*Thick-80675.2     * pmax(0, 2531.8-Depth)*pmax(0, Perm+14.0278)*pmax(0, Perm+14.5929)*Thick              \
    +1.24129e+09  * pmax(0, Perm+12.8819)*pmax(0, Perm+14.0278)*pmax(0, Perm+14.5929)*Thick-6.46106e+08 * pmax(0, -12.8819-Perm)*pmax(0, Perm+14.0278)*pmax(0, Perm+14.5929)*Thick            \
    -3.15614e+10 * pmax(0, Perm+12.8869)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick+8.43827e+09  * pmax(0, -12.8869-Perm)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick          \
    +572.26       * pmax(0, Depth-1547.67)*Thick*Thick+459.7        * pmax(0, 1547.67-Depth)*Thick*Thick                                      \
    +9.71806e+09  * pmax(0, Perm+12.8344)*pmax(0, Perm+13.9911)-7.49692e+09 * pmax(0, -12.8344-Perm)*pmax(0, Perm+13.9911)                             \
    -450900      * pmax(0, Perm+13.572)*pmax(0, 2872.52-Depth)*pmax(0, Perm+14.5929)*Thick+202259       * pmax(0, -13.572-Perm)*pmax(0, 2872.52-Depth)*pmax(0, Perm+14.5929)*Thick             \
    +157313       * pmax(0, Perm+13.1385)*pmax(0, Depth-1547.67)*Thick*Thick-236.243     * pmax(0, -13.1385-Perm)*pmax(0, Depth-1547.67)*Thick*Thick                       
    ROM_4_MCO2_10yr = ROM_4_MCO2_10yr / 1000000000 / 30       
    return ROM_4_MCO2_10yr
 
#############
ROM: 1-10
#############
def ROM_5_MCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_MCO2_10yr =-8.35789e+09   +1.36649e+10  * pmax(0, Perm+13.7386)-1.15323e+10 * pmax(0, -13.7386-Perm)                                           \
    +2.22239e+06  * pmax(0, Depth-4489.41)-1.8997e+06  * pmax(0, 4489.41-Depth)                                            \
    +1.22444e+09  * Thick-2.59939e+07 * Thick*Thick+1.52973e+11  * pmax(0, GeoGrad-0.0275088)                                          \
    -3.5658e+11  * pmax(0, 0.0275088-GeoGrad)+265088       * Thick*Thick*Thick                                                 \
    -353.172     * pmax(0, Depth-1694.49)*pmax(0, 4489.41-Depth)+961.835      * pmax(0, 1694.49-Depth)*pmax(0, 4489.41-Depth)                              \
    -974.315     * Thick*Thick*Thick*Thick+1.62148e+09  * pmax(0, Perm+14.3252)*Thick                                         \
    -3.33565e+08 * pmax(0, -14.3252-Perm)*Thick-1.37898e+06 * pmax(0, Depth-1937.07)*pmax(0, Perm+14.3252)*Thick                           \
    -2.30345e+06 * pmax(0, 1937.07-Depth)*pmax(0, Perm+14.3252)*Thick+4.49567e+06  * pmax(0, Perm+13.3381)*pmax(0, Depth-1937.07)*pmax(0, Perm+14.3252)*Thick             \
    -3.61039e+06 * pmax(0, -13.3381-Perm)*pmax(0, Depth-1937.07)*pmax(0, Perm+14.3252)*Thick+5.05225e+09  * pmax(0, Perm+12.7006)*pmax(0, Perm+14.3252)*Thick                           \
    -1.31616e+09 * pmax(0, -12.7006-Perm)*pmax(0, Perm+14.3252)*Thick+2.07098e+06  * pmax(0, GeoGrad-0.0269517)*pmax(0, Depth-1937.07)*pmax(0, Perm+14.3252)*Thick           \
    -6.6285e+06  * pmax(0, 0.0269517-GeoGrad)*pmax(0, Depth-1937.07)*pmax(0, Perm+14.3252)*Thick+3.48686e+06  * pmax(0, Depth-1742.79)*pmax(0, Perm+13.7386)                              \
    -1.36654e+07 * pmax(0, 1742.79-Depth)*pmax(0, Perm+13.7386)+4.05673e+09  * pmax(0, GeoGrad-0.0379934)*pmax(0, Perm+14.3252)*Thick                         \
    -1.60926e+10 * pmax(0, 0.0379934-GeoGrad)*pmax(0, Perm+14.3252)*Thick-1.70271e+10 * pmax(0, Perm+13.1991)*pmax(0, 0.0379934-GeoGrad)*pmax(0, Perm+14.3252)*Thick           \
    +1.91547e+10  * pmax(0, -13.1991-Perm)*pmax(0, 0.0379934-GeoGrad)*pmax(0, Perm+14.3252)*Thick-4.1825e+06  * pmax(0, Depth-2323.05)*pmax(0, 0.0379934-GeoGrad)*pmax(0, Perm+14.3252)*Thick           \
    +1.18855e+07  * pmax(0, 2323.05-Depth)*pmax(0, 0.0379934-GeoGrad)*pmax(0, Perm+14.3252)*Thick+3.17847e+06  * pmax(0, Perm+13.1548)*pmax(0, 4489.41-Depth)                                    \
    +3.15895e+06  * pmax(0, Depth-1938.46)*pmax(0, -12.7006-Perm)*pmax(0, Perm+14.3252)*Thick-2.53568e+06 * pmax(0, 1938.46-Depth)*pmax(0, -12.7006-Perm)*pmax(0, Perm+14.3252)*Thick            \
    -7.09003e+08 * pmax(0, Perm+13.7997)*pmax(0, -12.7006-Perm)*pmax(0, Perm+14.3252)*Thick+7.26671e+08  * pmax(0, -13.7997-Perm)*pmax(0, -12.7006-Perm)*pmax(0, Perm+14.3252)*Thick           \
    +58473.6      * pmax(0, Depth-1948.72)*Thick-302844      * pmax(0, 1948.72-Depth)*Thick+3.54133e+06  * pmax(0, -12.307-Perm)*pmax(0, 1937.07-Depth)*pmax(0, Perm+14.3252)*Thick             
    ROM_5_MCO2_10yr = ROM_5_MCO2_10yr / 1000000000 / 30       
    return ROM_5_MCO2_10yr
#############
# ROM: 5-50
############# 
def ROM_6_MCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_6_MCO2_10yr =-2.17395e+10  +9.94447e+10  * pmax(0, Perm+12.9411)-1.35887e+11 * pmax(0, -12.9411-Perm)                                          \
    +2.32061e+07  * pmax(0, Depth-3166.53)-3.34779e+07 * pmax(0, 3166.53-Depth)+6.74555e+09  * Thick-1.08447e+08 * Thick*Thick+3.24137e+11  * pmax(0, GeoGrad-0.0345342)                                         \
    -1.37769e+12 * pmax(0, 0.0345342-GeoGrad)+971447       * Thick*Thick*Thick                                                \
    +4533.16      * pmax(0, Depth-1822.78)*pmax(0, 3166.53-Depth)-7540.75     * pmax(0, 1822.78-Depth)*pmax(0, 3166.53-Depth)                             \
    -3294.1      * Thick*Thick*Thick*Thick-2.02418e+07 * pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)                             \
    -1.4304e+07  * pmax(0, -13.6336-Perm)*pmax(0, Depth-3166.53)+2.30424e+06  * Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)                          \
    +3.81965e+06  * pmax(0, Perm+12.9279)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)-2.15362e+06 * pmax(0, -12.9279-Perm)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)           \
    +3.97803e+09  * pmax(0, Perm+13.3533)*Thick-2.07412e+06 * pmax(0, 3261.68-Depth)*pmax(0, Perm+13.3533)*Thick                          \
    +8.65069e+09  * pmax(0, Perm+12.7914)*pmax(0, Perm+13.3533)*Thick-5.2966e+09  * pmax(0, -12.7914-Perm)*pmax(0, Perm+13.3533)*Thick                         \
    -4.11979e+07 * pmax(0, GeoGrad-0.0175175)*pmax(0, Depth-3261.68)*pmax(0, Perm+13.3533)*Thick+5.72348e+06  * pmax(0, Depth-2447.08)*pmax(0, Perm+12.7914)*pmax(0, Perm+13.3533)*Thick            \
    -3.60449e+06 * pmax(0, 2447.08-Depth)*pmax(0, Perm+12.7914)*pmax(0, Perm+13.3533)*Thick            \
    +9.50704e+10  * pmax(0, GeoGrad-0.0254346)*pmax(0, Perm+13.3533)*Thick-1.52836e+11 * pmax(0, 0.0254346-GeoGrad)*pmax(0, Perm+13.3533)*Thick                        \
    -4.86621e+07 * pmax(0, GeoGrad-0.0226121)*pmax(0, 3261.68-Depth)*pmax(0, Perm+13.3533)*Thick+8.13981e+07  * pmax(0, 0.0226121-GeoGrad)*pmax(0, 3261.68-Depth)*pmax(0, Perm+13.3533)*Thick          \
    -1.24836e+09 * pmax(0, Poro-0.126417)*pmax(0, Perm+13.3533)*Thick+5.06138e+09  * pmax(0, 0.126417-Poro)*pmax(0, Perm+13.3533)*Thick                         \
    -2.71033e+07 * pmax(0, Perm+12.7955)*Thick*Thick-4.95651e+06 * pmax(0, -12.7955-Perm)*Thick*Thick+1261.96      * pmax(0, Depth-1618.38)*Thick*Thick+8042.11      * pmax(0, 1618.38-Depth)*Thick*Thick                              \
    +3.69724e+07  * pmax(0, GeoGrad-0.0217177)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)-9.14551e+07 * pmax(0, 0.0217177-GeoGrad)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)          \
    +6.43237e+10  * GeoGrad*pmax(0, Perm+12.7914)*pmax(0, Perm+13.3533)*Thick                       
    ROM_6_MCO2_10yr = ROM_6_MCO2_10yr / 1000000000 / 30       
    return ROM_6_MCO2_10yr 
###########
# ROM: 10-max
###########
def ROM_7_MCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_7_MCO2_10yr =+4.74554e+10  -4.30982e+10 * pmax(0, Perm+12.8373)-6.86611e+10 * pmax(0, -12.8373-Perm)                                          \
    +2.71725e+09  * pmax(0, Depth-5322.61)*pmax(0, Perm+12.8373)-8.32535e+08 * Thick*pmax(0, Perm+12.8373)                                        \
    +1.17077e+07  * pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)-1.55144e+06 * pmax(0, 2093.48-Depth)*Thick*pmax(0, Perm+12.8373)                          \
    +7.11281e+06  * pmax(0, Depth-2962.7)+1.19024e+10  * Thick+2.38989e+10  * pmax(0, GeoGrad-0.028942)*Thick                                       \
    -6.91839e+10 * pmax(0, 0.028942-GeoGrad)*Thick-85546.1     * Thick*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)                       \
    +4.84161e+10  * pmax(0, Perm+12.4319)*Thick-1.43197e+10 * pmax(0, -12.4319-Perm)*Thick                                       \
    +1.11285e+08  * pmax(0, GeoGrad-0.0288039)*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)-1.84108e+08 * pmax(0, 0.0288039-GeoGrad)*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)          \
    +1.37017e+06  * pmax(0, Depth-4670.83)*Thick-2.57024e+06 * pmax(0, 4670.83-Depth)*Thick                                        \
    -6.89644e+06 * pmax(0, Perm+12.4431)*pmax(0, 4670.83-Depth)*Thick+2.07736e+06  * pmax(0, -12.4431-Perm)*pmax(0, 4670.83-Depth)*Thick                         \
    +8.54683e+10  * pmax(0, Perm+12.5412)*pmax(0, -12.4319-Perm)*Thick+4.86942e+09  * pmax(0, -12.5412-Perm)*pmax(0, -12.4319-Perm)*Thick                        \
    -1.48621e+08 * Thick*pmax(0, Perm+12.4319)*Thick+4.07214e+12  * pmax(0, GeoGrad-0.023341)*pmax(0, Perm+12.8373)                            \
    -7.8401e+12  * pmax(0, 0.023341-GeoGrad)*pmax(0, Perm+12.8373)                            
    ROM_7_MCO2_10yr = ROM_7_MCO2_10yr / 1000000000 / 30       
    return ROM_7_MCO2_10yr 
#################################################################################### 
# 15 years
####################################################################################
#############
ROM: 0-0.1
#############
def ROM_1_MCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad):
    ROM_1_MCO2_15yr =+4.38846e+07   +5.98501e+07  * Thick+51541.1      * pmax(0, Depth-2130.1)*Thick                             \
    -41252.4     * pmax(0, 2130.1-Depth)*Thick+1.5535e+08   * pmax(0, Perm+14.744)                                \
    -2.47843e+08 * pmax(0, -14.744-Perm)+5.79085e+09  * pmax(0, GeoGrad-0.017117)                              \
    -1.11891e+10 * pmax(0, 0.017117-GeoGrad)-2.48862e+08 * pmax(0, Perm+14.6582)*Thick                            \
    -7.17686e+07 * pmax(0, -14.6582-Perm)*Thick-87887.3     * pmax(0, Depth-1966.83)*pmax(0, -14.6582-Perm)*Thick             \
    +136705       * pmax(0, 1966.83-Depth)*pmax(0, -14.6582-Perm)*Thick+225735       * Depth*pmax(0, Perm+14.6582)*Thick                         \
    +273242       * pmax(0, Perm+14.2094)*Depth*pmax(0, Perm+14.6582)*Thick-132848      * pmax(0, -14.2094-Perm)*Depth*pmax(0, Perm+14.6582)*Thick          \
    +4.57808e+07  * pmax(0, GeoGrad-0.0209519)*pmax(0, Depth-2130.1)*Thick-1.2311e+06  * pmax(0, 0.0209519-GeoGrad)*pmax(0, Depth-2130.1)*Thick             \
    +55516.3      * pmax(0, Perm+14.7858)*pmax(0, 2130.1-Depth)*Thick-70121.1     * pmax(0, -14.7858-Perm)*pmax(0, 2130.1-Depth)*Thick              \
    +2.87871e+08  * pmax(0, GeoGrad-0.0280159)*Thick-3.65566e+08 * pmax(0, 0.0280159-GeoGrad)*Thick                          \
    -613576      * GeoGrad*pmax(0, 1966.83-Depth)*pmax(0, -14.6582-Perm)*Thick-2.96177e+06 * pmax(0, Depth-1949.35)*pmax(0, GeoGrad-0.017117)                \
    -7.98814e+06 * pmax(0, 1949.35-Depth)*pmax(0, GeoGrad-0.017117)+1.56024e+06  * GeoGrad*Depth*pmax(0, Perm+14.6582)*Thick                      \
    -9.19061e+07 * pmax(0, Perm+15.0335)*pmax(0, -14.6582-Perm)*Thick+116239       * pmax(0, 90-Thick)*Thick                                 \
    +170.768      * pmax(0, Depth-2980.93)*pmax(0, 90-Thick)*Thick-43.231      * pmax(0, 2980.93-Depth)*pmax(0, 90-Thick)*Thick                   \
    +3.00827e+06  * Perm*pmax(0, GeoGrad-0.0209519)*pmax(0, Depth-2130.1)*Thick+34354.8      * pmax(0, Depth-1247.37)                               \
    +135432       * pmax(0, 1247.37-Depth)                               
    ROM_1_MCO2_15yr = ROM_1_MCO2_15yr / 1000000000 / 30       
    return ROM_1_MCO2_15yr  
#############
# ROM: 0.05-0.5
#############
def ROM_2_MCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_MCO2_15yr =+3.27265e+11      +2.21902e+10  * Perm+2.04644e+11  * Thick+6.32465e+06  * pmax(0, Depth-3381.79)*Thick-3.01329e+07 * pmax(0, 3381.79-Depth)*Thick                                         \
    +1.45874e+10  * Thick*Perm+439713       * pmax(0, Depth-3381.79)*Thick*Perm-2.14244e+06 * pmax(0, 3381.79-Depth)*Thick*Perm-4.96007e+08 * pmax(0, GeoGrad-0.0371514)*Perm                                               \
    +1.45188e+09  * pmax(0, Perm+14.7285)*Perm-1.40557e+09 * pmax(0, -14.7285-Perm)*Perm                                        \
    -70219.4     * pmax(0, Depth-3774.14)*pmax(0, Perm+14.7285)*Perm+53622.8      * pmax(0, 3774.14-Depth)*pmax(0, Perm+14.7285)*Perm                           \
    +9.17104e+08  * pmax(0, Perm+13.9893)*Thick*Perm-9.03033e+08 * pmax(0, -13.9893-Perm)*Thick*Perm                                     \
    -102795      * pmax(0, Perm+13.9561)*pmax(0, 3381.79-Depth)*Thick*Perm+110085       * pmax(0, -13.9561-Perm)*pmax(0, 3381.79-Depth)*Thick*Perm                       \
    +890856       * pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm-5.39561e+06 * pmax(0, 1423.6-Depth)*pmax(0, 0.0371514-GeoGrad)*Perm                          \
    +30280.4      * Thick*pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm+3.93752e+09  * pmax(0, Perm+14.4494)*pmax(0, 0.0371514-GeoGrad)*Perm                         \
    -2.36908e+09 * pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm-7.79927     * pmax(0, Depth-1490.66)*pmax(0, 3381.79-Depth)*Thick                           \
    +21.9521      * pmax(0, 1490.66-Depth)*pmax(0, 3381.79-Depth)*Thick+2.39549e+10  * pmax(0, GeoGrad-0.0270544)*Thick                                       \
    -4.13941e+10 * pmax(0, 0.0270544-GeoGrad)*Thick-3.51027e+07 * pmax(0, Perm+14.9341)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +3.87168e+07  * pmax(0, -14.9341-Perm)*pmax(0, -13.9893-Perm)*Thick*Perm-20206.8     * pmax(0, Depth-1461.17)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +23320.3      * pmax(0, 1461.17-Depth)*pmax(0, -13.9893-Perm)*Thick*Perm+1.55024e+09  * pmax(0, GeoGrad-0.0270544)*Thick*Perm                                    \
    -2.693e+09   * pmax(0, 0.0270544-GeoGrad)*Thick*Perm-2.11998e+06 * pmax(0, Depth-2105.99)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm          \
    +1.20758e+07  * pmax(0, 2105.99-Depth)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm-461290      * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick                   \
    +761292       * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick                         
    ROM_2_MCO2_15yr = ROM_2_MCO2_15yr / 1000000000 / 30       
    return ROM_2_MCO2_15yr 
#############
# ROM: 0.1-1
#############
def ROM_3_MCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_3_MCO2_15yr =+3.83515e+09  -1.00169e+10 * pmax(0, Perm+14.9851)+8.49558e+09  * pmax(0, -14.9851-Perm)+2.88196e+08  * Thick-1.41235e+06 * pmax(0, Depth-2656.39)+2.03893e+06  * pmax(0, 2656.39-Depth)                                                   \
    +29812.4      * Thick*Thick*Thick-6.51313e+09 * pmax(0, GeoGrad-0.0282262)-3.35501e+10 * pmax(0, 0.0282262-GeoGrad)+35.6699      * Thick*Thick*Thick*Thick                                             \
    -104512      * pmax(0, Depth-1330.3)*Thick-155877      * pmax(0, 1330.3-Depth)*Thick                                         \
    +880611       * pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick-686809      * pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick                          \
    +6.71859e+08  * pmax(0, Perm+13.836)*Thick-4.94073e+08 * pmax(0, -13.836-Perm)*Thick                                        \
    +6.25554e+09  * pmax(0, Perm+14.4525)*pmax(0, Perm+14.9851)-8.6784e+09  * pmax(0, -14.4525-Perm)*pmax(0, Perm+14.9851)                            \
    +1.72315e+06  * pmax(0, Depth-1302.36)*pmax(0, Perm+14.9851)-5.41669e+06 * pmax(0, 1302.36-Depth)*pmax(0, Perm+14.9851)                             \
    +1.0417e+06   * pmax(0, GeoGrad-0.0192943)*pmax(0, Depth-1330.3)*Thick-1.11479e+06 * pmax(0, 0.0192943-GeoGrad)*pmax(0, Depth-1330.3)*Thick                         \
    +4.76628e+06  * pmax(0, Perm+14.5202)*pmax(0, GeoGrad-0.0192943)*pmax(0, Depth-1330.3)*Thick-1.38592e+06 * pmax(0, -14.5202-Perm)*pmax(0, GeoGrad-0.0192943)*pmax(0, Depth-1330.3)*Thick          \
    -6.42844e+06 * pmax(0, Perm+14.3514)*Thick*Thick+6.4554e+06   * pmax(0, -14.3514-Perm)*Thick*Thick+2.67354e+07  * GeoGrad*pmax(0, Perm+14.3514)*Thick*Thick+552666       * pmax(0, Depth-1340.37)*pmax(0, -13.836-Perm)*Thick                    \
    +60860.8      * pmax(0, 1340.37-Depth)*pmax(0, -13.836-Perm)*Thick-388726      * pmax(0, Perm+14.3016)*pmax(0, Depth-1340.37)*pmax(0, -13.836-Perm)*Thick            \
    +61926        * pmax(0, -14.3016-Perm)*pmax(0, Depth-1340.37)*pmax(0, -13.836-Perm)*Thick+6.66037e+06  * pmax(0, Perm+13.1849)*Thick*Thick*Thick                                  \
    -30278.9     * pmax(0, -13.1849-Perm)*Thick*Thick*Thick-1025.5      * pmax(0, Depth-1986.04)*Thick*Thick+1369.29      * pmax(0, 1986.04-Depth)*Thick*Thick+4.50407      * pmax(0, Depth-1986.04)*Thick*Thick*Thick                                  \
    -7.54211     * pmax(0, 1986.04-Depth)*Thick*Thick*Thick+3.20848e+10  * pmax(0, GeoGrad-0.0172495)*pmax(0, Perm+14.9851)                           \
    -1.77371e+11 * pmax(0, 0.0172495-GeoGrad)*pmax(0, Perm+14.9851)+1.2273e+06   * pmax(0, Perm+13.4562)*pmax(0, Depth-1302.36)*pmax(0, Perm+14.9851)               \
    +719888       * pmax(0, -13.4562-Perm)*pmax(0, Depth-1302.36)*pmax(0, Perm+14.9851)              
    ROM_3_MCO2_15yr = ROM_3_MCO2_15yr / 1000000000 / 30       
    return ROM_3_MCO2_15yr 
 
#############
# ROM: 0.5-5
#############
def ROM_4_MCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad):   
    ROM_4_MCO2_15yr =-7.50052e+09 +1.31943e+10  * pmax(0, Perm+13.9911)-8.65761e+09 * pmax(0, -13.9911-Perm)+7.99648e+08  * Thick+2.78241e+06  * pmax(0, Depth-2547.6)-3.61557e+06 * pmax(0, 2547.6-Depth)                                             \
    -1.52743e+07 * Thick*Thick+1.18535e+11  * pmax(0, GeoGrad-0.0253291)-3.17046e+11 * pmax(0, 0.0253291-GeoGrad)+151099       * Thick*Thick*Thick                                                 \
    -567.084     * Thick*Thick*Thick*Thick+5.29764e+08  * pmax(0, Perm+14.5929)*Thick-2.73404e+08 * pmax(0, -14.5929-Perm)*Thick+405324       * pmax(0, Depth-2886.06)*pmax(0, Perm+14.5929)*Thick                           \
    -337146      * pmax(0, 2886.06-Depth)*pmax(0, Perm+14.5929)*Thick+1.65301e+09  * pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick                           \
    -9.39979e+08 * pmax(0, -14.0329-Perm)*pmax(0, Perm+14.5929)*Thick-2.24577e+07 * pmax(0, Perm+13.1614)*pmax(0, 2547.6-Depth)                                        \
    -2.61104e+06 * pmax(0, GeoGrad-0.0364025)*pmax(0, Depth-2886.06)*pmax(0, Perm+14.5929)*Thick+3.30407e+09  * pmax(0, GeoGrad-0.0401399)*pmax(0, Perm+14.5929)*Thick                         \
    -1.94083e+10 * pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick+2.02677e+09  * pmax(0, Perm+12.8971)*pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick             \
    -1.18875e+09 * pmax(0, -12.8971-Perm)*pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick-7.70109e+06 * pmax(0, Depth-2181.2)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick            \
    +9.79921e+06  * pmax(0, 2181.2-Depth)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick-5.02884e+10 * pmax(0, Perm+12.8869)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick           \
    +1.30428e+10  * pmax(0, -12.8869-Perm)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick+1.5444e+10   * pmax(0, Perm+13.2065)*pmax(0, Perm+13.9911)                              \
    -9.81887e+09 * pmax(0, -13.2065-Perm)*pmax(0, Perm+13.9911)+318.278      * pmax(0, Depth-1367.21)*Thick*Thick                                      \
    +926.711      * pmax(0, 1367.21-Depth)*Thick*Thick-551461      * pmax(0, Perm+13.572)*pmax(0, 2886.06-Depth)*pmax(0, Perm+14.5929)*Thick              \
    +68313.4      * pmax(0, -13.572-Perm)*pmax(0, 2886.06-Depth)*pmax(0, Perm+14.5929)*Thick+688435       * pmax(0, Depth-2199.2)*pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick              \
    -336638      * pmax(0, 2199.2-Depth)*pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick              
    ROM_4_MCO2_15yr = ROM_4_MCO2_15yr / 1000000000 / 30       
    return ROM_4_MCO2_15yr
 
#############
# ROM: 1-10
#############
def ROM_5_MCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_MCO2_15yr =-2.62964e+09  +2.95552e+10  * pmax(0, Perm+13.5959)-2.16878e+10 * pmax(0, -13.5959-Perm)                                           \
    +4.56637e+06  * pmax(0, Depth-4489.41)-6.21214e+06 * pmax(0, 4489.41-Depth)                                            \
    +1.7388e+09   * Thick-3.05426e+07 * Thick*Thick+1.23371e+11  * pmax(0, GeoGrad-0.0275088)                                          \
    -7.06724e+11 * pmax(0, 0.0275088-GeoGrad)+284125       * Thick*Thick*Thick                                                          \
    -2307.25     * pmax(0, 1694.49-Depth)*pmax(0, 4489.41-Depth)-1014.03     * Thick*Thick*Thick*Thick                                              \
    +9.09204e+08  * pmax(0, Perm+14.3114)*Thick-4.23712e+08 * pmax(0, -14.3114-Perm)*Thick                                        \
    +504678       * pmax(0, Depth-3558.1)*pmax(0, Perm+14.3114)*Thick-549867      * pmax(0, 3558.1-Depth)*pmax(0, Perm+14.3114)*Thick                            \
    +1.58919e+09  * pmax(0, Perm+13.6677)*pmax(0, Perm+14.3114)*Thick-1.40186e+09 * pmax(0, -13.6677-Perm)*pmax(0, Perm+14.3114)*Thick                          \
    -2.63725e+06 * pmax(0, Perm+13.1196)*pmax(0, 3558.1-Depth)*pmax(0, Perm+14.3114)*Thick+336048       * pmax(0, -13.1196-Perm)*pmax(0, 3558.1-Depth)*pmax(0, Perm+14.3114)*Thick             \
    +3.6664e+09   * pmax(0, Perm+13.1071)*pmax(0, Perm+14.3114)*Thick+1.49073e+10  * pmax(0, GeoGrad-0.0179288)*pmax(0, Perm+14.3114)*Thick                         \
    -2.10077e+10 * pmax(0, 0.0179288-GeoGrad)*pmax(0, Perm+14.3114)*Thick+1.28834e+07  * pmax(0, Depth-1049.3)*pmax(0, GeoGrad-0.0179288)*pmax(0, Perm+14.3114)*Thick                      \
    +1.19478e+06  * pmax(0, Depth-2282.58)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3114)*Thick-288169      * pmax(0, 2282.58-Depth)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3114)*Thick             \
    +5.63927e+10  * pmax(0, Perm+12.6185)*pmax(0, GeoGrad-0.0179288)*pmax(0, Perm+14.3114)*Thick-2.07311e+10 * pmax(0, -12.6185-Perm)*pmax(0, GeoGrad-0.0179288)*pmax(0, Perm+14.3114)*Thick          \
    +2.83561e+09  * pmax(0, Perm+13.1548)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3114)*Thick-1.13581e+09 * pmax(0, -13.1548-Perm)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3114)*Thick            \
    +450.265      * pmax(0, Depth-1613.21)*Thick*Thick+2118.66      * pmax(0, 1613.21-Depth)*Thick*Thick                                      \
    -4.12724e+08 * pmax(0, Poro-0.0953138)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3114)*Thick+3.43899e+09  * pmax(0, 0.0953138-Poro)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3114)*Thick           
    ROM_5_MCO2_15yr = ROM_5_MCO2_15yr / 1000000000 / 30       
    return ROM_5_MCO2_15yr
 
#############
# ROM: 5-50
#############
def ROM_6_MCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_MCO2_15yr =-3.15986e+10  +1.5555e+11   * pmax(0, Perm+12.9374)-1.87939e+11 * pmax(0, -12.9374-Perm)                                           \
    +3.47902e+07  * pmax(0, Depth-3166.53)-5.01061e+07 * pmax(0, 3166.53-Depth)                                            \
    +9.93548e+09  * Thick-1.62474e+08 * Thick*Thick+4.13341e+11  * pmax(0, GeoGrad-0.0345342)                                          \
    -2.24236e+12 * pmax(0, 0.0345342-GeoGrad)+1.44959e+06  * Thick*Thick*Thick                                                         \
    -14605.1     * pmax(0, 1822.78-Depth)*pmax(0, 3166.53-Depth)-4961.93     * Thick*Thick*Thick*Thick                                              \
    -3.39645e+07 * pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)-1.67264e+07 * pmax(0, -13.6336-Perm)*pmax(0, Depth-3166.53)                             \
    +3.7126e+06   * Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)+7.27023e+06  * pmax(0, Perm+12.9279)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)             \
    -3.34181e+06 * pmax(0, -12.9279-Perm)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)            \
    +6.77021e+09  * pmax(0, Perm+13.3533)*Thick-7.11392e+08 * pmax(0, -13.3533-Perm)*Thick                                        \
    -767239      * pmax(0, Depth-3261.68)*pmax(0, Perm+13.3533)*Thick-3.45623e+06 * pmax(0, 3261.68-Depth)*pmax(0, Perm+13.3533)*Thick                           \
    +1.21058e+10  * pmax(0, Perm+12.7735)*pmax(0, Perm+13.3533)*Thick-8.35224e+09 * pmax(0, -12.7735-Perm)*pmax(0, Perm+13.3533)*Thick                          \
    +7.47056e+06  * pmax(0, Depth-1714.31)*pmax(0, Perm+12.7735)*pmax(0, Perm+13.3533)*Thick-5.08098e+06 * pmax(0, 1714.31-Depth)*pmax(0, Perm+12.7735)*pmax(0, Perm+13.3533)*Thick             \
    +1.3612e+11   * pmax(0, GeoGrad-0.0243418)*pmax(0, Perm+13.3533)*Thick-4.51425e+11 * pmax(0, 0.0243418-GeoGrad)*pmax(0, Perm+13.3533)*Thick                         \
    -5.3071e+07  * pmax(0, GeoGrad-0.0226121)*pmax(0, 3261.68-Depth)*pmax(0, Perm+13.3533)*Thick+1.68215e+08  * pmax(0, 0.0226121-GeoGrad)*pmax(0, 3261.68-Depth)*pmax(0, Perm+13.3533)*Thick           \
    -2.09475e+09 * pmax(0, Poro-0.145742)*pmax(0, Perm+13.3533)*Thick+7.90234e+09  * pmax(0, 0.145742-Poro)*pmax(0, Perm+13.3533)*Thick                          \
    +3.2768e+07   * pmax(0, GeoGrad-0.0217177)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)-1.1796e+08  * pmax(0, 0.0217177-GeoGrad)*Thick*pmax(0, Perm+13.6336)*pmax(0, Depth-3166.53)           \
    -4.25408e+07 * pmax(0, Perm+12.7819)*Thick*Thick-2.93791e+06 * pmax(0, -12.7819-Perm)*Thick*Thick+1848.44      * pmax(0, Depth-1653.27)*Thick*Thick+10794.9      * pmax(0, 1653.27-Depth)*Thick*Thick                                      \
    +2.43733e+12  * pmax(0, Perm+12.0301)*pmax(0, 0.0243418-GeoGrad)*pmax(0, Perm+13.3533)*Thick+2.54753e+11  * pmax(0, -12.0301-Perm)*pmax(0, 0.0243418-GeoGrad)*pmax(0, Perm+13.3533)*Thick          
    ROM_6_MCO2_15yr = ROM_6_MCO2_15yr / 1000000000 / 30       
    return ROM_6_MCO2_15yr
 
###########
# ROM: 10-max
###########
def ROM_7_MCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_7_MCO2_15yr =+6.34452e+10   -2.09216e+11 * pmax(0, Perm+12.8373)-1.18596e+11 * pmax(0, -12.8373-Perm)                                          \
    +1.00151e+09  * pmax(0, Depth-5322.61)*pmax(0, Perm+12.8373)+1.55091e+08  * pmax(0, 5322.61-Depth)*pmax(0, Perm+12.8373)                             \
    -6.14233e+09 * Thick*pmax(0, Perm+12.8373)+1.97737e+07  * pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)                          \
    -7.99449e+06 * pmax(0, 2093.48-Depth)*Thick*pmax(0, Perm+12.8373)+2.5346e+07   * pmax(0, Depth-2962.7)                                            \
    -5.36607e+07 * pmax(0, 2962.7-Depth)+1.07419e+10  * Thick-130085      * Thick*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)                       \
    +2.21427e+12  * pmax(0, GeoGrad-0.028678)-7.83788e+12 * pmax(0, 0.028678-GeoGrad)                                          \
    +5.68461e+10  * pmax(0, Perm+12.4285)*Thick-1.62211e+10 * pmax(0, -12.4285-Perm)*Thick                                       \
    +1.61366e+08  * pmax(0, GeoGrad-0.0288039)*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)          \
    -2.76852e+08 * pmax(0, 0.0288039-GeoGrad)*pmax(0, Depth-2093.48)*Thick*pmax(0, Perm+12.8373)          \
    +4.03063e+06  * pmax(0, Depth-2757.87)*Thick-2.21347e+06 * pmax(0, 2757.87-Depth)*Thick                                        \
    +1.22853e+07  * pmax(0, Perm+12.3555)*pmax(0, Depth-2757.87)*Thick-3.0855e+06  * pmax(0, -12.3555-Perm)*pmax(0, Depth-2757.87)*Thick                         \
    +8.06283e+10  * pmax(0, Perm+12.5456)*pmax(0, -12.4285-Perm)*Thick+8.16047e+09  * pmax(0, -12.5456-Perm)*pmax(0, -12.4285-Perm)*Thick                        \
    -2.7103e+08  * Thick*pmax(0, Perm+12.4285)*Thick-5.01365e+08 * pmax(0, Perm+12.5055)*pmax(0, 2962.7-Depth)                              \
    +1.20792e+08  * pmax(0, -12.5055-Perm)*pmax(0, 2962.7-Depth)+1.0216e+11   * pmax(0, GeoGrad-0.0180549)*Thick*pmax(0, Perm+12.8373)                        \
    -2.56651e+11 * pmax(0, 0.0180549-GeoGrad)*Thick*pmax(0, Perm+12.8373)                        
    ROM_7_MCO2_15yr = ROM_7_MCO2_15yr / 1000000000 / 30       
    return ROM_7_MCO2_15yr
 
#################################################################################### 
# 20 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_MCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_MCO2_20yr =+1.88254e+09  +1.08946e+07  * pmax(0, Thick-90)-3.47835e+07 * pmax(0, 90-Thick)                                           \
    +1.70463e+06  * pmax(0, Depth-1105.76)-2.28389e+06 * pmax(0, 1105.76-Depth)                                      \
    +2.53866e+09  * pmax(0, Perm+14.9223)-2.52343e+09 * pmax(0, -14.9223-Perm)                                     \
    +1.12447e+06  * Thick*pmax(0, 90-Thick)+911.921      * pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)                                   \
    -1.26547e+10 * pmax(0, GeoGrad-0.046341)-4.96608e+09 * pmax(0, 0.046341-GeoGrad)                                     \
    +6.12168e+06  * pmax(0, Perm+13.9701)*Thick*pmax(0, 90-Thick)-1.87922e+06 * pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)                         \
    +3174.78      * pmax(0, Perm+14.4797)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-1199.63     * pmax(0, -14.4797-Perm)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)           \
    +7280.02      * pmax(0, GeoGrad-0.0284601)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-13318.8     * pmax(0, 0.0284601-GeoGrad)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)          \
    -18758.3     * pmax(0, Depth-1655.41)*pmax(0, 90-Thick)+19857.1      * pmax(0, 1655.41-Depth)*pmax(0, 90-Thick)                             \
    -2.24723e+07 * pmax(0, Perm+14.762)*pmax(0, 90-Thick)+6.20414e+07  * pmax(0, -14.762-Perm)*pmax(0, 90-Thick)                             \
    -2.02017e+06 * pmax(0, Perm+14.4628)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)+1.41823e+06  * pmax(0, -14.4628-Perm)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)          \
    -8.30749e+08 * GeoGrad*pmax(0, -14.762-Perm)*pmax(0, 90-Thick)+263295       * pmax(0, Depth-1575.51)*pmax(0, Perm+14.9223)                        \
    -596823      * pmax(0, 1575.51-Depth)*pmax(0, Perm+14.9223)+1.00967e+07  * GeoGrad*Thick*pmax(0, 90-Thick)                                               \
    -4.77076e+10 * pmax(0, -14.788-Perm)*pmax(0, 0.046341-GeoGrad)+0.0259433    * pmax(0, Depth-3452.13)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)            \
    -0.0672283   * pmax(0, 3452.13-Depth)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)            \
    +6.40421e+07  * pmax(0, Perm+14.1759)*GeoGrad*Thick*pmax(0, 90-Thick)                       \
    -1.06745e+07 * pmax(0, -14.1759-Perm)*GeoGrad*Thick*pmax(0, 90-Thick)                      
    ROM_1_MCO2_20yr = ROM_1_MCO2_20yr / 1000000000 / 30       
    return ROM_1_MCO2_20yr
 
#############
# ROM: 0.05-0.5
#############
def ROM_2_MCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_2_MCO2_20yr =+4.48482e+11  +3.0416e+10   * Perm+2.76872e+11  * Thick+8.15949e+06  * pmax(0, Depth-3381.79)*Thick-4.14165e+07 * pmax(0, 3381.79-Depth)*Thick                                         \
    +1.97362e+10  * Thick*Perm+566740       * pmax(0, Depth-3381.79)*Thick*Perm-2.94498e+06 * pmax(0, 3381.79-Depth)*Thick*Perm-8.32482e+08 * pmax(0, GeoGrad-0.0371514)*Perm                                       \
    -9.61522e+08 * pmax(0, 0.0371514-GeoGrad)*Perm+2.00899e+09  * pmax(0, Perm+14.7285)*Perm-1.97417e+09 * pmax(0, -14.7285-Perm)*Perm-91986.7     * pmax(0, Depth-3774.14)*pmax(0, Perm+14.7285)*Perm                           \
    +63468.4      * pmax(0, 3774.14-Depth)*pmax(0, Perm+14.7285)*Perm+1.23993e+09  * pmax(0, Perm+13.9893)*Thick*Perm                                      \
    -1.22503e+09 * pmax(0, -13.9893-Perm)*Thick*Perm-141719      * pmax(0, Perm+13.9561)*pmax(0, 3381.79-Depth)*Thick*Perm                        \
    +153616       * pmax(0, -13.9561-Perm)*pmax(0, 3381.79-Depth)*Thick*Perm+952879       * pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm                          \
    -3.90435e+06 * pmax(0, 1423.6-Depth)*pmax(0, 0.0371514-GeoGrad)*Perm+50020.9      * Thick*pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm                       \
    +5.94441e+09  * pmax(0, Perm+14.4494)*pmax(0, 0.0371514-GeoGrad)*Perm-9.06233     * pmax(0, Depth-1490.66)*pmax(0, 3381.79-Depth)*Thick                           \
    +34.4         * pmax(0, 1490.66-Depth)*pmax(0, 3381.79-Depth)*Thick+5.07996e+10  * pmax(0, GeoGrad-0.0270544)*Thick                                       \
    -1.20708e+11 * pmax(0, 0.0270544-GeoGrad)*Thick-4.78633e+07 * pmax(0, Perm+14.9341)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +5.28861e+07  * pmax(0, -14.9341-Perm)*pmax(0, -13.9893-Perm)*Thick*Perm-25708.5     * pmax(0, Depth-1461.17)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +30662.1      * pmax(0, 1461.17-Depth)*pmax(0, -13.9893-Perm)*Thick*Perm+3.3533e+09   * pmax(0, GeoGrad-0.0270544)*Thick*Perm                                    \
    -8.03874e+09 * pmax(0, 0.0270544-GeoGrad)*Thick*Perm-2.2011e+06  * pmax(0, Depth-2105.99)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm          \
    +1.01988e+07  * pmax(0, 2105.99-Depth)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm-1.12868e+07 * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick                         \
    +3.85604e+07  * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick-728985      * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick*Perm                      \
    +2.5552e+06   * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick*Perm                      
    ROM_2_MCO2_20yr = ROM_2_MCO2_20yr / 1000000000 / 30       
    return ROM_2_MCO2_20yr
 
#############
# ROM: 0.1-1
#############
def ROM_3_MCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad):   
    ROM_3_MCO2_20yr =+4.65232e+09   -1.05011e+10 * pmax(0, Perm+14.9896)+8.9047e+09   * pmax(0, -14.9896-Perm)+2.90856e+08  * Thick-1.32514e+06 * pmax(0, Depth-2656.39)+2.29495e+06  * pmax(0, 2656.39-Depth)                                           \
    +1.1457e+06   * Thick*Thick-2.90618e+10 * pmax(0, GeoGrad-0.0282262)-2.68119e+10 * pmax(0, 0.0282262-GeoGrad)+71.831       * Thick*Thick*Thick*Thick                                             \
    +200545       * pmax(0, Depth-1330.3)*Thick-106904      * pmax(0, 1330.3-Depth)*Thick                                         \
    +765387       * pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick-1.68256e+06 * pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick                          \
    +1.14278e+09  * pmax(0, Perm+13.836)*Thick-5.66274e+08 * pmax(0, -13.836-Perm)*Thick                                        \
    +6.0823e+09   * pmax(0, Perm+14.4525)*pmax(0, Perm+14.9896)-7.81186e+09 * pmax(0, -14.4525-Perm)*pmax(0, Perm+14.9896)                            \
    +2.02621e+06  * pmax(0, Depth-1302.36)*pmax(0, Perm+14.9896)-7.48004e+06 * pmax(0, 1302.36-Depth)*pmax(0, Perm+14.9896)                             \
    +1.24585e+06  * pmax(0, GeoGrad-0.0192943)*pmax(0, Depth-1330.3)*Thick-1.47787e+06 * pmax(0, 0.0192943-GeoGrad)*pmax(0, Depth-1330.3)*Thick                         \
    +6.10445e+06  * pmax(0, Perm+14.5202)*pmax(0, GeoGrad-0.0192943)*pmax(0, Depth-1330.3)*Thick-1.3641e+06  * pmax(0, -14.5202-Perm)*pmax(0, GeoGrad-0.0192943)*pmax(0, Depth-1330.3)*Thick          \
    -5.68963e+06 * pmax(0, Perm+14.3514)*Thick*Thick+7.49191e+06  * pmax(0, -14.3514-Perm)*Thick*Thick-1343.48     * pmax(0, Depth-1786.01)*Thick*Thick+1499.1       * pmax(0, 1786.01-Depth)*Thick*Thick                                     \
    -124484      * pmax(0, Perm+13.7489)*Thick*Thick*Thick-33937.9     * pmax(0, -13.7489-Perm)*Thick*Thick*Thick+6.3038       * pmax(0, Depth-1313.16)*Thick*Thick*Thick-9.34248     * pmax(0, 1313.16-Depth)*Thick*Thick*Thick                                  \
    +4.90416e+10  * pmax(0, GeoGrad-0.0174106)*pmax(0, Perm+14.9896)-2.46558e+11 * pmax(0, 0.0174106-GeoGrad)*pmax(0, Perm+14.9896)                           \
    +1.07307e+09  * Thick*pmax(0, GeoGrad-0.0174106)*pmax(0, Perm+14.9896)+1.7105e+06   * pmax(0, Perm+13.4547)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick             \
    -612629      * pmax(0, -13.4547-Perm)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick-104622      * Perm*pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick                       \
    +1.57502e+09  * pmax(0, Perm+13.2105)*pmax(0, Perm+13.836)*Thick-2.38691e+08 * pmax(0, -13.2105-Perm)*pmax(0, Perm+13.836)*Thick                          \
    -1895.86     * pmax(0, Depth-1350.12)*pmax(0, Perm+14.3514)*Thick*Thick-2455.94     * pmax(0, 1350.12-Depth)*pmax(0, Perm+14.3514)*Thick*Thick                       
    ROM_3_MCO2_20yr = ROM_3_MCO2_20yr / 1000000000 / 30       
    return ROM_3_MCO2_20yr
 
#############
# ROM: 0.5-5
#############
def ROM_4_MCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad):   
    ROM_4_MCO2_20yr =-1.0845e+10  +3.65518e+10  * pmax(0, Perm+13.9911)-1.20028e+10 * pmax(0, -13.9911-Perm)+1.13961e+09  * Thick+3.78672e+06  * pmax(0, Depth-2547.6)-6.87284e+06 * pmax(0, 2547.6-Depth)                                             \
    -2.22716e+07 * Thick*Thick+1.52011e+11  * pmax(0, GeoGrad-0.0253291)-4.10504e+11 * pmax(0, 0.0253291-GeoGrad)+222352       * Thick*Thick*Thick-832.801     * Thick*Thick*Thick*Thick+6.92474e+08  * pmax(0, Perm+14.5929)*Thick-3.46133e+08 * pmax(0, -14.5929-Perm)*Thick                                        \
    +513083       * pmax(0, Depth-2886.06)*pmax(0, Perm+14.5929)*Thick-284455      * pmax(0, 2886.06-Depth)*pmax(0, Perm+14.5929)*Thick                           \
    -1.83984e+08 * pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick-1.19918e+09 * pmax(0, -14.0329-Perm)*pmax(0, Perm+14.5929)*Thick                          \
    -2.85466e+07 * pmax(0, Perm+13.1614)*pmax(0, 2547.6-Depth)+4.98048e+06  * pmax(0, -13.1614-Perm)*pmax(0, 2547.6-Depth)                                        \
    -4.50311e+06 * pmax(0, 0.0364025-GeoGrad)*pmax(0, Depth-2886.06)*pmax(0, Perm+14.5929)*Thick+4.12682e+09  * pmax(0, GeoGrad-0.0401399)*pmax(0, Perm+14.5929)*Thick                         \
    -2.75794e+10 * pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick+2.6684e+09   * pmax(0, Perm+12.9083)*pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick             \
    -1.42429e+09 * pmax(0, -12.9083-Perm)*pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick+964958       * Depth*pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick                        \
    -6.1196e+06  * pmax(0, Depth-2181.2)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick+1.47126e+07  * pmax(0, 2181.2-Depth)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick            \
    -6.5084e+10  * pmax(0, Perm+12.9034)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick+1.79173e+10  * pmax(0, -12.9034-Perm)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick          \
    +3.21107e+10  * pmax(0, Perm+12.307)*pmax(0, Perm+13.9911)-1.84326e+10 * pmax(0, -12.307-Perm)*pmax(0, Perm+13.9911)                              \
    +387.002      * pmax(0, Depth-1367.21)*Thick*Thick+1577.21      * pmax(0, 1367.21-Depth)*Thick*Thick                                      \
    -185926      * pmax(0, Perm+13.572)*pmax(0, 2886.06-Depth)*pmax(0, Perm+14.5929)*Thick-316903      * pmax(0, -13.572-Perm)*pmax(0, 2886.06-Depth)*pmax(0, Perm+14.5929)*Thick             \
    -8.6338e+07  * pmax(0, Poro-0.152149)*pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick+9.77871e+08  * pmax(0, 0.152149-Poro)*pmax(0, Perm+14.0329)*pmax(0, Perm+14.5929)*Thick            
    ROM_4_MCO2_20yr = ROM_4_MCO2_20yr / 1000000000 / 30       
    return ROM_4_MCO2_20yr
 
#############
# ROM: 1-10
#############
def ROM_5_MCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_MCO2_20yr =-4.57008e+09   +3.95296e+10  * pmax(0, Perm+13.5959)-2.80328e+10 * pmax(0, -13.5959-Perm)+5.89956e+06  * pmax(0, Depth-4489.41)-7.99929e+06 * pmax(0, 4489.41-Depth)+2.39048e+09  * Thick                                                      \
    -4.33922e+07 * Thick*Thick+1.5822e+11   * pmax(0, GeoGrad-0.0275088)-9.23777e+11 * pmax(0, 0.0275088-GeoGrad)                                         \
    +410671       * Thick*Thick*Thick-2935.86     * pmax(0, 1694.49-Depth)*pmax(0, 4489.41-Depth)-1480.06     * Thick*Thick*Thick*Thick+2.30891e+09  * pmax(0, Perm+14.3061)*Thick                                        \
    -5.6853e+08  * pmax(0, -14.3061-Perm)*Thick+680423       * pmax(0, Depth-3594.45)*pmax(0, Perm+14.3061)*Thick                          \
    -725624      * pmax(0, 3594.45-Depth)*pmax(0, Perm+14.3061)*Thick+3.37148e+08  * pmax(0, Perm+13.6677)*pmax(0, Perm+14.3061)*Thick                                   \
    -2.86772e+06 * pmax(0, Perm+13.1196)*pmax(0, 3594.45-Depth)*pmax(0, Perm+14.3061)*Thick            \
    +424890       * pmax(0, -13.1196-Perm)*pmax(0, 3594.45-Depth)*pmax(0, Perm+14.3061)*Thick           \
    +5.94278e+09  * pmax(0, Perm+13.1017)*pmax(0, Perm+14.3061)*Thick-1.87885e+09 * pmax(0, -13.1017-Perm)*pmax(0, Perm+14.3061)*Thick                         \
    +2.13678e+10  * pmax(0, GeoGrad-0.017872)*pmax(0, Perm+14.3061)*Thick-2.9002e+10  * pmax(0, 0.017872-GeoGrad)*pmax(0, Perm+14.3061)*Thick                         \
    +1.72097e+07  * pmax(0, Depth-1049.3)*pmax(0, GeoGrad-0.017872)*pmax(0, Perm+14.3061)*Thick-1.57732e+07 * pmax(0, 1049.3-Depth)*pmax(0, GeoGrad-0.017872)*pmax(0, Perm+14.3061)*Thick            \
    +1.63129e+06  * pmax(0, Depth-2282.58)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3061)*Thick-517507      * pmax(0, 2282.58-Depth)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3061)*Thick            \
    +1.10734e+11  * pmax(0, Perm+12.6048)*pmax(0, GeoGrad-0.017872)*pmax(0, Perm+14.3061)*Thick-2.8448e+10  * pmax(0, -12.6048-Perm)*pmax(0, GeoGrad-0.017872)*pmax(0, Perm+14.3061)*Thick          \
    +3.30748e+09  * pmax(0, Perm+13.1664)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3061)*Thick-1.7125e+09  * pmax(0, -13.1664-Perm)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3061)*Thick           \
    +621.122      * pmax(0, Depth-1613.21)*Thick*Thick+3001.83      * pmax(0, 1613.21-Depth)*Thick*Thick-7.28061e+08 * pmax(0, Poro-0.0953138)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3061)*Thick          \
    +5.81196e+09  * pmax(0, 0.0953138-Poro)*pmax(0, Perm+13.6677)*pmax(0, Perm+14.3061)*Thick+1.89751e+06  * pmax(0, Perm+12.7133)*pmax(0, Depth-1613.21)*Thick*Thick                                
    ROM_5_MCO2_20yr = ROM_5_MCO2_20yr / 1000000000 / 30       
    return ROM_5_MCO2_20yr 
#############
# ROM: 5-50
#############
def ROM_6_MCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_6_MCO2_20yr =-9.63079e+10  +3.07787e+11  * pmax(0, Perm+12.9374)-3.43299e+11 * pmax(0, -12.9374-Perm)                                          \
    +1.51462e+10  * Thick+6.51269e+07  * pmax(0, Depth-2436.2)-1.3791e+08  * pmax(0, 2436.2-Depth)                                            \
    -2.48354e+08 * Thick*Thick+6.55747e+11  * pmax(0, GeoGrad-0.0347305)                                         \
    -4.02934e+12 * pmax(0, 0.0347305-GeoGrad)+2.19077e+06  * Thick*Thick*Thick                                                \
    -7407.75     * Thick*Thick*Thick*Thick-6.17952e+07 * pmax(0, Perm+13.6145)*pmax(0, Depth-2436.2)                              \
    -2.34786e+07 * pmax(0, -13.6145-Perm)*pmax(0, Depth-2436.2)+5.64819e+06  * Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2436.2)                           \
    +1.72043e+07  * pmax(0, Perm+12.7547)*Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2436.2)-4.26974e+06 * pmax(0, -12.7547-Perm)*Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2436.2)            \
    +4.55622e+09  * pmax(0, Perm+13.2438)*Thick+673723       * pmax(0, Depth-2299.32)*pmax(0, Perm+13.2438)*Thick                          \
    -8.05902e+06 * pmax(0, 2299.32-Depth)*pmax(0, Perm+13.2438)*Thick+1.37157e+10  * pmax(0, Perm+12.8558)*pmax(0, Perm+13.2438)*Thick                          \
    -1.25001e+10 * pmax(0, -12.8558-Perm)*pmax(0, Perm+13.2438)*Thick-8.31688e+07 * pmax(0, 0.0256567-GeoGrad)*pmax(0, Depth-2299.32)*pmax(0, Perm+13.2438)*Thick          \
    +1.03908e+11  * pmax(0, GeoGrad-0.0254416)*pmax(0, Perm+13.2438)*Thick-1.93776e+11 * pmax(0, 0.0254416-GeoGrad)*pmax(0, Perm+13.2438)*Thick                        \
    -1.49332e+07 * pmax(0, Perm+12.3804)*pmax(0, 2299.32-Depth)*pmax(0, Perm+13.2438)*Thick+5.90757e+06  * pmax(0, -12.3804-Perm)*pmax(0, 2299.32-Depth)*pmax(0, Perm+13.2438)*Thick           \
    -3.97024e+09 * pmax(0, Poro-0.14441)*pmax(0, Perm+13.2438)*Thick+1.59451e+10  * pmax(0, 0.14441-Poro)*pmax(0, Perm+13.2438)*Thick                          \
    +3.95805e+08  * pmax(0, Depth-2041.33)*pmax(0, 0.0347305-GeoGrad)+7.42319e+09  * pmax(0, 2041.33-Depth)*pmax(0, 0.0347305-GeoGrad)                           \
    +4.12584e+07  * pmax(0, GeoGrad-0.0290289)*Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2436.2)-8.64416e+07 * pmax(0, 0.0290289-GeoGrad)*Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2436.2)           \
    +1.85888e+10  * pmax(0, Perm+12.3843)*pmax(0, Perm+12.8558)*pmax(0, Perm+13.2438)*Thick-4.91341e+09 * pmax(0, -12.3843-Perm)*pmax(0, Perm+12.8558)*pmax(0, Perm+13.2438)*Thick           
    ROM_6_MCO2_20yr = ROM_6_MCO2_20yr / 1000000000 / 30       
    return ROM_6_MCO2_20yr 
###########
# ROM: 10-max
###########
def ROM_7_MCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_7_MCO2_20yr =+1.22614e+11  -2.26878e+11 * pmax(0, -12.8093-Perm)+1.06325e+08  * pmax(0, Depth-3762.41)*pmax(0, Perm+12.8093)                             \
    -9.8857e+07  * pmax(0, 3762.41-Depth)*pmax(0, Perm+12.8093)+9.73184e+09  * Thick*pmax(0, Perm+12.8093)                                        \
    +1.42264e+07  * Depth*Thick*pmax(0, Perm+12.8093)+3.9713e+07   * pmax(0, Depth-3630.86)                                           \
    -1.34499e+07 * pmax(0, 3630.86-Depth)+2.92975e+09  * Thick-116925      * Thick*Depth*Thick*pmax(0, Perm+12.8093)                                  \
    +3.19546e+12  * pmax(0, GeoGrad-0.028678)-9.8341e+12  * pmax(0, 0.028678-GeoGrad)                                                  \
    -1.95897e+09 * pmax(0, -12.3938-Perm)*Thick+1.10747e+08  * pmax(0, GeoGrad-0.0288039)*Depth*Thick*pmax(0, Perm+12.8093)                     \
    -2.28365e+08 * pmax(0, 0.0288039-GeoGrad)*Depth*Thick*pmax(0, Perm+12.8093)+8.43048e+06  * pmax(0, Depth-1493.19)*Thick                                        \
    -4.46562e+06 * pmax(0, 1493.19-Depth)*Thick+1.91234e+07  * pmax(0, Perm+12.2782)*pmax(0, Depth-1493.19)*Thick                          \
    -8.92716e+06 * pmax(0, -12.2782-Perm)*pmax(0, Depth-1493.19)*Thick-1.16251e+07 * pmax(0, Perm+12.7505)*pmax(0, -12.2782-Perm)*pmax(0, Depth-1493.19)*Thick           \
    +3.7234e+06   * pmax(0, -12.7505-Perm)*pmax(0, -12.2782-Perm)*pmax(0, Depth-1493.19)*Thick          \
    +1.61335e+12  * pmax(0, Perm+12.164)*pmax(0, Perm+12.8093)-1.02545e+12 * pmax(0, -12.164-Perm)*pmax(0, Perm+12.8093)                             
    ROM_7_MCO2_20yr = ROM_7_MCO2_20yr / 1000000000 / 30       
    return ROM_7_MCO2_20yr
 
#################################################################################### 
# 25 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_MCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_MCO2_25yr =+2.32684e+09  +1.34213e+07  * pmax(0, Thick-90)-4.31103e+07 * pmax(0, 90-Thick)                                           \
    +2.11299e+06  * pmax(0, Depth-1105.76)-2.83399e+06 * pmax(0, 1105.76-Depth)+3.18645e+09  * pmax(0, Perm+14.9223)-3.1764e+09  * pmax(0, -14.9223-Perm)                                     \
    +1.41871e+06  * Thick*pmax(0, 90-Thick)+1136.66      * pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)                                   \
    -1.56108e+10 * pmax(0, GeoGrad-0.046341)-5.98543e+09 * pmax(0, 0.046341-GeoGrad)+7.73948e+06  * pmax(0, Perm+13.9701)*Thick*pmax(0, 90-Thick)                      \
    -2.34614e+06 * pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)+3967.46      * pmax(0, Perm+14.4797)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)            \
    -1496.42     * pmax(0, -14.4797-Perm)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)+8956.58      * pmax(0, GeoGrad-0.0284601)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)          \
    -16449.2     * pmax(0, 0.0284601-GeoGrad)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-23261.7     * pmax(0, Depth-1655.41)*pmax(0, 90-Thick)                             \
    +24616.9      * pmax(0, 1655.41-Depth)*pmax(0, 90-Thick)-2.8233e+07  * pmax(0, Perm+14.762)*pmax(0, 90-Thick)                              \
    +7.60856e+07  * pmax(0, -14.762-Perm)*pmax(0, 90-Thick)-2.53044e+06 * pmax(0, Perm+14.472)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)            \
    +1.77916e+06  * pmax(0, -14.472-Perm)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)-1.00064e+09 * GeoGrad*pmax(0, -14.762-Perm)*pmax(0, 90-Thick)                          \
    +323444       * pmax(0, Depth-1575.51)*pmax(0, Perm+14.9223)-743101      * pmax(0, 1575.51-Depth)*pmax(0, Perm+14.9223)                        \
    +1.23042e+07  * GeoGrad*Thick*pmax(0, 90-Thick)-5.69573e+10 * pmax(0, -14.788-Perm)*pmax(0, 0.046341-GeoGrad)                       \
    +0.0316768    * pmax(0, Depth-3452.13)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)            \
    -0.083828    * pmax(0, 3452.13-Depth)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)            \
    +7.90703e+07  * pmax(0, Perm+14.1759)*GeoGrad*Thick*pmax(0, 90-Thick)                       \
    -1.2981e+07  * pmax(0, -14.1759-Perm)*GeoGrad*Thick*pmax(0, 90-Thick)                      
    ROM_1_MCO2_25yr = ROM_1_MCO2_25yr / 1000000000 / 30       
    return ROM_1_MCO2_25yr 
#############
# ROM: 0.05-0.5
#############
def ROM_2_MCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_2_MCO2_25yr =+5.57736e+11  +3.78246e+10  * Perm+3.49759e+11  * Thick+1.01303e+07  * pmax(0, Depth-3381.79)*Thick-5.19344e+07 * pmax(0, 3381.79-Depth)*Thick+2.49328e+10  * Thick*Perm                                                    \
    +703677       * pmax(0, Depth-3381.79)*Thick*Perm-3.69303e+06 * pmax(0, 3381.79-Depth)*Thick*Perm-1.01825e+09 * pmax(0, GeoGrad-0.0371514)*Perm-1.22252e+09 * pmax(0, 0.0371514-GeoGrad)*Perm                                       \
    +2.50135e+09  * pmax(0, Perm+14.7285)*Perm-2.45517e+09 * pmax(0, -14.7285-Perm)*Perm-114246      * pmax(0, Depth-3774.14)*pmax(0, Perm+14.7285)*Perm+77701.8      * pmax(0, 3774.14-Depth)*pmax(0, Perm+14.7285)*Perm                           \
    +1.56873e+09  * pmax(0, Perm+13.9893)*Thick*Perm-1.54933e+09 * pmax(0, -13.9893-Perm)*Thick*Perm-177835      * pmax(0, Perm+13.9561)*pmax(0, 3381.79-Depth)*Thick*Perm+193013       * pmax(0, -13.9561-Perm)*pmax(0, 3381.79-Depth)*Thick*Perm                       \
    +1.18524e+06  * pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm-4.77013e+06 * pmax(0, 1423.6-Depth)*pmax(0, 0.0371514-GeoGrad)*Perm                          \
    +61095        * Thick*pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm+7.29316e+09  * pmax(0, Perm+14.4494)*pmax(0, 0.0371514-GeoGrad)*Perm                                  \
    -11.3052     * pmax(0, Depth-1490.66)*pmax(0, 3381.79-Depth)*Thick+42.9918      * pmax(0, 1490.66-Depth)*pmax(0, 3381.79-Depth)*Thick                           \
    +6.24686e+10  * pmax(0, GeoGrad-0.0270544)*Thick-1.48999e+11 * pmax(0, 0.0270544-GeoGrad)*Thick-6.09418e+07 * pmax(0, Perm+14.9341)*pmax(0, -13.9893-Perm)*Thick*Perm+6.72228e+07  * pmax(0, -14.9341-Perm)*pmax(0, -13.9893-Perm)*Thick*Perm                      \
    -31945.2     * pmax(0, Depth-1461.17)*pmax(0, -13.9893-Perm)*Thick*Perm+38150.2      * pmax(0, 1461.17-Depth)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +4.1226e+09   * pmax(0, GeoGrad-0.0270544)*Thick*Perm-9.92232e+09 * pmax(0, 0.0270544-GeoGrad)*Thick*Perm-2.70313e+06 * pmax(0, Depth-2105.99)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm          \
    +1.27361e+07  * pmax(0, 2105.99-Depth)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm-1.3781e+07  * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick                         \
    +4.75193e+07  * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick-889003      * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick*Perm                      \
    +3.14824e+06  * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick*Perm                      
    ROM_2_MCO2_25yr = ROM_2_MCO2_25yr / 1000000000 / 30       
    return ROM_2_MCO2_25yr  
#############
# ROM: 0.1-1
#############
def ROM_3_MCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad):   
    ROM_3_MCO2_25yr =+5.84659e+09  -1.31333e+10 * pmax(0, Perm+14.9896)+1.107e+10    * pmax(0, -14.9896-Perm)                                          \
    +3.72214e+08  * Thick-1.65259e+06 * pmax(0, Depth-2656.39)+2.84758e+06  * pmax(0, 2656.39-Depth)                                           \
    +1.39483e+06  * Thick*Thick-3.59777e+10 * pmax(0, GeoGrad-0.0282262)-3.27699e+10 * pmax(0, 0.0282262-GeoGrad)                                         \
    +90.168       * Thick*Thick*Thick*Thick+248572       * pmax(0, Depth-1330.3)*Thick-133649      * pmax(0, 1330.3-Depth)*Thick+954500       * pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick                           \
    -2.09481e+06 * pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick+1.44234e+09  * pmax(0, Perm+13.8264)*Thick                                        \
    -7.10734e+08 * pmax(0, -13.8264-Perm)*Thick+7.62275e+09  * pmax(0, Perm+14.4525)*pmax(0, Perm+14.9896)                             \
    -9.71436e+09 * pmax(0, -14.4525-Perm)*pmax(0, Perm+14.9896)+2.51221e+06  * pmax(0, Depth-1302.36)*pmax(0, Perm+14.9896)                             \
    -9.34458e+06 * pmax(0, 1302.36-Depth)*pmax(0, Perm+14.9896)+1.53386e+06  * pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick                         \
    -1.85745e+06 * pmax(0, 0.0189446-GeoGrad)*pmax(0, Depth-1330.3)*Thick+7.47054e+06  * pmax(0, Perm+14.5202)*pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick           \
    -1.6735e+06  * pmax(0, -14.5202-Perm)*pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick-7.15811e+06 * pmax(0, Perm+14.3475)*Thick*Thick+9.411e+06    * pmax(0, -14.3475-Perm)*Thick*Thick                                    \
    -1675.49     * pmax(0, Depth-1786.01)*Thick*Thick+1867.34      * pmax(0, 1786.01-Depth)*Thick*Thick-164969      * pmax(0, Perm+13.7489)*Thick*Thick*Thick-42566.5     * pmax(0, -13.7489-Perm)*Thick*Thick*Thick                                 \
    +7.84157      * pmax(0, Depth-1313.16)*Thick*Thick*Thick-11.5569     * pmax(0, 1313.16-Depth)*Thick*Thick*Thick+6.02482e+10  * pmax(0, GeoGrad-0.0174106)*pmax(0, Perm+14.9896)-3.03038e+11 * pmax(0, 0.0174106-GeoGrad)*pmax(0, Perm+14.9896)                           \
    +1.31535e+09  * Thick*pmax(0, GeoGrad-0.0174106)*pmax(0, Perm+14.9896)+2.14532e+06  * pmax(0, Perm+13.4547)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick             \
    -763693      * pmax(0, -13.4547-Perm)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick            \
    -130329      * Perm*pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick+2.03705e+09  * pmax(0, Perm+13.2121)*pmax(0, Perm+13.8264)*Thick                          \
    -2.47171e+08 * pmax(0, -13.2121-Perm)*pmax(0, Perm+13.8264)*Thick-2414.25     * pmax(0, Depth-1350.12)*pmax(0, Perm+14.3475)*Thick*Thick                       \
    -2945.26     * pmax(0, 1350.12-Depth)*pmax(0, Perm+14.3475)*Thick*Thick                       
    ROM_3_MCO2_25yr = ROM_3_MCO2_25yr / 1000000000 / 30       
    return ROM_3_MCO2_25yr 
#############
# ROM: 0.5-5
#############
def ROM_4_MCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad):   
    ROM_4_MCO2_25yr =-1.32299e+10 +4.41536e+10  * pmax(0, Perm+13.9911)-1.78753e+10 * pmax(0, -13.9911-Perm)+1.47417e+09  * Thick+4.84908e+06  * pmax(0, Depth-2547.6)-9.16099e+06 * pmax(0, 2547.6-Depth)                                             \
    -2.82943e+07 * Thick*Thick+276435       * Thick*Thick*Thick+1.78727e+11  * pmax(0, GeoGrad-0.0258077)                                          \
    -5.00766e+11 * pmax(0, 0.0258077-GeoGrad)-1020.09     * Thick*Thick*Thick*Thick+7.56476e+08  * pmax(0, Perm+14.5929)*Thick-3.01465e+08 * pmax(0, -14.5929-Perm)*Thick                                        \
    +607014       * pmax(0, Depth-2886.06)*pmax(0, Perm+14.5929)*Thick-320256      * pmax(0, 2886.06-Depth)*pmax(0, Perm+14.5929)*Thick                           \
    -2.82324e+08 * pmax(0, Perm+14.0446)*pmax(0, Perm+14.5929)*Thick-1.43862e+09 * pmax(0, -14.0446-Perm)*pmax(0, Perm+14.5929)*Thick                          \
    -3.24422e+07 * pmax(0, Perm+13.1614)*pmax(0, 2547.6-Depth)+5.64824e+06  * pmax(0, -13.1614-Perm)*pmax(0, 2547.6-Depth)                                       \
    -5.66823e+06 * pmax(0, 0.0364025-GeoGrad)*pmax(0, Depth-2886.06)*pmax(0, Perm+14.5929)*Thick+5.37937e+09  * pmax(0, GeoGrad-0.0401399)*pmax(0, Perm+14.5929)*Thick                         \
    -3.50053e+10 * pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick+3.38075e+09  * pmax(0, Perm+12.9083)*pmax(0, Perm+14.0446)*pmax(0, Perm+14.5929)*Thick             \
    -1.5428e+09  * pmax(0, -12.9083-Perm)*pmax(0, Perm+14.0446)*pmax(0, Perm+14.5929)*Thick+1.19592e+06  * Depth*pmax(0, Perm+14.0446)*pmax(0, Perm+14.5929)*Thick                        \
    -7.51697e+06 * pmax(0, Depth-2181.2)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick+1.86161e+07  * pmax(0, 2181.2-Depth)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick            \
    -8.47052e+10 * pmax(0, Perm+12.9034)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick+2.27986e+10  * pmax(0, -12.9034-Perm)*pmax(0, 0.0401399-GeoGrad)*pmax(0, Perm+14.5929)*Thick          \
    +4.10944e+10  * pmax(0, Perm+12.307)*pmax(0, Perm+13.9911)-2.17286e+10 * pmax(0, -12.307-Perm)*pmax(0, Perm+13.9911)+952.152      * pmax(0, Depth-1367.21)*Thick*Thick+1578.18      * pmax(0, 1367.21-Depth)*Thick*Thick                                      \
    -147168      * pmax(0, Perm+13.572)*pmax(0, 2886.06-Depth)*pmax(0, Perm+14.5929)*Thick-334129      * pmax(0, -13.572-Perm)*pmax(0, 2886.06-Depth)*pmax(0, Perm+14.5929)*Thick             \
    -1.61147e+08 * pmax(0, Poro-0.152149)*pmax(0, Perm+14.0446)*pmax(0, Perm+14.5929)*Thick+1.36847e+09  * pmax(0, 0.152149-Poro)*pmax(0, Perm+14.0446)*pmax(0, Perm+14.5929)*Thick            \
    +266008       * pmax(0, Perm+13.1385)*pmax(0, Depth-1367.21)*Thick*Thick-325.419     * pmax(0, -13.1385-Perm)*pmax(0, Depth-1367.21)*Thick*Thick                       
    ROM_4_MCO2_25yr = ROM_4_MCO2_25yr / 1000000000 / 30       
    return ROM_4_MCO2_25yr 
#############
# ROM: 1-10
#############
def ROM_5_MCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_MCO2_25yr =-2.68476e+10 +5.87876e+10  * pmax(0, Perm+13.5922)-3.34195e+10 * pmax(0, -13.5922-Perm)+3.1481e+09   * Thick+8.86424e+06  * pmax(0, Depth-2690.86)                                           \
    -1.88736e+07 * pmax(0, 2690.86-Depth)-5.77191e+07 * Thick*Thick+3.15949e+11  * pmax(0, GeoGrad-0.0275088)+527078       * Thick*Thick*Thick                                                \
    -1857.11     * Thick*Thick*Thick*Thick-1925.91     * pmax(0, 1830-Depth)*pmax(0, 2690.86-Depth)+1.37619e+09  * pmax(0, Perm+14.2717)*Thick                                        \
    -5.9964e+08  * pmax(0, -14.2717-Perm)*Thick+1.18888e+06  * pmax(0, Depth-2653.74)*pmax(0, Perm+14.2717)*Thick                          \
    -1.64478e+06 * pmax(0, 2653.74-Depth)*pmax(0, Perm+14.2717)*Thick+3.6292e+09   * pmax(0, Perm+13.6644)*pmax(0, Perm+14.2717)*Thick                          \
    -2.47476e+09 * pmax(0, -13.6644-Perm)*pmax(0, Perm+14.2717)*Thick-3.82091e+06 * pmax(0, Perm+13.1657)*pmax(0, 2653.74-Depth)*pmax(0, Perm+14.2717)*Thick            \
    +1.74305e+06  * pmax(0, -13.1657-Perm)*pmax(0, 2653.74-Depth)*pmax(0, Perm+14.2717)*Thick+5.06901e+09  * pmax(0, Perm+13.1996)*pmax(0, Perm+13.6644)*pmax(0, Perm+14.2717)*Thick            \
    -1.48325e+09 * pmax(0, -13.1996-Perm)*pmax(0, Perm+13.6644)*pmax(0, Perm+14.2717)*Thick+3.06236e+06  * pmax(0, Perm+13.5536)*pmax(0, Depth-2653.74)*pmax(0, Perm+14.2717)*Thick            \
    -836329      * pmax(0, -13.5536-Perm)*pmax(0, Depth-2653.74)*pmax(0, Perm+14.2717)*Thick+1.18434e+07  * pmax(0, GeoGrad-0.0224135)*pmax(0, Depth-2653.74)*pmax(0, Perm+14.2717)*Thick          \
    -4.93368e+07 * pmax(0, 0.0224135-GeoGrad)*pmax(0, Depth-2653.74)*pmax(0, Perm+14.2717)*Thick+2.79022e+10  * pmax(0, GeoGrad-0.034189)*pmax(0, Perm+13.6644)*pmax(0, Perm+14.2717)*Thick           \
    -3.96434e+10 * pmax(0, 0.034189-GeoGrad)*pmax(0, Perm+13.6644)*pmax(0, Perm+14.2717)*Thick+2186.56      * pmax(0, Depth-1410.26)*Thick*Thick                                     \
    +3605.2       * pmax(0, 1410.26-Depth)*Thick*Thick-1.05681e+09 * pmax(0, Poro-0.111318)*pmax(0, Perm+13.6644)*pmax(0, Perm+14.2717)*Thick           \
    +7.05403e+09  * pmax(0, 0.111318-Poro)*pmax(0, Perm+13.6644)*pmax(0, Perm+14.2717)*Thick-1.31008e+07 * pmax(0, GeoGrad-0.0332488)*pmax(0, 2653.74-Depth)*pmax(0, Perm+14.2717)*Thick          \
    +3.53818e+07  * pmax(0, 0.0332488-GeoGrad)*pmax(0, 2653.74-Depth)*pmax(0, Perm+14.2717)*Thick+1.60201e+10  * pmax(0, GeoGrad-0.03429)*pmax(0, Perm+14.2717)*Thick                          \
    -4.00893e+10 * pmax(0, 0.03429-GeoGrad)*pmax(0, Perm+14.2717)*Thick+2.06486e+06  * pmax(0, Perm+12.7133)*pmax(0, Depth-1410.26)*Thick*Thick                       \
    -658.333     * pmax(0, -12.7133-Perm)*pmax(0, Depth-1410.26)*Thick*Thick-1.00125e+12 * pmax(0, Perm+13.981)*pmax(0, 0.0275088-GeoGrad)-3.00042e+12 * pmax(0, -13.981-Perm)*pmax(0, 0.0275088-GeoGrad)                           
    ROM_5_MCO2_25yr = ROM_5_MCO2_25yr / 1000000000 / 30       
    return ROM_5_MCO2_25yr 
#############
# ROM: 5-50
#############
def ROM_6_MCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_6_MCO2_25yr =-9.16848e+10  +3.39362e+11  * pmax(0, Perm+12.9374)-4.35463e+11 * pmax(0, -12.9374-Perm)+1.73776e+10  * Thick                                                      \
    +7.99459e+07  * pmax(0, Depth-2404.97)-1.91651e+08 * pmax(0, 2404.97-Depth)-2.76551e+08 * Thick*Thick+6.88818e+11  * pmax(0, GeoGrad-0.0347305)                                         \
    -5.22264e+12 * pmax(0, 0.0347305-GeoGrad)+2.43424e+06  * Thick*Thick*Thick-8278.94     * Thick*Thick*Thick*Thick-7.99509e+07 * pmax(0, Perm+13.6145)*pmax(0, Depth-2404.97)                             \
    -2.73003e+07 * pmax(0, -13.6145-Perm)*pmax(0, Depth-2404.97)+7.14783e+06  * Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2404.97)                          \
    +2.19228e+07  * pmax(0, Perm+12.7547)*Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2404.97)-5.52933e+06 * pmax(0, -12.7547-Perm)*Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2404.97)           \
    +8.98483e+09  * pmax(0, Perm+13.2582)*Thick+991879       * pmax(0, Depth-2248.33)*pmax(0, Perm+13.2582)*Thick-1.11495e+07 * pmax(0, 2248.33-Depth)*pmax(0, Perm+13.2582)*Thick                          \
    +2.90604e+10  * pmax(0, Perm+12.6224)*pmax(0, Perm+13.2582)*Thick-1.65478e+10 * pmax(0, -12.6224-Perm)*pmax(0, Perm+13.2582)*Thick                                  \
    -1.1867e+08  * pmax(0, 0.0256567-GeoGrad)*pmax(0, Depth-2248.33)*pmax(0, Perm+13.2582)*Thick+1.28741e+11  * pmax(0, GeoGrad-0.024353)*pmax(0, Perm+13.2582)*Thick                         \
    -2.27017e+11 * pmax(0, 0.024353-GeoGrad)*pmax(0, Perm+13.2582)*Thick-1.03768e+07 * pmax(0, Perm+12.2874)*pmax(0, 2248.33-Depth)*pmax(0, Perm+13.2582)*Thick            \
    +9.72601e+06  * pmax(0, -12.2874-Perm)*pmax(0, 2248.33-Depth)*pmax(0, Perm+13.2582)*Thick-5.37139e+09 * pmax(0, Poro-0.14441)*pmax(0, Perm+13.2582)*Thick                          \
    +2.19165e+10  * pmax(0, 0.14441-Poro)*pmax(0, Perm+13.2582)*Thick+5.67269e+08  * pmax(0, Depth-2041.33)*pmax(0, 0.0347305-GeoGrad)                           \
    +8.96235e+09  * pmax(0, 2041.33-Depth)*pmax(0, 0.0347305-GeoGrad)+5.05453e+07  * pmax(0, GeoGrad-0.0290289)*Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2404.97)          \
    -1.02236e+08 * pmax(0, 0.0290289-GeoGrad)*Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2404.97)-8.83169e+07 * pmax(0, Perm+12.6105)*Thick*Thick                                              
    ROM_6_MCO2_25yr = ROM_6_MCO2_25yr / 1000000000 / 30       
    return ROM_6_MCO2_25yr 
###########
# ROM: 10-max
###########
def ROM_7_MCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_7_MCO2_25yr =      +1.60116e+11  -4.432e+11   * pmax(0, Perm+12.8093)-2.84867e+11 * pmax(0, -12.8093-Perm)+1.28964e+08  * pmax(0, Depth-3762.41)*pmax(0, Perm+12.8093)                             \
    -1.12902e+08 * pmax(0, 3762.41-Depth)*pmax(0, Perm+12.8093)+1.20952e+10  * Thick*pmax(0, Perm+12.8093)+1.86465e+07  * Depth*Thick*pmax(0, Perm+12.8093)                                     \
    +4.55089e+07  * pmax(0, Depth-3610.5)-1.91908e+07 * pmax(0, 3610.5-Depth)+3.83556e+09  * Thick-151965      * Thick*Depth*Thick*pmax(0, Perm+12.8093)                                  \
    +3.93642e+12  * pmax(0, GeoGrad-0.0285925)-1.24502e+13 * pmax(0, 0.0285925-GeoGrad)-2.73531e+09 * pmax(0, -12.3938-Perm)*Thick                                       \
    +1.39016e+08  * pmax(0, GeoGrad-0.0288039)*Depth*Thick*pmax(0, Perm+12.8093)                     \
    -2.82887e+08 * pmax(0, 0.0288039-GeoGrad)*Depth*Thick*pmax(0, Perm+12.8093)                     \
    +1.05037e+07  * pmax(0, Depth-1493.19)*Thick                                        \
    -5.79504e+06 * pmax(0, 1493.19-Depth)*Thick                                        \
    +2.37412e+07  * pmax(0, Perm+12.2782)*pmax(0, Depth-1493.19)*Thick                          \
    -1.10815e+07 * pmax(0, -12.2782-Perm)*pmax(0, Depth-1493.19)*Thick                         \
    -1.44444e+07 * pmax(0, Perm+12.7505)*pmax(0, -12.2782-Perm)*pmax(0, Depth-1493.19)*Thick           \
    +4.63809e+06  * pmax(0, -12.7505-Perm)*pmax(0, -12.2782-Perm)*pmax(0, Depth-1493.19)*Thick          \
    +1.67338e+12  * pmax(0, Perm+12.4332)*pmax(0, Perm+12.8093)                             \
    -7.14611e+11 * pmax(0, -12.4332-Perm)*pmax(0, Perm+12.8093)                            
    ROM_7_MCO2_25yr = ROM_7_MCO2_25yr / 1000000000 / 30       
    return ROM_7_MCO2_25yr 
#################################################################################### 
# 30 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_MCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_MCO2_30yr =+2.77297e+09  +1.56585e+07  * pmax(0, Thick-90)-5.15162e+07 * pmax(0, 90-Thick)+2.49165e+06  * pmax(0, Depth-1105.76)-3.43888e+06 * pmax(0, 1105.76-Depth)                                       \
    +3.9208e+09   * pmax(0, Perm+14.9223)-4.08096e+09 * pmax(0, -14.9223-Perm)+2.59897e+06  * Thick*pmax(0, 90-Thick)+1380.99      * pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)                                    \
    -6.57627e+09 * pmax(0, 0.046341-GeoGrad)+1.42638e+07  * pmax(0, Perm+13.9701)*Thick*pmax(0, 90-Thick)                           \
    -3.87275e+06 * pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)+5017.16      * pmax(0, Perm+14.4797)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)             \
    -1821.53     * pmax(0, -14.4797-Perm)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)+10413.8      * pmax(0, GeoGrad-0.0284601)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)           \
    -19869.5     * pmax(0, 0.0284601-GeoGrad)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-27392       * pmax(0, Depth-1655.41)*pmax(0, 90-Thick)                              \
    +29137.2      * pmax(0, 1655.41-Depth)*pmax(0, 90-Thick)-3.41742e+07 * pmax(0, Perm+14.762)*pmax(0, 90-Thick)                               \
    +9.10547e+07  * pmax(0, -14.762-Perm)*pmax(0, 90-Thick)-5.79876e+06 * pmax(0, Perm+14.472)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)             \
    +2.58604e+06  * pmax(0, -14.472-Perm)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)-1.18842e+09 * GeoGrad*pmax(0, -14.762-Perm)*pmax(0, 90-Thick)                           \
    +359373       * pmax(0, Depth-1575.51)*pmax(0, Perm+14.9223)-807133      * pmax(0, 1575.51-Depth)*pmax(0, Perm+14.9223)                         \
    +4.14541e+06  * pmax(0, GeoGrad-0.0300566)*Thick*pmax(0, 90-Thick)-2.35281e+07 * pmax(0, 0.0300566-GeoGrad)*Thick*pmax(0, 90-Thick)                         \
    -4.72148e+09 * pmax(0, Perm+14.788)*pmax(0, 0.046341-GeoGrad)-6.2995e+10  * pmax(0, -14.788-Perm)*pmax(0, 0.046341-GeoGrad)                        \
    +0.0364479    * pmax(0, Depth-3452.13)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-0.0982414   * pmax(0, 3452.13-Depth)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)             \
    -3.72584e+08 * pmax(0, Perm+13.9701)*pmax(0, 0.0300566-GeoGrad)*Thick*pmax(0, 90-Thick)+2.1378e+07   * pmax(0, -13.9701-Perm)*pmax(0, 0.0300566-GeoGrad)*Thick*pmax(0, 90-Thick)          
    ROM_1_MCO2_30yr = ROM_1_MCO2_30yr / 1000000000 / 30       
    return ROM_1_MCO2_30yr 
#############
# ROM: 0.05-0.5
#############
def ROM_2_MCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_2_MCO2_30yr =+6.66117e+11  +4.51742e+10  * Perm+4.23425e+11  * Thick+1.20842e+07  * pmax(0, Depth-3381.79)*Thick-6.23862e+07 * pmax(0, 3381.79-Depth)*Thick                                         \
    +3.0185e+10   * Thick*Perm+839422       * pmax(0, Depth-3381.79)*Thick*Perm-4.4364e+06  * pmax(0, 3381.79-Depth)*Thick*Perm                                      \
    -1.24457e+09 * pmax(0, GeoGrad-0.0371514)*Perm-1.51569e+09 * pmax(0, 0.0371514-GeoGrad)*Perm+2.98994e+09  * pmax(0, Perm+14.7285)*Perm                                         \
    -2.93231e+09 * pmax(0, -14.7285-Perm)*Perm-136281      * pmax(0, Depth-3774.14)*pmax(0, Perm+14.7285)*Perm+91843.6      * pmax(0, 3774.14-Depth)*pmax(0, Perm+14.7285)*Perm                           \
    +1.90165e+09  * pmax(0, Perm+13.9893)*Thick*Perm-1.87746e+09 * pmax(0, -13.9893-Perm)*Thick*Perm                                     \
    -213702      * pmax(0, Perm+13.9561)*pmax(0, 3381.79-Depth)*Thick*Perm+232200       * pmax(0, -13.9561-Perm)*pmax(0, 3381.79-Depth)*Thick*Perm                       \
    +1.42214e+06  * pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm-5.65488e+06 * pmax(0, 1423.6-Depth)*pmax(0, 0.0371514-GeoGrad)*Perm                          \
    +72621.1      * Thick*pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm+8.62504e+09  * pmax(0, Perm+14.4494)*pmax(0, 0.0371514-GeoGrad)*Perm                                  \
    -13.5333     * pmax(0, Depth-1490.66)*pmax(0, 3381.79-Depth)*Thick+51.6152      * pmax(0, 1490.66-Depth)*pmax(0, 3381.79-Depth)*Thick                           \
    +7.39587e+10  * pmax(0, GeoGrad-0.027274)*Thick-1.74393e+11 * pmax(0, 0.027274-GeoGrad)*Thick                                        \
    -7.43172e+07 * pmax(0, Perm+14.9341)*pmax(0, -13.9893-Perm)*Thick*Perm+8.18371e+07  * pmax(0, -14.9341-Perm)*pmax(0, -13.9893-Perm)*Thick*Perm                      \
    -38124.1     * pmax(0, Depth-1461.17)*pmax(0, -13.9893-Perm)*Thick*Perm+45585.9      * pmax(0, 1461.17-Depth)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +4.88071e+09  * pmax(0, GeoGrad-0.027274)*Thick*Perm-1.16132e+10 * pmax(0, 0.027274-GeoGrad)*Thick*Perm                                     \
    -3.21827e+06 * pmax(0, Depth-2105.99)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm+1.52855e+07  * pmax(0, 2105.99-Depth)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm          \
    -1.65906e+07 * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick+5.56449e+07  * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick                         \
    -1.07044e+06 * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick*Perm+3.68636e+06  * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick*Perm                      
    ROM_2_MCO2_30yr = ROM_2_MCO2_30yr / 1000000000 / 30       
    return ROM_2_MCO2_30yr 
#############
# ROM: 0.1-1
#############
def ROM_3_MCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_3_MCO2_30yr =+1.7643e+12    +1.23234e+11  * Perm+8.70752e+08  * Thick-68732       * pmax(0, Depth-2656.39)*Perm                                         \
    +40444.1      * pmax(0, 2656.39-Depth)*Perm-7.77819e+06 * Thick*Thick+84923.6      * Thick*Thick*Thick-1.08762e+09 * pmax(0, GeoGrad-0.0282262)*Perm                                       \
    +1.78735e+10  * pmax(0, 0.0282262-GeoGrad)*Perm-329.542     * Thick*Thick*Thick*Thick-190247      * pmax(0, -14.4473-Perm)*pmax(0, 2656.39-Depth)*Perm-512939      * pmax(0, Depth-1251.72)*Thick                                         \
    -378362      * pmax(0, 1251.72-Depth)*Thick+1.79916e+09  * pmax(0, Perm+13.5403)*Thick-4.01927e+08 * pmax(0, -13.5403-Perm)*Thick                                        \
    +2.35956e+06  * pmax(0, Perm+14.1926)*pmax(0, Depth-1251.72)*Thick-1.69344e+06 * pmax(0, -14.1926-Perm)*pmax(0, Depth-1251.72)*Thick                          \
    -4.77908e+08 * pmax(0, Perm+14.8441)*pmax(0, -13.5403-Perm)*Thick+2.48038e+08  * pmax(0, -14.8441-Perm)*pmax(0, -13.5403-Perm)*Thick                         \
    +8.81252e+09  * pmax(0, Perm+14.3203)*Perm-7.84903e+09 * pmax(0, -14.3203-Perm)*Perm+2.08944e+06  * pmax(0, GeoGrad-0.0192943)*pmax(0, Depth-1251.72)*Thick                         \
    -2.75773e+06 * pmax(0, 0.0192943-GeoGrad)*pmax(0, Depth-1251.72)*Thick+1.22369e+07  * pmax(0, Perm+14.4202)*pmax(0, GeoGrad-0.0192943)*pmax(0, Depth-1251.72)*Thick           \
    -2.70449e+06 * pmax(0, -14.4202-Perm)*pmax(0, GeoGrad-0.0192943)*pmax(0, Depth-1251.72)*Thick+1.15155e+06  * pmax(0, Depth-1263.09)*pmax(0, -13.5403-Perm)*Thick                          \
    +177762       * pmax(0, 1263.09-Depth)*pmax(0, -13.5403-Perm)*Thick-1.31601e+06 * pmax(0, Perm+14.1723)*pmax(0, Depth-1263.09)*pmax(0, -13.5403-Perm)*Thick            \
    +202418       * pmax(0, -14.1723-Perm)*pmax(0, Depth-1263.09)*pmax(0, -13.5403-Perm)*Thick+172755       * pmax(0, 1888.58-Depth)*pmax(0, Perm+14.8441)*pmax(0, -13.5403-Perm)*Thick                     \
    -1.7502e+10  * pmax(0, -13.6182-Perm)*pmax(0, 0.0282262-GeoGrad)*Perm-1.22264e+08 * pmax(0, Perm+14.2822)*pmax(0, Perm+14.8441)*pmax(0, -13.5403-Perm)*Thick            \
    +3.29304e+08  * pmax(0, -14.2822-Perm)*pmax(0, Perm+14.8441)*pmax(0, -13.5403-Perm)*Thick-111051      * pmax(0, Depth-1148.76)*pmax(0, Perm+14.3203)*Perm                           \
    +1.23783e+06  * pmax(0, 1148.76-Depth)*pmax(0, Perm+14.3203)*Perm-1.30563e+09 * pmax(0, 0.0335429-GeoGrad)*Thick                                       
    ROM_3_MCO2_30yr = ROM_3_MCO2_30yr / 1000000000 / 30       
    return ROM_3_MCO2_30yr 
#############
# ROM: 0.5-5
#############
def ROM_4_MCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_4_MCO2_30yr =-2.10446e+10  +3.494e+10    * pmax(0, Perm+13.9911)-1.37133e+10 * pmax(0, -13.9911-Perm)                                          \
    +2.11975e+09  * Thick+2.59639e+06  * pmax(0, Depth-2547.6)-8.22632e+06 * pmax(0, 2547.6-Depth)-4.39729e+07 * Thick*Thick                                                   \
    +455828       * Thick*Thick*Thick+2.1468e+11   * pmax(0, GeoGrad-0.0258077)-5.91354e+11 * pmax(0, 0.0258077-GeoGrad)-1698.51     * Thick*Thick*Thick*Thick                       \
    +5.00782e+09  * pmax(0, Perm+14.5929)*Thick-5.8405e+08  * pmax(0, -14.5929-Perm)*Thick+1.59675e+06  * pmax(0, Depth-2893.14)*pmax(0, Perm+14.5929)*Thick                          \
    -1.89772e+06 * pmax(0, 2893.14-Depth)*pmax(0, Perm+14.5929)*Thick+2.17832e+10  * pmax(0, Perm+12.9207)*pmax(0, Perm+14.5929)*Thick                          \
    -2.71229e+09 * pmax(0, -12.9207-Perm)*pmax(0, Perm+14.5929)*Thick+9.31951e+06  * pmax(0, Depth-2347.76)*pmax(0, Perm+13.9911)                             \
    -3.65805e+06 * pmax(0, 2347.76-Depth)*pmax(0, Perm+13.9911)-3.89381e+06 * pmax(0, GeoGrad-0.0364025)*pmax(0, Depth-2893.14)*pmax(0, Perm+14.5929)*Thick                  \
    -9.16279e+06 * pmax(0, Perm+12.9207)*pmax(0, 2893.14-Depth)*pmax(0, Perm+14.5929)*Thick+822001       * pmax(0, -12.9207-Perm)*pmax(0, 2893.14-Depth)*pmax(0, Perm+14.5929)*Thick           \
    -1.67133e+09 * pmax(0, Perm+14.0278)*pmax(0, -12.9207-Perm)*pmax(0, Perm+14.5929)*Thick+1.57418e+09  * pmax(0, -14.0278-Perm)*pmax(0, -12.9207-Perm)*pmax(0, Perm+14.5929)*Thick          \
    +7.45362e+09  * pmax(0, GeoGrad-0.0397006)*pmax(0, Perm+14.5929)*Thick-5.23678e+10 * pmax(0, 0.0397006-GeoGrad)*pmax(0, Perm+14.5929)*Thick                        \
    -1.46518e+07 * pmax(0, Depth-1971.39)*pmax(0, 0.0397006-GeoGrad)*pmax(0, Perm+14.5929)*Thick+2.06947e+07  * pmax(0, 1971.39-Depth)*pmax(0, 0.0397006-GeoGrad)*pmax(0, Perm+14.5929)*Thick          \
    +6.88127e+11  * pmax(0, Perm+12.307)*pmax(0, 0.0397006-GeoGrad)*pmax(0, Perm+14.5929)*Thick+2.6986e+10   * pmax(0, -12.307-Perm)*pmax(0, 0.0397006-GeoGrad)*pmax(0, Perm+14.5929)*Thick          \
    +90470.8      * pmax(0, Depth-2975.36)*Thick-229412      * pmax(0, 2975.36-Depth)*Thick-642468      * pmax(0, Depth-1497.08)*pmax(0, -12.9207-Perm)*pmax(0, Perm+14.5929)*Thick           \
    +1.03078e+06  * pmax(0, 1497.08-Depth)*pmax(0, -12.9207-Perm)*pmax(0, Perm+14.5929)*Thick-1.59663e+10 * pmax(0, Poro-0.0713728)*pmax(0, Perm+13.9911)+2.85694e+11  * pmax(0, 0.0713728-Poro)*pmax(0, Perm+13.9911)                           
    ROM_4_MCO2_30yr = ROM_4_MCO2_30yr / 1000000000 / 30       
    return ROM_4_MCO2_30yr 
#############
# ROM: 1-10
#############
def ROM_5_MCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_MCO2_30yr =-1.8627e+10  +5.04458e+10  * pmax(0, Perm+13.5653)-3.75168e+10 * pmax(0, -13.5653-Perm)+2.70721e+09  * Thick                                                       \
    +5.59558e+06  * pmax(0, Depth-2690.86)-1.41291e+07 * pmax(0, 2690.86-Depth)-5.49035e+07 * Thick*Thick+2.61763e+11  * pmax(0, GeoGrad-0.0275088)                                          \
    -2.90807e+11 * pmax(0, 0.0275088-GeoGrad)+537693       * Thick*Thick*Thick-1954.56     * Thick*Thick*Thick*Thick-1908.65     * pmax(0, 1830-Depth)*pmax(0, 2690.86-Depth)                                 \
    +8.30148e+08  * pmax(0, Perm+14.2596)*Thick+1.04693e+06  * pmax(0, Depth-2669.97)*pmax(0, Perm+14.2596)*Thick                           \
    -1.38445e+06 * pmax(0, 2669.97-Depth)*pmax(0, Perm+14.2596)*Thick+4.09548e+09  * pmax(0, Perm+13.6495)*pmax(0, Perm+14.2596)*Thick                           \
    -2.1027e+09  * pmax(0, -13.6495-Perm)*pmax(0, Perm+14.2596)*Thick-5.78427e+06 * pmax(0, Perm+13.0979)*pmax(0, 2669.97-Depth)*pmax(0, Perm+14.2596)*Thick             \
    +2.33973e+06  * pmax(0, -13.0979-Perm)*pmax(0, 2669.97-Depth)*pmax(0, Perm+14.2596)*Thick+7.8468e+09   * pmax(0, Perm+13.1468)*pmax(0, Perm+13.6495)*pmax(0, Perm+14.2596)*Thick             \
    -2.0849e+09  * pmax(0, -13.1468-Perm)*pmax(0, Perm+13.6495)*pmax(0, Perm+14.2596)*Thick+3.98997e+06  * pmax(0, Perm+13.5536)*pmax(0, Depth-2669.97)*pmax(0, Perm+14.2596)*Thick             \
    -1.08122e+06 * pmax(0, -13.5536-Perm)*pmax(0, Depth-2669.97)*pmax(0, Perm+14.2596)*Thick-2.37455e+10 * pmax(0, GeoGrad-0.0185572)*pmax(0, Perm+14.2596)*Thick                         \
    -3.49355e+10 * pmax(0, 0.0185572-GeoGrad)*pmax(0, Perm+14.2596)*Thick+3.58788e+07  * pmax(0, Depth-1233.33)*pmax(0, GeoGrad-0.0185572)*pmax(0, Perm+14.2596)*Thick           \
    -3.12996e+07 * pmax(0, 1233.33-Depth)*pmax(0, GeoGrad-0.0185572)*pmax(0, Perm+14.2596)*Thick+4.55234e+10  * pmax(0, Perm+14.0011)*pmax(0, GeoGrad-0.0185572)*pmax(0, Perm+14.2596)*Thick           \
    +2.37405e+11  * pmax(0, -14.0011-Perm)*pmax(0, GeoGrad-0.0185572)*pmax(0, Perm+14.2596)*Thick-1.51567e+09 * pmax(0, Poro-0.111318)*pmax(0, Perm+13.6495)*pmax(0, Perm+14.2596)*Thick            \
    +9.63353e+09  * pmax(0, 0.111318-Poro)*pmax(0, Perm+13.6495)*pmax(0, Perm+14.2596)*Thick+652424       * pmax(0, Depth-1436.02)*Thick                                                  \
    +1.29721e+07  * pmax(0, Perm+12.8359)*pmax(0, Depth-1436.02)*Thick-300891      * pmax(0, -12.8359-Perm)*pmax(0, Depth-1436.02)*Thick                          \
    -2.38867e+07 * pmax(0, GeoGrad-0.0224135)*pmax(0, Depth-2669.97)*pmax(0, Perm+14.2596)*Thick-5.03083e+07 * pmax(0, 0.0224135-GeoGrad)*pmax(0, Depth-2669.97)*pmax(0, Perm+14.2596)*Thick           \
    -1.65004e+12 * pmax(0, Perm+13.6067)*pmax(0, 0.0275088-GeoGrad)-1.42347e+12 * pmax(0, -13.6067-Perm)*pmax(0, 0.0275088-GeoGrad)
    ROM_5_MCO2_30yr = ROM_5_MCO2_30yr / 1000000000 / 30       
    return ROM_5_MCO2_30yr 
#############
# ROM: 5-50
#############
def ROM_6_MCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_6_MCO2_30yr =-1.43435e+11   +3.89622e+11  * pmax(0, Perm+12.9374)-4.53867e+11 * pmax(0, -12.9374-Perm)+2.12888e+10  * Thick                                                      \
    +9.11057e+07  * pmax(0, Depth-2404.97)-1.77036e+08 * pmax(0, 2404.97-Depth)-3.628e+08   * Thick*Thick+1.0009e+12   * pmax(0, GeoGrad-0.0347305)-4.26153e+12 * pmax(0, 0.0347305-GeoGrad)                              \
    +3.35168e+06  * Thick*Thick*Thick-11804.5     * Thick*Thick*Thick*Thick-7.19627e+07 * pmax(0, Perm+13.6145)*pmax(0, Depth-2404.97)                             \
    -3.77891e+07 * pmax(0, -13.6145-Perm)*pmax(0, Depth-2404.97)+5.65303e+06  * Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2404.97)                          \
    +2.89503e+09  * pmax(0, Perm+13.308)*Thick+2.65257e+06  * pmax(0, Depth-1975.74)*pmax(0, Perm+13.308)*Thick                           \
    -9.92113e+06 * pmax(0, 1975.74-Depth)*pmax(0, Perm+13.308)*Thick-5.49373e+08 * pmax(0, GeoGrad-0.0256615)*pmax(0, Depth-1975.74)*pmax(0, Perm+13.308)*Thick           \
    +3.17961e+08  * pmax(0, 0.0256615-GeoGrad)*pmax(0, Depth-1975.74)*pmax(0, Perm+13.308)*Thick+2.81516e+07  * pmax(0, Perm+12.6327)*pmax(0, Depth-1975.74)*pmax(0, Perm+13.308)*Thick             \
    -1.19813e+07 * pmax(0, -12.6327-Perm)*pmax(0, Depth-1975.74)*pmax(0, Perm+13.308)*Thick+2.67164e+10  * pmax(0, Perm+12.7617)*pmax(0, Perm+13.308)*Thick                           \
    -8.05081e+09 * pmax(0, -12.7617-Perm)*pmax(0, Perm+13.308)*Thick-6.86674e+09 * pmax(0, Poro-0.13216)*pmax(0, Perm+13.308)*Thick                           \
    +2.8834e+10   * pmax(0, 0.13216-Poro)*pmax(0, Perm+13.308)*Thick+7.48529e+10  * pmax(0, GeoGrad-0.0137038)*pmax(0, Perm+13.308)*Thick                                  \
    -1.08039e+07 * pmax(0, Perm+12.202)*pmax(0, 1975.74-Depth)*pmax(0, Perm+13.308)*Thick+1.31636e+07  * pmax(0, -12.202-Perm)*pmax(0, 1975.74-Depth)*pmax(0, Perm+13.308)*Thick             \
    +5.18304e+08  * pmax(0, Depth-1810.06)*pmax(0, GeoGrad-0.0137038)*pmax(0, Perm+13.308)*Thick-1.93013e+08 * pmax(0, 1810.06-Depth)*pmax(0, GeoGrad-0.0137038)*pmax(0, Perm+13.308)*Thick           \
    -1.02035e+08 * pmax(0, Perm+12.7089)*Thick*Thick+1.97759e+11  * pmax(0, Perm+13.0614)*pmax(0, GeoGrad-0.0137038)*pmax(0, Perm+13.308)*Thick           \
    +4.90695e+11  * pmax(0, -13.0614-Perm)*pmax(0, GeoGrad-0.0137038)*pmax(0, Perm+13.308)*Thick+4.90392e+07  * pmax(0, GeoGrad-0.0347248)*Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2404.97)          \
    -9.18424e+07 * pmax(0, 0.0347248-GeoGrad)*Thick*pmax(0, Perm+13.6145)*pmax(0, Depth-2404.97)          
    ROM_6_MCO2_30yr = ROM_6_MCO2_30yr / 1000000000 / 30       
    return ROM_6_MCO2_30yr 
###########
# ROM: 10-max
###########
def ROM_7_MCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_7_MCO2_30yr =     +9.51622e+10   -1.20816e+11 * pmax(0, -12.8093-Perm)+1.22813e+08  * pmax(0, Depth-3762.41)*pmax(0, Perm+12.8093)                             \
    -3.30429e+07 * pmax(0, 3762.41-Depth)*pmax(0, Perm+12.8093)+2.3057e+07   * Depth*Thick*pmax(0, Perm+12.8093)                                     \
    +6.5063e+07   * pmax(0, Depth-3601.88)-4.5876e+07  * pmax(0, 3601.88-Depth)+6.47282e+09  * Thick                                                      \
    -181281      * Thick*Depth*Thick*pmax(0, Perm+12.8093)+3.6556e+12   * pmax(0, GeoGrad-0.0284806)                                         \
    -1.02202e+13 * pmax(0, 0.0284806-GeoGrad)-4.84521e+09 * pmax(0, -12.3976-Perm)*Thick                                       \
    +1.2719e+08   * pmax(0, GeoGrad-0.0288039)*Depth*Thick*pmax(0, Perm+12.8093)                     \
    -1.97089e+08 * pmax(0, 0.0288039-GeoGrad)*Depth*Thick*pmax(0, Perm+12.8093)                     \
    +1.63992e+06  * pmax(0, Depth-1466.11)*Thick                                        \
    -4.57234e+06 * pmax(0, 1466.11-Depth)*Thick                                        \
    +8.37336e+06  * pmax(0, Perm+13.2844)*pmax(0, Depth-1466.11)*Thick                          \
    -1.75927e+06 * pmax(0, -13.2844-Perm)*pmax(0, Depth-1466.11)*Thick                         \
    +1.83639e+07  * pmax(0, Perm+12.5561)*Depth*Thick*pmax(0, Perm+12.8093)                       \
    +7.53258e+06  * pmax(0, -12.5561-Perm)*Depth*Thick*pmax(0, Perm+12.8093)                      \
    +6.0927e+07   * pmax(0, GeoGrad-0.0265985)*pmax(0, Perm+13.2844)*pmax(0, Depth-1466.11)*Thick          \
    -1.81616e+08 * pmax(0, 0.0265985-GeoGrad)*pmax(0, Perm+13.2844)*pmax(0, Depth-1466.11)*Thick          
    ROM_7_MCO2_30yr = ROM_7_MCO2_30yr / 1000000000 / 30       
    return ROM_7_MCO2_30yr 
#################################################################################### 
# 35 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_MCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_MCO2_35yr =+3.17401e+09        +1.82593e+07  * pmax(0, Thick-90)-5.96918e+07 * pmax(0, 90-Thick)+2.93051e+06  * pmax(0, Depth-1105.76)                                      \
    -3.90999e+06 * pmax(0, 1105.76-Depth)+4.41733e+09  * pmax(0, Perm+14.9223)                                      \
    -4.5745e+09  * pmax(0, -14.9223-Perm)+3.1372e+06   * Thick*pmax(0, 90-Thick)                                        \
    +1569.99      * pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-1.76691e+10 * pmax(0, GeoGrad-0.046341)                                     \
    -5.72363e+09 * pmax(0, 0.046341-GeoGrad)+1.37254e+07  * pmax(0, Perm+13.9701)*Thick*pmax(0, 90-Thick)-4.79415e+06 * pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)                         \
    +5595.59      * pmax(0, Perm+14.4797)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-2072.84     * pmax(0, -14.4797-Perm)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)           \
    +12516.4      * pmax(0, GeoGrad-0.0284601)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-21855.6     * pmax(0, 0.0284601-GeoGrad)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)          \
    -32288.3     * pmax(0, Depth-1655.41)*pmax(0, 90-Thick)+34178.5      * pmax(0, 1655.41-Depth)*pmax(0, 90-Thick)                             \
    -3.59484e+07 * pmax(0, Perm+14.762)*pmax(0, 90-Thick)+1.0257e+08   * pmax(0, -14.762-Perm)*pmax(0, 90-Thick)                             \
    -7.68776e+06 * pmax(0, Perm+14.472)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)+3.67689e+06  * pmax(0, -14.472-Perm)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)           \
    -1.2637e+09  * GeoGrad*pmax(0, -14.762-Perm)*pmax(0, 90-Thick)+452480       * pmax(0, Depth-1575.51)*pmax(0, Perm+14.9223)                        \
    -1.00408e+06 * pmax(0, 1575.51-Depth)*pmax(0, Perm+14.9223)+7.34891e+06  * pmax(0, GeoGrad-0.0300566)*Thick*pmax(0, 90-Thick)                        \
    -9.22489e+06 * pmax(0, 0.0300566-GeoGrad)*Thick*pmax(0, 90-Thick)-1.48334e+10 * pmax(0, Perm+14.788)*pmax(0, 0.046341-GeoGrad)                        \
    -7.78266e+10 * pmax(0, -14.788-Perm)*pmax(0, 0.046341-GeoGrad)+0.0433969    * pmax(0, Depth-3452.13)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)            \
    -0.113255    * pmax(0, 3452.13-Depth)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-2.34104e+07 * Thick*GeoGrad*pmax(0, -14.762-Perm)*pmax(0, 90-Thick)                       
    ROM_1_MCO2_35yr = ROM_1_MCO2_35yr / 1000000000 / 30       
    return ROM_1_MCO2_35yr 
#############
# ROM: 0.05-0.5
#############
def ROM_2_MCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_2_MCO2_35yr =+7.73032e+11  +5.24237e+10  * Perm+4.98116e+11  * Thick+1.40591e+07  * pmax(0, Depth-3381.79)*Thick-7.29437e+07 * pmax(0, 3381.79-Depth)*Thick                                         \
    +3.55108e+10  * Thick*Perm+976721       * pmax(0, Depth-3381.79)*Thick*Perm-5.18731e+06 * pmax(0, 3381.79-Depth)*Thick*Perm-1.38904e+09 * pmax(0, GeoGrad-0.0371514)*Perm                                       \
    -1.77796e+09 * pmax(0, 0.0371514-GeoGrad)*Perm+3.47298e+09  * pmax(0, Perm+14.7285)*Perm-3.40259e+09 * pmax(0, -14.7285-Perm)*Perm                                        \
    -158354      * pmax(0, Depth-3774.14)*pmax(0, Perm+14.7285)*Perm+105381       * pmax(0, 3774.14-Depth)*pmax(0, Perm+14.7285)*Perm                           \
    +2.23995e+09  * pmax(0, Perm+13.9893)*Thick*Perm-2.21043e+09 * pmax(0, -13.9893-Perm)*Thick*Perm                                     \
    -250016      * pmax(0, Perm+13.9561)*pmax(0, 3381.79-Depth)*Thick*Perm+271720       * pmax(0, -13.9561-Perm)*pmax(0, 3381.79-Depth)*Thick*Perm                       \
    +1.65331e+06  * pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm-6.44781e+06 * pmax(0, 1423.6-Depth)*pmax(0, 0.0371514-GeoGrad)*Perm                          \
    +82794.9      * Thick*pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm+9.92385e+09  * pmax(0, Perm+14.4494)*pmax(0, 0.0371514-GeoGrad)*Perm                                   \
    -15.7675     * pmax(0, Depth-1490.66)*pmax(0, 3381.79-Depth)*Thick+60.0877      * pmax(0, 1490.66-Depth)*pmax(0, 3381.79-Depth)*Thick                           \
    +8.50747e+10  * pmax(0, GeoGrad-0.0270544)*Thick-2.04155e+11 * pmax(0, 0.0270544-GeoGrad)*Thick                                       \
    -8.79648e+07 * pmax(0, Perm+14.9341)*pmax(0, -13.9893-Perm)*Thick*Perm+9.67506e+07  * pmax(0, -14.9341-Perm)*pmax(0, -13.9893-Perm)*Thick*Perm                      \
    -44430.6     * pmax(0, Depth-1461.17)*pmax(0, -13.9893-Perm)*Thick*Perm+53121.1      * pmax(0, 1461.17-Depth)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +5.61259e+09  * pmax(0, GeoGrad-0.0270544)*Thick*Perm-1.35945e+10 * pmax(0, 0.0270544-GeoGrad)*Thick*Perm                                    \
    -3.6953e+06  * pmax(0, Depth-2105.99)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm+1.7786e+07   * pmax(0, 2105.99-Depth)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm          \
    -1.85496e+07 * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick+6.49268e+07  * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick                         \
    -1.19434e+06 * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick*Perm+4.30039e+06  * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick*Perm                      
    ROM_2_MCO2_35yr = ROM_2_MCO2_35yr / 1000000000 / 30       
    return ROM_2_MCO2_35yr 
#############
# ROM: 0.1-1
#############
def ROM_3_MCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_3_MCO2_35yr =+3.69489e+09  +1.9423e+10   * pmax(0, Perm+13.4721)-4.57997e+09 * pmax(0, -13.4721-Perm)+4.7901e+08   * Thick                                                      \
    +933181       * pmax(0, Depth-2676.4)-1.4663e+06  * pmax(0, 2676.4-Depth)-6.25694e+06 * Thick*Thick                                                   \
    +65328.2      * Thick*Thick*Thick+1.07833e+10  * pmax(0, GeoGrad-0.0282262)-1.29889e+11 * pmax(0, 0.0282262-GeoGrad)                                         \
    -248.927     * Thick*Thick*Thick*Thick+252453       * pmax(0, Depth-1330.3)*Thick                                         \
    -203362      * pmax(0, 1330.3-Depth)*Thick+657389       * pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick                           \
    -119227      * pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick+3.07381e+08  * pmax(0, Perm+14.0893)*Thick                                        \
    -3.76669e+08 * pmax(0, -14.0893-Perm)*Thick+2.47761e+06  * pmax(0, Perm+13.8985)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick             \
    -1.36008e+06 * pmax(0, -13.8985-Perm)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick+257948       * pmax(0, -14.3667-Perm)*pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick           \
    +2.87774e+06  * pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick-2.57831e+06 * pmax(0, 0.0189446-GeoGrad)*pmax(0, Depth-1330.3)*Thick                         \
    +1.8458e+07   * pmax(0, Perm+14.4167)*pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick-3.92847e+06 * pmax(0, -14.4167-Perm)*pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick                    \
    -1.03908e+06 * pmax(0, 1350.12-Depth)*pmax(0, Perm+14.0893)*Thick+1.09647e+09  * pmax(0, Perm+13.9302)*pmax(0, Perm+14.0893)*Thick                          \
    +1.44295e+09  * pmax(0, -13.9302-Perm)*pmax(0, Perm+14.0893)*Thick-1.93424e+08 * pmax(0, Perm+14.939)*pmax(0, -14.0893-Perm)*Thick                          \
    +4.84661e+07  * pmax(0, -14.939-Perm)*pmax(0, -14.0893-Perm)*Thick+1.35696e+10  * GeoGrad*pmax(0, Perm+14.0893)*Thick                                     \
    +15.7697      * pmax(0, Depth-3374.59)*pmax(0, Depth-1330.3)*Thick-50.2649     * pmax(0, 3374.59-Depth)*pmax(0, Depth-1330.3)*Thick                           \
    -320566      * pmax(0, Depth-2254.8)*pmax(0, -14.0893-Perm)*Thick+204144       * pmax(0, 2254.8-Depth)*pmax(0, -14.0893-Perm)*Thick                          \
    +15562.4      * pmax(0, Poro-0.114762)*pmax(0, Depth-1330.3)*Thick-57749.1     * pmax(0, 0.114762-Poro)*pmax(0, Depth-1330.3)*Thick                          
    ROM_3_MCO2_35yr = ROM_3_MCO2_35yr / 1000000000 / 30       
    return ROM_3_MCO2_35yr 
#############
# ROM: 0.5-5
#############
def ROM_4_MCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_4_MCO2_35yr =-1.93554e+10  +4.42575e+10  * pmax(0, Perm+13.9911)-1.77969e+10 * pmax(0, -13.9911-Perm)                                          \
    +2.31468e+09  * Thick+2.25317e+06  * pmax(0, Depth-2547.6)-3.13126e+06 * pmax(0, 2547.6-Depth)                                            \
    -4.91871e+07 * Thick*Thick+517472       * Thick*Thick*Thick+2.37967e+11  * pmax(0, GeoGrad-0.0258077)                                         \
    -6.77055e+11 * pmax(0, 0.0258077-GeoGrad)-1942.41     * Thick*Thick*Thick*Thick                                             \
    +6.50821e+09  * pmax(0, Perm+14.5929)*Thick-6.53254e+08 * pmax(0, -14.5929-Perm)*Thick                                       \
    +1.943e+06    * pmax(0, Depth-2893.14)*pmax(0, Perm+14.5929)*Thick-1.99366e+06 * pmax(0, 2893.14-Depth)*pmax(0, Perm+14.5929)*Thick                          \
    +2.15155e+10  * pmax(0, Perm+12.9207)*pmax(0, Perm+14.5929)*Thick-3.60471e+09 * pmax(0, -12.9207-Perm)*pmax(0, Perm+14.5929)*Thick                         \
    +1.23178e+07  * pmax(0, Depth-2347.76)*pmax(0, Perm+13.9911)-1.20697e+07 * pmax(0, 2347.76-Depth)*pmax(0, Perm+13.9911)                             \
    -3.74232e+06 * pmax(0, GeoGrad-0.0364025)*pmax(0, Depth-2893.14)*pmax(0, Perm+14.5929)*Thick-4.53512e+06 * pmax(0, 0.0364025-GeoGrad)*pmax(0, Depth-2893.14)*pmax(0, Perm+14.5929)*Thick          \
    -7.92489e+06 * pmax(0, Perm+12.9207)*pmax(0, 2893.14-Depth)*pmax(0, Perm+14.5929)*Thick+472079       * pmax(0, -12.9207-Perm)*pmax(0, 2893.14-Depth)*pmax(0, Perm+14.5929)*Thick           \
    -2.63434e+09 * pmax(0, Perm+14.0278)*pmax(0, -12.9207-Perm)*pmax(0, Perm+14.5929)*Thick+2.15668e+09  * pmax(0, -14.0278-Perm)*pmax(0, -12.9207-Perm)*pmax(0, Perm+14.5929)*Thick          \
    +8.97251e+09  * pmax(0, GeoGrad-0.0397006)*pmax(0, Perm+14.5929)*Thick-6.59718e+10 * pmax(0, 0.0397006-GeoGrad)*pmax(0, Perm+14.5929)*Thick                        \
    -1.42652e+07 * pmax(0, Depth-1971.39)*pmax(0, 0.0397006-GeoGrad)*pmax(0, Perm+14.5929)*Thick+2.66161e+07  * pmax(0, 1971.39-Depth)*pmax(0, 0.0397006-GeoGrad)*pmax(0, Perm+14.5929)*Thick          \
    -2.51774e+11 * pmax(0, Perm+12.307)*pmax(0, 0.0397006-GeoGrad)*pmax(0, Perm+14.5929)*Thick+3.37855e+10  * pmax(0, -12.307-Perm)*pmax(0, 0.0397006-GeoGrad)*pmax(0, Perm+14.5929)*Thick          \
    +120999       * pmax(0, Depth-2975.36)*Thick-220278      * pmax(0, 2975.36-Depth)*Thick-840202      * pmax(0, Depth-1497.08)*pmax(0, -12.9207-Perm)*pmax(0, Perm+14.5929)*Thick           \
    +1.25708e+06  * pmax(0, 1497.08-Depth)*pmax(0, -12.9207-Perm)*pmax(0, Perm+14.5929)*Thick-2.37675e+10 * pmax(0, Poro-0.0713728)*pmax(0, Perm+13.9911)                           \
    +4.1122e+11   * pmax(0, 0.0713728-Poro)*pmax(0, Perm+13.9911)+8.121e+10    * pmax(0, Perm+12.3761)*pmax(0, Perm+13.9911)                             \
    -1.63147e+10 * pmax(0, -12.3761-Perm)*pmax(0, Perm+13.9911)-826837      * pmax(0, Perm+13.5706)*pmax(0, 2893.14-Depth)*pmax(0, Perm+14.5929)*Thick                      
    ROM_4_MCO2_35yr = ROM_4_MCO2_35yr / 1000000000 / 30       
    return ROM_4_MCO2_35yr 
#############
# ROM: 1-10
#############
def ROM_5_MCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_MCO2_35yr =-4.97478e+10  +8.37079e+10  * pmax(0, Perm+13.5653)-3.51481e+10 * pmax(0, -13.5653-Perm)+5.13948e+09  * Thick                                                      \
    +1.32486e+07  * pmax(0, Depth-2690.86)-1.00244e+07 * pmax(0, 2690.86-Depth)-1.08933e+08 * Thick*Thick                                                   \
    +4.81878e+11  * pmax(0, GeoGrad-0.0275088)+1.23153e+12  * pmax(0, 0.0275088-GeoGrad)                                         \
    +1.10898e+06  * Thick*Thick*Thick-4117.29     * Thick*Thick*Thick*Thick+3.84488e+09  * pmax(0, Perm+14.2857)*Thick                                        \
    -1.26795e+09 * pmax(0, -14.2857-Perm)*Thick-1.02384e+07 * pmax(0, 1522.12-Depth)*pmax(0, Perm+14.2857)*Thick                          \
    +1.30539e+07  * pmax(0, Perm+13.1341)*pmax(0, Depth-1522.12)*pmax(0, Perm+14.2857)*Thick-7.9611e+06  * pmax(0, -13.1341-Perm)*pmax(0, Depth-1522.12)*pmax(0, Perm+14.2857)*Thick           \
    +1.70867e+10  * pmax(0, Perm+12.6899)*pmax(0, Perm+14.2857)*Thick-5.46309e+09 * pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2857)*Thick                         \
    +1.64065e+07  * pmax(0, GeoGrad-0.0258527)*pmax(0, Depth-1522.12)*pmax(0, Perm+14.2857)*Thick-5.50949e+07 * pmax(0, 0.0258527-GeoGrad)*pmax(0, Depth-1522.12)*pmax(0, Perm+14.2857)*Thick          \
    +6.07771e+06  * pmax(0, Depth-1507.8)*pmax(0, Perm+13.5653)-5.28759e+07 * pmax(0, 1507.8-Depth)*pmax(0, Perm+13.5653)                              \
    +7.97171e+09  * pmax(0, GeoGrad-0.0379934)*pmax(0, Perm+14.2857)*Thick-2.16073e+10 * pmax(0, 0.0379934-GeoGrad)*pmax(0, Perm+14.2857)*Thick                        \
    -3.83855e+08 * pmax(0, Poro-0.191619)*pmax(0, Perm+14.2857)*Thick+2.28389e+09  * pmax(0, 0.191619-Poro)*pmax(0, Perm+14.2857)*Thick                         \
    -3.15603e+12 * pmax(0, Perm+13.981)*pmax(0, 0.0275088-GeoGrad)-6.97105e+12 * pmax(0, -13.981-Perm)*pmax(0, 0.0275088-GeoGrad)                           \
    +1805.47      * pmax(0, Depth-2199.6)*Thick*Thick+887.235      * pmax(0, 2199.6-Depth)*Thick*Thick                                      \
    +9.87632e+10  * pmax(0, Perm+12.8022)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2857)*Thick+1.89677e+09  * pmax(0, -12.8022-Perm)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2857)*Thick          \
    +6.04077e+06  * pmax(0, Depth-1498.21)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2857)*Thick-1.07206e+07 * pmax(0, 1498.21-Depth)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2857)*Thick           \
    +4.91559e+07  * pmax(0, Perm+12.1592)*pmax(0, 1522.12-Depth)*pmax(0, Perm+14.2857)*Thick+1.31376e+07  * pmax(0, -12.1592-Perm)*pmax(0, 1522.12-Depth)*pmax(0, Perm+14.2857)*Thick           
    ROM_5_MCO2_35yr = ROM_5_MCO2_35yr / 1000000000 / 30       
    return ROM_5_MCO2_35yr 
#############
# ROM: 5-50
#############
def ROM_6_MCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_6_MCO2_35yr =-1.86765e+11 +5.32332e+11  * pmax(0, Perm+12.9305)-6.36235e+11 * pmax(0, -12.9305-Perm)                                           \
    +2.821e+10    * Thick+1.18196e+08  * pmax(0, Depth-2388.33)                                            \
    -2.17178e+08 * pmax(0, 2388.33-Depth)-4.5569e+08  * Thick*Thick                                                              \
    -5.66141e+12 * pmax(0, 0.0350799-GeoGrad)+3.87744e+06  * Thick*Thick*Thick                                                 \
    -12688.9     * Thick*Thick*Thick*Thick-9.1689e+07  * pmax(0, Perm+13.5902)*pmax(0, Depth-2388.33)                                       \
    +6.26025e+06  * Thick*pmax(0, Perm+13.5902)*pmax(0, Depth-2388.33)+8.2022e+06   * pmax(0, Depth-1983.48)*pmax(0, Perm+13.2654)*Thick                           \
    -1.35872e+07 * pmax(0, 1983.48-Depth)*pmax(0, Perm+13.2654)*Thick+1.92632e+10  * pmax(0, Perm+13.2381)*pmax(0, Perm+13.2654)*Thick                           \
    -4.37083e+12 * pmax(0, -13.2381-Perm)*pmax(0, Perm+13.2654)*Thick+3.18065e+07  * pmax(0, Perm+12.7539)*pmax(0, Depth-1983.48)*pmax(0, Perm+13.2654)*Thick             \
    -1.18049e+07 * pmax(0, -12.7539-Perm)*pmax(0, Depth-1983.48)*pmax(0, Perm+13.2654)*Thick-4.11245e+08 * pmax(0, 0.0256615-GeoGrad)*pmax(0, Depth-1983.48)*pmax(0, Perm+13.2654)*Thick           \
    +2.07877e+11  * pmax(0, GeoGrad-0.0256663)*pmax(0, Perm+13.2654)*Thick-2.8091e+11  * pmax(0, 0.0256663-GeoGrad)*pmax(0, Perm+13.2654)*Thick                         \
    -1.13104e+10 * pmax(0, Poro-0.0811778)*pmax(0, Perm+13.2654)*Thick+6.20566e+10  * pmax(0, 0.0811778-Poro)*pmax(0, Perm+13.2654)*Thick                         \
    -3.52215e+07 * pmax(0, Perm+12.3804)*pmax(0, 1983.48-Depth)*pmax(0, Perm+13.2654)*Thick+9.68093e+06  * pmax(0, -12.3804-Perm)*pmax(0, 1983.48-Depth)*pmax(0, Perm+13.2654)*Thick            \
    +2.90846e+10  * pmax(0, Perm+12.3494)*pmax(0, Perm+13.2381)*pmax(0, Perm+13.2654)*Thick-6.62502e+09 * pmax(0, -12.3494-Perm)*pmax(0, Perm+13.2381)*pmax(0, Perm+13.2654)*Thick                     \
    -3.1248e+12  * pmax(0, 0.180538-Poro)*pmax(0, GeoGrad-0.0256663)*pmax(0, Perm+13.2654)*Thick-8.19641e+08 * pmax(0, Depth-1734.05)*pmax(0, 0.0350799-GeoGrad)                            \
    +1.30648e+10  * pmax(0, 1734.05-Depth)*pmax(0, 0.0350799-GeoGrad) 
    ROM_6_MCO2_35yr = ROM_6_MCO2_35yr / 1000000000 / 30       
    return ROM_6_MCO2_35yr
###########
# ROM: 10-max
###########
def ROM_7_MCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_7_MCO2_35yr =  -2.66024e+11   +4.51085e+13  * pmax(0, Perm+12.9203)+1.04126e+09  * pmax(0, 5429.04-Depth)*pmax(0, Perm+12.9203)-3.08468e+10 * pmax(0, Depth-5347.89)*Thick*pmax(0, Perm+12.9203)+3.33499e+07  * pmax(0, 5347.89-Depth)*Thick*pmax(0, Perm+12.9203)                            \
    +1.0304e+08   * Depth+1.44873e+08  * Thick*Depth-2.77436e+09 * Thick*Thick*pmax(0, Perm+12.9203)-4.55345e+12 * pmax(0, Poro-0.438909)*Thick*Thick*pmax(0, Perm+12.9203)-3.74919e+08 * pmax(0, 0.438909-Poro)*Thick*Thick*pmax(0, Perm+12.9203)                        \
    +5.69335e+06  * pmax(0, Depth-5280.5)*Thick*Thick*pmax(0, Perm+12.9203)-1.28773e+09 * pmax(0, Perm+12.5368)*Thick*Depth+7.66019e+08  * pmax(0, -12.5368-Perm)*Thick*Depth-2.41151e+09 * Perm*pmax(0, Depth-5347.89)*Thick*pmax(0, Perm+12.9203)                         \
    -1.9895e+09  * pmax(0, GeoGrad-0.0143965)*pmax(0, Perm+12.5368)*Thick*Depth+3.09503e+13  * pmax(0, GeoGrad-0.0324985)-6.52076e+13 * pmax(0, 0.0324985-GeoGrad)-1.11051e+08 * Poro*pmax(0, Perm+12.5368)*Thick*Depth                                    \
    -6.59459e+10 * pmax(0, Perm+11.9856)*pmax(0, Perm+12.5368)*Thick*Depth+1.22812e+09  * pmax(0, -11.9856-Perm)*pmax(0, Perm+12.5368)*Thick*Depth+8.32382e+13  * pmax(0, -12.0508-Perm)*pmax(0, 0.0324985-GeoGrad)+311616       * pmax(0, 5347.89-Depth)*Thick*Thick*pmax(0, Perm+12.9203)                         \
    +2.49836e+14  * pmax(0, Perm+12.4524)*pmax(0, GeoGrad-0.0324985)-3.42528e+13 * pmax(0, -12.4524-Perm)*pmax(0, GeoGrad-0.0324985)+8.92323e+06  * Thick*Thick*Thick*pmax(0, Perm+12.9203)+3.74059e+12  * Perm*pmax(0, Perm+12.9203)                                          \
    +4.02499e+10  * pmax(0, Perm+11.9856)*Thick*Depth-9.87905e+09 * Poro*pmax(0, Perm+11.9856)*Thick*Depth+1.69832e+10  * pmax(0, Perm+12.0244)*pmax(0, -11.9856-Perm)*Thick*Depth                        \
    -2.41469e+08 * pmax(0, -12.0244-Perm)*pmax(0, -11.9856-Perm)*Thick*Depth+4.48474e+07  * Depth*Thick*pmax(0, Perm+12.9203)-2.76533e+09 * pmax(0, GeoGrad-0.0400188)*Depth*Thick*pmax(0, Perm+12.9203)                       \
    +5.69824e+08  * pmax(0, 0.0400188-GeoGrad)*Depth*Thick*pmax(0, Perm+12.9203)+1.7657e+13   * pmax(0, GeoGrad-0.0453649)*Thick*pmax(0, Perm+12.9203)-4.54077e+12 * pmax(0, 0.0453649-GeoGrad)*Thick*pmax(0, Perm+12.9203)                          \
    +8.23369e+15  * pmax(0, GeoGrad-0.0417854)*pmax(0, 0.0453649-GeoGrad)*Thick*pmax(0, Perm+12.9203)-5.12272e+13 * pmax(0, 0.0417854-GeoGrad)*pmax(0, 0.0453649-GeoGrad)*Thick*pmax(0, Perm+12.9203)          \
    -3.48869e+10 * pmax(0, GeoGrad-0.020272)*Thick*Thick*pmax(0, Perm+12.9203)+5.43228e+10  * pmax(0, 0.020272-GeoGrad)*Thick*Thick*pmax(0, Perm+12.9203)                        \
    -1.08983e+13 * pmax(0, Poro-0.359106)*pmax(0, 0.0453649-GeoGrad)*Thick*pmax(0, Perm+12.9203)+3.8099e+12   * pmax(0, 0.359106-Poro)*pmax(0, 0.0453649-GeoGrad)*Thick*pmax(0, Perm+12.9203)           \
    -4.28518e+10 * GeoGrad*pmax(0, 5429.04-Depth)*pmax(0, Perm+12.9203)+3.85876e+06  * pmax(0, Depth-1278.83)*GeoGrad*pmax(0, 5429.04-Depth)*pmax(0, Perm+12.9203)              \
    -1.97905e+07 * pmax(0, 1278.83-Depth)*GeoGrad*pmax(0, 5429.04-Depth)*pmax(0, Perm+12.9203)+3.21485e+07  * pmax(0, Poro-0.146268)*Depth*Thick*pmax(0, Perm+12.9203)                        \
    -1.39809e+08 * pmax(0, 0.146268-Poro)*Depth*Thick*pmax(0, Perm+12.9203)-5.07759e+13 * pmax(0, -12.5148-Perm)*pmax(0, -12.0508-Perm)*pmax(0, 0.0324985-GeoGrad)             \
    +2.3235e+11   * pmax(0, Poro-0.411248)*GeoGrad*pmax(0, 5429.04-Depth)*pmax(0, Perm+12.9203)+2.8152e+10   * pmax(0, 0.411248-Poro)*GeoGrad*pmax(0, 5429.04-Depth)*pmax(0, Perm+12.9203)             \
    +1.34912e+09  * pmax(0, Perm+12.4261)*Depth*Thick*pmax(0, Perm+12.9203)+1.55099e+07  * pmax(0, -12.4261-Perm)*Depth*Thick*pmax(0, Perm+12.9203)-5.70421e+08 * pmax(0, -12.4122-Perm)*Thick*Depth                                      \
    +3.24454e+08  * Poro*pmax(0, Perm+12.4122)*Thick*Depth+18288.7      * pmax(0, Depth-3682.31)*pmax(0, 5347.89-Depth)*Thick*pmax(0, Perm+12.9203)-6.64397e+12 * pmax(0, -12.5339-Perm)*pmax(0, Perm+12.5368)*Thick*Depth                        \
    -1.67749e+13 * Thick*pmax(0, Perm+12.5148)*pmax(0, -12.0508-Perm)*pmax(0, 0.0324985-GeoGrad)+7.81943e+09  * pmax(0, Perm+12.4594)*pmax(0, -12.4122-Perm)*Thick*Depth+2.46032e+08  * pmax(0, -12.4594-Perm)*pmax(0, -12.4122-Perm)*Thick*Depth                       
    ROM_7_MCO2_35yr = ROM_7_MCO2_35yr / 1000000000 / 30       
    return ROM_7_MCO2_35yr 
#################################################################################### 
# 40 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_MCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_MCO2_40yr =+3.56228e+09  +2.03517e+07  * pmax(0, Thick-90)-6.75951e+07 * pmax(0, 90-Thick)+3.19662e+06  * pmax(0, Depth-1105.76)-4.51118e+06 * pmax(0, 1105.76-Depth)                                      \
    +6.45526e+09  * pmax(0, Perm+14.9223)-6.92944e+09 * pmax(0, -14.9223-Perm)+3.01117e+06  * Thick*pmax(0, 90-Thick)+1883.2       * pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)                                  \
    -1.42986e+10 * pmax(0, 0.046341-GeoGrad)+1.55214e+07  * pmax(0, Perm+13.9701)*Thick*pmax(0, 90-Thick)-4.52897e+06 * pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)                         \
    +6954.64      * pmax(0, Perm+14.4797)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-2510.28     * pmax(0, -14.4797-Perm)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)           \
    +11667.3      * pmax(0, GeoGrad-0.0284601)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-21964.5     * pmax(0, 0.0284601-GeoGrad)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)          \
    -34992.2     * pmax(0, Depth-1655.41)*pmax(0, 90-Thick)+37292.4      * pmax(0, 1655.41-Depth)*pmax(0, 90-Thick)                             \
    -5.98029e+07 * pmax(0, Perm+14.762)*pmax(0, 90-Thick)+1.02638e+08  * pmax(0, -14.762-Perm)*pmax(0, 90-Thick)                             \
    -7.48945e+06 * pmax(0, Perm+14.472)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)+3.1615e+06   * pmax(0, -14.472-Perm)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)           \
    -9.35671e+08 * GeoGrad*pmax(0, -14.762-Perm)*pmax(0, 90-Thick)+405029       * pmax(0, Depth-1575.51)*pmax(0, Perm+14.9223)                        \
    -959961      * pmax(0, 1575.51-Depth)*pmax(0, Perm+14.9223)+3.8875e+06   * pmax(0, GeoGrad-0.0300566)*Thick*pmax(0, 90-Thick)                        \
    -8.87379e+06 * pmax(0, 0.0300566-GeoGrad)*Thick*pmax(0, 90-Thick)+0.0410907    * pmax(0, Depth-3635.17)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)            \
    -0.112684    * pmax(0, 3635.17-Depth)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)            
    ROM_1_MCO2_40yr = ROM_1_MCO2_40yr / 1000000000 / 30       
    return ROM_1_MCO2_40yr 
#############
# ROM: 0.05-0.5
#############
def ROM_2_MCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_2_MCO2_40yr =+8.79325e+11    +5.96314e+10  * Perm+5.73609e+11  * Thick+1.60317e+07  * pmax(0, Depth-3381.79)*Thick-8.34309e+07 * pmax(0, 3381.79-Depth)*Thick                                         \
    +4.08939e+10  * Thick*Perm+1.11386e+06  * pmax(0, Depth-3381.79)*Thick*Perm-5.93322e+06 * pmax(0, 3381.79-Depth)*Thick*Perm                                      \
    -1.57559e+09 * pmax(0, GeoGrad-0.0371514)*Perm-2.07173e+09 * pmax(0, 0.0371514-GeoGrad)*Perm+3.9532e+09   * pmax(0, Perm+14.7285)*Perm                                         \
    -3.87017e+09 * pmax(0, -14.7285-Perm)*Perm-180199      * pmax(0, Depth-3774.14)*pmax(0, Perm+14.7285)*Perm                           \
    +118919       * pmax(0, 3774.14-Depth)*pmax(0, Perm+14.7285)*Perm+2.58241e+09  * pmax(0, Perm+13.9893)*Thick*Perm                                      \
    -2.54721e+09 * pmax(0, -13.9893-Perm)*Thick*Perm-286043      * pmax(0, Perm+13.9561)*pmax(0, 3381.79-Depth)*Thick*Perm                        \
    +310947       * pmax(0, -13.9561-Perm)*pmax(0, 3381.79-Depth)*Thick*Perm+1.88845e+06  * pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm                          \
    -7.26804e+06 * pmax(0, 1423.6-Depth)*pmax(0, 0.0371514-GeoGrad)*Perm+93520.3      * Thick*pmax(0, Depth-1423.6)*pmax(0, 0.0371514-GeoGrad)*Perm                       \
    +1.12188e+10  * pmax(0, Perm+14.4494)*pmax(0, 0.0371514-GeoGrad)*Perm-17.9848     * pmax(0, Depth-1490.66)*pmax(0, 3381.79-Depth)*Thick                           \
    +68.5766      * pmax(0, 1490.66-Depth)*pmax(0, 3381.79-Depth)*Thick+9.60661e+10  * pmax(0, GeoGrad-0.0270544)*Thick                                       \
    -2.31213e+11 * pmax(0, 0.0270544-GeoGrad)*Thick-1.01913e+08 * pmax(0, Perm+14.9341)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +1.11945e+08  * pmax(0, -14.9341-Perm)*pmax(0, -13.9893-Perm)*Thick*Perm-50736.5     * pmax(0, Depth-1461.17)*pmax(0, -13.9893-Perm)*Thick*Perm                       \
    +60657.9      * pmax(0, 1461.17-Depth)*pmax(0, -13.9893-Perm)*Thick*Perm+6.33692e+09  * pmax(0, GeoGrad-0.0270544)*Thick*Perm                                    \
    -1.53961e+10 * pmax(0, 0.0270544-GeoGrad)*Thick*Perm-4.18764e+06 * pmax(0, Depth-2105.99)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm          \
    +2.02988e+07  * pmax(0, 2105.99-Depth)*pmax(0, -14.4494-Perm)*pmax(0, 0.0371514-GeoGrad)*Perm-2.0827e+07  * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick                         \
    +7.34414e+07  * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick-1.33988e+06 * pmax(0, GeoGrad-0.0263619)*pmax(0, 3381.79-Depth)*Thick*Perm                      \
    +4.8639e+06   * pmax(0, 0.0263619-GeoGrad)*pmax(0, 3381.79-Depth)*Thick*Perm                      
    ROM_2_MCO2_40yr = ROM_2_MCO2_40yr / 1000000000 / 30       
    return ROM_2_MCO2_40yr 
#############
# ROM: 0.1-1
#############
def ROM_3_MCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_3_MCO2_40yr =+4.18904e+09   +2.23989e+10  * pmax(0, Perm+13.4721)-5.19826e+09 * pmax(0, -13.4721-Perm)+5.46612e+08  * Thick+1.05639e+06  * pmax(0, Depth-2676.4)-1.6699e+06  * pmax(0, 2676.4-Depth)-7.15567e+06 * Thick*Thick                                                   \
    +74597.8      * Thick*Thick*Thick+1.15127e+10  * pmax(0, GeoGrad-0.0282262)-1.46027e+11 * pmax(0, 0.0282262-GeoGrad)                                         \
    -283.866     * Thick*Thick*Thick*Thick+287217       * pmax(0, Depth-1330.3)*Thick-230978      * pmax(0, 1330.3-Depth)*Thick                                         \
    +753261       * pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick-136788      * pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick                          \
    +3.54143e+08  * pmax(0, Perm+14.0893)*Thick-4.28761e+08 * pmax(0, -14.0893-Perm)*Thick+2.81291e+06  * pmax(0, Perm+13.8985)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick             \
    -1.5615e+06  * pmax(0, -13.8985-Perm)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick+294382       * pmax(0, -14.3667-Perm)*pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick           \
    +3.26505e+06  * pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick-2.91965e+06 * pmax(0, 0.0189446-GeoGrad)*pmax(0, Depth-1330.3)*Thick                         \
    +2.09799e+07  * pmax(0, Perm+14.4167)*pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick-4.45924e+06 * pmax(0, -14.4167-Perm)*pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick                  \
    -1.19867e+06 * pmax(0, 1350.12-Depth)*pmax(0, Perm+14.0893)*Thick+1.26917e+09  * pmax(0, Perm+13.9302)*pmax(0, Perm+14.0893)*Thick+1.56186e+09  * pmax(0, -13.9302-Perm)*pmax(0, Perm+14.0893)*Thick-2.2217e+08  * pmax(0, Perm+14.939)*pmax(0, -14.0893-Perm)*Thick                          \
    +5.50392e+07  * pmax(0, -14.939-Perm)*pmax(0, -14.0893-Perm)*Thick+1.54438e+10  * GeoGrad*pmax(0, Perm+14.0893)*Thick+17.9343      * pmax(0, Depth-3374.59)*pmax(0, Depth-1330.3)*Thick-57.1344     * pmax(0, 3374.59-Depth)*pmax(0, Depth-1330.3)*Thick                           \
    -364449      * pmax(0, Depth-2254.8)*pmax(0, -14.0893-Perm)*Thick+232354       * pmax(0, 2254.8-Depth)*pmax(0, -14.0893-Perm)*Thick+17811.3      * pmax(0, Poro-0.114762)*pmax(0, Depth-1330.3)*Thick-61601.1     * pmax(0, 0.114762-Poro)*pmax(0, Depth-1330.3)*Thick                          
    ROM_3_MCO2_40yr = ROM_3_MCO2_40yr / 1000000000 / 30       
    return ROM_3_MCO2_40yr 
#############
# ROM: 0.5-5
#############
def ROM_4_MCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_4_MCO2_40yr =-1.09987e+10   +6.50165e+10  * pmax(0, Perm+13.9792)+7.36351e+10  * pmax(0, -13.9792-Perm)+9.25531e+09  * Thick-2.75156e+06 * pmax(0, Depth-2547.6)                                             \
    +5.21611e+07  * pmax(0, 2547.6-Depth)-6.17826e+07 * Thick*Thick+301375       * Thick*Thick*Thick-2.12673e+11 * pmax(0, 0.0258077-GeoGrad)                                                   \
    +3.9956e+10   * pmax(0, Perm+12.9758)*Thick-6.92225e+09 * pmax(0, -12.9758-Perm)*Thick+1.16343e+07  * pmax(0, Perm+14.6448)*pmax(0, Depth-2547.6)                               \
    -3.95934e+07 * pmax(0, -14.6448-Perm)*pmax(0, Depth-2547.6)+1.28386e+06  * Thick*pmax(0, Perm+14.6448)*pmax(0, Depth-2547.6)                            \
    +3.94434e+06  * pmax(0, Perm+13.6228)*Thick*pmax(0, Perm+14.6448)*pmax(0, Depth-2547.6)-1.17613e+06 * pmax(0, -13.6228-Perm)*Thick*pmax(0, Perm+14.6448)*pmax(0, Depth-2547.6)             \
    -5.07331e+08 * pmax(0, Perm+12.9598)*Thick*Thick+5.01726e+07  * pmax(0, -12.9598-Perm)*Thick*Thick+3985.36      * pmax(0, 1283.03-Depth)*pmax(0, 2547.6-Depth)                                        \
    -1.86517e+07 * pmax(0, 0.038072-GeoGrad)*Thick*pmax(0, Perm+14.6448)*pmax(0, Depth-2547.6)+4.07142e+06  * pmax(0, Perm+12.9497)*Thick*Thick*Thick                                   \
    -245035      * pmax(0, -12.9497-Perm)*Thick*Thick*Thick+9.47592e+07  * pmax(0, Perm+13.421)*pmax(0, 2547.6-Depth)-9.14917e+07 * pmax(0, -13.421-Perm)*pmax(0, 2547.6-Depth)                               \
    +245915       * pmax(0, Depth-2613.27)*Thick-2.08888e+06 * pmax(0, 2613.27-Depth)*Thick-1.99685e+09 * pmax(0, Perm+14.2872)*pmax(0, -12.9758-Perm)*Thick                          \
    +1.51957e+09  * pmax(0, -14.2872-Perm)*pmax(0, -12.9758-Perm)*Thick-1.18816e+07 * pmax(0, Perm+12.9847)*pmax(0, 2613.27-Depth)*Thick                           \
    +1.64994e+06  * pmax(0, -12.9847-Perm)*pmax(0, 2613.27-Depth)*Thick+2.07793e+10  * pmax(0, GeoGrad-0.0320404)*pmax(0, Perm+14.2872)*pmax(0, -12.9758-Perm)*Thick          \
    -4.52987e+10 * pmax(0, 0.0320404-GeoGrad)*pmax(0, Perm+14.2872)*pmax(0, -12.9758-Perm)*Thick-6.79167e+06 * pmax(0, GeoGrad-0.0235124)*pmax(0, -12.9847-Perm)*pmax(0, 2613.27-Depth)*Thick          \
    +2.72412e+07  * pmax(0, 0.0235124-GeoGrad)*pmax(0, -12.9847-Perm)*pmax(0, 2613.27-Depth)*Thick-1.17459e+07 * pmax(0, Depth-2496.86)*pmax(0, Perm+13.9792)                              \
    -1.3411e+08  * pmax(0, 2496.86-Depth)*pmax(0, Perm+13.9792)+1.2856e+11   * pmax(0, Perm+12.307)*pmax(0, Perm+13.9792)-4.17761e+10 * pmax(0, -12.307-Perm)*pmax(0, Perm+13.9792)                              \
    +7.78769e+11  * pmax(0, GeoGrad-0.0247534)*pmax(0, Perm+13.9792)-1.42965e+12 * pmax(0, 0.0247534-GeoGrad)*pmax(0, Perm+13.9792)-2.64326e+10 * pmax(0, Poro-0.0713728)*pmax(0, Perm+13.9792)                            \
    +5.58086e+11  * pmax(0, 0.0713728-Poro)*pmax(0, Perm+13.9792)+5.20746e+09  * pmax(0, GeoGrad-0.0197777)*Thick-1.51528e+10 * pmax(0, 0.0197777-GeoGrad)*Thick                                       
    ROM_4_MCO2_40yr = ROM_4_MCO2_40yr / 1000000000 / 30       
    return ROM_4_MCO2_40yr 
#############
# ROM: 1-10
#############
def ROM_5_MCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_MCO2_40yr =-5.7526e+10  +9.60957e+10  * pmax(0, Perm+13.5653)-3.96035e+10 * pmax(0, -13.5653-Perm)+5.90544e+09  * Thick+1.50673e+07  * pmax(0, Depth-2669.97)                                           \
    -1.17001e+07 * pmax(0, 2669.97-Depth)-1.25278e+08 * Thick*Thick+5.47801e+11  * pmax(0, GeoGrad-0.0276017)+1.35914e+12  * pmax(0, 0.0276017-GeoGrad)                                         \
    +1.27491e+06  * Thick*Thick*Thick-4730.25     * Thick*Thick*Thick*Thick+4.50345e+09  * pmax(0, Perm+14.2765)*Thick-1.45915e+09 * pmax(0, -14.2765-Perm)*Thick                                                \
    -1.24083e+07 * pmax(0, 1519.09-Depth)*pmax(0, Perm+14.2765)*Thick+1.51808e+07  * pmax(0, Perm+13.1341)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2765)*Thick            \
    -9.23979e+06 * pmax(0, -13.1341-Perm)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2765)*Thick+2.03589e+10  * pmax(0, Perm+12.6899)*pmax(0, Perm+14.2765)*Thick                          \
    -6.38066e+09 * pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2765)*Thick+1.89858e+07  * pmax(0, GeoGrad-0.0258527)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2765)*Thick          \
    -6.37566e+07 * pmax(0, 0.0258527-GeoGrad)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2765)*Thick+6.51191e+06  * pmax(0, Depth-1507.8)*pmax(0, Perm+13.5653)                              \
    -5.83123e+07 * pmax(0, 1507.8-Depth)*pmax(0, Perm+13.5653)-5.15977e+08 * pmax(0, Poro-0.191619)*pmax(0, Perm+14.2765)*Thick                         \
    +2.91523e+09  * pmax(0, 0.191619-Poro)*pmax(0, Perm+14.2765)*Thick+9.73935e+09  * pmax(0, GeoGrad-0.0379934)*pmax(0, Perm+14.2765)*Thick                        \
    -2.52545e+10 * pmax(0, 0.0379934-GeoGrad)*pmax(0, Perm+14.2765)*Thick-3.55354e+12 * pmax(0, Perm+13.981)*pmax(0, 0.0276017-GeoGrad)                            \
    -7.93105e+12 * pmax(0, -13.981-Perm)*pmax(0, 0.0276017-GeoGrad)+2103.36      * pmax(0, Depth-2199.6)*Thick*Thick                                      \
    +951.452      * pmax(0, 2199.6-Depth)*Thick*Thick+1.1949e+11   * pmax(0, Perm+12.8022)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2765)*Thick           \
    +2.23181e+09  * pmax(0, -12.8022-Perm)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2765)*Thick+7.00829e+06  * pmax(0, Depth-1498.21)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2765)*Thick           \
    -1.32853e+07 * pmax(0, 1498.21-Depth)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2765)*Thick+5.67463e+07  * pmax(0, Perm+12.1592)*pmax(0, 1519.09-Depth)*pmax(0, Perm+14.2765)*Thick            \
    +1.61498e+07  * pmax(0, -12.1592-Perm)*pmax(0, 1519.09-Depth)*pmax(0, Perm+14.2765)*Thick           
    ROM_5_MCO2_40yr = ROM_5_MCO2_40yr / 1000000000 / 30       
    return ROM_5_MCO2_40yr 
#############
# ROM: 5-50
#############
def ROM_6_MCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_6_MCO2_40yr =-1.62952e+11 +5.77351e+11  * pmax(0, Perm+12.9225)-6.56571e+11 * pmax(0, -12.9225-Perm)+2.85539e+10  * Thick+1.27806e+08  * pmax(0, Depth-2346.97)                                           \
    -2.7141e+08  * pmax(0, 2346.97-Depth)-4.62292e+08 * Thick*Thick+4.0864e+06   * Thick*Thick*Thick                                                \
    -14016       * Thick*Thick*Thick*Thick-9.34479e+07 * pmax(0, Perm+13.5537)*pmax(0, Depth-2346.97)                             \
    -5.60498e+07 * pmax(0, -13.5537-Perm)*pmax(0, Depth-2346.97)+8.0738e+06   * Thick*pmax(0, Perm+13.5537)*pmax(0, Depth-2346.97)                                   \
    -2.41982e+12 * pmax(0, Depth-1956.33)*pmax(0, Perm+13.2531)*Thick-3.75511e+06 * pmax(0, 1956.33-Depth)*pmax(0, Perm+13.2531)*Thick                          \
    +2.90658e+10  * pmax(0, Perm+13.2503)*pmax(0, Perm+13.2531)*Thick-1.31917e+16 * pmax(0, -13.2503-Perm)*pmax(0, Perm+13.2531)*Thick                         \
    -4.87404e+12 * pmax(0, Perm+12.7539)*pmax(0, Depth-1956.33)*pmax(0, Perm+13.2531)*Thick+4.87407e+12  * pmax(0, -12.7539-Perm)*pmax(0, Depth-1956.33)*pmax(0, Perm+13.2531)*Thick                     \
    -5.41344e+08 * pmax(0, 0.0256615-GeoGrad)*pmax(0, Depth-1956.33)*pmax(0, Perm+13.2531)*Thick-9.31089e+13 * Poro*pmax(0, 0.0356536-GeoGrad)                                                \
    -7.61928e+07 * pmax(0, 0.119834-Poro)*Thick*pmax(0, Perm+13.5537)*pmax(0, Depth-2346.97)+9.86005e+13  * pmax(0, Perm+12.3757)*Poro*pmax(0, 0.0356536-GeoGrad)                        \
    +2.96738e+13  * pmax(0, -12.3757-Perm)*Poro*pmax(0, 0.0356536-GeoGrad)                       \
    +4.87408e+12  * pmax(0, Depth-1956.33)*pmax(0, Perm+13.2503)*pmax(0, Perm+13.2531)*Thick            \
    -1.18612e+07 * pmax(0, 1956.33-Depth)*pmax(0, Perm+13.2503)*pmax(0, Perm+13.2531)*Thick            \
    -9.41583e+07 * Thick*pmax(0, Perm+13.2503)*pmax(0, Perm+13.2531)*Thick                       \
    +5.19624e+13  * pmax(0, Poro-0.117981)*pmax(0, 0.0356536-GeoGrad)                          \
    +7.47124e+13  * pmax(0, 0.117981-Poro)*pmax(0, 0.0356536-GeoGrad)                          
    ROM_6_MCO2_40yr = ROM_6_MCO2_40yr / 1000000000 / 30       
    return ROM_6_MCO2_40yr 
###########
# ROM: 10-max
###########
def ROM_7_MCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_7_MCO2_40yr =-9.79114e+11  +1.70743e+10  * pmax(0, Depth-5280.5)*pmax(0, Perm+12.9748)+4.59095e+09  * Thick+3.33747e+07  * Depth*Thick-930860      * Thick*Depth*Thick+1.192e+06    * pmax(0, -11.9856-Perm)*Thick*Depth*Thick-2.07824e+11 * pmax(0, Perm+12.076)*pmax(0, -12.058-Perm)*Depth*Thick                                             \
    -117156      * pmax(0, 0.438167-Poro)*Thick*Depth*Thick+1.88262e+10  * pmax(0, Poro-0.438167)*pmax(0, -12.058-Perm)*Depth*Thick+2.29323e+07  * pmax(0, 0.438167-Poro)*pmax(0, -12.058-Perm)*Depth*Thick-2.0201e+08  * pmax(0, Perm+12.4053)*pmax(0, -12.058-Perm)*Depth*Thick                                   \
    +5.14823e+08  * pmax(0, -12.4053-Perm)*pmax(0, -12.058-Perm)*Depth*Thick+1.59765e+10  * pmax(0, Perm+12.0965)*pmax(0, -12.058-Perm)*Depth*Thick+1.09293e+09  * pmax(0, -12.0965-Perm)*pmax(0, -12.058-Perm)*Depth*Thick-794065      * pmax(0, -12.5201-Perm)*Thick*Depth*Thick                                             \
    -7.9788e+09  * GeoGrad*pmax(0, Perm+12.058)*Depth*Thick+5.27752e+11  * pmax(0, Perm+12.2237)*Thick-1.60308e+09 * pmax(0, -12.178-Perm)*pmax(0, -12.058-Perm)*Depth*Thick-4.8407e+12  * GeoGrad*pmax(0, Perm+12.2237)*Thick                                                 \
    -1.88368e+12 * pmax(0, Perm+12.2217)*pmax(0, Perm+12.2237)*Thick+7.44327e+13  * pmax(0, Perm+12.0445)*GeoGrad*pmax(0, Perm+12.2237)*Thick+9.72147e+10  * pmax(0, 0.0390234-GeoGrad)*pmax(0, 5280.5-Depth)*pmax(0, Perm+12.9748)-1.13314e+13 * Thick*pmax(0, 0.0407969-GeoGrad)*pmax(0, Perm+12.9748)                                            \
    +8.45307e+12  * pmax(0, Perm+12.4118)*Thick*pmax(0, 0.0407969-GeoGrad)*pmax(0, Perm+12.9748)-1.00065e+13 * pmax(0, -12.4118-Perm)*Thick*pmax(0, 0.0407969-GeoGrad)*pmax(0, Perm+12.9748)+7.0231e+10   * Thick*Thick*pmax(0, 0.0407969-GeoGrad)*pmax(0, Perm+12.9748)-345457      * pmax(0, -12.9302-Perm)*Thick*Depth*Thick                                             \
    -1.50398e+11 * pmax(0, Perm+12.5486)*pmax(0, 0.0390234-GeoGrad)*pmax(0, 5280.5-Depth)*pmax(0, Perm+12.9748)+2.0439e+11   * pmax(0, -12.5486-Perm)*pmax(0, 0.0390234-GeoGrad)*pmax(0, 5280.5-Depth)*pmax(0, Perm+12.9748)                     \
    -2.94981e+09 * Thick*pmax(0, GeoGrad-0.0181354)*pmax(0, Depth-1767.33)*pmax(0, Perm+12.9748)+7.65567e+10  * Poro*pmax(0, GeoGrad-0.0181354)*pmax(0, Depth-1767.33)*pmax(0, Perm+12.9748)+5.27368e+07  * pmax(0, Perm+12.9678)*Depth*Thick+1.13709e+08  * pmax(0, Poro-0.244494)*pmax(0, Perm+12.9678)*Depth*Thick                                  \
    -3.72327e+07 * pmax(0, 0.244494-Poro)*pmax(0, Perm+12.9678)*Depth*Thick-2.9248e+13  * pmax(0, Poro-0.390804)*Thick*pmax(0, 0.0407969-GeoGrad)*pmax(0, Perm+12.9748)+8.61112e+12  * pmax(0, 0.390804-Poro)*Thick*pmax(0, 0.0407969-GeoGrad)*pmax(0, Perm+12.9748)+2.06761e+09  * pmax(0, Perm+12.1898)*pmax(0, 5280.5-Depth)*pmax(0, Perm+12.9748)                                     \
    -2.17866e+08 * pmax(0, Depth-5323.86)*pmax(0, Depth-5280.5)*pmax(0, Perm+12.9748)+6.2571e+09   * pmax(0, 5323.86-Depth)*pmax(0, Depth-5280.5)*pmax(0, Perm+12.9748)                            \
    -8.19835e+12 * pmax(0, Poro-0.212816)+3.32679e+12  * pmax(0, 0.212816-Poro)+3.34632e+13  * pmax(0, Perm+12.2923)*pmax(0, Poro-0.212816)+2.07019e+13  * pmax(0, -12.2923-Perm)*pmax(0, Poro-0.212816)                                       \
    -9.9268e+11  * pmax(0, Perm+12.1573)*pmax(0, GeoGrad-0.0181354)*pmax(0, Depth-1767.33)*pmax(0, Perm+12.9748)+7.82618e+10  * pmax(0, -12.1573-Perm)*pmax(0, GeoGrad-0.0181354)*pmax(0, Depth-1767.33)*pmax(0, Perm+12.9748)          \
    -9.91828e+08 * pmax(0, GeoGrad-0.0299582)*pmax(0, Perm+12.9678)*Depth*Thick+2.28865e+08  * pmax(0, 0.0299582-GeoGrad)*pmax(0, Perm+12.9678)*Depth*Thick+52708.5      * pmax(0, Depth-5322.61)*pmax(0, Perm+12.9678)*Depth*Thick                                           \
    +5.03816e+11  * pmax(0, Poro-0.390804)*pmax(0, 0.0390234-GeoGrad)*pmax(0, 5280.5-Depth)*pmax(0, Perm+12.9748)-1.16051e+11 * pmax(0, 0.390804-Poro)*pmax(0, 0.0390234-GeoGrad)*pmax(0, 5280.5-Depth)*pmax(0, Perm+12.9748)           \
    -2.62993e+07 * pmax(0, Poro-0.205492)*Depth*Thick-3.48873e+07 * pmax(0, 0.205492-Poro)*Depth*Thick+9.07057e+08  * GeoGrad*pmax(0, Poro-0.205492)*Depth*Thick-2.10095e+08 * Thick*pmax(0, 5323.86-Depth)*pmax(0, Depth-5280.5)*pmax(0, Perm+12.9748)+3.96505e+11  * pmax(0, Perm+12.5242)*pmax(0, -12.2237-Perm)*Thick                                             \
    -1.30665e+14 * pmax(0, Perm+12.0592)*pmax(0, Poro-0.212816)+602.421      * Thick*Thick*Depth*Thick+1.54683e+10  * pmax(0, Perm+12.0383)*pmax(0, Perm+12.058)*Depth*Thick                                    \
    +6.38877e+10  * pmax(0, -12.0383-Perm)*pmax(0, Perm+12.058)*Depth*Thick-8.81305e+10 * pmax(0, Poro-0.438324)*pmax(0, Poro-0.205492)*Depth*Thick-8.2057e+10  * pmax(0, Depth-5487.74)*pmax(0, GeoGrad-0.0181354)*pmax(0, Depth-1767.33)*pmax(0, Perm+12.9748)           \
    +1.26726e+07  * pmax(0, 5487.74-Depth)*pmax(0, GeoGrad-0.0181354)*pmax(0, Depth-1767.33)*pmax(0, Perm+12.9748)-2.36841e+14 * GeoGrad*pmax(0, -12.2923-Perm)*pmax(0, Poro-0.212816)-1.9437e+10  * pmax(0, Perm+12.01)*pmax(0, Perm+12.058)*Depth*Thick                                      \
    +1.16846e+10  * pmax(0, -12.01-Perm)*pmax(0, Perm+12.058)*Depth*Thick                                     
    ROM_7_MCO2_40yr = ROM_7_MCO2_40yr / 1000000000 / 30       
    return ROM_7_MCO2_40yr 
#################################################################################### 
# 45 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_MCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_MCO2_45yr =+3.94545e+09  +2.32225e+07  * pmax(0, Thick-90)-1.19485e+08 * pmax(0, 90-Thick)+3.59257e+06  * pmax(0, Depth-1105.76)-5.2371e+06  * pmax(0, 1105.76-Depth)                                      \
    +7.45094e+09  * pmax(0, Perm+14.9223)-7.06263e+09 * pmax(0, -14.9223-Perm)+3.25382e+06  * Thick*pmax(0, 90-Thick)+2363.57      * pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)                                    \
    +21335.2      * GeoGrad*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)+1.1797e+07   * pmax(0, Perm+13.9701)*Thick*pmax(0, 90-Thick)                          \
    -4.38342e+06 * pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)+3252.93      * pmax(0, -14.5972-Perm)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)           \
    +1.33811e+10  * pmax(0, GeoGrad-0.039297)-2.73347e+10 * pmax(0, 0.039297-GeoGrad)-4.5328e+06  * pmax(0, Perm+14.6242)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)           \
    +3.34484e+06  * pmax(0, -14.6242-Perm)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)-39565.5     * pmax(0, Depth-1655.41)*pmax(0, 90-Thick)                             \
    +42231.4      * pmax(0, 1655.41-Depth)*pmax(0, 90-Thick)-5.50337e+07 * pmax(0, Perm+14.1759)*pmax(0, 90-Thick)                             \
    +8.98599e+07  * pmax(0, -14.1759-Perm)*pmax(0, 90-Thick)-4.27675e+08 * GeoGrad*pmax(0, -14.1759-Perm)*pmax(0, 90-Thick)                         \
    +500226       * pmax(0, Depth-1575.51)*pmax(0, Perm+14.9223)-834927      * pmax(0, 1575.51-Depth)*pmax(0, Perm+14.9223)                        \
    +3.96005e+06  * pmax(0, GeoGrad-0.0254405)*Thick*pmax(0, 90-Thick)-9.56288e+06 * pmax(0, 0.0254405-GeoGrad)*Thick*pmax(0, 90-Thick)                        \
    +0.0574936    * pmax(0, Depth-3355.27)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-0.138093    * pmax(0, 3355.27-Depth)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)            \
    +10387.9      * pmax(0, Perm+14.362)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)-5767.52     * pmax(0, -14.362-Perm)*pmax(0, Depth-1100.28)*Thick*pmax(0, 90-Thick)            
    ROM_1_MCO2_45yr = ROM_1_MCO2_45yr / 1000000000 / 30       
    return ROM_1_MCO2_45yr 
#############
# ROM: 0.05-0.5
#############
def ROM_2_MCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_2_MCO2_45yr =+9.94801e+11  +6.74615e+10  * Perm+6.45804e+11  * Thick+1.81164e+07  * pmax(0, Depth-3381.79)*Thick-9.42791e+07 * pmax(0, 3381.79-Depth)*Thick                                        \
    +4.60421e+10  * Thick*Perm+1.259e+06    * pmax(0, Depth-3381.79)*Thick*Perm-6.70541e+06 * pmax(0, 3381.79-Depth)*Thick*Perm                                     \
    -1.6213e+09  * pmax(0, GeoGrad-0.037294)*Perm-2.29284e+09 * pmax(0, 0.037294-GeoGrad)*Perm+4.479e+09    * pmax(0, Perm+14.7285)*Perm                                        \
    -4.38112e+09 * pmax(0, -14.7285-Perm)*Perm-201918      * pmax(0, Depth-3774.14)*pmax(0, Perm+14.7285)*Perm+132480       * pmax(0, 3774.14-Depth)*pmax(0, Perm+14.7285)*Perm                          \
    +2.90991e+09  * pmax(0, Perm+13.9893)*Thick*Perm-2.86971e+09 * pmax(0, -13.9893-Perm)*Thick*Perm-324899      * pmax(0, Perm+13.9561)*pmax(0, 3381.79-Depth)*Thick*Perm                       \
    +351734       * pmax(0, -13.9561-Perm)*pmax(0, 3381.79-Depth)*Thick*Perm+2.11247e+06  * pmax(0, Depth-1423.6)*pmax(0, 0.037294-GeoGrad)*Perm-8.02807e+06 * pmax(0, 1423.6-Depth)*pmax(0, 0.037294-GeoGrad)*Perm+101920       * Thick*pmax(0, Depth-1423.6)*pmax(0, 0.037294-GeoGrad)*Perm                       \
    +1.24423e+10  * pmax(0, Perm+14.4494)*pmax(0, 0.037294-GeoGrad)*Perm-20.282      * pmax(0, Depth-1490.66)*pmax(0, 3381.79-Depth)*Thick+76.9226      * pmax(0, 1490.66-Depth)*pmax(0, 3381.79-Depth)*Thick-1.14163e+08 * pmax(0, Perm+14.9208)*pmax(0, -13.9893-Perm)*Thick*Perm                      \
    +1.24975e+08  * pmax(0, -14.9208-Perm)*pmax(0, -13.9893-Perm)*Thick*Perm+1.1518e+11   * pmax(0, GeoGrad-0.0258384)*Thick-2.64824e+11 * pmax(0, 0.0258384-GeoGrad)*Thick-57555.1     * pmax(0, Depth-1461.17)*pmax(0, -13.9893-Perm)*Thick*Perm                      \
    +68689.4      * pmax(0, 1461.17-Depth)*pmax(0, -13.9893-Perm)*Thick*Perm+7.60764e+09  * pmax(0, GeoGrad-0.0258384)*Thick*Perm                                   \
    -1.76283e+10 * pmax(0, 0.0258384-GeoGrad)*Thick*Perm-4.59568e+06 * pmax(0, Depth-2105.99)*pmax(0, -14.4494-Perm)*pmax(0, 0.037294-GeoGrad)*Perm          \
    +2.25337e+07  * pmax(0, 2105.99-Depth)*pmax(0, -14.4494-Perm)*pmax(0, 0.037294-GeoGrad)*Perm-2.65187e+07 * pmax(0, GeoGrad-0.0247837)*pmax(0, 3381.79-Depth)*Thick                        \
    +8.63821e+07  * pmax(0, 0.0247837-GeoGrad)*pmax(0, 3381.79-Depth)*Thick-1.71552e+06 * pmax(0, GeoGrad-0.0247837)*pmax(0, 3381.79-Depth)*Thick*Perm                     \
    +5.71672e+06  * pmax(0, 0.0247837-GeoGrad)*pmax(0, 3381.79-Depth)*Thick*Perm                     
    ROM_2_MCO2_45yr = ROM_2_MCO2_45yr / 1000000000 / 30       
    return ROM_2_MCO2_45yr 
#############
# ROM: 0.1-1
#############
def ROM_3_MCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_3_MCO2_45yr =+4.6709e+09   +2.5414e+10   * pmax(0, Perm+13.4721)-5.80269e+09 * pmax(0, -13.4721-Perm)+6.13779e+08  * Thick+1.17759e+06  * pmax(0, Depth-2676.4)-1.87035e+06 * pmax(0, 2676.4-Depth)                                            \
    -8.04448e+06 * Thick*Thick+83743.4      * Thick*Thick*Thick+1.21148e+10  * pmax(0, GeoGrad-0.0282262)-1.6185e+11  * pmax(0, 0.0282262-GeoGrad)                                         \
    -318.219     * Thick*Thick*Thick*Thick+321964       * pmax(0, Depth-1330.3)*Thick-258559      * pmax(0, 1330.3-Depth)*Thick                                         \
    +849684       * pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick-154308      * pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick                          \
    +4.01109e+08  * pmax(0, Perm+14.0893)*Thick-4.8104e+08  * pmax(0, -14.0893-Perm)*Thick+3.14521e+06  * pmax(0, Perm+13.8985)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick             \
    -1.76683e+06 * pmax(0, -13.8985-Perm)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick+330828       * pmax(0, -14.3667-Perm)*pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick           \
    +3.65132e+06  * pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick-3.25839e+06 * pmax(0, 0.0189446-GeoGrad)*pmax(0, Depth-1330.3)*Thick                         \
    +2.35031e+07  * pmax(0, Perm+14.4167)*pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick-4.9895e+06  * pmax(0, -14.4167-Perm)*pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick                   \
    -1.3609e+06  * pmax(0, 1350.12-Depth)*pmax(0, Perm+14.0893)*Thick+1.44603e+09  * pmax(0, Perm+13.9302)*pmax(0, Perm+14.0893)*Thick                          \
    +1.66115e+09  * pmax(0, -13.9302-Perm)*pmax(0, Perm+14.0893)*Thick-2.51367e+08 * pmax(0, Perm+14.939)*pmax(0, -14.0893-Perm)*Thick                          \
    +6.15831e+07  * pmax(0, -14.939-Perm)*pmax(0, -14.0893-Perm)*Thick+1.73322e+10  * GeoGrad*pmax(0, Perm+14.0893)*Thick                                     \
    +20.0815      * pmax(0, Depth-3374.59)*pmax(0, Depth-1330.3)*Thick-63.9433     * pmax(0, 3374.59-Depth)*pmax(0, Depth-1330.3)*Thick                           \
    -408248      * pmax(0, Depth-2254.8)*pmax(0, -14.0893-Perm)*Thick+260663       * pmax(0, 2254.8-Depth)*pmax(0, -14.0893-Perm)*Thick                          \
    +19858.7      * pmax(0, Poro-0.116608)*pmax(0, Depth-1330.3)*Thick-62848.7     * pmax(0, 0.116608-Poro)*pmax(0, Depth-1330.3)*Thick                          
    ROM_3_MCO2_45yr = ROM_3_MCO2_45yr / 1000000000 / 30       
    return ROM_3_MCO2_45yr 
#############
# ROM: 0.5-5
#############
def ROM_4_MCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_4_MCO2_45yr =-1.8709e+10 +6.47889e+10  * pmax(0, Perm+13.9792)+6.76477e+10  * pmax(0, -13.9792-Perm)+1.09472e+10  * Thick-3.65134e+06 * pmax(0, Depth-2532.72)+6.74576e+07  * pmax(0, 2532.72-Depth)                                            \
    -7.24462e+07 * Thick*Thick+428856       * Thick*Thick*Thick+3.28327e+11  * pmax(0, GeoGrad-0.0258979)-6.08617e+11 * pmax(0, 0.0258979-GeoGrad)-562.595     * Thick*Thick*Thick*Thick                                              \
    +4.42496e+10  * pmax(0, Perm+12.9758)*Thick-6.84533e+09 * pmax(0, -12.9758-Perm)*Thick+1.54237e+07  * pmax(0, Perm+14.644)*pmax(0, Depth-2532.72)+746062       * Thick*pmax(0, Perm+14.644)*pmax(0, Depth-2532.72)                            \
    +4.64084e+06  * pmax(0, Perm+13.6228)*Thick*pmax(0, Perm+14.644)*pmax(0, Depth-2532.72)-1.31288e+06 * pmax(0, -13.6228-Perm)*Thick*pmax(0, Perm+14.644)*pmax(0, Depth-2532.72)             \
    -2.86512e+08 * pmax(0, Perm+12.9598)*Thick*Thick+4.80147e+07  * pmax(0, -12.9598-Perm)*Thick*Thick-2.53131e+07 * pmax(0, 0.0364025-GeoGrad)*Thick*pmax(0, Perm+14.644)*pmax(0, Depth-2532.72)                     \
    -230554      * pmax(0, -12.9497-Perm)*Thick*Thick*Thick+1.18535e+08  * pmax(0, Perm+13.421)*pmax(0, 2532.72-Depth)-1.15702e+08 * pmax(0, -13.421-Perm)*pmax(0, 2532.72-Depth)                              \
    +1.39254e+06  * pmax(0, Depth-2647.75)*Thick-2.50546e+06 * pmax(0, 2647.75-Depth)*Thick-2.50737e+09 * pmax(0, Perm+14.2872)*pmax(0, -12.9758-Perm)*Thick                          \
    +1.97436e+09  * pmax(0, -14.2872-Perm)*pmax(0, -12.9758-Perm)*Thick-1.45104e+07 * pmax(0, Perm+12.9847)*pmax(0, 2647.75-Depth)*Thick+1.25281e+06  * pmax(0, -12.9847-Perm)*pmax(0, 2647.75-Depth)*Thick                          \
    +2.1392e+10   * pmax(0, GeoGrad-0.0386215)*pmax(0, Perm+14.2872)*pmax(0, -12.9758-Perm)*Thick-3.19205e+10 * pmax(0, 0.0386215-GeoGrad)*pmax(0, Perm+14.2872)*pmax(0, -12.9758-Perm)*Thick          \
    +8.86952e+11  * pmax(0, GeoGrad-0.0247534)*pmax(0, Perm+13.9792)-1.02424e+12 * pmax(0, 0.0247534-GeoGrad)*pmax(0, Perm+13.9792)                            \
    +1.006e+11    * pmax(0, Perm+12.5084)*pmax(0, Perm+13.9792)-4.26646e+10 * pmax(0, -12.5084-Perm)*pmax(0, Perm+13.9792)-1.68187e+07 * pmax(0, Depth-2496.86)*pmax(0, Perm+13.9792)-1.60864e+08 * pmax(0, 2496.86-Depth)*pmax(0, Perm+13.9792)                              \
    -3.38715e+10 * pmax(0, Poro-0.0713728)*pmax(0, Perm+13.9792)+6.73823e+11  * pmax(0, 0.0713728-Poro)*pmax(0, Perm+13.9792)                            \
    -297097      * pmax(0, GeoGrad-0.0234058)*pmax(0, 2480.79-Depth)*pmax(0, 2532.72-Depth)+1.67044e+06  * pmax(0, 0.0234058-GeoGrad)*pmax(0, 2480.79-Depth)*pmax(0, 2532.72-Depth)              \
    -7.00006e+10 * Thick*pmax(0, 0.0247534-GeoGrad)*pmax(0, Perm+13.9792)-659993      * pmax(0, Depth-1360.44)*pmax(0, -12.9758-Perm)*Thick                          \
    +1.17303e+06  * pmax(0, 1360.44-Depth)*pmax(0, -12.9758-Perm)*Thick                          
    ROM_4_MCO2_45yr = ROM_4_MCO2_45yr / 1000000000 / 30       
    return ROM_4_MCO2_45yr 
#############
# ROM: 1-10
#############
def ROM_5_MCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_MCO2_45yr =-6.55104e+10  +1.0903e+11   * pmax(0, Perm+13.5653)-4.38993e+10 * pmax(0, -13.5653-Perm)+6.67987e+09  * Thick+1.69088e+07  * pmax(0, Depth-2669.97)                                           \
    -1.32812e+07 * pmax(0, 2669.97-Depth)-1.42024e+08 * Thick*Thick+1.44557e+06  * Thick*Thick*Thick+6.19975e+11  * pmax(0, GeoGrad-0.0275088)                                         \
    +1.54954e+12  * pmax(0, 0.0275088-GeoGrad)-5361.48     * Thick*Thick*Thick*Thick+5.19282e+09  * pmax(0, Perm+14.2717)*Thick                                        \
    -1.6513e+09  * pmax(0, -14.2717-Perm)*Thick-1.43409e+07 * pmax(0, 1519.09-Depth)*pmax(0, Perm+14.2717)*Thick+1.73312e+07  * pmax(0, Perm+13.1341)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2717)*Thick            \
    -1.05264e+07 * pmax(0, -13.1341-Perm)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2717)*Thick+2.35856e+10  * pmax(0, Perm+12.6899)*pmax(0, Perm+14.2717)*Thick                          \
    -7.34727e+09 * pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2717)*Thick+2.12567e+07  * pmax(0, GeoGrad-0.0258527)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2717)*Thick          \
    -7.25421e+07 * pmax(0, 0.0258527-GeoGrad)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2717)*Thick-6.80968e+08 * pmax(0, Poro-0.187922)*pmax(0, Perm+14.2717)*Thick                         \
    +3.65622e+09  * pmax(0, 0.187922-Poro)*pmax(0, Perm+14.2717)*Thick+6.78645e+06  * pmax(0, Depth-1507.8)*pmax(0, Perm+13.5653)                              \
    -6.56838e+07 * pmax(0, 1507.8-Depth)*pmax(0, Perm+13.5653)+1.14712e+10  * pmax(0, GeoGrad-0.0379934)*pmax(0, Perm+14.2717)*Thick                        \
    -2.90567e+10 * pmax(0, 0.0379934-GeoGrad)*pmax(0, Perm+14.2717)*Thick-4.03273e+12 * pmax(0, Perm+13.981)*pmax(0, 0.0275088-GeoGrad)                            \
    -9.04841e+12 * pmax(0, -13.981-Perm)*pmax(0, 0.0275088-GeoGrad)+2384.79      * pmax(0, Depth-2187.86)*Thick*Thick+1000.42      * pmax(0, 2187.86-Depth)*Thick*Thick                                     \
    +1.40794e+11  * pmax(0, Perm+12.8022)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2717)*Thick+2.58972e+09  * pmax(0, -12.8022-Perm)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2717)*Thick          \
    +7.97763e+06  * pmax(0, Depth-1498.21)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2717)*Thick-1.54121e+07 * pmax(0, 1498.21-Depth)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2717)*Thick           \
    +6.46461e+07  * pmax(0, Perm+12.1592)*pmax(0, 1519.09-Depth)*pmax(0, Perm+14.2717)*Thick+1.87171e+07  * pmax(0, -12.1592-Perm)*pmax(0, 1519.09-Depth)*pmax(0, Perm+14.2717)*Thick           
    ROM_5_MCO2_45yr = ROM_5_MCO2_45yr / 1000000000 / 30       
    return ROM_5_MCO2_45yr 
#############
# ROM: 5-50
#############
def ROM_6_MCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_6_MCO2_45yr =-1.42495e+11  +6.22669e+11  * pmax(0, Perm+12.8813)-1.09351e+12 * pmax(0, -12.8813-Perm)+2.96728e+10  * Thick+2.02554e+08  * pmax(0, Depth-2333.46)-3.54014e+08 * pmax(0, 2333.46-Depth)                                          \
    -2.84261e+08 * Thick*Thick+1.18436e+06  * Thick*Thick*Thick+2.0784e+12   * pmax(0, GeoGrad-0.0325252)-7.08869e+12 * pmax(0, 0.0325252-GeoGrad)+1.7928e+10   * pmax(0, Perm+13.4303)*Thick                                                \
    +1.35712e+07  * pmax(0, Depth-3472.72)*pmax(0, Perm+13.4303)*Thick-1.21905e+07 * pmax(0, 3472.72-Depth)*pmax(0, Perm+13.4303)*Thick+5.90421e+10  * pmax(0, Perm+12.7993)*pmax(0, Perm+13.4303)*Thick                         \
    -2.17889e+10 * pmax(0, -12.7993-Perm)*pmax(0, Perm+13.4303)*Thick+3.68612e+07  * pmax(0, Depth-2447.08)*pmax(0, Perm+12.7993)*pmax(0, Perm+13.4303)*Thick           \
    -2.24675e+07 * pmax(0, 2447.08-Depth)*pmax(0, Perm+12.7993)*pmax(0, Perm+13.4303)*Thick-1.40106e+14 * Thick*pmax(0, 0.197994-Poro)*pmax(0, GeoGrad-0.0325252)                      \
    -1.14539e+13 * Perm*Thick*pmax(0, 0.197994-Poro)*pmax(0, GeoGrad-0.0325252)-2.08613e+09 * Depth*Thick*pmax(0, 0.197994-Poro)*pmax(0, GeoGrad-0.0325252)                   \
    +2.04259e+11  * pmax(0, GeoGrad-0.0256615)*pmax(0, Perm+13.4303)*Thick-5.06673e+11 * pmax(0, 0.0256615-GeoGrad)*pmax(0, Perm+13.4303)*Thick                       \
    -2.68014e+09 * pmax(0, Depth-2041.33)*pmax(0, 0.0325252-GeoGrad)-2.04117e+08 * pmax(0, Perm+13.4449)*pmax(0, Depth-2333.46)                                     \
    -3.74627e+07 * pmax(0, Poro-0.180432)*pmax(0, 3472.72-Depth)*pmax(0, Perm+13.4303)*Thick+6.01635e+07  * pmax(0, 0.180432-Poro)*pmax(0, 3472.72-Depth)*pmax(0, Perm+13.4303)*Thick          \
    -1.89751e+08 * pmax(0, Perm+12.7955)*Thick*Thick-1.02945e+07 * pmax(0, -12.7955-Perm)*Thick*Thick-9.67572e+10 * Thick*Thick*pmax(0, 0.197994-Poro)*pmax(0, GeoGrad-0.0325252)                   \
    +3.07703e+08  * Thick*pmax(0, 2041.33-Depth)*pmax(0, 0.0325252-GeoGrad)+2.30077e+10  * pmax(0, Poro-0.117872)*pmax(0, Perm+13.4303)*Thick                        \
    -1.57877e+11 * pmax(0, 0.117872-Poro)*pmax(0, Perm+13.4303)*Thick-1.87256e+07 * pmax(0, Depth-2374.81)*pmax(0, Poro-0.117872)*pmax(0, Perm+13.4303)*Thick          \
    +5.20181e+07  * pmax(0, 2374.81-Depth)*pmax(0, Poro-0.117872)*pmax(0, Perm+13.4303)*Thick+1.38302e+14  * pmax(0, 0.129501-Poro)*pmax(0, 0.0325252-GeoGrad)                         \
    +1.74189e+07  * pmax(0, Perm+13.1244)*pmax(0, Depth-3472.72)*pmax(0, Perm+13.4303)*Thick+2.3692e+07   * pmax(0, -13.1244-Perm)*pmax(0, Depth-3472.72)*pmax(0, Perm+13.4303)*Thick          
    ROM_6_MCO2_45yr = ROM_6_MCO2_45yr / 1000000000 / 30       
    return ROM_6_MCO2_45yr 
###########
# ROM: 10-max
###########
def ROM_7_MCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_7_MCO2_45yr =-2.47059e+11 -2.53166e+12 * pmax(0, -12.0659-Perm)+1.90764e+08  * pmax(0, Depth-2725.2)+4.12129e+09  * pmax(0, 2725.2-Depth)+9.55365e+10  * Thick+6.61867e+09  * pmax(0, Perm+12.419)*pmax(0, Depth-2725.2)-9.50869e+11 * GeoGrad*pmax(0, Perm+12.419)*pmax(0, Depth-2725.2)+2.48993e+12  * Poro*GeoGrad*pmax(0, Perm+12.419)*pmax(0, Depth-2725.2)                                    \
    +7.45585e+06  * Thick*Thick*Thick-1.18581e+09 * pmax(0, 0.438167-Poro)*Thick*Thick+2.91345e+10  * pmax(0, 0.0212618-GeoGrad)*Thick*Thick-9.03703e+10 * pmax(0, Perm+12.7249)*pmax(0, GeoGrad-0.0212618)*Thick*Thick+1.78719e+10  * pmax(0, -12.7249-Perm)*pmax(0, GeoGrad-0.0212618)*Thick*Thick+1.06805e+08  * pmax(0, Depth-2783.95)*pmax(0, GeoGrad-0.0212618)*Thick*Thick-9.79153e+07 * pmax(0, 2783.95-Depth)*pmax(0, GeoGrad-0.0212618)*Thick*Thick+2.58164e+12  * pmax(0, 0.438167-Poro)*pmax(0, -12.0659-Perm)\
    -4.93553e+10 * pmax(0, GeoGrad-0.0237984)*pmax(0, 0.438167-Poro)*Thick*Thick+9.84808e+10  * pmax(0, 0.0237984-GeoGrad)*pmax(0, 0.438167-Poro)*Thick*Thick-1.32879e+10 * pmax(0, Perm+12.3551)*pmax(0, Perm+12.419)*pmax(0, Depth-2725.2)+1.89505e+14  * pmax(0, Perm+12.055)*pmax(0, Perm+12.0659)+1.09042e+15  * Thick*pmax(0, -12.055-Perm)*pmax(0, Perm+12.0659)+2.03062e+07  * pmax(0, 5296.14-Depth)*Thick                                                   \
    +8.28963e+11  * pmax(0, Perm+12.8257)*Thick-1.68095e+11 * pmax(0, -12.8257-Perm)*Thick+1.7308e+09   * pmax(0, -12.8093-Perm)*Thick*Thick-2.7429e+09  * pmax(0, Depth-5322.61)*pmax(0, Perm+12.8257)*Thick+7.19492e+10  * pmax(0, GeoGrad-0.0189387)*pmax(0, 5322.61-Depth)*pmax(0, Perm+12.8257)*Thick                     \
    -7.08044e+10 * pmax(0, 0.0189387-GeoGrad)*pmax(0, 5322.61-Depth)*pmax(0, Perm+12.8257)*Thick-1.33802e+06 * pmax(0, Depth-1645.87)*pmax(0, Perm+12.8093)*Thick*Thick+811040       * pmax(0, 1645.87-Depth)*pmax(0, Perm+12.8093)*Thick*Thick-1.60186e+14 * GeoGrad*pmax(0, Perm+12.8257)*Thick                               \
    -1.40923e+11 * GeoGrad*pmax(0, 2725.2-Depth)+1.10282e+09  * pmax(0, Perm+12.8243)*pmax(0, 5296.14-Depth)*Thick+1.31135e+07  * pmax(0, -12.8243-Perm)*pmax(0, 5296.14-Depth)*Thick+1.55661e+11  * pmax(0, Perm+12.0344)*pmax(0, 0.438167-Poro)*Thick*Thick                                 \
    +1.88194e+09  * pmax(0, -12.0344-Perm)*pmax(0, 0.438167-Poro)*Thick*Thick-1.16514e+10 * Thick*GeoGrad*pmax(0, Perm+12.419)*pmax(0, Depth-2725.2)+2.8332e+08   * Thick*pmax(0, Perm+12.419)*pmax(0, Depth-2725.2)+6.61002e+10  * pmax(0, Depth-3107.81)*GeoGrad*pmax(0, Perm+12.8257)*Thick                                  \
    -6.78516e+10 * pmax(0, 3107.81-Depth)*GeoGrad*pmax(0, Perm+12.8257)*Thick-2.06802e+09 * pmax(0, Perm+12.0703)*pmax(0, 0.438167-Poro)*pmax(0, 5296.14-Depth)*Thick-6.04866e+07 * pmax(0, -12.0703-Perm)*pmax(0, 0.438167-Poro)*pmax(0, 5296.14-Depth)*Thick+1.23098e+13  * pmax(0, Poro-0.28121)*GeoGrad*pmax(0, Perm+12.8257)*Thick                                  \
    -2.01628e+13 * pmax(0, 0.28121-Poro)*GeoGrad*pmax(0, Perm+12.8257)*Thick+647.986      * pmax(0, Depth-2916.18)*Thick*Thick*Thick-1484.64     * pmax(0, 2916.18-Depth)*Thick*Thick*Thick+2.59347e+14  * pmax(0, -12.3629-Perm)*pmax(0, 0.0272482-GeoGrad)                                     \
    -1.27179e+07 * pmax(0, Perm+12.3781)*Thick*Thick*Thick-2.8919e+16  * pmax(0, Perm+12.0805)*pmax(0, -12.0659-Perm)+2.22649e+12  * pmax(0, -12.0805-Perm)*pmax(0, -12.0659-Perm)-5.99473e+11 * Depth*Thick*pmax(0, -12.055-Perm)*pmax(0, Perm+12.0659)                                  \
    +1.71301e+07  * Thick*pmax(0, Depth-5322.61)*pmax(0, Perm+12.8257)*Thick-1.08582e+07 * pmax(0, 0.330819-Poro)*Thick*Thick*Thick-1.86336e+10 * pmax(0, Depth-2708.76)*pmax(0, GeoGrad-0.0272482)+9.62049e+10  * pmax(0, 2708.76-Depth)*pmax(0, GeoGrad-0.0272482)                                      \
    +5.91975e+12  * pmax(0, GeoGrad-0.0297014)*Thick-7.53443e+12 * pmax(0, 0.0297014-GeoGrad)*Thick+4.17565e+08  * Thick*pmax(0, GeoGrad-0.0212618)*Thick*Thick-4.93712e+13 * pmax(0, GeoGrad-0.0270761)*pmax(0, -12.0805-Perm)*pmax(0, -12.0659-Perm)                                \
    -3.95297e+08 * pmax(0, Perm+11.9856)*Thick*Thick*Thick-1.0593e+07  * pmax(0, -11.9856-Perm)*Thick*Thick*Thick+1.36139e+08  * pmax(0, Perm+12.2529)*pmax(0, Perm+12.8243)*pmax(0, 5296.14-Depth)*Thick-5.07461e+07 * pmax(0, -12.2529-Perm)*pmax(0, Perm+12.8243)*pmax(0, 5296.14-Depth)*Thick-7.64963e+10 * pmax(0, Perm+12.5788)*pmax(0, Perm+12.8257)*Thick-1.91282e+11 * pmax(0, -12.5788-Perm)*pmax(0, Perm+12.8257)*Thick                                    \
    +1.4929e+08   * pmax(0, Perm+12.879)*pmax(0, 0.438167-Poro)*pmax(0, 5296.14-Depth)*Thick-2.83379e+15 * pmax(0, Perm+12.1652)*pmax(0, 0.438167-Poro)*pmax(0, -12.0659-Perm)-7.56539e+15 * pmax(0, Perm+12.0341)*pmax(0, Perm+12.3629)*pmax(0, 0.0272482-GeoGrad)                                 \
    -1.02406e+09 * GeoGrad*pmax(0, 5296.14-Depth)*Thick+1.33751e+09  * pmax(0, GeoGrad-0.0234193)*pmax(0, 0.438167-Poro)*pmax(0, 5296.14-Depth)*Thick-3.54163e+09 * pmax(0, 0.0234193-GeoGrad)*pmax(0, 0.438167-Poro)*pmax(0, 5296.14-Depth)*Thick                             \
    -7.53012e+10 * pmax(0, 5324.93-Depth)*pmax(0, Depth-5322.61)*pmax(0, Perm+12.8257)*Thick-7.87274e+12 * pmax(0, Perm+12.1996)*GeoGrad*pmax(0, Perm+12.8257)*Thick+2.33736e+12  * pmax(0, -12.1996-Perm)*GeoGrad*pmax(0, Perm+12.8257)*Thick                                          \
    +543084       * Thick*pmax(0, 0.438167-Poro)*pmax(0, 5296.14-Depth)*Thick+2.25187e+10  * pmax(0, Perm+12.6735)*pmax(0, 0.438909-Poro)*pmax(0, Depth-2725.2)-7.66567e+09 * pmax(0, -12.6735-Perm)*pmax(0, 0.438909-Poro)*pmax(0, Depth-2725.2)                         \
    -1.2012e+14  * pmax(0, Perm+12.6849)*pmax(0, -12.6735-Perm)*pmax(0, 0.438909-Poro)*pmax(0, Depth-2725.2)+1.33965e+11  * GeoGrad*pmax(0, -12.6735-Perm)*pmax(0, 0.438909-Poro)*pmax(0, Depth-2725.2)-7.40788e+09 * pmax(0, Perm+12.6849)*pmax(0, Depth-2725.2)                                                 \
    +1.51598e+11  * GeoGrad*pmax(0, Perm+12.6849)*pmax(0, Depth-2725.2)-2.39738e+12 * pmax(0, Poro-0.438909)*pmax(0, Perm+12.8093)*Thick*Thick-2.44595e+09 * pmax(0, 0.438909-Poro)*pmax(0, Perm+12.8093)*Thick*Thick-1.20497e+08 * pmax(0, Poro-0.195607)*pmax(0, 0.438167-Poro)*pmax(0, 5296.14-Depth)*Thick                              \
    -1.1514e+08  * pmax(0, Depth-2127.56)*pmax(0, GeoGrad-0.0212618)*Thick*Thick+1.09388e+08  * pmax(0, 2127.56-Depth)*pmax(0, GeoGrad-0.0212618)*Thick*Thick                                
    ROM_7_MCO2_45yr = ROM_7_MCO2_45yr / 1000000000 / 30       
    return ROM_7_MCO2_45yr 
#################################################################################### 
# 50 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_MCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_MCO2_50yr =+4.35749e+09  +2.55223e+07  * pmax(0, Thick-90)-1.3172e+08  * pmax(0, 90-Thick)+3.93884e+06  * pmax(0, Depth-1105.76)-5.848e+06   * pmax(0, 1105.76-Depth)                                      \
    +8.22734e+09  * pmax(0, Perm+14.9223)-7.80832e+09 * pmax(0, -14.9223-Perm)+3.66752e+06  * Thick*pmax(0, 90-Thick)+23542        * GeoGrad*pmax(0, Depth-1108.25)*Thick*pmax(0, 90-Thick)                       \
    +1.32579e+07  * pmax(0, Perm+13.9701)*Thick*pmax(0, 90-Thick)-4.94035e+06 * pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)                         \
    +11297.2      * pmax(0, Perm+14.5972)*pmax(0, Depth-1108.25)*Thick*pmax(0, 90-Thick)-7589.84     * pmax(0, -14.5972-Perm)*pmax(0, Depth-1108.25)*Thick*pmax(0, 90-Thick)           \
    +1.47512e+10  * pmax(0, GeoGrad-0.039297)-2.96031e+10 * pmax(0, 0.039297-GeoGrad)-5.17706e+06 * pmax(0, Perm+14.6242)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)           \
    +3.76898e+06  * pmax(0, -14.6242-Perm)*pmax(0, -13.9701-Perm)*Thick*pmax(0, 90-Thick)-43364.7     * pmax(0, Depth-1655.41)*pmax(0, 90-Thick)                             \
    +46564.5      * pmax(0, 1655.41-Depth)*pmax(0, 90-Thick)-6.04007e+07 * pmax(0, Perm+14.1759)*pmax(0, 90-Thick)                             \
    +9.87755e+07  * pmax(0, -14.1759-Perm)*pmax(0, 90-Thick)-4.63507e+08 * GeoGrad*pmax(0, -14.1759-Perm)*pmax(0, 90-Thick)                         \
    +538135       * pmax(0, Depth-1575.51)*pmax(0, Perm+14.9223)-978176      * pmax(0, 1575.51-Depth)*pmax(0, Perm+14.9223)                        \
    +4.35322e+06  * pmax(0, GeoGrad-0.0254405)*Thick*pmax(0, 90-Thick)-1.05765e+07 * pmax(0, 0.0254405-GeoGrad)*Thick*pmax(0, 90-Thick)                        \
    +0.0630347    * pmax(0, Depth-3355.27)*pmax(0, Depth-1108.25)*Thick*pmax(0, 90-Thick)-0.149865    * pmax(0, 3355.27-Depth)*pmax(0, Depth-1108.25)*Thick*pmax(0, 90-Thick)                      \
    +4796.75      * pmax(0, -14.362-Perm)*pmax(0, Depth-1108.25)*Thick*pmax(0, 90-Thick)            
    ROM_1_MCO2_50yr = ROM_1_MCO2_50yr / 1000000000 / 30       
    return ROM_1_MCO2_50yr 
#############
# ROM: 0.05-0.5
#############
def ROM_2_MCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_2_MCO2_50yr =+1.1008e+12 +7.46492e+10  * Perm+7.22676e+11  * Thick+2.01252e+07  * pmax(0, Depth-3381.79)*Thick-1.04793e+08 * pmax(0, 3381.79-Depth)*Thick+5.15239e+10  * Thick*Perm                                                   \
    +1.39875e+06  * pmax(0, Depth-3381.79)*Thick*Perm-7.45333e+06 * pmax(0, 3381.79-Depth)*Thick*Perm-1.79911e+09 * pmax(0, GeoGrad-0.037294)*Perm                                       \
    -2.59704e+09 * pmax(0, 0.037294-GeoGrad)*Perm+4.9589e+09   * pmax(0, Perm+14.7285)*Perm-4.84764e+09 * pmax(0, -14.7285-Perm)*Perm                                       \
    -223490      * pmax(0, Depth-3774.14)*pmax(0, Perm+14.7285)*Perm+145721       * pmax(0, 3774.14-Depth)*pmax(0, Perm+14.7285)*Perm                          \
    +3.25968e+09  * pmax(0, Perm+13.9893)*Thick*Perm-3.21306e+09 * pmax(0, -13.9893-Perm)*Thick*Perm-361165      * pmax(0, Perm+13.9561)*pmax(0, 3381.79-Depth)*Thick*Perm                       \
    +390953       * pmax(0, -13.9561-Perm)*pmax(0, 3381.79-Depth)*Thick*Perm+2.3463e+06   * pmax(0, Depth-1423.6)*pmax(0, 0.037294-GeoGrad)*Perm                          \
    -8.82689e+06 * pmax(0, 1423.6-Depth)*pmax(0, 0.037294-GeoGrad)*Perm+112299       * Thick*pmax(0, Depth-1423.6)*pmax(0, 0.037294-GeoGrad)*Perm                       \
    +1.37189e+10  * pmax(0, Perm+14.4494)*pmax(0, 0.037294-GeoGrad)*Perm-22.4891     * pmax(0, Depth-1490.66)*pmax(0, 3381.79-Depth)*Thick                          \
    +85.3068      * pmax(0, 1490.66-Depth)*pmax(0, 3381.79-Depth)*Thick-1.28488e+08 * pmax(0, Perm+14.9208)*pmax(0, -13.9893-Perm)*Thick*Perm                      \
    +1.40485e+08  * pmax(0, -14.9208-Perm)*pmax(0, -13.9893-Perm)*Thick*Perm+1.2652e+11   * pmax(0, GeoGrad-0.0258384)*Thick                                      \
    -2.92513e+11 * pmax(0, 0.0258384-GeoGrad)*Thick-64048.2     * pmax(0, Depth-1461.17)*pmax(0, -13.9893-Perm)*Thick*Perm                      \
    +76393.5      * pmax(0, 1461.17-Depth)*pmax(0, -13.9893-Perm)*Thick*Perm+8.35581e+09  * pmax(0, GeoGrad-0.0258384)*Thick*Perm                                   \
    -1.94714e+10 * pmax(0, 0.0258384-GeoGrad)*Thick*Perm-5.07364e+06 * pmax(0, Depth-2105.99)*pmax(0, -14.4494-Perm)*pmax(0, 0.037294-GeoGrad)*Perm          \
    +2.50012e+07  * pmax(0, 2105.99-Depth)*pmax(0, -14.4494-Perm)*pmax(0, 0.037294-GeoGrad)*Perm-2.89515e+07 * pmax(0, GeoGrad-0.0247837)*pmax(0, 3381.79-Depth)*Thick                        \
    +9.53778e+07  * pmax(0, 0.0247837-GeoGrad)*pmax(0, 3381.79-Depth)*Thick-1.87171e+06 * pmax(0, GeoGrad-0.0247837)*pmax(0, 3381.79-Depth)*Thick*Perm                     \
    +6.31172e+06  * pmax(0, 0.0247837-GeoGrad)*pmax(0, 3381.79-Depth)*Thick*Perm                     
    ROM_2_MCO2_50yr = ROM_2_MCO2_50yr / 1000000000 / 30       
    return ROM_2_MCO2_50yr 
#############
# ROM: 0.1-1
#############
def ROM_3_MCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_3_MCO2_50yr =+5.13982e+09  +2.84674e+10  * pmax(0, Perm+13.4721)-6.39241e+09 * pmax(0, -13.4721-Perm)+6.80466e+08  * Thick+1.29703e+06  * pmax(0, Depth-2676.4)-2.06707e+06 * pmax(0, 2676.4-Depth)                                            \
    -8.91873e+06 * Thick*Thick+92702.9      * Thick*Thick*Thick+1.26104e+10  * pmax(0, GeoGrad-0.0282262)-1.77374e+11 * pmax(0, 0.0282262-GeoGrad)-351.706     * Thick*Thick*Thick*Thick                                             \
    +356687       * pmax(0, Depth-1330.3)*Thick-286142      * pmax(0, 1330.3-Depth)*Thick+946615       * pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick                           \
    -172139      * pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick+4.4796e+08   * pmax(0, Perm+14.0893)*Thick-5.34245e+08 * pmax(0, -14.0893-Perm)*Thick                                       \
    +3.47508e+06  * pmax(0, Perm+13.8985)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick-1.97824e+06 * pmax(0, -13.8985-Perm)*pmax(0, Perm+14.2866)*pmax(0, Depth-1330.3)*Thick                     \
    +367754       * pmax(0, -14.3667-Perm)*pmax(0, -14.2866-Perm)*pmax(0, Depth-1330.3)*Thick+4.03706e+06  * pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick                         \
    -3.59552e+06 * pmax(0, 0.0189446-GeoGrad)*pmax(0, Depth-1330.3)*Thick+2.60286e+07  * pmax(0, Perm+14.4167)*pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick           \
    -5.51966e+06 * pmax(0, -14.4167-Perm)*pmax(0, GeoGrad-0.0189446)*pmax(0, Depth-1330.3)*Thick-1.52578e+06 * pmax(0, 1350.12-Depth)*pmax(0, Perm+14.0893)*Thick                          \
    +1.62732e+09  * pmax(0, Perm+13.9302)*pmax(0, Perm+14.0893)*Thick+1.7376e+09   * pmax(0, -13.9302-Perm)*pmax(0, Perm+14.0893)*Thick                         \
    -2.81675e+08 * pmax(0, Perm+14.9364)*pmax(0, -14.0893-Perm)*Thick+7.26535e+07  * pmax(0, -14.9364-Perm)*pmax(0, -14.0893-Perm)*Thick                        \
    +1.92421e+10  * GeoGrad*pmax(0, Perm+14.0893)*Thick+22.2035      * pmax(0, Depth-3374.59)*pmax(0, Depth-1330.3)*Thick                           \
    -70.692      * pmax(0, 3374.59-Depth)*pmax(0, Depth-1330.3)*Thick-451996      * pmax(0, Depth-2254.8)*pmax(0, -14.0893-Perm)*Thick                          \
    +289116       * pmax(0, 2254.8-Depth)*pmax(0, -14.0893-Perm)*Thick+21916.9      * pmax(0, Poro-0.116608)*pmax(0, Depth-1330.3)*Thick                          \
    -63542.9     * pmax(0, 0.116608-Poro)*pmax(0, Depth-1330.3)*Thick                          
    ROM_3_MCO2_50yr = ROM_3_MCO2_50yr / 1000000000 / 30       
    return ROM_3_MCO2_50yr 
#############
# ROM: 0.5-5
#############
def ROM_4_MCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_4_MCO2_50yr =-2.05829e+10  +7.26614e+10  * pmax(0, Perm+13.9792)+7.74723e+10  * pmax(0, -13.9792-Perm)+1.22712e+10  * Thick-4.20616e+06 * pmax(0, Depth-2532.72)+7.58988e+07  * pmax(0, 2532.72-Depth)                                            \
    -8.07833e+07 * Thick*Thick+471358       * Thick*Thick*Thick+3.60632e+11  * pmax(0, GeoGrad-0.0258979)-6.68931e+11 * pmax(0, 0.0258979-GeoGrad)-579.07      * Thick*Thick*Thick*Thick                                              \
    +5.00511e+10  * pmax(0, Perm+12.9758)*Thick-7.72863e+09 * pmax(0, -12.9758-Perm)*Thick+1.73484e+07  * pmax(0, Perm+14.644)*pmax(0, Depth-2532.72)+824220       * Thick*pmax(0, Perm+14.644)*pmax(0, Depth-2532.72)                            \
    +5.17871e+06  * pmax(0, Perm+13.6228)*Thick*pmax(0, Perm+14.644)*pmax(0, Depth-2532.72)-1.46579e+06 * pmax(0, -13.6228-Perm)*Thick*pmax(0, Perm+14.644)*pmax(0, Depth-2532.72)             \
    -3.28048e+08 * pmax(0, Perm+12.9598)*Thick*Thick+5.45713e+07  * pmax(0, -12.9598-Perm)*Thick*Thick-2.8013e+07  * pmax(0, 0.0364025-GeoGrad)*Thick*pmax(0, Perm+14.644)*pmax(0, Depth-2532.72)                    
    -262056      * pmax(0, -12.9497-Perm)*Thick*Thick*Thick+1.33047e+08  * pmax(0, Perm+13.421)*pmax(0, 2532.72-Depth)-1.29866e+08 * pmax(0, -13.421-Perm)*pmax(0, 2532.72-Depth)+1.55458e+06  * pmax(0, Depth-2647.75)*Thick                                         \
    -2.80378e+06 * pmax(0, 2647.75-Depth)*Thick-2.82199e+09 * pmax(0, Perm+14.2872)*pmax(0, -12.9758-Perm)*Thick+2.21629e+09  * pmax(0, -14.2872-Perm)*pmax(0, -12.9758-Perm)*Thick-1.62786e+07 * pmax(0, Perm+12.9847)*pmax(0, 2647.75-Depth)*Thick                           \
    +1.40497e+06  * pmax(0, -12.9847-Perm)*pmax(0, 2647.75-Depth)*Thick+2.39207e+10  * pmax(0, GeoGrad-0.0386215)*pmax(0, Perm+14.2872)*pmax(0, -12.9758-Perm)*Thick          \
    -3.57069e+10 * pmax(0, 0.0386215-GeoGrad)*pmax(0, Perm+14.2872)*pmax(0, -12.9758-Perm)*Thick+9.94388e+11  * pmax(0, GeoGrad-0.0247534)*pmax(0, Perm+13.9792)                            \
    -1.14196e+12 * pmax(0, 0.0247534-GeoGrad)*pmax(0, Perm+13.9792)+1.1529e+11   * pmax(0, Perm+12.5084)*pmax(0, Perm+13.9792)-4.83775e+10 * pmax(0, -12.5084-Perm)*pmax(0, Perm+13.9792)-1.90577e+07 * pmax(0, Depth-2496.86)*pmax(0, Perm+13.9792)                              \
    -1.80635e+08 * pmax(0, 2496.86-Depth)*pmax(0, Perm+13.9792)-4.16394e+10 * pmax(0, Poro-0.0713728)*pmax(0, Perm+13.9792)+7.95847e+11  * pmax(0, 0.0713728-Poro)*pmax(0, Perm+13.9792)                            \
    -327992      * pmax(0, GeoGrad-0.0234058)*pmax(0, 2480.79-Depth)*pmax(0, 2532.72-Depth)+1.86651e+06  * pmax(0, 0.0234058-GeoGrad)*pmax(0, 2480.79-Depth)*pmax(0, 2532.72-Depth)              \
    -7.89636e+10 * Thick*pmax(0, 0.0247534-GeoGrad)*pmax(0, Perm+13.9792)-737067      * pmax(0, Depth-1360.44)*pmax(0, -12.9758-Perm)*Thick+1.31191e+06  * pmax(0, 1360.44-Depth)*pmax(0, -12.9758-Perm)*Thick                          
    ROM_4_MCO2_50yr = ROM_4_MCO2_50yr / 1000000000 / 30       
    return ROM_4_MCO2_50yr 
#############
# ROM: 1-10
#############
def ROM_5_MCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_MCO2_50yr =-7.32105e+10  +1.22327e+11  * pmax(0, Perm+13.5624)-4.85175e+10 * pmax(0, -13.5624-Perm)+7.46655e+09  * Thick+1.8743e+07   * pmax(0, Depth-2669.97)                                           \
    -1.50008e+07 * pmax(0, 2669.97-Depth)-1.58997e+08 * Thick*Thick+1.61873e+06  * Thick*Thick*Thick+6.90307e+11  * pmax(0, GeoGrad-0.0275088)                                         \
    +1.70583e+12  * pmax(0, 0.0275088-GeoGrad)-6001.67     * Thick*Thick*Thick*Thick+5.89738e+09  * pmax(0, Perm+14.2664)*Thick-1.84332e+09 * pmax(0, -14.2664-Perm)*Thick                                                \
    -1.63504e+07 * pmax(0, 1519.09-Depth)*pmax(0, Perm+14.2664)*Thick+1.95237e+07  * pmax(0, Perm+13.1341)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2664)*Thick            \
    -1.18415e+07 * pmax(0, -13.1341-Perm)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2664)*Thick+2.69575e+10  * pmax(0, Perm+12.6899)*pmax(0, Perm+14.2664)*Thick                          \
    -8.34087e+09 * pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2664)*Thick+2.3635e+07   * pmax(0, GeoGrad-0.0258527)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2664)*Thick          \
    -8.14e+07    * pmax(0, 0.0258527-GeoGrad)*pmax(0, Depth-1519.09)*pmax(0, Perm+14.2664)*Thick-8.43056e+08 * pmax(0, Poro-0.187922)*pmax(0, Perm+14.2664)*Thick                         \
    +4.38868e+09  * pmax(0, 0.187922-Poro)*pmax(0, Perm+14.2664)*Thick+7.00079e+06  * pmax(0, Depth-1507.8)*pmax(0, Perm+13.5624)                              \
    -7.317e+07   * pmax(0, 1507.8-Depth)*pmax(0, Perm+13.5624)+1.33e+10     * pmax(0, GeoGrad-0.0379934)*pmax(0, Perm+14.2664)*Thick                        \
    -3.29377e+10 * pmax(0, 0.0379934-GeoGrad)*pmax(0, Perm+14.2664)*Thick-4.47321e+12 * pmax(0, Perm+13.981)*pmax(0, 0.0275088-GeoGrad)                            \
    -1.00775e+13 * pmax(0, -13.981-Perm)*pmax(0, 0.0275088-GeoGrad)+2677.83      * pmax(0, Depth-2187.86)*Thick*Thick                                     \
    +1005.18      * pmax(0, 2187.86-Depth)*Thick*Thick+1.63905e+11  * pmax(0, Perm+12.8022)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2664)*Thick           \
    +2.95257e+09  * pmax(0, -12.8022-Perm)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2664)*Thick+8.96874e+06  * pmax(0, Depth-1498.21)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2664)*Thick           \
    -1.7623e+07  * pmax(0, 1498.21-Depth)*pmax(0, -12.6899-Perm)*pmax(0, Perm+14.2664)*Thick+7.29385e+07  * pmax(0, Perm+12.1592)*pmax(0, 1519.09-Depth)*pmax(0, Perm+14.2664)*Thick            \
    +2.13933e+07  * pmax(0, -12.1592-Perm)*pmax(0, 1519.09-Depth)*pmax(0, Perm+14.2664)*Thick           
    ROM_5_MCO2_50yr = ROM_5_MCO2_50yr / 1000000000 / 30       
    return ROM_5_MCO2_50yr 
#############
# ROM: 5-50
#############
def ROM_6_MCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_6_MCO2_50yr =-2.98014e+11  +9.70972e+11  * pmax(0, Perm+12.8781)-1.07963e+12 * pmax(0, -12.8781-Perm)+4.47705e+10  * Thick+2.06716e+08  * pmax(0, Depth-2346.97)-4.62969e+08 * pmax(0, 2346.97-Depth)                                                        \
    -7.74557e+08 * Thick*Thick+7.07463e+06  * Thick*Thick*Thick-6.89801e+12 * pmax(0, 0.0337502-GeoGrad)-23867.4     * Thick*Thick*Thick*Thick                                                          \
    -2.25329e+08 * pmax(0, Perm+13.5382)*pmax(0, Depth-2346.97)+1.07045e+07  * Thick*pmax(0, Perm+13.5382)*pmax(0, Depth-2346.97)+4.80056e+11  * pmax(0, Perm+13.2394)*Thick                                                              \
    +2.69637e+08  * pmax(0, Depth-1956.33)*pmax(0, Perm+13.2394)*Thick-2.66465e+08 * pmax(0, 1956.33-Depth)*pmax(0, Perm+13.2394)*Thick-7.08498e+13 * pmax(0, Poro-0.131008)*pmax(0, 0.0337502-GeoGrad)                                       \
    -3.23782e+14 * pmax(0, 0.131008-Poro)*pmax(0, 0.0337502-GeoGrad)+6.97828e+10  * Perm*pmax(0, Perm+13.2394)*Thick+3.11897e+07  * pmax(0, Perm+12.6682)*pmax(0, Depth-1956.33)*pmax(0, Perm+13.2394)*Thick                                  \
    -1.3989e+09  * pmax(0, GeoGrad-0.0440471)*pmax(0, Depth-1956.33)*pmax(0, Perm+13.2394)*Thick-2.77055e+08 * pmax(0, 0.0440471-GeoGrad)*pmax(0, Depth-1956.33)*pmax(0, Perm+13.2394)*Thick                       \
    -267213      * pmax(0, Poro-0.185284)*Thick*Thick*Thick-1.50127e+06 * pmax(0, 0.185284-Poro)*Thick*Thick*Thick-1.3761e+08  * pmax(0, Perm+13.0715)*Thick*Thick                                                  \
    -1.25687e+07 * pmax(0, -13.0715-Perm)*Thick*Thick+1.98368e+07  * pmax(0, Depth-3620.65)*Perm*pmax(0, Perm+13.2394)*Thick-2.01396e+07 * pmax(0, 3620.65-Depth)*Perm*pmax(0, Perm+13.2394)*Thick                                    \
    +1.49063e+14  * pmax(0, Perm+12.4118)*pmax(0, Poro-0.131008)*pmax(0, 0.0337502-GeoGrad)+1.20009e+14  * pmax(0, -12.4118-Perm)*pmax(0, Poro-0.131008)*pmax(0, 0.0337502-GeoGrad)                        \
    +2.90833e+08  * pmax(0, Poro-0.119834)*pmax(0, Perm+13.5382)*pmax(0, Depth-2346.97)+2.4577e+10   * pmax(0, 0.119834-Poro)*pmax(0, Perm+13.5382)*pmax(0, Depth-2346.97)                           \
    -5.93882e+11 * GeoGrad*pmax(0, 0.119834-Poro)*pmax(0, Perm+13.5382)*pmax(0, Depth-2346.97)+6.48524e+12  * Thick*pmax(0, 0.131008-Poro)*pmax(0, 0.0337502-GeoGrad)                                    \
    -3.27228e+11 * pmax(0, Poro-0.152761)+1.44548e+12  * pmax(0, 0.152761-Poro)+2.11005e+14  * pmax(0, 0.249936-Poro)*pmax(0, GeoGrad-0.0337502)                                       \
    -9.16488e+13 * Thick*pmax(0, 0.249936-Poro)*pmax(0, GeoGrad-0.0337502)-6.88291e+12 * Perm*Thick*pmax(0, 0.249936-Poro)*pmax(0, GeoGrad-0.0337502)                                 \
    -1.51608e+09 * Depth*Thick*pmax(0, 0.249936-Poro)*pmax(0, GeoGrad-0.0337502)+1.10492e+11  * pmax(0, GeoGrad-0.0233844)*Thick-2.0501e+11  * pmax(0, 0.0233844-GeoGrad)*Thick                                                            \
    -2.85763e+08 * pmax(0, 0.119834-Poro)*pmax(0, Depth-1956.33)*pmax(0, Perm+13.2394)*Thick-4.54423e+06 * pmax(0, Poro-0.105996)*Thick*pmax(0, Perm+13.5382)*pmax(0, Depth-2346.97)                        \
    -3.66936e+08 * pmax(0, 0.105996-Poro)*Thick*pmax(0, Perm+13.5382)*pmax(0, Depth-2346.97)-1.46024e+10 * pmax(0, Depth-2731.04)*pmax(0, -12.4118-Perm)*pmax(0, Poro-0.131008)*pmax(0, 0.0337502-GeoGrad)          
    +7.00556e+10  * pmax(0, 2731.04-Depth)*pmax(0, -12.4118-Perm)*pmax(0, Poro-0.131008)*pmax(0, 0.0337502-GeoGrad)          
    ROM_6_MCO2_50yr = ROM_6_MCO2_50yr / 1000000000 / 30       
    return ROM_6_MCO2_50yr 
###########
# ROM: 10-max
###########
def ROM_7_MCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_7_MCO2_50yr =-3.31617e+11  +1.47999e+13  * pmax(0, Perm+12.1326)+4.41488e+12  * pmax(0, -12.1326-Perm)-5.8593e+09  * pmax(0, Depth-2725.2)+2.62462e+09  * pmax(0, 2725.2-Depth)+2.97332e+11  * Thick+4.7251e+09   * Thick*Thick-1.21075e+10 * pmax(0, Perm+12.4869)*pmax(0, Depth-2725.2)-1.43683e+10 * pmax(0, -12.4869-Perm)*pmax(0, Depth-2725.2)                                           \
    +1.43417e+12  * GeoGrad*pmax(0, Perm+12.4869)*pmax(0, Depth-2725.2)-1.98043e+10 * Thick*GeoGrad*pmax(0, Perm+12.4869)*pmax(0, Depth-2725.2)+4.74105e+08  * Thick*pmax(0, Perm+12.4869)*pmax(0, Depth-2725.2)-1.56884e+06 * Thick*Thick*pmax(0, Perm+12.4869)*pmax(0, Depth-2725.2)+6.37731e+08  * Poro*Thick*pmax(0, Perm+12.4869)*pmax(0, Depth-2725.2)                                      \
    -4.19665e+08 * pmax(0, Perm+12.419)*Thick*pmax(0, Perm+12.4869)*pmax(0, Depth-2725.2)-3.3101e+09  * pmax(0, -12.419-Perm)*Thick*pmax(0, Perm+12.4869)*pmax(0, Depth-2725.2)-4.47734e+07 * Thick*Thick*Thick-1.88786e+08 * Depth*GeoGrad*pmax(0, Perm+12.4869)*pmax(0, Depth-2725.2)+4.73437e+12  * pmax(0, GeoGrad-0.0222154)*Thick-1.11234e+13 * pmax(0, 0.0222154-GeoGrad)*Thick                                                    \
    +4.08589e+12  * pmax(0, Perm+12.7975)*pmax(0, GeoGrad-0.0222154)*Thick+3.38584e+12  * pmax(0, -12.7975-Perm)*pmax(0, GeoGrad-0.0222154)*Thick-3.51623e+10 * GeoGrad*pmax(0, 2725.2-Depth)-1.03056e+11 * pmax(0, GeoGrad-0.0218154)*Thick*Thick+4.77727e+11  * pmax(0, 0.0218154-GeoGrad)*Thick*Thick+1.22197e+13  * Poro*pmax(0, GeoGrad-0.0222154)*Thick-5.55043e+09 * pmax(0, Depth-1289.78)*pmax(0, Perm+12.7975)*pmax(0, GeoGrad-0.0222154)*Thick                                  \
    -2.11665e+13 * pmax(0, -12.3766-Perm)*Poro*pmax(0, GeoGrad-0.0222154)*Thick+3.64271e+12  * pmax(0, -12.7866-Perm)*pmax(0, -12.1326-Perm)-1.85353e+11 * Poro*GeoGrad*pmax(0, 2725.2-Depth)-4.14059e+10 * pmax(0, Perm+12.3766)*pmax(0, GeoGrad-0.0218154)*Thick*Thick-5.03073e+06 * pmax(0, Depth-2783.95)*pmax(0, GeoGrad-0.0218154)*Thick*Thick+1.06142e+07  * pmax(0, 2783.95-Depth)*pmax(0, GeoGrad-0.0218154)*Thick*Thick                                   \
    +1.49804e+09  * pmax(0, Depth-1289.16)*Poro*pmax(0, GeoGrad-0.0222154)*Thick-5.83521e+06 * pmax(0, 0.19125-Poro)*Thick*Thick*Thick-2.05493e+12 * Poro*pmax(0, -12.1326-Perm)-1.00516e+14 * pmax(0, GeoGrad-0.0234601)*Poro*pmax(0, GeoGrad-0.0222154)*Thick                                 \
    +5.21163e+16  * pmax(0, 0.0234601-GeoGrad)*Poro*pmax(0, GeoGrad-0.0222154)*Thick+7.54179e+09  * pmax(0, Depth-3762.41)*pmax(0, Perm+12.7866)*pmax(0, -12.1326-Perm)-2.3417e+09  * pmax(0, 3762.41-Depth)*pmax(0, Perm+12.7866)*pmax(0, -12.1326-Perm)-2.78861e+07 * pmax(0, -12.27-Perm)*Thick*Thick*Thick+1.32947e+10  * pmax(0, Depth-2707.8)*pmax(0, -12.1326-Perm)+1.31455e+09  * pmax(0, 2707.8-Depth)*pmax(0, -12.1326-Perm)-1.91381e+09 * pmax(0, Depth-4954.5)*pmax(0, 4990.65-Depth)*Thick                                         \
    -3733.11     * pmax(0, 4954.5-Depth)*pmax(0, 4990.65-Depth)*Thick-1.44162e+08 * Perm*pmax(0, Depth-4954.5)*pmax(0, 4990.65-Depth)*Thick-1.35432e+14 * pmax(0, GeoGrad-0.0227806)*pmax(0, -12.1326-Perm)+2.70618e+14  * pmax(0, 0.0227806-GeoGrad)*pmax(0, -12.1326-Perm)                                        \
    -6.67302e+10 * pmax(0, Perm+12.8074)*pmax(0, GeoGrad-0.0218154)*Thick*Thick+2.60024e+10  * Perm*pmax(0, 0.0218154-GeoGrad)*Thick*Thick+2.8936e+06   * Depth*pmax(0, Perm+12.4869)*pmax(0, Depth-2725.2)-2.41438e+15 * pmax(0, Perm+12.4204)*pmax(0, GeoGrad-0.0227806)*pmax(0, -12.1326-Perm)                          \
    +1.23185e+14  * pmax(0, -12.4204-Perm)*pmax(0, GeoGrad-0.0227806)*pmax(0, -12.1326-Perm)-4.54375e+11 * pmax(0, -12.1981-Perm)*Thick+1.27538e+10  * pmax(0, Perm+12.2237)*Thick*Thick+5.90774e+09  * pmax(0, -12.2237-Perm)*Thick*Thick                                                  \
    +5.23819e+08  * GeoGrad*Thick*Thick*Thick+7.68284e+09  * Poro*pmax(0, Perm+12.2237)*Thick*Thick-1.97381e+16 * Depth*pmax(0, Perm+12.0816)*pmax(0, -12.0794-Perm)*pmax(0, Perm+12.1326)-1.84977e+15 * pmax(0, Perm+12.0445)*pmax(0, Perm+12.0794)*pmax(0, Perm+12.1326)                                      \
    -3.02369e+13 * pmax(0, Poro-0.276546)*pmax(0, Perm+12.7866)*pmax(0, -12.1326-Perm)-4.08746e+13 * pmax(0, 0.276546-Poro)*pmax(0, Perm+12.7866)*pmax(0, -12.1326-Perm)-1.51341e+06 * Depth*Thick*Thick+6980.89      * pmax(0, Depth-1147.98)*Thick*Thick*Thick                                                \
    -6733.25     * pmax(0, 1147.98-Depth)*Thick*Thick*Thick-2.44825e+13 * Depth*pmax(0, -12.0445-Perm)*pmax(0, Perm+12.0794)*pmax(0, Perm+12.1326)+9.58106e+12  * pmax(0, Perm+11.9856)*Poro*GeoGrad*pmax(0, 2725.2-Depth)+2.74842e+11  * pmax(0, -11.9856-Perm)*Poro*GeoGrad*pmax(0, 2725.2-Depth)+1.49727e+13  * pmax(0, -12.834-Perm)*Poro*pmax(0, GeoGrad-0.0222154)*Thick+117095       * Thick*Thick*Thick*Thick                                                                  \
    -2.03326e+16 * pmax(0, Perm+12.5449)*pmax(0, -12.4204-Perm)*pmax(0, GeoGrad-0.0227806)*pmax(0, -12.1326-Perm)-9.17086e+13 * pmax(0, -12.5449-Perm)*pmax(0, -12.4204-Perm)*pmax(0, GeoGrad-0.0227806)*pmax(0, -12.1326-Perm)          \
    -1.51075e+09 * Thick*Poro*GeoGrad*pmax(0, 2725.2-Depth)-281181      * pmax(0, Perm+12.5412)*Depth*Thick*Thick+67983.5      * pmax(0, -12.5412-Perm)*Depth*Thick*Thick-3.31858e+11 * pmax(0, Perm+12.2186)*pmax(0, Perm+12.2237)*Thick*Thick+6.04956e+13  * pmax(0, -12.2186-Perm)*pmax(0, Perm+12.2237)*Thick*Thick                                    
    +8.47776e+11  * pmax(0, Perm+12.2509)*pmax(0, -12.2237-Perm)*Thick*Thick+3.29598e+11  * pmax(0, Perm+12.178)*pmax(0, Perm+12.2237)*Thick*Thick+1.02971e+08  * pmax(0, Depth-4462.75)*Thick-9.02208e+07 * pmax(0, 4462.75-Depth)*Thick  
    ROM_7_MCO2_50yr = ROM_7_MCO2_50yr / 1000000000 / 30       
    return ROM_7_MCO2_50yr



#################################################################################### 
# 5 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogMCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_1_LogMCO2_5yr =+7.82853   +0.0164325    * Thick\
    +1.30783e-05  * pmax(0, Depth-1826.12)*Thick\
    -1.48054e-06 * pmax(0, 1826.12-Depth)*Thick\
    +0.949251     * pmax(0, Perm+14.5911)                         \
    -0.940121    * pmax(0, -14.5911-Perm)                        \
    +11.1451      * pmax(0, GeoGrad-0.0194368)                       \
    -8.45012     * pmax(0, 0.0194368-GeoGrad)                       \
    +0.000196065  * pmax(0, Depth-1967.7)                          \
    -0.000450332 * pmax(0, 1967.7-Depth)                          \
    -8.70216e-05 * pmax(0, Thick-90)*Thick                           \
    +0.000664518  * pmax(0, 90-Thick)*Thick                           \
    -1.53556e-05 * Thick*pmax(0, 90-Thick)*Thick                        \
    +1.21297e-07  * Thick*Thick*pmax(0, 90-Thick)*Thick                     \
    -2.30041e-08 * pmax(0, Depth-2465.71)*pmax(0, Depth-1967.7)            
    -3.86827e-07 * pmax(0, 2465.71-Depth)*pmax(0, Depth-1967.7)            \
    -7.54409e-09 * pmax(0, Depth-1754.41)*Thick*pmax(0, 90-Thick)*Thick                    \
    -123.11      * GeoGrad*pmax(0, GeoGrad-0.0194368)                  
    ROM_1_LogMCO2_5yr =     10 ** ROM_1_LogMCO2_5yr / 1000000000 / 30    
    return ROM_1_LogMCO2_5yr
 
#############
# ROM: 0.05-0.5
#############
def ROM_2_LogMCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_2_LogMCO2_5yr =+21.8311   +0.934171     * Perm                                        \
    +0.0643157    * Thick                                        \
    -2.32445e-05 * pmax(0, Depth-2522.5)*Perm                           \
    +2.84494e-05  * pmax(0, 2522.5-Depth)*Perm                           \
    -0.00141545  * Thick*Thick                                     \
    +1.47603e-05  * Thick*Thick*Thick                                  \
    -0.249689    * pmax(0, GeoGrad-0.0328986)*Perm                        \
    +0.606168     * pmax(0, 0.0328986-GeoGrad)*Perm                        \
    -5.5644e-08  * Thick*Thick*Thick*Thick                               \
    -6.92517e-05 * pmax(0, Depth-1472.61)                             \
    -0.000161566 * pmax(0, 1472.61-Depth)                             \
    -2.87019e-08 * pmax(0, Depth-2625.36)*pmax(0, Depth-1472.61)               \
    +5.87595e-08  * pmax(0, 2625.36-Depth)*pmax(0, Depth-1472.61)                         \
    -0.000148703 * pmax(0, 2250.43-Depth)*pmax(0, 0.0328986-GeoGrad)*Perm         
    ROM_2_LogMCO2_5yr = 10 ** ROM_2_LogMCO2_5yr / 1000000000 / 30          
    return ROM_2_LogMCO2_5yr 
#############
# ROM: 0.1-1
#############
def ROM_3_LogMCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_3_LogMCO2_5yr =+7.81   +0.895162     * pmax(0, Perm+14.9896)                          \
    -1.06544     * pmax(0, -14.9896-Perm)                         \
    +0.0628807    * Thick                                     \
    +0.000313063  * pmax(0, Depth-2676.4)                      \
    -0.000325879 * pmax(0, 2676.4-Depth)                        \
    -0.00134848  * Thick*Thick                                  \
    +1.37662e-05  * Thick*Thick*Thick                            \
    +3.40228      * pmax(0, GeoGrad-0.0334528)                    \
    -9.08845     * pmax(0, 0.0334528-GeoGrad)                      \
    -5.10158e-08 * Thick*Thick*Thick*Thick                          \
    +6.14257e-08  * pmax(0, Depth-1738.98)*pmax(0, 2676.4-Depth)     \
    -1.24641e-07 * pmax(0, 1738.98-Depth)*pmax(0, 2676.4-Depth)       \
    +2.21187e-05  * pmax(0, 4625.53-Depth)*pmax(0, Perm+14.9896)       \
    -2.74778e-08 * Depth*pmax(0, Depth-2676.4)                        \
    +0.000301745  * pmax(0, Depth-2250.43)*pmax(0, 0.0334528-GeoGrad)  \
    +0.00262714   * pmax(0, 2250.43-Depth)*pmax(0, 0.0334528-GeoGrad)          
    ROM_3_LogMCO2_5yr = 10 ** ROM_3_LogMCO2_5yr / 1000000000 / 30           
    return ROM_3_LogMCO2_5yr
#############
# ROM: 0.5-5
#############
def ROM_4_LogMCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_4_LogMCO2_5yr =+8.43924  +0.942688     * pmax(0, Perm+14.1939)\
    -0.941916    * pmax(0, -14.1939-Perm)\
    +0.0616616    * Thick                 \
    +0.000219819  * pmax(0, Depth-2383.1)  \
    -0.000294396 * pmax(0, 2383.1-Depth)    \
    -0.0012823   * Thick*Thick               \
    +4.73584      * pmax(0, GeoGrad-0.025134) \
    -10.5219     * pmax(0, 0.025134-GeoGrad)   \
    +1.27588e-05  * Thick*Thick*Thick           \
    -4.63078e-08 * Thick*Thick*Thick*Thick       \
    -2.33722e-08 * pmax(0, Depth-3027.11)*pmax(0, Depth-2383.1)  \
    -1.14414e-07 * pmax(0, 1851.31-Depth)*pmax(0, 2383.1-Depth)   \
    +7.47518e-08  * pmax(0, Depth-2839.33)*Thick                   \
    -2.9629e-07  * pmax(0, 2839.33-Depth)*Thick                    
    ROM_4_LogMCO2_5yr = 10 ** ROM_4_LogMCO2_5yr / 1000000000 / 30          
    return ROM_4_LogMCO2_5yr
#############
# ROM: 1-10
#############
def ROM_5_LogMCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogMCO2_5yr =+9.22865 +0.944175     * pmax(0, Perm+13.8238)\
    -0.93844     * pmax(0, -13.8238-Perm)                       \
    +0.000122347  * pmax(0, Depth-4489.41)                       \
    -0.000204915 * pmax(0, 4489.41-Depth)                        \
    +0.0610078    * Thick                                   \
    -0.00126571  * Thick*Thick                               \
    +3.64305      * pmax(0, GeoGrad-0.0319448)                \
    -8.4337      * pmax(0, 0.0319448-GeoGrad)                  \
    +1.25604e-05  * Thick*Thick*Thick                           \
    +3.13638e-08  * pmax(0, Depth-1804.56)*pmax(0, 4489.41-Depth)\
    -7.20916e-08 * pmax(0, 1804.56-Depth)*pmax(0, 4489.41-Depth)  \
    -4.54839e-08 * Thick*Thick*Thick*Thick                         \
    +8.53471e-08  * pmax(0, Depth-2609.14)*Thick                    \
    -3.76565e-07 * pmax(0, 2609.14-Depth)*Thick                     
    ROM_5_LogMCO2_5yr = 10 ** ROM_5_LogMCO2_5yr / 1000000000 / 30          
    return ROM_5_LogMCO2_5yr 
#############
# ROM: 5-50
#############
def ROM_6_LogMCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_6_LogMCO2_5yr =+9.79766  +0.929815     * pmax(0, Perm+13.0949)        \
    -0.924238    * pmax(0, -13.0949-Perm)                         \
    +0.000134684  * pmax(0, Depth-3147.76)                         \
    -0.000260969 * pmax(0, 3147.76-Depth)                          \
    +0.0559748    * Thick                                     \
    -0.00110902  * Thick*Thick                                 \
    +3.21037      * pmax(0, GeoGrad-0.0326175)                  \
    -9.69778     * pmax(0, 0.0326175-GeoGrad)                    \
    +1.06715e-05  * Thick*Thick*Thick                             \
    -3.77967e-08 * Thick*Thick*Thick*Thick                         \
    +4.09287e-08  * pmax(0, Depth-1764.26)*pmax(0, 3147.76-Depth)   \
    -9.53559e-08 * pmax(0, 1764.26-Depth)*pmax(0, 3147.76-Depth)     \
    -2.30576e-07 * pmax(0, Depth-4404.65)*Thick                       \
    -3.1527e-07  * pmax(0, 4404.65-Depth)*Thick                       \
    +0.000812387  * pmax(0, Depth-2968.34)*pmax(0, 0.0326175-GeoGrad)  \
    +0.0017968    * pmax(0, 2968.34-Depth)*pmax(0, 0.0326175-GeoGrad)          
    ROM_6_LogMCO2_5yr = 10 ** ROM_6_LogMCO2_5yr / 1000000000 / 30           
    return ROM_6_LogMCO2_5yr 
###########
# ROM: 10-max
###########
def ROM_7_LogMCO2_5yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_7_LogMCO2_5yr =+9.71052  +0.990605     * pmax(0, Perm+13.0468)\
    -1.01296     * pmax(0, -13.0468-Perm)                        \
    +0.000183638  * pmax(0, Depth-2597.09)                        \
    -0.000284116 * pmax(0, 2597.09-Depth)                         \
    +0.05432      * Thick -0.00101369  * Thick*Thick               \
    +3.1493       * pmax(0, GeoGrad-0.0323078)                      \
    -8.32874     * pmax(0, 0.0323078-GeoGrad)                       \
    +9.34736e-06  * Thick*Thick*Thick                              \
    -3.21168e-08 * Thick*Thick*Thick*Thick                          \
    -0.00135188  * pmax(0, Perm+13.6834)*Thick                       \
    +3.0108e-08   * pmax(0, Depth-1811.39)*pmax(0, 2597.09-Depth)     \
    -1.12683e-07 * pmax(0, 1811.39-Depth)*pmax(0, 2597.09-Depth)       \
    -2.04607e-08 * pmax(0, Depth-4154.22)*pmax(0, Depth-2597.09)        \
    +3.24291e-08  * pmax(0, 4154.22-Depth)*pmax(0, Depth-2597.09)        \
    -0.0941967   * pmax(0, Poro-0.222099)*pmax(0, Perm+13.0468)          \
    +0.40783      * pmax(0, 0.222099-Poro)*pmax(0, Perm+13.0468)                               
    ROM_7_LogMCO2_5yr = 10 ** ROM_7_LogMCO2_5yr / 1000000000 / 30           
    return ROM_7_LogMCO2_5yr        
#################################################################################### 
# 10 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogMCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogMCO2_10yr =+8.22355  +0.0156897    * Thick\
    +1.55401e-05  * pmax(0, Depth-1826.12)*Thick        \
    -6.49238e-07 * pmax(0, 1826.12-Depth)*Thick          \
    +0.948131     * pmax(0, Perm+14.5911)                 \
    -0.942048    * pmax(0, -14.5911-Perm)                  \
    +0.000205403  * pmax(0, Depth-1967.7)                   \
    -0.000576186 * pmax(0, 1967.7-Depth)                     \
    -9.00029e-05 * pmax(0, Thick-90)*Thick                    \
    +0.000648763  * pmax(0, 90-Thick)*Thick                    \
    -1.49061e-05 * Thick*pmax(0, 90-Thick)*Thick                \
    +1.17362e-07  * Thick*Thick*pmax(0, 90-Thick)*Thick          \
    -2.85713e-08 * pmax(0, Depth-2465.71)*pmax(0, Depth-1967.7)   \
    -9.14382e-09 * pmax(0, Depth-1826.12)*Thick*pmax(0, 90-Thick)*Thick\
    +1.42678e-07  * Depth*pmax(0, 1967.7-Depth)                       \
    +3.11334      * pmax(0, GeoGrad-0.0333472)                       \
    -7.21443     * pmax(0, 0.0333472-GeoGrad)                       
    ROM_1_LogMCO2_10yr = 10 ** ROM_1_LogMCO2_10yr / 1000000000 / 30           
    return ROM_1_LogMCO2_10yr     
#############
# ROM: 0.05-0.5
#############
def ROM_2_LogMCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_2_LogMCO2_10yr =+22.1564   +0.934403     * Perm           \
    +0.063898     * Thick                                        \
    -2.41111e-05 * pmax(0, Depth-2522.5)*Perm                     \
    +2.92477e-05  * pmax(0, 2522.5-Depth)*Perm                     \
    -0.00140883  * Thick*Thick                                     \
    +1.47049e-05  * Thick*Thick*Thick                                \
    -0.240459    * pmax(0, GeoGrad-0.0328986)*Perm                  \
    +0.588214     * pmax(0, 0.0328986-GeoGrad)*Perm                   \
    -5.54813e-08 * Thick*Thick*Thick*Thick                             \
    -8.50971e-05 * pmax(0, Depth-1472.61)                             \
    -0.000145811 * pmax(0, 1472.61-Depth)                             \
    -2.85747e-08 * pmax(0, Depth-2625.36)*pmax(0, Depth-1472.61)       \
    +5.83789e-08  * pmax(0, 2625.36-Depth)*pmax(0, Depth-1472.61)       \
    -0.000135278 * pmax(0, 2250.43-Depth)*pmax(0, 0.0328986-GeoGrad)*Perm         
    ROM_2_LogMCO2_10yr = 10 ** ROM_2_LogMCO2_10yr / 1000000000 / 30           
    return ROM_2_LogMCO2_10yr 
#############
# ROM: 0.1-1
#############
def ROM_3_LogMCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_3_LogMCO2_10yr =+8.11228  +0.893615     * pmax(0, Perm+14.9896)                     \
    -1.05906     * pmax(0, -14.9896-Perm)                         \
    +0.0624417    * Thick                                     \
    +0.000311528  * pmax(0, Depth-2668.3)                      \
    -0.000322623 * pmax(0, 2668.3-Depth)                        \
    -0.00134093  * Thick*Thick                                  \
    +1.36998e-05  * Thick*Thick*Thick                            \
    +3.28588      * pmax(0, GeoGrad-0.0334528)                    \
    -8.86392     * pmax(0, 0.0334528-GeoGrad)                      \
    -5.08095e-08 * Thick*Thick*Thick*Thick                          \
    +6.01265e-08  * pmax(0, Depth-1749.33)*pmax(0, 2668.3-Depth)       \
    -1.24479e-07 * pmax(0, 1749.33-Depth)*pmax(0, 2668.3-Depth)      \
    +2.32508e-05  * pmax(0, 4625.53-Depth)*pmax(0, Perm+14.9896)        \
    -2.74842e-08 * Depth*pmax(0, Depth-2668.3)                        \
    +0.000309862  * pmax(0, Depth-2250.43)*pmax(0, 0.0334528-GeoGrad)    \
    +0.00246334   * pmax(0, 2250.43-Depth)*pmax(0, 0.0334528-GeoGrad)          
    ROM_3_LogMCO2_10yr = 10 ** ROM_3_LogMCO2_10yr / 1000000000 / 30           
    return ROM_3_LogMCO2_10yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogMCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogMCO2_10yr =+8.74556 +0.950171     * pmax(0, Perm+14.1939)                        \
    -0.942844    * pmax(0, -14.1939-Perm)                       \
    +0.0610006    * Thick                                   \
    +0.000228877  * pmax(0, Depth-2383.1)                    \
    -0.000326465 * pmax(0, 2383.1-Depth)                      \
    -0.00127209  * Thick*Thick                                \
    +4.64875      * pmax(0, GeoGrad-0.025134)                      \
    -10.306      * pmax(0, 0.025134-GeoGrad)                   \
    +1.26811e-05  * Thick*Thick*Thick                           \
    -4.611e-08   * Thick*Thick*Thick*Thick                       \
    -2.50554e-08 * pmax(0, Depth-3027.11)*pmax(0, Depth-2383.1)   \
    -1.23069e-07 * pmax(0, 1858.56-Depth)*pmax(0, 2383.1-Depth)     \
    -1.36228e-05 * pmax(0, Depth-2235.32)*pmax(0, Perm+14.1939)        \
    +2.92511e-05  * pmax(0, 2235.32-Depth)*pmax(0, Perm+14.1939)        
    ROM_4_LogMCO2_10yr = 10 ** ROM_4_LogMCO2_10yr / 1000000000 / 30          
    return ROM_4_LogMCO2_10yr 
#############
# ROM: 1-10
#############
def ROM_5_LogMCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogMCO2_10yr =+9.51543  +0.955492     * pmax(0, Perm+13.8238)                        \
    -0.941314    * pmax(0, -13.8238-Perm)                       \
    +0.000120504  * pmax(0, Depth-4489.41)                       \
    -0.000202013 * pmax(0, 4489.41-Depth)                        \
    +0.0614131    * Thick -0.00127937  * Thick*Thick                                \
    +3.68262      * pmax(0, GeoGrad-0.0311951)                    \
    -8.53397     * pmax(0, 0.0311951-GeoGrad)                      \
    +1.27185e-05  * Thick*Thick*Thick                             \
    +3.05385e-08  * pmax(0, Depth-1812.22)*pmax(0, 4489.41-Depth)  \
    -7.11589e-08 * pmax(0, 1812.22-Depth)*pmax(0, 4489.41-Depth)    \
    -4.61111e-08 * Thick*Thick*Thick*Thick                          \
    +9.3197e-08   * pmax(0, Depth-2609.14)*Thick                     \
    -4.16973e-07 * pmax(0, 2609.14-Depth)*Thick                     
    ROM_5_LogMCO2_10yr = 10 ** ROM_5_LogMCO2_10yr / 1000000000 / 30           
    return ROM_5_LogMCO2_10yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogMCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogMCO2_10yr = +10.0768  +0.958928     * pmax(0, Perm+13.0923)                            \
    -0.938563    * pmax(0, -13.0923-Perm)                           \
    +0.000137809  * pmax(0, Depth-3134.51)                           \
    -0.000251668 * pmax(0, 3134.51-Depth)                            \
    +0.0573318    * Thick  -0.00114243  * Thick*Thick                 \
    +3.19258      * pmax(0, GeoGrad-0.0325252)                         \
    -8.33757     * pmax(0, 0.0325252-GeoGrad)                          \
    +1.10121e-05  * Thick*Thick*Thick                                 \
    -3.90183e-08 * Thick*Thick*Thick*Thick                             \
    +3.58769e-08  * pmax(0, Depth-1763.39)*pmax(0, 3134.51-Depth)       \
    -9.6872e-08  * pmax(0, 1763.39-Depth)*pmax(0, 3134.51-Depth)         \
    -2.20065e-07 * pmax(0, Depth-4358.92)*Thick                         \
    -3.00672e-07 * pmax(0, 4358.92-Depth)*Thick                         \
    -4.07956e-07 * pmax(0, Poro-0.136223)*pmax(0, 4358.92-Depth)*Thick   \
    +1.63459e-06  * pmax(0, 0.136223-Poro)*pmax(0, 4358.92-Depth)*Thick          
    ROM_6_LogMCO2_10yr = 10 ** ROM_6_LogMCO2_10yr / 1000000000 / 30       
    return ROM_6_LogMCO2_10yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogMCO2_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogMCO2_10yr =+10.0038      +1.0178       * pmax(0, Perm+13.0468)                         \
    -1.03796     * pmax(0, -13.0468-Perm)                        \
    +0.000182504  * pmax(0, Depth-2581.42)                        \
    -0.000281135 * pmax(0, 2581.42-Depth)                         \
    +0.0533921    * Thick -0.00103585  * Thick*Thick               \
    +3.04014      * pmax(0, GeoGrad-0.0323078)                      \
    -8.2779      * pmax(0, 0.0323078-GeoGrad)                       \
    +9.57068e-06  * Thick*Thick*Thick                              \
    -3.2926e-08  * Thick*Thick*Thick*Thick                          \
    -0.00152201  * pmax(0, Perm+12.3561)*Thick                      \
    +0.00143096   * pmax(0, -12.3561-Perm)*Thick                     \
    -1.15516e-07 * pmax(0, 1824.15-Depth)*pmax(0, 2581.42-Depth)      \
    -2.04723e-08 * pmax(0, Depth-4101.57)*pmax(0, Depth-2581.42)       \
    +3.15136e-08  * pmax(0, 4101.57-Depth)*pmax(0, Depth-2581.42)       \
    -0.135557    * pmax(0, Poro-0.208559)*pmax(0, Perm+13.0468)          \
    +0.646698     * pmax(0, 0.208559-Poro)*pmax(0, Perm+13.0468)          
    ROM_7_LogMCO2_10yr = 10 ** ROM_7_LogMCO2_10yr / 1000000000 / 30           
    return ROM_7_LogMCO2_10yr 
#################################################################################### 
# 15 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogMCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogMCO2_15yr =+8.28082   +0.0157542    * Thick                                    \
    +1.46607e-05  * pmax(0, Depth-1754.41)*Thick                      \
    -1.11363e-06 * pmax(0, 1754.41-Depth)*Thick                      \
    +0.945348     * pmax(0, Perm+14.5911)                         \
    -0.943648    * pmax(0, -14.5911-Perm)                        \
    +6.80485      * pmax(0, GeoGrad-0.0194368)                    \
    -8.30344     * pmax(0, 0.0194368-GeoGrad)                      \
    +0.000198294  * pmax(0, Depth-1826.12)                         \
    -0.000458671 * pmax(0, 1826.12-Depth)                         \
    -8.81955e-05 * pmax(0, Thick-90)*Thick                         \
    +0.000649337  * pmax(0, 90-Thick)*Thick                         \
    -1.50507e-05 * Thick*pmax(0, 90-Thick)*Thick                     \
    +1.19363e-07  * Thick*Thick*pmax(0, 90-Thick)*Thick               \
    -2.6236e-08  * pmax(0, Depth-2568.81)*pmax(0, Depth-1826.12)       \
    -7.98998e-08 * pmax(0, 2568.81-Depth)*pmax(0, Depth-1826.12)        \
    -8.52821e-09 * pmax(0, Depth-1754.41)*Thick*pmax(0, 90-Thick)*Thick  \
    -3.66716     * pmax(0, GeoGrad-0.0333472)                                 
    ROM_1_LogMCO2_15yr = 10 ** ROM_1_LogMCO2_15yr / 1000000000 / 30           
    return ROM_1_LogMCO2_15yr 
#############
# ROM: 0.05-0.5
#############
def ROM_2_LogMCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_2_LogMCO2_15yr =+22.3492 +0.934818     * Perm                                        \
    +0.0637239    * Thick                                        \
    -2.46006e-05 * pmax(0, Depth-2522.5)*Perm                     \
    +2.97503e-05  * pmax(0, 2522.5-Depth)*Perm                     \
    -0.00140641  * Thick*Thick                                     \
    +1.46849e-05  * Thick*Thick*Thick                               \
    -0.231757    * pmax(0, GeoGrad-0.0330801)*Perm                  \
    +0.573821     * pmax(0, 0.0330801-GeoGrad)*Perm                   \
    -5.54285e-08 * Thick*Thick*Thick*Thick                           \
    -9.33035e-05 * pmax(0, Depth-1463.02)                             \
    -0.000138284 * pmax(0, 1463.02-Depth)                             \
    -2.85846e-08 * pmax(0, Depth-2625.36)*pmax(0, Depth-1463.02)       \
    +5.97524e-08  * pmax(0, 2625.36-Depth)*pmax(0, Depth-1463.02)       \
    -0.000130388 * pmax(0, 2250.43-Depth)*pmax(0, 0.0330801-GeoGrad)*Perm         
    ROM_2_LogMCO2_15yr = 10 ** ROM_2_LogMCO2_15yr / 1000000000 / 30          
    return ROM_2_LogMCO2_15yr 
#############
# ROM: 0.1-1
#############
def ROM_3_LogMCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad):  
    ROM_3_LogMCO2_15yr =+8.28761  +0.893098     * pmax(0, Perm+14.9896)                      \
    -1.05473     * pmax(0, -14.9896-Perm)                         \
    +0.0622783    * Thick                                     \
    +0.000310759  * pmax(0, Depth-2668.3)                      \
    -0.000321373 * pmax(0, 2668.3-Depth)                        \
    -0.00133868  * Thick*Thick                                  \
    +1.36825e-05  * Thick*Thick*Thick                            \
    +3.21317      * pmax(0, GeoGrad-0.0334528)                    \
    -8.68929     * pmax(0, 0.0334528-GeoGrad)                      \
    -5.07692e-08 * Thick*Thick*Thick*Thick                          \
    +6.00536e-08  * pmax(0, Depth-1749.33)*pmax(0, 2668.3-Depth)      \
    -1.24228e-07 * pmax(0, 1749.33-Depth)*pmax(0, 2668.3-Depth)      \
    +2.4007e-05   * pmax(0, 4625.53-Depth)*pmax(0, Perm+14.9896)       \
    -2.74777e-08 * Depth*pmax(0, Depth-2668.3)                        \
    +0.000296172  * pmax(0, Depth-2250.43)*pmax(0, 0.0334528-GeoGrad)  \
    +0.00239456   * pmax(0, 2250.43-Depth)*pmax(0, 0.0334528-GeoGrad)          
    ROM_3_LogMCO2_15yr = 10 ** ROM_3_LogMCO2_15yr / 1000000000 / 30        
    return ROM_3_LogMCO2_15yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogMCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogMCO2_15yr =8.91935 +  0.953409     * pmax(0, Perm+14.1939) \
    -0.943315    * pmax(0, -14.1939-Perm) +0.0614185    * Thick          \
    +0.000213555  * pmax(0, Depth-2383.1)                       \
    -0.000287808 * pmax(0, 2383.1-Depth)                       \
    -0.00129101  * Thick*Thick                              \
    +4.56043      * pmax(0, GeoGrad-0.025134)                \
    -10.2818     * pmax(0, 0.025134-GeoGrad)                  \
    +1.28783e-05  * Thick*Thick*Thick                          \
    -4.68362e-08 * Thick*Thick*Thick*Thick                      \
    -2.35531e-08 * pmax(0, Depth-3027.11)*pmax(0, Depth-2383.1)  \
    +1.65203e-07  * pmax(0, Depth-1391.04)*Thick                  \
    -8.91795e-07 * pmax(0, 1391.04-Depth)*Thick                   \
    -5.86665e-07 * pmax(0, Depth-2109.77)*pmax(0, 2383.1-Depth)    \
    -8.82446e-08 * pmax(0, 2109.77-Depth)*pmax(0, 2383.1-Depth)         
    ROM_4_LogMCO2_15yr = 10 ** ROM_4_LogMCO2_15yr / 1000000000 / 30          
    return ROM_4_LogMCO2_15yr 
#############
# ROM: 1-10
#############
def ROM_5_LogMCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogMCO2_15yr =+9.65882 +0.966263     * pmax(0, Perm+13.8238)            \
    -0.944817    * pmax(0, -13.8238-Perm)                       \
    +0.000119565  * pmax(0, Depth-4489.41)                       \
    -0.000200837 * pmax(0, 4489.41-Depth)                        \
    +0.0619287    * Thick                                   \
    -0.00129248  * Thick*Thick                               \
    +4.2076       * pmax(0, GeoGrad-0.0275088)                \
    -9.55392     * pmax(0, 0.0275088-GeoGrad)                  \
    +1.28493e-05  * Thick*Thick*Thick                           \
    +3.03546e-08  * pmax(0, Depth-1812.22)*pmax(0, 4489.41-Depth)\
    -7.08231e-08 * pmax(0, 1812.22-Depth)*pmax(0, 4489.41-Depth)  \
    -4.65784e-08 * Thick*Thick*Thick*Thick                         \
    +9.79241e-08  * pmax(0, Depth-2609.14)*Thick                    \
    -4.36319e-07 * pmax(0, 2609.14-Depth)*Thick                     
    ROM_5_LogMCO2_15yr = 10 ** ROM_5_LogMCO2_15yr / 1000000000 / 30           
    return ROM_5_LogMCO2_15yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogMCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogMCO2_15yr = +10.2553  +0.972649     * pmax(0, Perm+13.0923)                          \
    -0.951534    * pmax(0, -13.0923-Perm)                           \
    +0.000131033  * pmax(0, Depth-3134.51)                           \
    -0.000255921 * pmax(0, 3134.51-Depth)                            \
    +0.0580423    * Thick                                       \
    -0.00115984  * Thick*Thick                                    \
    +3.13969      * pmax(0, GeoGrad-0.0325252)                   \
    -9.74013     * pmax(0, 0.0325252-GeoGrad)                      \
    +1.12002e-05  * Thick*Thick*Thick                               \
    -3.97499e-08 * Thick*Thick*Thick*Thick                           \
    +3.99663e-08  * pmax(0, Depth-1763.39)*pmax(0, 3134.51-Depth)     \
    -9.67737e-08 * pmax(0, 1763.39-Depth)*pmax(0, 3134.51-Depth)       \
    -1.96854e-07 * pmax(0, Depth-4358.92)*Thick                         \
    -3.09947e-07 * pmax(0, 4358.92-Depth)*Thick                         \
    -5.43114e-07 * pmax(0, Poro-0.136223)*pmax(0, 4358.92-Depth)*Thick   \
    +2.14748e-06  * pmax(0, 0.136223-Poro)*pmax(0, 4358.92-Depth)*Thick   \
    +0.000961106  * pmax(0, Depth-2968.34)*pmax(0, 0.0325252-GeoGrad)      \
    +0.0016609    * pmax(0, 2968.34-Depth)*pmax(0, 0.0325252-GeoGrad)            
    ROM_6_LogMCO2_15yr = 10 ** ROM_6_LogMCO2_15yr / 1000000000 / 30         
    return ROM_6_LogMCO2_15yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogMCO2_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogMCO2_15yr =+10.1791 +1.02301      * pmax(0, Perm+13.0468)                        \
    -1.05542     * pmax(0, -13.0468-Perm)                       \
    +0.000180514  * pmax(0, Depth-2581.42)                        \
    -0.000279386 * pmax(0, 2581.42-Depth)                        \
    +0.0539905    * Thick                                   \
    -0.00104822  * Thick*Thick                                \
    +2.95294      * pmax(0, GeoGrad-0.0323078)                      \
    -8.21974     * pmax(0, 0.0323078-GeoGrad)                      \
    +9.67953e-06  * Thick*Thick*Thick                             \
    -3.32695e-08 * Thick*Thick*Thick*Thick                          \
    -0.00201097  * pmax(0, Perm+12.3561)*Thick                     \
    +0.0014043    * pmax(0, -12.3561-Perm)*Thick                             \
    -1.10522e-07 * pmax(0, 1824.15-Depth)*pmax(0, 2581.42-Depth)          \
    -1.99689e-08 * pmax(0, Depth-4101.57)*pmax(0, Depth-2581.42)          \
    +3.07309e-08  * pmax(0, 4101.57-Depth)*pmax(0, Depth-2581.42)          \
    -0.0683759   * pmax(0, Poro-0.221886)                       \
    +0.151688     * pmax(0, 0.221886-Poro)                       
    ROM_7_LogMCO2_15yr = 10 ** ROM_7_LogMCO2_15yr / 1000000000 / 30          
    return ROM_7_LogMCO2_15yr 
#################################################################################### 
# 20 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogMCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogMCO2_20yr =+8.41754  +0.0156769    * Thick                                      \
    +1.41329e-05  * pmax(0, Depth-1754.41)*Thick                        \
    -1.10384e-06 * pmax(0, 1754.41-Depth)*Thick                        \
    +0.948037     * pmax(0, Perm+14.5911)                           \
    -0.885795    * pmax(0, -14.5911-Perm)                          \
    +4.92627      * pmax(0, GeoGrad-0.0194368)                         \
    -8.79385     * pmax(0, 0.0194368-GeoGrad)                         \
    +0.000199127  * pmax(0, Depth-1826.12)                           \
    -0.000457318 * pmax(0, 1826.12-Depth)                           \
    -8.92459e-05 * pmax(0, Thick-90)*Thick                             \
    +0.00064622   * pmax(0, 90-Thick)*Thick                             \
    -1.49479e-05 * Thick*pmax(0, 90-Thick)*Thick                          \
    +1.18215e-07  * Thick*Thick*pmax(0, 90-Thick)*Thick                       \
    -2.66817e-08 * pmax(0, Depth-2568.81)*pmax(0, Depth-1826.12)             \
    -8.68526e-08 * pmax(0, 2568.81-Depth)*pmax(0, Depth-1826.12)             \
    -8.15229e-09 * pmax(0, Depth-1754.41)*Thick*pmax(0, 90-Thick)*Thick                     \
    -9.6624      * pmax(0, GeoGrad-0.0366303)*pmax(0, -14.5911-Perm)          \
    -4.23945     * pmax(0, 0.0366303-GeoGrad)*pmax(0, -14.5911-Perm)          
    ROM_1_LogMCO2_20yr = 10 ** ROM_1_LogMCO2_20yr / 1000000000 / 30           
    return ROM_1_LogMCO2_20yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogMCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogMCO2_20yr =+22.489  +0.935416     * Perm                                        \
    +0.0636324    * Thick                                        \
    -2.49921e-05 * pmax(0, Depth-2522.5)*Perm                           \
    +3.01325e-05  * pmax(0, 2522.5-Depth)*Perm                           \
    -0.00140543  * Thick*Thick                                     \
    +1.46778e-05  * Thick*Thick*Thick                                  \
    -0.22712     * pmax(0, GeoGrad-0.0330801)*Perm                        \
    +0.564958     * pmax(0, 0.0330801-GeoGrad)*Perm                        \
    -5.5417e-08  * Thick*Thick*Thick*Thick                               \
    -0.000100009 * pmax(0, Depth-1463.02)                             \
    -0.000131263 * pmax(0, 1463.02-Depth)                             \
    -2.85487e-08 * pmax(0, Depth-2625.36)*pmax(0, Depth-1463.02)               \
    +5.97644e-08  * pmax(0, 2625.36-Depth)*pmax(0, Depth-1463.02)                         \
    -0.000130752 * pmax(0, 2250.43-Depth)*pmax(0, 0.0330801-GeoGrad)*Perm          
    ROM_2_LogMCO2_20yr = 10 ** ROM_2_LogMCO2_20yr / 1000000000 / 30          
    return ROM_2_LogMCO2_20yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogMCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogMCO2_20yr =+8.40618  +0.980072     * pmax(0, Perm+14.9896)                              \
    -0.952879    * pmax(0, -14.9896-Perm)                                     \
    +0.0614713    * Thick                                                 \
    +0.000305168  * pmax(0, Depth-2668.3)                                       \
    -0.000321211 * pmax(0, 2668.3-Depth)                                       \
    -0.00131321  * Thick*Thick                                              \
    +1.33861e-05  * Thick*Thick*Thick                                           \
    +3.16459      * pmax(0, GeoGrad-0.0334528)                                    \
    -7.70351     * pmax(0, 0.0334528-GeoGrad)                                    \
    -4.96206e-08 * Thick*Thick*Thick*Thick                                        \
    -2.12679e-05 * pmax(0, Depth-1450.43)*pmax(0, Perm+14.9896)                                 \
    +5.32785e-08  * pmax(0, Depth-1706.53)*pmax(0, 2668.3-Depth)                         \
    -1.1282e-07  * pmax(0, 1706.53-Depth)*pmax(0, 2668.3-Depth)                         \
    -2.59747e-08 * Depth*pmax(0, Depth-2668.3)                                    \
    -3.91487e-05 * pmax(0, Perm+13.836)*pmax(0, Depth-1450.43)*pmax(0, Perm+14.9896)                    
    ROM_3_LogMCO2_20yr = 10 ** ROM_3_LogMCO2_20yr / 1000000000 / 30          
    return ROM_3_LogMCO2_20yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogMCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogMCO2_20yr =+9.04398  +0.945997     * pmax(0, Perm+14.1939)                            \
    -0.945397    * pmax(0, -14.1939-Perm)                           \
    +0.0616323    * Thick                                       \
    +0.000190203  * pmax(0, Depth-2383.1)                             \
    -0.000260846 * pmax(0, 2383.1-Depth)                             \
    -0.00128383  * Thick*Thick                                    \
    +4.53484      * pmax(0, GeoGrad-0.025134)                           \
    -10.1547     * pmax(0, 0.025134-GeoGrad)                           \
    +1.2795e-05   * Thick*Thick*Thick                                 \
    -4.64897e-08 * Thick*Thick*Thick*Thick                                       \
    -1.28671e-07 * pmax(0, 4047.09-Depth)*Thick                               \
    -1.20182e-07 * pmax(0, 2087.99-Depth)*pmax(0, 2383.1-Depth)               \
    -1.95148e-08 * pmax(0, Depth-3950.1)*pmax(0, Depth-2383.1)                \
    +3.83948e-08  * pmax(0, 3950.1-Depth)*pmax(0, Depth-2383.1)                \
    +5.39831e-06  * pmax(0, Perm+12.9167)*pmax(0, 4047.09-Depth)*Thick           \
    -9.65071e-08 * pmax(0, -12.9167-Perm)*pmax(0, 4047.09-Depth)*Thick          
    ROM_4_LogMCO2_20yr = 10 ** ROM_4_LogMCO2_20yr / 1000000000 / 30           
    return ROM_4_LogMCO2_20yr 
#############
# ROM: 1-10
#############
def ROM_5_LogMCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogMCO2_20yr = +9.45426 +0.976529     * pmax(0, Perm+13.8238)                        \
    -0.94796     * pmax(0, -13.8238-Perm)                       \
    +0.0622358    * Thick                                   \
    +0.000203857  * pmax(0, Depth-2609.14)                        \
    -0.000266985 * pmax(0, 2609.14-Depth)                        \
    -0.00131013  * Thick*Thick                                \
    +4.18428      * pmax(0, GeoGrad-0.0275088)                      \
    -9.5184      * pmax(0, 0.0275088-GeoGrad)                      \
    +1.30397e-05  * Thick*Thick*Thick                             \
    -4.73e-08    * Thick*Thick*Thick*Thick                          \
    +1.83012e-07  * pmax(0, Depth-1453.52)*Thick                     \
    -8.67715e-07 * pmax(0, 1453.52-Depth)*Thick                     \
    -2.27786e-08 * pmax(0, Depth-3010.67)*pmax(0, Depth-2609.14)                    \
    -8.86558e-08 * pmax(0, 2062.79-Depth)*pmax(0, 2609.14-Depth)          
    ROM_5_LogMCO2_20yr = 10 ** ROM_5_LogMCO2_20yr / 1000000000 / 30          
    return ROM_5_LogMCO2_20yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogMCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogMCO2_20yr =+10.2278   +0.982903     * pmax(0, Perm+13.0923)                            \
    -0.959326    * pmax(0, -13.0923-Perm)                           \
    +0.0585061    * Thick                                       \
    +0.000178062  * pmax(0, Depth-2457.9)                             \
    -0.000270759 * pmax(0, 2457.9-Depth)                             \
    -0.00117294  * Thick*Thick                                    \
    +2.92418      * pmax(0, GeoGrad-0.0333784)                          \
    -8.10211     * pmax(0, 0.0333784-GeoGrad)                          \
    +1.13226e-05  * Thick*Thick*Thick                                 \
    -4.01455e-08 * Thick*Thick*Thick*Thick                                        \
    -2.91783e-07 * pmax(0, 4099.72-Depth)*Thick                                  \
    -1.18569e-07 * pmax(0, 1842.81-Depth)*pmax(0, 2457.9-Depth)               \
    -7.1156e-07  * pmax(0, Poro-0.136387)*pmax(0, 4099.72-Depth)*Thick          \
    +2.78813e-06  * pmax(0, 0.136387-Poro)*pmax(0, 4099.72-Depth)*Thick          \
    -1.70755e-08 * pmax(0, Depth-3762.6)*pmax(0, Depth-2457.9)                \
    +4.69679e-08  * pmax(0, 3762.6-Depth)*pmax(0, Depth-2457.9)                
    ROM_6_LogMCO2_20yr = 10 ** ROM_6_LogMCO2_20yr / 1000000000 / 30           
    return ROM_6_LogMCO2_20yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogMCO2_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogMCO2_20yr =+10.3033   +1.01511      * pmax(0, Perm+13.0468)                        \
    -1.08709     * pmax(0, -13.0468-Perm)                       \
    +0.00018647   * pmax(0, Depth-2581.42)                        \
    -0.000298828 * pmax(0, 2581.42-Depth)                        \
    +0.0535511    * Thick                                   \
    -0.00103355  * Thick*Thick                                \
    +2.86999      * pmax(0, GeoGrad-0.0323078)                      \
    -8.20066     * pmax(0, 0.0323078-GeoGrad)                      \
    +9.50624e-06  * Thick*Thick*Thick                             \
    -3.25978e-08 * Thick*Thick*Thick*Thick                          \
    -0.00250593  * pmax(0, Perm+12.3561)*Thick                     \
    +0.00147944   * pmax(0, -12.3561-Perm)*Thick                    \
    -0.0758243   * pmax(0, Poro-0.21655)                        \
    +0.196356     * pmax(0, 0.21655-Poro)                        \
    +4.24183e-08  * pmax(0, Depth-1767.33)*pmax(0, 2581.42-Depth)          \
    -1.19166e-07 * pmax(0, 1767.33-Depth)*pmax(0, 2581.42-Depth)          \
    -2.27734e-08 * pmax(0, Depth-4154.22)*pmax(0, Depth-2581.42)          \
    +3.77124e-08  * pmax(0, 4154.22-Depth)*pmax(0, Depth-2581.42)                  \
    +2.9779e-05   * pmax(0, 3762.41-Depth)*pmax(0, Perm+13.0468)          
    ROM_7_LogMCO2_20yr = 10 ** ROM_7_LogMCO2_20yr / 1000000000 / 30           
    return ROM_7_LogMCO2_20yr 
#################################################################################### 
# 25 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogMCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogMCO2_25yr =+8.51597  +0.0156266    * Thick                                      \
    +1.42136e-05  * pmax(0, Depth-1754.41)*Thick                        \
    -1.13206e-06 * pmax(0, 1754.41-Depth)*Thick                        \
    +0.94792      * pmax(0, Perm+14.5911)                           \
    -0.885791    * pmax(0, -14.5911-Perm)                          \
    +4.81372      * pmax(0, GeoGrad-0.0194368)                         \
    -8.60074     * pmax(0, 0.0194368-GeoGrad)                         \
    +0.00019763   * pmax(0, Depth-1826.12)                           \
    -0.000454749 * pmax(0, 1826.12-Depth)                           \
    -8.84948e-05 * pmax(0, Thick-90)*Thick                             \
    +0.000645032  * pmax(0, 90-Thick)*Thick                             \
    -1.49304e-05 * Thick*pmax(0, 90-Thick)*Thick                          \
    +1.18228e-07  * Thick*Thick*pmax(0, 90-Thick)*Thick                       \
    -2.65863e-08 * pmax(0, Depth-2568.81)*pmax(0, Depth-1826.12)             \
    -8.59314e-08 * pmax(0, 2568.81-Depth)*pmax(0, Depth-1826.12)             \
    -8.18483e-09 * pmax(0, Depth-1754.41)*Thick*pmax(0, 90-Thick)*Thick                     \
    -9.59372     * pmax(0, GeoGrad-0.0366303)*pmax(0, -14.5911-Perm)          \
    -4.23505     * pmax(0, 0.0366303-GeoGrad)*pmax(0, -14.5911-Perm)          
    ROM_1_LogMCO2_25yr = 10 ** ROM_1_LogMCO2_25yr / 1000000000 / 30          
    return ROM_1_LogMCO2_25yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogMCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogMCO2_25yr =+22.6005    +0.936079     * Perm                                        \
    +0.0635762    * Thick                                        \
    -2.53534e-05 * pmax(0, Depth-2522.5)*Perm                           \
    +3.04967e-05  * pmax(0, 2522.5-Depth)*Perm                           \
    -0.00140495  * Thick*Thick                                     \
    +1.46741e-05  * Thick*Thick*Thick                                  \
    -0.223443    * pmax(0, GeoGrad-0.0330801)*Perm                        \
    +0.557902     * pmax(0, 0.0330801-GeoGrad)*Perm                        \
    -5.54104e-08 * Thick*Thick*Thick*Thick                               \
    -0.00010593  * pmax(0, Depth-1463.02)                             \
    -0.000125146 * pmax(0, 1463.02-Depth)                             \
    -2.85298e-08 * pmax(0, Depth-2625.36)*pmax(0, Depth-1463.02)               \
    +5.98374e-08  * pmax(0, 2625.36-Depth)*pmax(0, Depth-1463.02)                        \
    -0.000132654 * pmax(0, 2250.43-Depth)*pmax(0, 0.0330801-GeoGrad)*Perm          
    ROM_2_LogMCO2_25yr = 10 ** ROM_2_LogMCO2_25yr / 1000000000 / 30           
    return ROM_2_LogMCO2_25yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogMCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogMCO2_25yr =+8.50047  +0.98209      * pmax(0, Perm+14.9896)                                      \
    -0.950674    * pmax(0, -14.9896-Perm)                                     \
    +0.0614459    * Thick                                                 \
    +0.000304993  * pmax(0, Depth-2668.3)                                       \
    -0.000321147 * pmax(0, 2668.3-Depth)                                       \
    -0.00131348  * Thick*Thick                                              \
    +1.33911e-05  * Thick*Thick*Thick                                           \
    +3.12597      * pmax(0, GeoGrad-0.0334528)                                    \
    -7.60685     * pmax(0, 0.0334528-GeoGrad)                                    \
    -4.96481e-08 * Thick*Thick*Thick*Thick                                        \
    -2.18576e-05 * pmax(0, Depth-1450.43)*pmax(0, Perm+14.9896)                                \
    +5.37245e-08  * pmax(0, Depth-1706.53)*pmax(0, 2668.3-Depth)                         \
    -1.12416e-07 * pmax(0, 1706.53-Depth)*pmax(0, 2668.3-Depth)                         \
    -2.59693e-08 * Depth*pmax(0, Depth-2668.3)                                    \
    -3.91966e-05 * pmax(0, Perm+13.836)*pmax(0, Depth-1450.43)*pmax(0, Perm+14.9896)                   
    ROM_3_LogMCO2_25yr = 10 ** ROM_3_LogMCO2_25yr / 1000000000 / 30           
    return ROM_3_LogMCO2_25yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogMCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogMCO2_25yr =+9.12059  +0.969796     * pmax(0, Perm+14.1939)                         \
    -0.94657     * pmax(0, -14.1939-Perm)                        \
    +0.062369     * Thick                                    \
    +0.000190587  * pmax(0, Depth-2383.1)                          \
    -0.000256135 * pmax(0, 2383.1-Depth)                          \
    -0.00129847  * Thick*Thick                                 \
    +4.49639      * pmax(0, GeoGrad-0.025134)                        \
    -10.1187     * pmax(0, 0.025134-GeoGrad)                        \
    +1.29319e-05  * Thick*Thick*Thick                              \
    -4.69737e-08 * Thick*Thick*Thick*Thick                                  \
    -2.62756e-07 * pmax(0, 4047.09-Depth)*Thick                               \
    -1.16839e-07 * pmax(0, 2087.99-Depth)*pmax(0, 2383.1-Depth)            \
    -1.93884e-08 * pmax(0, Depth-3950.1)*pmax(0, Depth-2383.1)             \
    +3.79879e-08  * pmax(0, 3950.1-Depth)*pmax(0, Depth-2383.1)             \
    -0.0375642   * pmax(0, Poro-0.103072)*pmax(0, Perm+14.1939)          \
    +0.581426     * pmax(0, 0.103072-Poro)*pmax(0, Perm+14.1939)          
    ROM_4_LogMCO2_25yr = 10 ** ROM_4_LogMCO2_25yr / 1000000000 / 30           
    return ROM_4_LogMCO2_25yr 
#############
# ROM: 1-10
#############
def ROM_5_LogMCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogMCO2_25yr =+9.56368 +0.989115     * pmax(0, Perm+13.8203)                         \
    -0.95133     * pmax(0, -13.8203-Perm)                        \
    +0.0622983    * Thick                                    \
    +0.000186076  * pmax(0, Depth-2609.14)                         \
    -0.000334    * pmax(0, 2609.14-Depth)                         \
    -0.00130702  * Thick*Thick                                 \
    +4.26495      * pmax(0, GeoGrad-0.0275088)                       \
    -9.25126     * pmax(0, 0.0275088-GeoGrad)                       \
    +1.30132e-05  * Thick*Thick*Thick                              \
    -4.7244e-08  * Thick*Thick*Thick*Thick                           \
    +1.28719e-07  * pmax(0, Depth-1453.52)*Thick                      \
    -2.90187e-06 * pmax(0, 1453.52-Depth)*Thick                      \
    -1.63687e-08 * pmax(0, Depth-3010.67)*pmax(0, Depth-2609.14)           \
    -5.0148e-07  * pmax(0, 3010.67-Depth)*pmax(0, Depth-2609.14)           \
    -0.0820149   * pmax(0, Poro-0.152232)*pmax(0, Perm+13.8203)          \
    +0.507543     * pmax(0, 0.152232-Poro)*pmax(0, Perm+13.8203)         
    ROM_5_LogMCO2_25yr = 10 ** ROM_5_LogMCO2_25yr / 1000000000 / 30          
    return ROM_5_LogMCO2_25yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogMCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogMCO2_25yr =+10.3233  +0.990109     * pmax(0, Perm+13.0923)                            \
    -0.966806    * pmax(0, -13.0923-Perm)                           \
    +0.0589076    * Thick                                       \
    +0.000177524  * pmax(0, Depth-2457.9)                             \
    -0.000272706 * pmax(0, 2457.9-Depth)                             \
    -0.00118242  * Thick*Thick                                    \
    +2.87935      * pmax(0, GeoGrad-0.0333784)                          \
    -8.07488     * pmax(0, 0.0333784-GeoGrad)                          \
    +1.14205e-05  * Thick*Thick*Thick                                 \
    -4.0505e-08  * Thick*Thick*Thick*Thick                                       \
    -3.01872e-07 * pmax(0, 4099.72-Depth)*Thick                         \
    -7.94816e-07 * pmax(0, Poro-0.136387)*pmax(0, 4099.72-Depth)*Thick          \
    +3.11572e-06  * pmax(0, 0.136387-Poro)*pmax(0, 4099.72-Depth)*Thick          \
    +5.54767e-08  * pmax(0, Depth-1784.44)*pmax(0, 2457.9-Depth)               \
    -1.19925e-07 * pmax(0, 1784.44-Depth)*pmax(0, 2457.9-Depth)               \
    -1.71112e-08 * pmax(0, Depth-3762.6)*pmax(0, Depth-2457.9)                \
    +5.07428e-08  * pmax(0, 3762.6-Depth)*pmax(0, Depth-2457.9)                
    ROM_6_LogMCO2_25yr = 10 ** ROM_6_LogMCO2_25yr / 1000000000 / 30          
    return ROM_6_LogMCO2_25yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogMCO2_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogMCO2_25yr =+10.4012  +1.02311      * pmax(0, Perm+13.0468)                        \
    -1.09828     * pmax(0, -13.0468-Perm)                       \
    +0.000185498  * pmax(0, Depth-2581.42)                        \
    -0.000297642 * pmax(0, 2581.42-Depth)                        \
    +0.0538306    * Thick -0.00104011  * Thick*Thick                                \
    +2.8234       * pmax(0, GeoGrad-0.0323078)                      \
    -8.14496     * pmax(0, 0.0323078-GeoGrad)                      \
    +9.56701e-06  * Thick*Thick*Thick                             \
    -3.28014e-08 * Thick*Thick*Thick*Thick                          \
    -0.00259202  * pmax(0, Perm+12.3648)*Thick                     \
    +0.00152997   * pmax(0, -12.3648-Perm)*Thick                    \
    -0.0836288   * pmax(0, Poro-0.214814)                       \
    +0.221775     * pmax(0, 0.214814-Poro)                       \
    +4.21477e-08  * pmax(0, Depth-1767.33)*pmax(0, 2581.42-Depth)          \
    -1.1941e-07  * pmax(0, 1767.33-Depth)*pmax(0, 2581.42-Depth)          \
    -2.27462e-08 * pmax(0, Depth-4154.22)*pmax(0, Depth-2581.42)          \
    +3.76933e-08  * pmax(0, 4154.22-Depth)*pmax(0, Depth-2581.42)                  \
    +3.09297e-05  * pmax(0, 3762.41-Depth)*pmax(0, Perm+13.0468)          
    ROM_7_LogMCO2_25yr = 10 ** ROM_7_LogMCO2_25yr / 1000000000 / 30         
    return ROM_7_LogMCO2_25yr 
#################################################################################### 
# 30 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogMCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogMCO2_30yr = 8.59591 + 0.015587 * Thick + 1.42795e-05 * pmax(0, Depth-1754.41) * Thick-1.15625e-06 * pmax(0, 1754.41-Depth) * Thick + 0.947937 * pmax(0, Perm+14.5911) - 0.885917 * pmax(0, -14.5911-Perm)+4.7154* pmax(0, GeoGrad-0.0194368)  -8.42901 * pmax(0, 0.0194368-GeoGrad) + 0.00019654 * pmax(0, Depth-1826.12) \
    -0.000452777 * pmax(0, 1826.12-Depth)-8.78814e-05 * pmax(0, Thick-90)*Thick+0.000644175  * pmax(0, 90-Thick)*Thick-1.49189e-05 * Thick*pmax(0, 90-Thick)*Thick+1.18253e-07  * Thick*Thick*pmax(0, 90-Thick)*Thick-2.65273e-08 * pmax(0, Depth-2568.81)*pmax(0, Depth-1826.12)-8.50627e-08 * pmax(0, 2568.81-Depth)*pmax(0, Depth-1826.12)  -8.21374e-09 * pmax(0, Depth-1754.41)*Thick*pmax(0, 90-Thick)*Thick \
    -9.52831     * pmax(0, GeoGrad-0.0366303)*pmax(0, -14.5911-Perm)-4.22929     * pmax(0, 0.0366303-GeoGrad)*pmax(0, -14.5911-Perm)
    ROM_1_LogMCO2_30yr = 10 ** ROM_1_LogMCO2_30yr / 1000000000 / 30          
    return ROM_1_LogMCO2_30yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogMCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogMCO2_30yr =22.6945  +0.936802 * Perm +0.0635403 * Thick -2.57106e-05 * pmax(0, Depth-2522.5)*Perm \
    +3.0864e-05   * pmax(0, 2522.5-Depth)*Perm \
    -0.00140477  * Thick*Thick      \
    +1.46724e-05  * Thick*Thick*Thick \
    -0.220429    * pmax(0, GeoGrad-0.0330801)*Perm    \
    +0.552063     * pmax(0, 0.0330801-GeoGrad)*Perm    \
    -5.54063e-08 * Thick*Thick*Thick*Thick              \
    -0.000111586 * pmax(0, Depth-1463.02)                \
    -0.000119406 * pmax(0, 1463.02-Depth)                 \
    -2.85215e-08 * pmax(0, Depth-2625.36)*pmax(0, Depth-1463.02) \
    +5.99429e-08  * pmax(0, 2625.36-Depth)*pmax(0, Depth-1463.02) \
    -0.000135224 * pmax(0, 2250.43-Depth)*pmax(0, 0.0330801-GeoGrad)*Perm          
    ROM_2_LogMCO2_30yr = 10 ** ROM_2_LogMCO2_30yr / 1000000000 / 30           
    return ROM_2_LogMCO2_30yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogMCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogMCO2_30yr =+8.57673  +0.984198     * pmax(0, Perm+14.9896)                                       \
    -0.948761    * pmax(0, -14.9896-Perm)                                     \
    +0.0614451    * Thick                                                 \
    +0.000305034  * pmax(0, Depth-2668.3)                                       \
    -0.000321293 * pmax(0, 2668.3-Depth)                                       \
    -0.00131418  * Thick*Thick                                              \
    +1.33997e-05  * Thick*Thick*Thick                                           \
    +3.09624      * pmax(0, GeoGrad-0.0334528)                                    \
    -7.52532     * pmax(0, 0.0334528-GeoGrad)                                    \
    -4.96852e-08 * Thick*Thick*Thick*Thick                                        
    -2.24321e-05 * pmax(0, Depth-1450.43)*pmax(0, Perm+14.9896)                                \
    +5.41804e-08  * pmax(0, Depth-1706.53)*pmax(0, 2668.3-Depth)                         \
    -1.12084e-07 * pmax(0, 1706.53-Depth)*pmax(0, 2668.3-Depth)                         \
    -2.5979e-08  * Depth*pmax(0, Depth-2668.3)                                    \
    -3.93038e-05 * pmax(0, Perm+13.836)*pmax(0, Depth-1450.43)*pmax(0, Perm+14.9896)              
    ROM_3_LogMCO2_30yr = 10 ** ROM_3_LogMCO2_30yr / 1000000000 / 30           
    return ROM_3_LogMCO2_30yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogMCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogMCO2_30yr =+9.19451  +0.971363     * pmax(0, Perm+14.1939)                       \
    -0.949       * pmax(0, -14.1939-Perm)                      \
    +0.0628482    * Thick                                  \
    +0.000189699  * pmax(0, Depth-2383.1)                        \
    -0.000255874 * pmax(0, 2383.1-Depth)                        \
    -0.00131262  * Thick*Thick                               \
    +4.46001      * pmax(0, GeoGrad-0.025134)                      \
    -10.1692     * pmax(0, 0.025134-GeoGrad)                      \
    +1.30933e-05  * Thick*Thick*Thick                            \
    -4.76059e-08 * Thick*Thick*Thick*Thick                                 \
    -2.69116e-07 * pmax(0, 4047.09-Depth)*Thick                              \
    -1.13634e-07 * pmax(0, 2109.77-Depth)*pmax(0, 2383.1-Depth)          \
    -1.91524e-08 * pmax(0, Depth-3950.1)*pmax(0, Depth-2383.1)           \
    +3.7298e-08   * pmax(0, 3950.1-Depth)*pmax(0, Depth-2383.1)           
    ROM_4_LogMCO2_30yr = 10 ** ROM_4_LogMCO2_30yr / 1000000000 / 30           
    return ROM_4_LogMCO2_30yr 
#############
# ROM: 1-10
#############
def ROM_5_LogMCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogMCO2_30yr =+9.62875  +1.04177      * pmax(0, Perm+13.8203)                         \
    -0.958964    * pmax(0, -13.8203-Perm)                        \
    +0.0621432    * Thick                                    \
    +0.00020947   * pmax(0, Depth-2609.14)                         \
    -0.000338759 * pmax(0, 2609.14-Depth)                         \
    -0.00129337  * Thick*Thick                                 \
    +4.22867      * pmax(0, GeoGrad-0.0275088)                       \
    -9.29361     * pmax(0, 0.0275088-GeoGrad)                       \
    +1.28409e-05  * Thick*Thick*Thick                              \
    -4.65213e-08 * Thick*Thick*Thick*Thick                                    \
    -2.17839e-06 * pmax(0, 1527.78-Depth)*Thick                      \
    -2.03537e-08 * pmax(0, Depth-2992.66)*pmax(0, Depth-2609.14)           \
    -3.64585e-07 * pmax(0, 2992.66-Depth)*pmax(0, Depth-2609.14)           \
    -0.11128     * pmax(0, Poro-0.136827)*pmax(0, Perm+13.8203)          \
    +0.674317     * pmax(0, 0.136827-Poro)*pmax(0, Perm+13.8203)          \
    -2.94604e-05 * pmax(0, Depth-1742.79)*pmax(0, Perm+13.8203)           \
    -6.6022e-05  * pmax(0, 1742.79-Depth)*pmax(0, Perm+13.8203)           
    ROM_5_LogMCO2_30yr = 10 ** ROM_5_LogMCO2_30yr / 1000000000 / 30           
    return ROM_5_LogMCO2_30yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogMCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogMCO2_30yr =+10.4006  +0.995985     * pmax(0, Perm+13.0923)                            \
    -0.972968    * pmax(0, -13.0923-Perm)                           \
    +0.0592448    * Thick                                       \
    +0.000175889  * pmax(0, Depth-2457.9)                             \
    -0.00026904  * pmax(0, 2457.9-Depth)                             \
    -0.00119045  * Thick*Thick                                    \
    +2.95806      * pmax(0, GeoGrad-0.0328211)                     \
    -8.16887     * pmax(0, 0.0328211-GeoGrad)                       \
    +1.1503e-05   * Thick*Thick*Thick                                \
    -4.08037e-08 * Thick*Thick*Thick*Thick                            \
    -3.11001e-07 * pmax(0, 4099.72-Depth)*Thick                        \
    -8.60943e-07 * pmax(0, Poro-0.136387)*pmax(0, 4099.72-Depth)*Thick  \
    +3.37893e-06  * pmax(0, 0.136387-Poro)*pmax(0, 4099.72-Depth)*Thick  \
    +5.44514e-08  * pmax(0, Depth-1796.28)*pmax(0, 2457.9-Depth)          \
    -1.19955e-07 * pmax(0, 1796.28-Depth)*pmax(0, 2457.9-Depth)            \
    -1.68045e-08 * pmax(0, Depth-3762.6)*pmax(0, Depth-2457.9)              \
    +5.09724e-08  * pmax(0, 3762.6-Depth)*pmax(0, Depth-2457.9)                
    ROM_6_LogMCO2_30yr = 10 ** ROM_6_LogMCO2_30yr / 1000000000 / 30          
    return ROM_6_LogMCO2_30yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogMCO2_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogMCO2_30yr =+10.4838  +1.0297       * pmax(0, Perm+13.0468) \
    -1.10835     * pmax(0, -13.0468-Perm)                       \
    +0.000184604  * pmax(0, Depth-2581.42)                       \
    -0.000296523 * pmax(0, 2581.42-Depth)                        \
    +0.0540388    * Thick  -0.00104541  * Thick*Thick             \
    +2.78364      * pmax(0, GeoGrad-0.0323078)                     \
    -8.09333     * pmax(0, 0.0323078-GeoGrad)                      \
    +9.61609e-06  * Thick*Thick*Thick                             \
    -3.2966e-08  * Thick*Thick*Thick*Thick                         \
    -0.00268376  * pmax(0, Perm+12.3648)*Thick                     \
    +0.00158073   * pmax(0, -12.3648-Perm)*Thick                    \
    -0.0943474   * pmax(0, Poro-0.201185)                       \
    +0.255098     * pmax(0, 0.201185-Poro)                       \
    +4.17994e-08  * pmax(0, Depth-1767.33)*pmax(0, 2581.42-Depth) \
    -1.19519e-07 * pmax(0, 1767.33-Depth)*pmax(0, 2581.42-Depth)   \
    -2.27209e-08 * pmax(0, Depth-4154.22)*pmax(0, Depth-2581.42)    \
    +3.76659e-08  * pmax(0, 4154.22-Depth)*pmax(0, Depth-2581.42)    \
    +3.18519e-05  * pmax(0, 3762.41-Depth)*pmax(0, Perm+13.0468)          
    ROM_7_LogMCO2_30yr = 10 ** ROM_7_LogMCO2_30yr / 1000000000 / 30           
    return ROM_7_LogMCO2_30yr 
#################################################################################### 
# 35 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogMCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogMCO2_35yr =+8.66316  +0.0155546    * Thick                                      \
    +1.43375e-05  * pmax(0, Depth-1754.41)*Thick                        \
    -1.1781e-06  * pmax(0, 1754.41-Depth)*Thick                        \
    +0.948032     * pmax(0, Perm+14.5911)                           \
    -0.886127    * pmax(0, -14.5911-Perm)                          \
    +4.62748      * pmax(0, GeoGrad-0.0194368)                         \
    -8.2739      * pmax(0, 0.0194368-GeoGrad)                         \
    +0.000195705  * pmax(0, Depth-1826.12)                           \
    -0.000451185 * pmax(0, 1826.12-Depth)                           \
    -8.73653e-05 * pmax(0, Thick-90)*Thick                             \
    +0.000643504  * pmax(0, 90-Thick)*Thick                             \
    -1.49102e-05 * Thick*pmax(0, 90-Thick)*Thick                          \
    +1.18272e-07  * Thick*Thick*pmax(0, 90-Thick)*Thick                       \
    -2.6491e-08  * pmax(0, Depth-2568.81)*pmax(0, Depth-1826.12)             \
    -8.42293e-08 * pmax(0, 2568.81-Depth)*pmax(0, Depth-1826.12)             \
    -8.24066e-09 * pmax(0, Depth-1754.41)*Thick*pmax(0, 90-Thick)*Thick                     \
    -9.46473     * pmax(0, GeoGrad-0.0366303)*pmax(0, -14.5911-Perm)          \
    -4.22359     * pmax(0, 0.0366303-GeoGrad)*pmax(0, -14.5911-Perm)          
    ROM_1_LogMCO2_35yr = 10 ** ROM_1_LogMCO2_35yr / 1000000000 / 30              
    return ROM_1_LogMCO2_35yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogMCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogMCO2_35yr =+22.777   +0.937581     * Perm                                        \
    +0.0635186    * Thick                                        \
    -2.60717e-05 * pmax(0, Depth-2522.5)*Perm                           \
    +3.12395e-05  * pmax(0, 2522.5-Depth)*Perm                           \
    -0.00140481  * Thick*Thick                                     \
    +1.46725e-05  * Thick*Thick*Thick                                  \
    -0.217903    * pmax(0, GeoGrad-0.0330801)*Perm                        \
    +0.547098     * pmax(0, 0.0330801-GeoGrad)*Perm                        \
    -5.54057e-08 * Thick*Thick*Thick*Thick                               \
    -0.000117164 * pmax(0, Depth-1463.02)                             \
    -0.00011383  * pmax(0, 1463.02-Depth)                             \
    -2.85197e-08 * pmax(0, Depth-2625.36)*pmax(0, Depth-1463.02)               \
    +6.00645e-08  * pmax(0, 2625.36-Depth)*pmax(0, Depth-1463.02)                        \
    -0.000138049 * pmax(0, 2250.43-Depth)*pmax(0, 0.0330801-GeoGrad)*Perm          
    ROM_2_LogMCO2_35yr = 10 ** ROM_2_LogMCO2_35yr / 1000000000 / 30           
    return ROM_2_LogMCO2_35yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogMCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogMCO2_35yr =+8.64061  +0.986386     * pmax(0, Perm+14.9896)                                      \
    -0.947027    * pmax(0, -14.9896-Perm)                                     \
    +0.0614611    * Thick                                                 \
    +0.000305216  * pmax(0, Depth-2668.3)                                       \
    -0.000321572 * pmax(0, 2668.3-Depth)                                       \
    -0.00131516  * Thick*Thick                                              \
    +1.3411e-05   * Thick*Thick*Thick                                           \
    +3.07281      * pmax(0, GeoGrad-0.0334528)                                    \
    -7.45562     * pmax(0, 0.0334528-GeoGrad)                                    \
    -4.97297e-08 * Thick*Thick*Thick*Thick                                        \
    -2.29973e-05 * pmax(0, Depth-1450.43)*pmax(0, Perm+14.9896)                                 \
    +5.46413e-08  * pmax(0, Depth-1706.53)*pmax(0, 2668.3-Depth)                         \
    -1.11809e-07 * pmax(0, 1706.53-Depth)*pmax(0, 2668.3-Depth)                         \
    -2.59984e-08 * Depth*pmax(0, Depth-2668.3)                                    \
    -3.94495e-05 * pmax(0, Perm+13.836)*pmax(0, Depth-1450.43)*pmax(0, Perm+14.9896)               
    ROM_3_LogMCO2_35yr = 10 ** ROM_3_LogMCO2_35yr / 1000000000 / 30           
    return ROM_3_LogMCO2_35yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogMCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogMCO2_35yr =+9.25206   +0.976952     * pmax(0, Perm+14.1975)                       \
    -0.950749    * pmax(0, -14.1975-Perm)                      \
    +0.0631548    * Thick                                  \
    +0.0001889    * pmax(0, Depth-2383.1)                        \
    -0.000255945 * pmax(0, 2383.1-Depth)                        \
    -0.0013202   * Thick*Thick                               \
    +4.4426       * pmax(0, GeoGrad-0.025134)                      \
    -10.1577     * pmax(0, 0.025134-GeoGrad)                      \
    +1.31716e-05  * Thick*Thick*Thick                            \
    -4.78933e-08 * Thick*Thick*Thick*Thick                                \
    -2.74827e-07 * pmax(0, 4047.09-Depth)*Thick                          \
    -1.13125e-07 * pmax(0, 2109.77-Depth)*pmax(0, 2383.1-Depth)          \
    -1.89752e-08 * pmax(0, Depth-3967.91)*pmax(0, Depth-2383.1)          \
    +3.67133e-08  * pmax(0, 3967.91-Depth)*pmax(0, Depth-2383.1)          
    ROM_4_LogMCO2_35yr = 10 ** ROM_4_LogMCO2_35yr / 1000000000 / 30          
    return ROM_4_LogMCO2_35yr 
#############
# ROM: 1-10
#############
def ROM_5_LogMCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogMCO2_35yr =+9.68958  +1.02907      * pmax(0, Perm+13.8203)                         \
    -0.96364     * pmax(0, -13.8203-Perm) +0.0622064    * Thick                                    \
    +0.000214981  * pmax(0, Depth-2609.14)                         \
    -0.000299403 * pmax(0, 2609.14-Depth) -0.00129966  * Thick*Thick                                 \
    +4.20704      * pmax(0, GeoGrad-0.0275088)                       \
    -9.37216     * pmax(0, 0.0275088-GeoGrad)                       \
    +1.2904e-05   * Thick*Thick*Thick                              \
    -4.6748e-08  * Thick*Thick*Thick*Thick                           \
    +8.33973e-08  * pmax(0, Depth-1527.78)*Thick                      \
    -4.16266e-07 * pmax(0, 1527.78-Depth)*Thick                      \
    -2.3873e-08  * pmax(0, Depth-2992.66)*pmax(0, Depth-2609.14)                    \
    -0.122865    * pmax(0, Poro-0.136827)*pmax(0, Perm+13.8203)          \
    +0.776807     * pmax(0, 0.136827-Poro)*pmax(0, Perm+13.8203)          \
    -2.08408e-05 * pmax(0, Depth-1742.79)*pmax(0, Perm+13.8203)           \
    +3.61977e-05  * pmax(0, 1742.79-Depth)*pmax(0, Perm+13.8203)           \
    +4.32874e-08  * pmax(0, Depth-1820.93)*pmax(0, 2609.14-Depth)           \
    -1.15744e-07 * pmax(0, 1820.93-Depth)*pmax(0, 2609.14-Depth)           
    ROM_5_LogMCO2_35yr = 10 ** ROM_5_LogMCO2_35yr / 1000000000 / 30           
    return ROM_5_LogMCO2_35yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogMCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogMCO2_35yr =+10.4878 +1.003        * pmax(0, Perm+13.0906)                        \
    -0.981348    * pmax(0, -13.0906-Perm)                       \
    +0.0587306    * Thick                                   \
    +0.000173494  * pmax(0, Depth-2454.98)                        \
    -0.000269142 * pmax(0, 2454.98-Depth)                        \
    -0.00117456  * Thick*Thick                                \
    +2.9372       * pmax(0, GeoGrad-0.032782)                       \
    -8.22067     * pmax(0, 0.032782-GeoGrad)                       \
    +1.13131e-05  * Thick*Thick*Thick                             \
    -4.00289e-08 * Thick*Thick*Thick*Thick                                  \
    -4.00839e-07 * pmax(0, 4112.23-Depth)*Thick                     \
    -0.0933377   * pmax(0, Poro-0.143059)                       \
    +0.351648     * pmax(0, 0.143059-Poro)                       \
    +6.00223e-08  * pmax(0, Depth-1791.59)*pmax(0, 2454.98-Depth)          \
    -1.20455e-07 * pmax(0, 1791.59-Depth)*pmax(0, 2454.98-Depth)          \
    -1.60942e-08 * pmax(0, Depth-3772.21)*pmax(0, Depth-2454.98)          \
    +5.07775e-08  * pmax(0, 3772.21-Depth)*pmax(0, Depth-2454.98)          
    ROM_6_LogMCO2_35yr = 10 ** ROM_6_LogMCO2_35yr / 1000000000 / 30           
    return ROM_6_LogMCO2_35yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogMCO2_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogMCO2_35yr =+24.9117 +1.14559      * Perm                                      \
    -1.90233e-05 * pmax(0, Depth-2670.3)                                     \
    +0.0557485    * Thick  -0.00106822  * Thick*Thick                                   \
    -0.218876    * pmax(0, GeoGrad-0.032243)*Perm                       \
    +0.639909     * pmax(0, 0.032243-GeoGrad)*Perm                       \
    +9.87718e-06  * Thick*Thick*Thick                                \
    -3.39695e-08 * Thick*Thick*Thick*Thick                             \
    -0.00210888  * pmax(0, Perm+12.8915)*Thick                        \
    +0.00116025   * pmax(0, -12.8915-Perm)*Thick                       \
    -2.30782     * pmax(0, Poro-0.190741)                          \
    +2.55893      * pmax(0, 0.190741-Poro)                          \
    -1.92142e-05 * pmax(0, Depth-1515.68)*Perm                        \
    +4.20941e-05  * pmax(0, 1515.68-Depth)*Perm                        \
    +2.10713e-09  * pmax(0, Depth-3925.38)*pmax(0, Depth-1515.68)*Perm          \
    -3.33925e-09 * pmax(0, 3925.38-Depth)*pmax(0, Depth-1515.68)*Perm          \
    -0.172417    * pmax(0, Poro-0.082106)*Perm                       \
    +0.142006     * pmax(0, 0.082106-Poro)*Perm                      
    ROM_7_LogMCO2_35yr = 10 ** ROM_7_LogMCO2_35yr / 1000000000 / 30          
    return ROM_7_LogMCO2_35yr 
#################################################################################### 
# 40 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogMCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogMCO2_40yr =+8.72119   +0.0155274    * Thick                                      \
    +1.43909e-05  * pmax(0, Depth-1754.41)*Thick                        \
    -1.19843e-06 * pmax(0, 1754.41-Depth)*Thick                        \
    +0.94817      * pmax(0, Perm+14.5911)                           \
    -0.886394    * pmax(0, -14.5911-Perm)                          \
    +4.54755      * pmax(0, GeoGrad-0.0194368)                         \
    -8.13209     * pmax(0, 0.0194368-GeoGrad)                         \
    +0.000195043  * pmax(0, Depth-1826.12)                           \
    -0.00044985  * pmax(0, 1826.12-Depth)                           \
    -8.69238e-05 * pmax(0, Thick-90)*Thick                             \
    +0.000642946  * pmax(0, 90-Thick)*Thick                             \
    -1.49031e-05 * Thick*pmax(0, 90-Thick)*Thick                          \
    +1.18278e-07  * Thick*Thick*pmax(0, 90-Thick)*Thick                       \
    -2.64697e-08 * pmax(0, Depth-2568.81)*pmax(0, Depth-1826.12)             \
    -8.34289e-08 * pmax(0, 2568.81-Depth)*pmax(0, Depth-1826.12)             \
    -8.26635e-09 * pmax(0, Depth-1754.41)*Thick*pmax(0, 90-Thick)*Thick                     \
    -9.40228     * pmax(0, GeoGrad-0.0366303)*pmax(0, -14.5911-Perm)          \
    -4.21874     * pmax(0, 0.0366303-GeoGrad)*pmax(0, -14.5911-Perm)        
    ROM_1_LogMCO2_40yr = 10 ** ROM_1_LogMCO2_40yr / 1000000000 / 30          
    return ROM_1_LogMCO2_40yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogMCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogMCO2_40yr =+22.8518   +0.938939     * Perm                                        \
    +0.063501     * Thick                                        \
    -2.63072e-05 * pmax(0, Depth-2496.48)*Perm                          \
    +3.1984e-05   * pmax(0, 2496.48-Depth)*Perm                          \
    -0.00140473  * Thick*Thick                                     \
    +1.467e-05    * Thick*Thick*Thick                                  \
    -0.216002    * pmax(0, GeoGrad-0.0330801)*Perm                        \
    +0.542824     * pmax(0, 0.0330801-GeoGrad)*Perm                        \
    -5.53909e-08 * Thick*Thick*Thick*Thick                               \
    -0.000119157 * pmax(0, Depth-1449.74)                             \
    -0.000105694 * pmax(0, 1449.74-Depth)                             \
    -2.79854e-08 * pmax(0, Depth-2496.48)*pmax(0, Depth-1449.74)               \
    +6.52329e-08  * pmax(0, 2496.48-Depth)*pmax(0, Depth-1449.74)                        \
    -0.000140975 * pmax(0, 2250.43-Depth)*pmax(0, 0.0330801-GeoGrad)*Perm          
    ROM_2_LogMCO2_40yr = 10 ** ROM_2_LogMCO2_40yr / 1000000000 / 30         
    return ROM_2_LogMCO2_40yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogMCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogMCO2_40yr =+23.0053 +0.954517     * Perm                                    \
    +0.0614392    * Thick                                    \
    -1.76566e-05 * pmax(0, Depth-2656.39)*Perm                      \
    +2.25429e-05  * pmax(0, 2656.39-Depth)*Perm                      \
    -0.00131419  * Thick*Thick                                 \
    +1.3393e-05   * Thick*Thick*Thick                              \
    -0.210209    * pmax(0, GeoGrad-0.0334528)*Perm                    \
    +0.517561     * pmax(0, 0.0334528-GeoGrad)*Perm                    \
    -4.96373e-08 * Thick*Thick*Thick*Thick                                   \
    -0.00022222  * pmax(0, 1510.02-Depth)                         \
    -2.59127e-08 * pmax(0, Depth-2622.72)*pmax(0, Depth-1510.02)           \
    +6.39329e-08  * pmax(0, 2622.72-Depth)*pmax(0, Depth-1510.02)           \
    -6.08626e-05 * pmax(0, Perm+13.8781)*pmax(0, Depth-1510.02)                 
    ROM_3_LogMCO2_40yr = 10 ** ROM_3_LogMCO2_40yr / 1000000000 / 30          
    return ROM_3_LogMCO2_40yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogMCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogMCO2_40yr =+9.30419   +0.982343     * pmax(0, Perm+14.1975)                       \
    -0.952687    * pmax(0, -14.1975-Perm)                      \
    +0.0634512    * Thick                                  \
    +0.000188667  * pmax(0, Depth-2383.1)                        \
    -0.00025443  * pmax(0, 2383.1-Depth)                        \
    -0.00132748  * Thick*Thick                               \
    +4.42917      * pmax(0, GeoGrad-0.025134)                      \
    -10.1535     * pmax(0, 0.025134-GeoGrad)                      \
    +1.32466e-05  * Thick*Thick*Thick                            \
    -4.81677e-08 * Thick*Thick*Thick*Thick                                  \
    -2.81229e-07 * pmax(0, 4034.13-Depth)*Thick                            \
    -1.12787e-07 * pmax(0, 2121.88-Depth)*pmax(0, 2383.1-Depth)          \
    -1.88815e-08 * pmax(0, Depth-3967.91)*pmax(0, Depth-2383.1)          \
    +3.65504e-08  * pmax(0, 3967.91-Depth)*pmax(0, Depth-2383.1)          
    ROM_4_LogMCO2_40yr = 10 ** ROM_4_LogMCO2_40yr / 1000000000 / 30          
    return ROM_4_LogMCO2_40yr 
#############
# ROM: 1-10
#############
def ROM_5_LogMCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogMCO2_40yr =+ 9.74305    + 1.03762      * pmax(0, Perm+13.8203)                        \
    + -0.967452    * pmax(0, -13.8203-Perm)  + 0.0624727    * Thick                                   \
    + 0.00021322   * pmax(0, Depth-2609.14)                        \
    + -0.000300178 * pmax(0, 2609.14-Depth)                        \
    + -0.0013056   * Thick*Thick                                \
    + 4.1989       * pmax(0, GeoGrad-0.0275088)                      \
    + -9.37237     * pmax(0, 0.0275088-GeoGrad)                      \
    + 1.29621e-05  * Thick*Thick*Thick                             \
    + -4.69524e-08 * Thick*Thick*Thick*Thick                          \
    + 8.24575e-08  * pmax(0, Depth-1527.78)*Thick                     \
    + -4.21554e-07 * pmax(0, 1527.78-Depth)*Thick                     \
    + -0.133687    * pmax(0, Poro-0.136827)*pmax(0, Perm+13.8203)         \
    + 0.839902     * pmax(0, 0.136827-Poro)*pmax(0, Perm+13.8203)         \
    + -2.38684e-08 * pmax(0, Depth-3067.14)*pmax(0, Depth-2609.14)                 \
    + -2.19023e-05 * pmax(0, Depth-1742.79)*pmax(0, Perm+13.8203)          \
    + 3.75452e-05  * pmax(0, 1742.79-Depth)*pmax(0, Perm+13.8203)          \
    + 4.268e-08    * pmax(0, Depth-1820.93)*pmax(0, 2609.14-Depth)          \
    + -1.15963e-07 * pmax(0, 1820.93-Depth)*pmax(0, 2609.14-Depth)          
    ROM_5_LogMCO2_40yr = 10 ** ROM_5_LogMCO2_40yr / 1000000000 / 30        
    return ROM_5_LogMCO2_40yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogMCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogMCO2_40yr =+10.5874   +1.01159      * pmax(0, Perm+13.0746)                        \
    -0.985889    * pmax(0, -13.0746-Perm)                       \
    +0.0592665    * Thick                                   \
    +0.000141175  * pmax(0, Depth-2456.12)                        \
    -0.000273307 * pmax(0, 2456.12-Depth)                        \
    -0.00118444  * Thick*Thick                                \
    +3.01207      * pmax(0, GeoGrad-0.0327909)                      \
    -8.13059     * pmax(0, 0.0327909-GeoGrad)                      \
    +1.14258e-05  * Thick*Thick*Thick                             \
    -4.04587e-08 * Thick*Thick*Thick*Thick                          \
    -2.75275e-07 * pmax(0, Depth-4118.42)*Thick                     \
    -5.21828e-07 * pmax(0, 4118.42-Depth)*Thick                     \
    -0.0374569   * pmax(0, Poro-0.139631)                       \
    +0.406054     * pmax(0, 0.139631-Poro)                       \
    -7.97348e-08 * pmax(0, Depth-1793.99)*pmax(0, 2456.12-Depth)          \
    -1.06154e-07 * pmax(0, 1793.99-Depth)*pmax(0, 2456.12-Depth)                  \
    -0.000103431 * pmax(0, 3429.8-Depth)*pmax(0, Poro-0.139631)          
    ROM_6_LogMCO2_40yr = 10 ** ROM_6_LogMCO2_40yr / 1000000000 / 30           
    return ROM_6_LogMCO2_40yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogMCO2_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogMCO2_40yr =+25.0815 +1.15503      * Perm                                      \
    -3.31759e-05 * pmax(0, Depth-2598.44)                                    \
    +0.056061     * Thick                                      \
    -0.00107649  * Thick*Thick                                   \
    -0.219336    * pmax(0, GeoGrad-0.0321691)*Perm                      \
    +0.63966      * pmax(0, 0.0321691-GeoGrad)*Perm                      \
    +9.971e-06    * Thick*Thick*Thick                                \
    -3.43391e-08 * Thick*Thick*Thick*Thick                             \
    -0.00216582  * pmax(0, Perm+12.896)*Thick                         \
    +0.00118293   * pmax(0, -12.896-Perm)*Thick                        \
    -2.32871     * pmax(0, Poro-0.190451)                          \
    +2.58927      * pmax(0, 0.190451-Poro)                          \
    -1.95442e-05 * pmax(0, Depth-1493.19)*Perm                        \
    +4.2787e-05   * pmax(0, 1493.19-Depth)*Perm                        \
    +1.96188e-09  * pmax(0, Depth-4088.68)*pmax(0, Depth-1493.19)*Perm          \
    -2.88622e-09 * pmax(0, 4088.68-Depth)*pmax(0, Depth-1493.19)*Perm          \
    -0.17349     * pmax(0, Poro-0.0811778)*Perm                      \
    +0.138349     * pmax(0, 0.0811778-Poro)*Perm                      
    ROM_7_LogMCO2_40yr = 10 ** ROM_7_LogMCO2_40yr / 1000000000 / 30           
    return ROM_7_LogMCO2_40yr 
#################################################################################### 
# 45 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogMCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogMCO2_45yr =+8.77211    +0.0155049    * Thick                                      \
    +1.44619e-05  * pmax(0, Depth-1754.41)*Thick                        \
    -1.22469e-06 * pmax(0, 1754.41-Depth)*Thick                        \
    +0.948386     * pmax(0, Perm+14.5911)                           \
    -0.886445    * pmax(0, -14.5911-Perm)                          \
    +4.48965      * pmax(0, GeoGrad-0.0194368)                         \
    -7.87526     * pmax(0, 0.0194368-GeoGrad)                         \
    +0.000194388  * pmax(0, Depth-1826.12)                           \
    -0.000448868 * pmax(0, 1826.12-Depth)                           \
    -8.56244e-05 * pmax(0, Thick-90)*Thick                             \
    +0.000642206  * pmax(0, 90-Thick)*Thick                             \
    -1.48862e-05 * Thick*pmax(0, 90-Thick)*Thick                          \
    +1.1821e-07   * Thick*Thick*pmax(0, 90-Thick)*Thick                       \
    -2.64438e-08 * pmax(0, Depth-2568.81)*pmax(0, Depth-1826.12)             \
    -8.34223e-08 * pmax(0, 2568.81-Depth)*pmax(0, Depth-1826.12)             \
    -8.30301e-09 * pmax(0, Depth-1754.41)*Thick*pmax(0, 90-Thick)*Thick                    \
    -8.47981     * pmax(0, GeoGrad-0.0356656)*pmax(0, -14.5911-Perm)          \
    -4.52516     * pmax(0, 0.0356656-GeoGrad)*pmax(0, -14.5911-Perm)          
    ROM_1_LogMCO2_45yr = 10 ** ROM_1_LogMCO2_45yr / 1000000000 / 30          
    return ROM_1_LogMCO2_45yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogMCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogMCO2_45yr =+22.92  +0.939832     * Perm                                        \
    +0.0634996    * Thick                                        \
    -2.66775e-05 * pmax(0, Depth-2496.48)*Perm                          \
    +3.23745e-05  * pmax(0, 2496.48-Depth)*Perm                          \
    -0.00140512  * Thick*Thick                                     \
    +1.46735e-05  * Thick*Thick*Thick                                  \
    -0.214145    * pmax(0, GeoGrad-0.0330801)*Perm                        \
    +0.539035     * pmax(0, 0.0330801-GeoGrad)*Perm                       \
    -5.54001e-08 * Thick*Thick*Thick*Thick                               \
    -0.000124722 * pmax(0, Depth-1449.74)                             \
    -0.000100228 * pmax(0, 1449.74-Depth)                             \
    -2.79872e-08 * pmax(0, Depth-2496.48)*pmax(0, Depth-1449.74)       \
    +6.53715e-08  * pmax(0, 2496.48-Depth)*pmax(0, Depth-1449.74)       \
    -0.000143787 * pmax(0, 2250.43-Depth)*pmax(0, 0.0330801-GeoGrad)*Perm  
    ROM_2_LogMCO2_45yr = 10 ** ROM_2_LogMCO2_45yr / 1000000000 / 30          
    return ROM_2_LogMCO2_45yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogMCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogMCO2_45yr =+23.0816   +0.95644      * Perm                                    \
    +0.061494     * Thick                                    \
    -1.76774e-05 * pmax(0, Depth-2656.39)*Perm                      \
    +2.25499e-05  * pmax(0, 2656.39-Depth)*Perm                      \
    -0.0013159   * Thick*Thick                                 \
    +1.34107e-05  * Thick*Thick*Thick                              \
    -0.209138    * pmax(0, GeoGrad-0.0334528)*Perm                    \
    +0.514043     * pmax(0, 0.0334528-GeoGrad)*Perm                    \
    -4.97015e-08 * Thick*Thick*Thick*Thick                                   \
    -0.000221682 * pmax(0, 1510.02-Depth)                         \
    -2.5991e-08  * pmax(0, Depth-2622.72)*pmax(0, Depth-1510.02)           \
    +6.44067e-08  * pmax(0, 2622.72-Depth)*pmax(0, Depth-1510.02)           \
    -6.18757e-05 * pmax(0, Perm+13.8781)*pmax(0, Depth-1510.02)            
    ROM_3_LogMCO2_45yr = 10 ** ROM_3_LogMCO2_45yr / 1000000000 / 30          
    return ROM_3_LogMCO2_45yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogMCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogMCO2_45yr =+9.34803   +0.996558     * pmax(0, Perm+14.1975)                         \
    -0.953507    * pmax(0, -14.1975-Perm)                        \
    +0.0634765    * Thick                                    \
    +0.000189698  * pmax(0, Depth-2383.1)                          \
    -0.000249993 * pmax(0, 2383.1-Depth)                          \
    -0.00132452  * Thick*Thick                                 \
    +4.44361      * pmax(0, GeoGrad-0.025134)                        \
    -10.0278     * pmax(0, 0.025134-GeoGrad)                        \
    +1.31926e-05  * Thick*Thick*Thick                              \
    -4.79099e-08 * Thick*Thick*Thick*Thick                                   \
    -2.86157e-07 * pmax(0, 4034.13-Depth)*Thick                              \
    -1.17009e-07 * pmax(0, 2121.88-Depth)*pmax(0, 2383.1-Depth)            \
    -0.0724107   * pmax(0, Poro-0.103072)*pmax(0, Perm+14.1975)          \
    +0.851355     * pmax(0, 0.103072-Poro)*pmax(0, Perm+14.1975)          \
    -1.91079e-08 * pmax(0, Depth-3950.1)*pmax(0, Depth-2383.1)             \
    +3.81171e-08  * pmax(0, 3950.1-Depth)*pmax(0, Depth-2383.1)             
    ROM_4_LogMCO2_45yr = 10 ** ROM_4_LogMCO2_45yr / 1000000000 / 30         
    return ROM_4_LogMCO2_45yr 
#############
# ROM: 1-10
#############
def ROM_5_LogMCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogMCO2_45yr =+9.79    +1.04549      * pmax(0, Perm+13.8203)                         \
    -0.971123    * pmax(0, -13.8203-Perm)                        \
    +0.0627131    * Thick                                    \
    +0.000213438  * pmax(0, Depth-2609.14)                         \
    -0.000300637 * pmax(0, 2609.14-Depth)                         \
    -0.00131093  * Thick*Thick                                 \
    +4.19215      * pmax(0, GeoGrad-0.0275088)                       \
    -9.37492     * pmax(0, 0.0275088-GeoGrad)                       \
    +1.30138e-05  * Thick*Thick*Thick                              \
    -4.7133e-08  * Thick*Thick*Thick*Thick                           \
    +8.18562e-08  * pmax(0, Depth-1527.78)*Thick                      \
    -4.28299e-07 * pmax(0, 1527.78-Depth)*Thick                      \
    -0.143697    * pmax(0, Poro-0.136827)*pmax(0, Perm+13.8203)          \
    +0.897736     * pmax(0, 0.136827-Poro)*pmax(0, Perm+13.8203)          \
    -2.39255e-08 * pmax(0, Depth-3067.14)*pmax(0, Depth-2609.14)                  \
    -2.28774e-05 * pmax(0, Depth-1742.79)*pmax(0, Perm+13.8203)           \
    +3.86768e-05  * pmax(0, 1742.79-Depth)*pmax(0, Perm+13.8203)           \
    +4.31918e-08  * pmax(0, Depth-1820.93)*pmax(0, 2609.14-Depth)           \
    -1.16206e-07 * pmax(0, 1820.93-Depth)*pmax(0, 2609.14-Depth)           
    ROM_5_LogMCO2_45yr = 10 ** ROM_5_LogMCO2_45yr / 1000000000 / 30           
    return ROM_5_LogMCO2_45yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogMCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogMCO2_45yr =+10.6245  +1.01546      * pmax(0, Perm+13.0906)                        \
    -0.98956     * pmax(0, -13.0906-Perm)                       \
    +0.0594289    * Thick                                   \
    +0.000140122  * pmax(0, Depth-2450.13)                        \
    -0.000271692 * pmax(0, 2450.13-Depth)                        \
    -0.00118852  * Thick*Thick                                \
    +2.98344      * pmax(0, GeoGrad-0.0328029)                      \
    -8.10649     * pmax(0, 0.0328029-GeoGrad)                      \
    +1.14698e-05  * Thick*Thick*Thick                             \
    -4.06235e-08 * Thick*Thick*Thick*Thick                          \
    -2.67327e-07 * pmax(0, Depth-4115.42)*Thick                     \
    -5.33324e-07 * pmax(0, 4115.42-Depth)*Thick                     \
    -0.0424797   * pmax(0, Poro-0.139473)                       \
    +0.433362     * pmax(0, 0.139473-Poro)                       \
    -8.23e-08    * pmax(0, Depth-1795.42)*pmax(0, 2450.13-Depth)          \
    -1.06345e-07 * pmax(0, 1795.42-Depth)*pmax(0, 2450.13-Depth)                   \
    -0.000105606 * pmax(0, 3429.8-Depth)*pmax(0, Poro-0.139473)          
    ROM_6_LogMCO2_45yr = 10 ** ROM_6_LogMCO2_45yr / 1000000000 / 30          
    return ROM_6_LogMCO2_45yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogMCO2_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogMCO2_45yr =+25.2014 +1.16099      * Perm                                     \
    -2.46762e-05 * pmax(0, Depth-2577.8)                                 \
    +0.0562644    * Thick                                     \
    -0.00108201  * Thick*Thick                                  \
    -0.215569    * pmax(0, GeoGrad-0.0322884)*Perm                     \
    +0.637119     * pmax(0, 0.0322884-GeoGrad)*Perm                     \
    +1.00306e-05  * Thick*Thick*Thick                               \
    -3.45657e-08 * Thick*Thick*Thick*Thick                            \
    -0.00220104  * pmax(0, Perm+12.8922)*Thick                       \
    +0.00121911   * pmax(0, -12.8922-Perm)*Thick                      \
    -2.38492     * pmax(0, Poro-0.190451)                         \
    +2.65755      * pmax(0, 0.190451-Poro)                         \
    -1.99106e-05 * pmax(0, Depth-1475.5)*Perm                        \
    +4.28006e-05  * pmax(0, 1475.5-Depth)*Perm                        \
    +2.13371e-09  * pmax(0, Depth-3813.06)*pmax(0, Depth-1475.5)*Perm          \
    -3.40341e-09 * pmax(0, 3813.06-Depth)*pmax(0, Depth-1475.5)*Perm          \
    -0.177508    * pmax(0, Poro-0.0822888)*Perm                     
    ROM_7_LogMCO2_45yr = 10 ** ROM_7_LogMCO2_45yr / 1000000000 / 30           
    return ROM_7_LogMCO2_45yr 
#################################################################################### 
# 50 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogMCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogMCO2_50yr =+8.81759  +0.0154852    * Thick                                      \
    +1.451e-05    * pmax(0, Depth-1754.41)*Thick                        \
    -1.24291e-06 * pmax(0, 1754.41-Depth)*Thick                        \
    +0.94856      * pmax(0, Perm+14.5911)                           \
    -0.886777    * pmax(0, -14.5911-Perm)                          \
    +4.42127      * pmax(0, GeoGrad-0.0194368)                         \
    -7.75349     * pmax(0, 0.0194368-GeoGrad)                         \
    +0.000193938  * pmax(0, Depth-1826.12)                           \
    -0.000447856 * pmax(0, 1826.12-Depth)                           \
    -8.53e-05    * pmax(0, Thick-90)*Thick                             \
    +0.000641767  * pmax(0, 90-Thick)*Thick                             \
    -1.488e-05   * Thick*pmax(0, 90-Thick)*Thick                          \
    +1.18183e-07  * Thick*Thick*pmax(0, 90-Thick)*Thick                       \
    -2.64406e-08 * pmax(0, Depth-2568.81)*pmax(0, Depth-1826.12)             \
    -8.26955e-08 * pmax(0, 2568.81-Depth)*pmax(0, Depth-1826.12)             \
    -8.32699e-09 * pmax(0, Depth-1754.41)*Thick*pmax(0, 90-Thick)*Thick                    \
    -8.42535     * pmax(0, GeoGrad-0.0356656)*pmax(0, -14.5911-Perm)          \
    -4.52269     * pmax(0, 0.0356656-GeoGrad)*pmax(0, -14.5911-Perm)          
    ROM_1_LogMCO2_50yr = 10 ** ROM_1_LogMCO2_50yr / 1000000000 / 30           
    return ROM_1_LogMCO2_50yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogMCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogMCO2_50yr =+22.9835   +0.940643     * Perm                                        \
    +0.0635044    * Thick                                        \
    -2.70425e-05 * pmax(0, Depth-2496.48)*Perm                          \
    +3.27714e-05  * pmax(0, 2496.48-Depth)*Perm                          \
    -0.00140555  * Thick*Thick                                     \
    +1.46761e-05  * Thick*Thick*Thick                                  \
    -0.207468    * pmax(0, GeoGrad-0.0334528)*Perm                        \
    +0.531013     * pmax(0, 0.0334528-GeoGrad)*Perm                        \
    -5.54009e-08 * Thick*Thick*Thick*Thick                               \
    -0.00013019  * pmax(0, Depth-1449.74)                             \
    -9.49707e-05 * pmax(0, 1449.74-Depth)                             \
    -2.79955e-08 * pmax(0, Depth-2496.48)*pmax(0, Depth-1449.74)               \
    +6.53988e-08  * pmax(0, 2496.48-Depth)*pmax(0, Depth-1449.74)                       \
    -0.00014308  * pmax(0, 2250.43-Depth)*pmax(0, 0.0334528-GeoGrad)*Perm          
    ROM_2_LogMCO2_50yr = 10 ** ROM_2_LogMCO2_50yr / 1000000000 / 30           
    return ROM_2_LogMCO2_50yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogMCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogMCO2_50yr =+23.1757 +0.956685     * Perm                                    \
    +0.0614678    * Thick                                    \
    -2.03175e-05 * pmax(0, Depth-2656.39)*Perm                      \
    +2.53385e-05  * pmax(0, 2656.39-Depth)*Perm                      \
    -0.00131607  * Thick*Thick                                 \
    +1.34166e-05  * Thick*Thick*Thick                              \
    -0.208418    * pmax(0, GeoGrad-0.0334528)*Perm                    \
    +0.510294     * pmax(0, 0.0334528-GeoGrad)*Perm                    \
    -4.97315e-08 * Thick*Thick*Thick*Thick                           \
    -3.99472e-05 * pmax(0, Depth-1510.02)                         \
    -0.000183996 * pmax(0, 1510.02-Depth)                         \
    -2.56818e-08 * pmax(0, Depth-2622.72)*pmax(0, Depth-1510.02)           \
    +6.34951e-08  * pmax(0, 2622.72-Depth)*pmax(0, Depth-1510.02)           \
    -5.86725e-05 * pmax(0, Perm+13.8781)*pmax(0, Depth-1510.02)                    
    ROM_3_LogMCO2_50yr = 10 ** ROM_3_LogMCO2_50yr / 1000000000 / 30           
    return ROM_3_LogMCO2_50yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogMCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogMCO2_50yr =+9.39087  +1.00254      * pmax(0, Perm+14.1975)                         \
    -0.955488    * pmax(0, -14.1975-Perm)                        \
    +0.0637372    * Thick                                    \
    +0.000189547  * pmax(0, Depth-2383.1)                          \
    -0.000249474 * pmax(0, 2383.1-Depth)                          \
    -0.0013306   * Thick*Thick                                 \
    +1.32538e-05  * Thick*Thick*Thick                              \
    +4.3861       * pmax(0, GeoGrad-0.0255165)                       \
    -9.86318     * pmax(0, 0.0255165-GeoGrad)                       \
    -4.81298e-08 * Thick*Thick*Thick*Thick                                     \
    -2.91171e-07 * pmax(0, 4034.13-Depth)*Thick                                \
    -1.17292e-07 * pmax(0, 2121.88-Depth)*pmax(0, 2383.1-Depth)            \
    -0.0799688   * pmax(0, Poro-0.103072)*pmax(0, Perm+14.1975)          \
    +0.908784     * pmax(0, 0.103072-Poro)*pmax(0, Perm+14.1975)          \
    -1.90563e-08 * pmax(0, Depth-3950.1)*pmax(0, Depth-2383.1)             \
    +3.81831e-08  * pmax(0, 3950.1-Depth)*pmax(0, Depth-2383.1)            
    ROM_4_LogMCO2_50yr = 10 ** ROM_4_LogMCO2_50yr / 1000000000 / 30           
    return ROM_4_LogMCO2_50yr 
#############
# ROM: 1-10
#############
def ROM_5_LogMCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogMCO2_50yr =+9.83206   +1.05273      * pmax(0, Perm+13.8203)                         \
    -0.974635    * pmax(0, -13.8203-Perm)                        \
    +0.0629318    * Thick                                    \
    +0.000213633  * pmax(0, Depth-2609.14)                         \
    -0.000300947 * pmax(0, 2609.14-Depth)                         \
    -0.00131572  * Thick*Thick                                 \
    +4.18604      * pmax(0, GeoGrad-0.0275088)                       \
    -9.37858     * pmax(0, 0.0275088-GeoGrad)                       \
    +1.30603e-05  * Thick*Thick*Thick                              \
    -4.72946e-08 * Thick*Thick*Thick*Thick                           \
    +8.14042e-08  * pmax(0, Depth-1539.25)*Thick                      \
    -4.26277e-07 * pmax(0, 1539.25-Depth)*Thick                      \
    -0.152976    * pmax(0, Poro-0.136827)*pmax(0, Perm+13.8203)          \
    +0.950987     * pmax(0, 0.136827-Poro)*pmax(0, Perm+13.8203)          \
    -2.3981e-08  * pmax(0, Depth-3067.14)*pmax(0, Depth-2609.14)                    \
    -2.37685e-05 * pmax(0, Depth-1742.79)*pmax(0, Perm+13.8203)           \
    +3.96506e-05  * pmax(0, 1742.79-Depth)*pmax(0, Perm+13.8203)           \
    +4.3393e-08   * pmax(0, Depth-1820.93)*pmax(0, 2609.14-Depth)           \
    -1.16491e-07 * pmax(0, 1820.93-Depth)*pmax(0, 2609.14-Depth)           
    ROM_5_LogMCO2_50yr = 10 ** ROM_5_LogMCO2_50yr / 1000000000 / 30        
    return ROM_5_LogMCO2_50yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogMCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogMCO2_50yr =+10.6879   +1.01945      * pmax(0, Perm+13.0755)                        \
    -0.993101    * pmax(0, -13.0755-Perm)                       \
    +0.0595821    * Thick                                   \
    +0.000138938  * pmax(0, Depth-2450.13)                        \
    -0.000269846 * pmax(0, 2450.13-Depth)                        \
    -0.00119263  * Thick*Thick                                \
    +2.98265      * pmax(0, GeoGrad-0.0327267)                      \
    -8.09524     * pmax(0, 0.0327267-GeoGrad)                      \
    +1.1515e-05   * Thick*Thick*Thick                             \
    -4.07942e-08 * Thick*Thick*Thick*Thick                          \
    -2.58078e-07 * pmax(0, Depth-4121.33)*Thick                     \
    -5.40207e-07 * pmax(0, 4121.33-Depth)*Thick                     \
    -0.0466667   * pmax(0, Poro-0.140024)                       \
    +0.45061      * pmax(0, 0.140024-Poro)                       \
    -8.08267e-08 * pmax(0, Depth-1793.99)*pmax(0, 2450.13-Depth)          \
    -1.06785e-07 * pmax(0, 1793.99-Depth)*pmax(0, 2450.13-Depth)                   \
    -0.000107923 * pmax(0, 3429.8-Depth)*pmax(0, Poro-0.140024)          
    ROM_6_LogMCO2_50yr = 10 ** ROM_6_LogMCO2_50yr / 1000000000 / 30           
    return ROM_6_LogMCO2_50yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogMCO2_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogMCO2_50yr =+25.3229  +1.16684      * Perm                                      \
    -2.53681e-05 * pmax(0, Depth-2573.68)                                  \
    +0.0564746    * Thick                                      \
    -0.00108805  * Thick*Thick                                   \
    -0.215497    * pmax(0, GeoGrad-0.0322245)*Perm                      \
    +0.636192     * pmax(0, 0.0322245-GeoGrad)*Perm                      \
    +1.00996e-05  * Thick*Thick*Thick                                \
    -3.48429e-08 * Thick*Thick*Thick*Thick                             \
    -0.00223407  * pmax(0, Perm+12.8878)*Thick                        \
    +0.00125463   * pmax(0, -12.8878-Perm)*Thick                       \
    -2.44419     * pmax(0, Poro-0.18992)                           \
    +2.72805      * pmax(0, 0.18992-Poro)                           \
    -1.9864e-05  * pmax(0, Depth-1481.55)*Perm                        \
    +4.25418e-05  * pmax(0, 1481.55-Depth)*Perm                        \
    +2.11931e-09  * pmax(0, Depth-3809.66)*pmax(0, Depth-1481.55)*Perm          \
    -3.36708e-09 * pmax(0, 3809.66-Depth)*pmax(0, Depth-1481.55)*Perm          \
    -0.181719    * pmax(0, Poro-0.0822888)*Perm                      \
    +0.145342     * pmax(0, 0.0822888-Poro)*Perm                    
    ROM_7_LogMCO2_50yr = 10 ** ROM_7_LogMCO2_50yr / 1000000000 / 30           
    return ROM_7_LogMCO2_50yr    


#################################################################################### 
# 5 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogArea_5yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogArea_5yr =+6.50011     -1.33968     * pmax(0, Poro-0.154993)                             \
    +3.27765      * pmax(0, 0.154993-Poro)  +0.743774     * pmax(0, Perm+14.7726)                              \
    -0.826724    * pmax(0, -14.7726-Perm)    +6.07528e-05  * pmax(0, Depth-2583.14)                              \
    -0.00017246  * pmax(0, 2583.14-Depth)    +4.25977      * pmax(0, GeoGrad-0.0373301)                          \
    -7.67852     * pmax(0, 0.0373301-GeoGrad)                                     \
    +32.6138      * pmax(0, 0.0752091-Poro)*pmax(0, 0.154993-Poro)                      \
    -9.5041e-08  * pmax(0, 1423.6-Depth)*pmax(0, 2583.14-Depth)                 \
    +1.27214      * pmax(0, GeoGrad-0.0385987)*Thick*pmax(0, Poro-0.154993)          \
    -0.316127    * pmax(0, 0.0385987-GeoGrad)*Thick*pmax(0, Poro-0.154993)          \
    +0.00720933   * Thick*pmax(0, Perm+14.7726)                                   \
    -2.12184     * pmax(0, 0.4276-Poro)*pmax(0, Poro-0.154993)                \
    +1.75495e-05  * pmax(0, Depth-2301.76)*Thick*pmax(0, Poro-0.154993)            \
    -2.11622e-06 * pmax(0, 2301.76-Depth)*Thick*pmax(0, Poro-0.154993)            
    ROM_1_LogArea_5yr = 10 ** ROM_1_LogArea_5yr
    return ROM_1_LogArea_5yr
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogArea_5yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogArea_5yr =+6.41274  +0.826144     * pmax(0, Perm+14.8133)                           \
    -0.916797    * pmax(0, -14.8133-Perm)  -2.19634     * pmax(0, Poro-0.134495)                          \
    +3.86786      * pmax(0, 0.134495-Poro)  +7.09816e-05  * pmax(0, Depth-2397.38)                           \
    -0.000191503 * pmax(0, 2397.38-Depth)  +3.91544      * pmax(0, GeoGrad-0.022249)                          \
    -12.4788     * pmax(0, 0.022249-GeoGrad)  +2.79059      * pmax(0, Poro-0.161831)*pmax(0, Poro-0.134495)          \
    -17.4947     * pmax(0, Poro-0.0641099)*pmax(0, 0.134495-Poro)          \
    +38.8043      * pmax(0, 0.0641099-Poro)*pmax(0, 0.134495-Poro)          \
    +4.0879       * pmax(0, Perm+13.9617)*pmax(0, GeoGrad-0.022249)            \
    +5.38624      * pmax(0, -13.9617-Perm)*pmax(0, GeoGrad-0.022249)           \
    -2.98228e-05 * pmax(0, Perm+14.3981)*pmax(0, 2397.38-Depth)             \
    -0.000115311 * pmax(0, -14.3981-Perm)*pmax(0, 2397.38-Depth)            
    ROM_2_LogArea_5yr = 10 ** ROM_2_LogArea_5yr
    return ROM_2_LogArea_5yr
#############
# ROM: 0.1-1
############# 
def ROM_3_LogArea_5yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogArea_5yr =+7.16942  +0.829277    * pmax(0, Perm+13.9152)                          \
    -0.779038   * pmax(0, -13.9152-Perm)                             \
    -2.05621    * pmax(0, Poro-0.135424)                             \
    +4.04978     * pmax(0, 0.135424-Poro)                             \
    +6.91037e-05 * pmax(0, Depth-2532.38)                              \
    -0.00019718 * pmax(0, 2532.38-Depth)                              \
    +6.56608     * pmax(0, GeoGrad-0.0261206)                            \
    -6.72965    * pmax(0, 0.0261206-GeoGrad)                                   \
    -4.52397    * pmax(0, -14.3174-Perm)*pmax(0, 0.0261206-GeoGrad)             \
    +2.67924     * pmax(0, Poro-0.182168)*pmax(0, Poro-0.135424)                      \
    -18.1028    * pmax(0, Poro-0.0548809)*pmax(0, 0.135424-Poro)             \
    +47.338      * pmax(0, 0.0548809-Poro)*pmax(0, 0.135424-Poro)             \
    -56.839     * Poro*pmax(0, -14.3174-Perm)*pmax(0, 0.0261206-GeoGrad)          
    ROM_3_LogArea_5yr = 10 ** ROM_3_LogArea_5yr
    return ROM_3_LogArea_5yr
#############
# ROM: 0.5-5
############# 
def ROM_4_LogArea_5yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogArea_5yr =+7.45735   +0.85826      * pmax(0, Perm+13.6045)                           \
    -0.796414    * pmax(0, -13.6045-Perm)                          \
    -2.07647     * pmax(0, Poro-0.135424)                          \
    +4.0999       * pmax(0, 0.135424-Poro)                          \
    +6.90195e-05  * pmax(0, Depth-2383.1)                            \
    -0.000218862 * pmax(0, 2383.1-Depth)                            \
    +5.61205      * pmax(0, GeoGrad-0.0300896)                         \
    -8.40801     * pmax(0, 0.0300896-GeoGrad)                         \
    +2.70255      * pmax(0, Poro-0.173883)*pmax(0, Poro-0.135424)                    \
    -17.2252     * pmax(0, Poro-0.0552838)*pmax(0, 0.135424-Poro)          \
    +47.1578      * pmax(0, 0.0552838-Poro)*pmax(0, 0.135424-Poro)          
    ROM_4_LogArea_5yr = 10 ** ROM_4_LogArea_5yr
    return ROM_4_LogArea_5yr
#############
# ROM: 1-10
#############
def ROM_5_LogArea_5yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogArea_5yr =+18.9562   +0.829518     * Perm                                         \
    -3.30198     * pmax(0, Poro-0.134274)                             \
    +4.51683      * pmax(0, 0.134274-Poro)                             \
    -5.29432e-06 * pmax(0, Depth-2279.91)*Perm                           \
    +1.77796e-05  * pmax(0, 2279.91-Depth)*Perm                           \
    -0.393614    * pmax(0, GeoGrad-0.0302376)*Perm                         \
    +0.57223      * pmax(0, 0.0302376-GeoGrad)*Perm                         \
    -0.166484    * pmax(0, Poro-0.277684)*Perm                          \
    +0.0944053    * pmax(0, 0.277684-Poro)*Perm                          \
    +0.196508     * pmax(0, Poro-0.0719274)*pmax(0, 0.277684-Poro)*Perm          \
    -1.27037     * pmax(0, 0.0719274-Poro)*pmax(0, 0.277684-Poro)*Perm         
    ROM_5_LogArea_5yr = 10 ** ROM_5_LogArea_5yr
    return ROM_5_LogArea_5yr
#############
# ROM: 5-50
############# 
def ROM_6_LogArea_5yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogArea_5yr =+7.77187   +0.945704     * pmax(0, Perm+13.1539)                           \
    -0.809325    * pmax(0, -13.1539-Perm)                          \
    -2.06726     * pmax(0, Poro-0.146935)                          \
    +3.84735      * pmax(0, 0.146935-Poro)                          \
    +6.9345e-05   * pmax(0, Depth-2404.97)                           \
    -0.000212592 * pmax(0, 2404.97-Depth)                           \
    +5.54434      * pmax(0, GeoGrad-0.0255306)                         \
    -6.74889     * pmax(0, 0.0255306-GeoGrad)                         \
    -0.0015887   * Thick*pmax(0, Perm+13.1539)                        \
    +2.63042      * pmax(0, Poro-0.189779)*pmax(0, Poro-0.146935)                    \
    -9.20345     * pmax(0, Poro-0.0706691)*pmax(0, 0.146935-Poro)          \
    +37.8664      * pmax(0, 0.0706691-Poro)*pmax(0, 0.146935-Poro)          \
    +0.236535     * pmax(0, Poro-0.186913)*pmax(0, -13.1539-Perm)           \
    -0.601919    * pmax(0, 0.186913-Poro)*pmax(0, -13.1539-Perm)         
    ROM_6_LogArea_5yr = 10 ** ROM_6_LogArea_5yr
    return ROM_6_LogArea_5yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogArea_5yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogArea_5yr =+8.58073  +0.94063      * pmax(0, Perm+12.419)                            \
    -0.957961    * pmax(0, -12.419-Perm)                           \
    -2.07783     * pmax(0, Poro-0.160589)                          \
    +3.78145      * pmax(0, 0.160589-Poro)                          \
    +5.9723e-05   * pmax(0, Depth-2944.65)                           \
    -0.000129442 * pmax(0, 2944.65-Depth)                           \
    +4.3922       * pmax(0, GeoGrad-0.0394786)                         \
    -5.98748     * pmax(0, 0.0394786-GeoGrad)                         \
    -0.0178367   * Thick                                      \
    -0.00132405  * Perm*Thick                                   \
    -9.4657e-09  * pmax(0, Depth-1888.61)*pmax(0, 2944.65-Depth)             \
    -6.02192e-08 * pmax(0, 1888.61-Depth)*pmax(0, 2944.65-Depth)             \
    +0.226958     * pmax(0, Poro-0.0694696)*pmax(0, -12.419-Perm)           \
    -1.34073     * pmax(0, 0.0694696-Poro)*pmax(0, -12.419-Perm)           \
    +2.49611      * pmax(0, Poro-0.18992)*pmax(0, Poro-0.160589)            \
    +22.3736      * pmax(0, 0.18992-Poro)*pmax(0, Poro-0.160589)            \
    -11.2196     * pmax(0, Poro-0.0704181)*pmax(0, 0.160589-Poro)          \
    +42.7618      * pmax(0, 0.0704181-Poro)*pmax(0, 0.160589-Poro)                               
    ROM_7_LogArea_5yr = 10 ** ROM_7_LogArea_5yr
    return ROM_7_LogArea_5yr       
#################################################################################### 
# 10 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogArea_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogArea_10yr =+6.75876   -1.78089     * pmax(0, Poro-0.154993)                          \
    +3.1647       * pmax(0, 0.154993-Poro)                          \
    +0.789316     * pmax(0, Perm+14.7726)                           \
    -0.836693    * pmax(0, -14.7726-Perm)                          \
    +4.3244e-05   * pmax(0, Depth-2583.14)                           \
    -0.000187114 * pmax(0, 2583.14-Depth)                           \
    +5.2168       * pmax(0, GeoGrad-0.0385635)                         \
    -7.32844     * pmax(0, 0.0385635-GeoGrad)                         \
    -16.0373     * pmax(0, Poro-0.0752091)*pmax(0, 0.154993-Poro)          \
    +31.4851      * pmax(0, 0.0752091-Poro)*pmax(0, 0.154993-Poro)          \
    +2.37082      * pmax(0, Poro-0.263399)*pmax(0, Poro-0.154993)           \
    -6.83069     * pmax(0, 0.263399-Poro)*pmax(0, Poro-0.154993)           \
    +4.5092e-08   * pmax(0, Depth-1105.76)*pmax(0, 2583.14-Depth)             \
    -1.30321e-07 * pmax(0, 1105.76-Depth)*pmax(0, 2583.14-Depth)             \
    +4.99074e-06  * Thick*pmax(0, Depth-2583.14)                        
    ROM_1_LogArea_10yr = 10 ** ROM_1_LogArea_10yr
    return ROM_1_LogArea_10yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogArea_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogArea_10yr =+6.6592  +0.821287     * pmax(0, Perm+14.8202)                           \
    -0.86117     * pmax(0, -14.8202-Perm)                          \
    -1.65808     * pmax(0, Poro-0.134495)                          \
    +2.81813      * pmax(0, 0.134495-Poro)                          \
    +6.79299e-05  * pmax(0, Depth-2390.49)                           \
    -0.000213354 * pmax(0, 2390.49-Depth)                           \
    +4.36251      * pmax(0, GeoGrad-0.0220961)                         \
    -10.7533     * pmax(0, 0.0220961-GeoGrad)                                  \
    +34.0986      * pmax(0, 0.0961708-Poro)*pmax(0, 0.134495-Poro)          \
    +2.32543      * pmax(0, Poro-0.332783)*pmax(0, Poro-0.134495)           \
    -3.81306     * pmax(0, 0.332783-Poro)*pmax(0, Poro-0.134495)           \
    +3.66464      * pmax(0, Perm+14.0557)*pmax(0, GeoGrad-0.0220961)           \
    +3.69282      * pmax(0, -14.0557-Perm)*pmax(0, GeoGrad-0.0220961)          
    ROM_2_LogArea_10yr = 10 ** ROM_2_LogArea_10yr
    return ROM_2_LogArea_10yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogArea_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogArea_10yr =+7.35779 +0.859416    * pmax(0, Perm+13.9539)                           \
    -0.78064    * pmax(0, -13.9539-Perm)                          \
    -2.01838    * pmax(0, Poro-0.135424)                          \
    +4.15742     * pmax(0, 0.135424-Poro)                          \
    +6.83272e-05 * pmax(0, Depth-2414)                              \
    -0.00020836 * pmax(0, 2414-Depth)                              \
    +5.71917     * pmax(0, GeoGrad-0.0237892)                         \
    -5.90311    * pmax(0, 0.0237892-GeoGrad)                         \
    +2.70752     * pmax(0, Poro-0.193726)*pmax(0, Poro-0.135424)                   \
    -19.4543    * pmax(0, Poro-0.0523905)*pmax(0, 0.135424-Poro)          \
    +52.3769     * pmax(0, 0.0523905-Poro)*pmax(0, 0.135424-Poro)          \
    +0.617645    * pmax(0, GeoGrad-0.0253757)*pmax(0, -13.9539-Perm)          \
    -7.4685     * pmax(0, 0.0253757-GeoGrad)*pmax(0, -13.9539-Perm)          
    ROM_3_LogArea_10yr = 10 ** ROM_3_LogArea_10yr
    return ROM_3_LogArea_10yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogArea_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogArea_10yr =+7.56426  +0.888447     * pmax(0, Perm+13.7686)                           \
    -0.79228     * pmax(0, -13.7686-Perm)                          \
    -2.09738     * pmax(0, Poro-0.134068)                          \
    +4.26776      * pmax(0, 0.134068-Poro)                          \
    +6.8506e-05   * pmax(0, Depth-2383.1)                            \
    -0.000223223 * pmax(0, 2383.1-Depth)                            \
    +5.49041      * pmax(0, GeoGrad-0.030241)                          \
    -7.73806     * pmax(0, 0.030241-GeoGrad)                          \
    +2.75363      * pmax(0, Poro-0.173883)*pmax(0, Poro-0.134068)                    \
    -18.1721     * pmax(0, Poro-0.0551532)*pmax(0, 0.134068-Poro)          \
    +50.5912      * pmax(0, 0.0551532-Poro)*pmax(0, 0.134068-Poro)          
    ROM_4_LogArea_10yr = 10 ** ROM_4_LogArea_10yr
    return ROM_4_LogArea_10yr 
#############
# ROM: 1-10
#############
def ROM_5_LogArea_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogArea_10yr =+30.8154  +1.61013      * Perm                                         \
    -4.87497     * pmax(0, Poro-0.134274)                             \
    +6.3542       * pmax(0, 0.134274-Poro)                             \
    +2.97987e-06  * pmax(0, Depth-2279.91)*Perm                           \
    +7.78943e-06  * pmax(0, 2279.91-Depth)*Perm                           \
    +5.42509      * pmax(0, GeoGrad-0.0325511)                            \
    -7.06882     * pmax(0, 0.0325511-GeoGrad)                            \
    -0.280357    * pmax(0, Poro-0.276215)*Perm                          \
    +0.206563     * pmax(0, 0.276215-Poro)*Perm                          \
    +0.0595173    * pmax(0, Perm+14.3114)*Perm                           \
    -0.0571691   * pmax(0, -14.3114-Perm)*Perm                          \
    +0.192111     * pmax(0, Poro-0.0709615)*pmax(0, 0.276215-Poro)*Perm          \
    -1.34593     * pmax(0, 0.0709615-Poro)*pmax(0, 0.276215-Poro)*Perm          \
    +9.12843e-05  * pmax(0, Depth-3966.64)                              \
    -0.000126712 * pmax(0, 3966.64-Depth)                              
    ROM_5_LogArea_10yr = 10 ** ROM_5_LogArea_10yr
    return ROM_5_LogArea_10yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogArea_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogArea_10yr =+8.09104 +0.999472     * pmax(0, Perm+13.1539)                           \
    -0.863288    * pmax(0, -13.1539-Perm)                          \
    -2.2105      * pmax(0, Poro-0.146935)                          \
    +4.1209       * pmax(0, 0.146935-Poro)                          \
    +6.96483e-05  * pmax(0, Depth-2404.97)                           \
    -0.000219086 * pmax(0, 2404.97-Depth)                           \
    +5.58857      * pmax(0, GeoGrad-0.0328542)                         \
    -6.96746     * pmax(0, 0.0328542-GeoGrad)                         \
    -0.00152829  * Thick*pmax(0, Perm+13.1539)                        \
    +2.83387      * pmax(0, Poro-0.189779)*pmax(0, Poro-0.146935)                    \
    -10.4531     * pmax(0, Poro-0.0706691)*pmax(0, 0.146935-Poro)          \
    +40.2618      * pmax(0, 0.0706691-Poro)*pmax(0, 0.146935-Poro)          \
    +0.338644     * pmax(0, Poro-0.186913)*pmax(0, -13.1539-Perm)           \
    -0.636704    * pmax(0, 0.186913-Poro)*pmax(0, -13.1539-Perm)           
    ROM_6_LogArea_10yr = 10 ** ROM_6_LogArea_10yr
    return ROM_6_LogArea_10yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogArea_10yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogArea_10yr =+8.88141  +1.02029      * pmax(0, Perm+12.4376)                           \
    -1.01547     * pmax(0, -12.4376-Perm)    -1.95824     * pmax(0, Poro-0.160589)                          \
    +3.27823      * pmax(0, 0.160589-Poro)  +5.95527e-05  * pmax(0, Depth-2944.65)                           \
    -0.000134572 * pmax(0, 2944.65-Depth) +4.71986      * pmax(0, GeoGrad-0.0382944)                         \
    -6.72113     * pmax(0, 0.0382944-GeoGrad)   -0.0013622   * Thick                                      \
    -0.00188286  * pmax(0, Perm+12.414)*Thick   +0.00122826   * pmax(0, -12.414-Perm)*Thick                      \
    -5.43489     * pmax(0, Poro-0.106148)*pmax(0, 0.160589-Poro)           \
    +24.042       * pmax(0, 0.106148-Poro)*pmax(0, 0.160589-Poro)           \
    +2.6536       * pmax(0, Poro-0.29874)*pmax(0, Poro-0.160589)            \
    -4.67216     * pmax(0, 0.29874-Poro)*pmax(0, Poro-0.160589)                     \
    -6.45107e-08 * pmax(0, 1822.78-Depth)*pmax(0, 2944.65-Depth)             \
    +0.250924     * pmax(0, Poro-0.0485233)*pmax(0, -12.4376-Perm)          \
    +2.91433      * pmax(0, 0.0485233-Poro)*pmax(0, -12.4376-Perm)          
    ROM_7_LogArea_10yr = 10 ** ROM_7_LogArea_10yr
    return ROM_7_LogArea_10yr 
#################################################################################### 
# 15 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogArea_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogArea_15yr =+6.70283   -1.74952     * pmax(0, Poro-0.154993)                          \
    +3.17147      * pmax(0, 0.154993-Poro)                          \
    +0.810905     * pmax(0, Perm+14.7726)                           \
    -0.822906    * pmax(0, -14.7726-Perm)                          \
    -9.11523e-05 * pmax(0, Depth-2583.14)                                    \
    +5.08144      * pmax(0, GeoGrad-0.0385635)                         \
    -6.9983      * pmax(0, 0.0385635-GeoGrad)                         \
    -16.2705     * pmax(0, Poro-0.0752091)*pmax(0, 0.154993-Poro)          \
    +32.5802      * pmax(0, 0.0752091-Poro)*pmax(0, 0.154993-Poro)          \
    +0.000150507  * pmax(0, Depth-1423.6)                            \
    -0.000297225 * pmax(0, 1423.6-Depth)                            \
    +2.32271      * pmax(0, Poro-0.263399)*pmax(0, Poro-0.154993)           \
    -6.73652     * pmax(0, 0.263399-Poro)*pmax(0, Poro-0.154993)           \
    +1.8314e-06   * Thick*pmax(0, Depth-1423.6)                         
    ROM_1_LogArea_15yr = 10 ** ROM_1_LogArea_15yr
    return ROM_1_LogArea_15yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogArea_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogArea_15yr =+19.119    +0.832917     * Perm                                         \
    -3.48296     * pmax(0, Poro-0.134495)                             \
    +5.34503      * pmax(0, 0.134495-Poro)                             \
    -1.0821e-05  * pmax(0, Depth-2371.91)*Perm                           \
    +1.93039e-05  * pmax(0, 2371.91-Depth)*Perm                           \
    -0.418719    * pmax(0, GeoGrad-0.0220961)*Perm                         \
    +0.674028     * pmax(0, 0.0220961-GeoGrad)*Perm                         \
    -0.0774985   * pmax(0, Poro-0.0543989)*Perm                         \
    -0.247621    * pmax(0, 0.0543989-Poro)*Perm                         \
    -0.176998    * pmax(0, Poro-0.125515)*pmax(0, Poro-0.0543989)*Perm          \
    +1.704        * pmax(0, 0.125515-Poro)*pmax(0, Poro-0.0543989)*Perm          \
    -8.86099e-05 * pmax(0, Depth-1401.15)                              \
    -4.16017e-05 * pmax(0, 1401.15-Depth)                              
    ROM_2_LogArea_15yr = 10 ** ROM_2_LogArea_15yr
    return ROM_2_LogArea_15yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogArea_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogArea_15yr =+7.4316     +0.869924     * pmax(0, Perm+14.0238)                           \
    -0.77999     * pmax(0, -14.0238-Perm)                          \
    -2.06134     * pmax(0, Poro-0.135424)                          \
    +3.88847      * pmax(0, 0.135424-Poro)                          \
    +6.81312e-05  * pmax(0, Depth-2397.43)                           \
    -0.000212288 * pmax(0, 2397.43-Depth)                           \
    +6.02327      * pmax(0, GeoGrad-0.0223937)                         \
    -9.25784     * pmax(0, 0.0223937-GeoGrad)                         \
    +2.77328      * pmax(0, Poro-0.180245)*pmax(0, Poro-0.135424)                   \
    -20.3336     * pmax(0, Poro-0.0523905)*pmax(0, 0.135424-Poro)          \
    +53.3277      * pmax(0, 0.0523905-Poro)*pmax(0, 0.135424-Poro)          \
    +0.817996     * pmax(0, Perm+14.7684)*pmax(0, 0.135424-Poro)                      
    ROM_3_LogArea_15yr = 10 ** ROM_3_LogArea_15yr
    return ROM_3_LogArea_15yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogArea_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogArea_15yr =+7.69537   +0.913165     * pmax(0, Perm+13.7912)                           \
    -0.798008    * pmax(0, -13.7912-Perm)                          \
    -2.09963     * pmax(0, Poro-0.134068)                          \
    +4.40408      * pmax(0, 0.134068-Poro)                          \
    +6.86166e-05  * pmax(0, Depth-2383.1)                            \
    -0.000225278 * pmax(0, 2383.1-Depth)                            \
    +5.38842      * pmax(0, GeoGrad-0.0316304)                         \
    -7.38585     * pmax(0, 0.0316304-GeoGrad)                         \
    +2.72355      * pmax(0, Poro-0.172569)*pmax(0, Poro-0.134068)           \
    +18.2793      * pmax(0, 0.172569-Poro)*pmax(0, Poro-0.134068)           \
    -17.1586     * pmax(0, Poro-0.0551532)*pmax(0, 0.134068-Poro)          \
    +52.7932      * pmax(0, 0.0551532-Poro)*pmax(0, 0.134068-Poro)          
    ROM_4_LogArea_15yr = 10 ** ROM_4_LogArea_15yr
    return ROM_4_LogArea_15yr 
#############
# ROM: 1-10
#############
def ROM_5_LogArea_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogArea_15yr =+7.74638   +1.00127      * pmax(0, Perm+13.7091)                           \
    -0.799903    * pmax(0, -13.7091-Perm)                          \
    -2.05702     * pmax(0, Poro-0.134274)                          \
    +3.81746      * pmax(0, 0.134274-Poro)                          \
    +7.14594e-05  * pmax(0, Depth-2279.91)                           \
    -0.000245792 * pmax(0, 2279.91-Depth)                           \
    +5.49706      * pmax(0, GeoGrad-0.0326267)                         \
    -7.16444     * pmax(0, 0.0326267-GeoGrad)                         \
    +2.74832      * pmax(0, Poro-0.170566)*pmax(0, Poro-0.134274)           \
    +28.8714      * pmax(0, 0.170566-Poro)*pmax(0, Poro-0.134274)           \
    -0.335428    * pmax(0, Poro-0.0528194)*pmax(0, Perm+13.7091)           \
    +7.81352      * pmax(0, 0.0528194-Poro)*pmax(0, Perm+13.7091)           \
    +10.5047      * pmax(0, Poro-0.0826292)*pmax(0, 0.134274-Poro)          \
    +33.7416      * pmax(0, 0.0826292-Poro)*pmax(0, 0.134274-Poro)          
    ROM_5_LogArea_15yr = 10 ** ROM_5_LogArea_15yr
    return ROM_5_LogArea_15yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogArea_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogArea_15yr =+8.26214   +1.03364      * pmax(0, Perm+13.1539)                           \
    -0.89571     * pmax(0, -13.1539-Perm)                          \
    -2.29308     * pmax(0, Poro-0.146935)                          \
    +4.28447      * pmax(0, 0.146935-Poro)                          \
    +6.94332e-05  * pmax(0, Depth-2404.97)                           \
    -0.000222161 * pmax(0, 2404.97-Depth)                           \
    +5.81431      * pmax(0, GeoGrad-0.0330617)                         \
    -7.30489     * pmax(0, 0.0330617-GeoGrad)                         \
    -0.00154036  * Thick*pmax(0, Perm+13.1539)                        \
    +2.93978      * pmax(0, Poro-0.189779)*pmax(0, Poro-0.146935)                    \
    -10.9025     * pmax(0, Poro-0.0706691)*pmax(0, 0.146935-Poro)          \
    +41.4638      * pmax(0, 0.0706691-Poro)*pmax(0, 0.146935-Poro)          \
    +0.373174     * pmax(0, Poro-0.186913)*pmax(0, -13.1539-Perm)           \
    -0.646049    * pmax(0, 0.186913-Poro)*pmax(0, -13.1539-Perm)         
    ROM_6_LogArea_15yr = 10 ** ROM_6_LogArea_15yr
    return ROM_6_LogArea_15yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogArea_15yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogArea_15yr =+9.07738  +1.06321      * pmax(0, Perm+12.4376)                           \
    -1.0498      * pmax(0, -12.4376-Perm)  -2.02807     * pmax(0, Poro-0.160589)                          \
    +3.4056       * pmax(0, 0.160589-Poro)    +5.88755e-05  * pmax(0, Depth-2944.65)                           \
    -0.000135008 * pmax(0, 2944.65-Depth) +4.87104      * pmax(0, GeoGrad-0.0382944)                         \
    -7.10659     * pmax(0, 0.0382944-GeoGrad)   -0.00139032  * Thick                                      \
    -0.00216316  * pmax(0, Perm+12.414)*Thick    +0.00126247   * pmax(0, -12.414-Perm)*Thick                       \
    -5.95569     * pmax(0, Poro-0.106148)*pmax(0, 0.160589-Poro)           \
    +24.7655      * pmax(0, 0.106148-Poro)*pmax(0, 0.160589-Poro)           \
    +2.748        * pmax(0, Poro-0.29874)*pmax(0, Poro-0.160589)            \
    -4.86231     * pmax(0, 0.29874-Poro)*pmax(0, Poro-0.160589)                   \
    -6.57072e-08 * pmax(0, 1822.78-Depth)*pmax(0, 2944.65-Depth)             \
    +0.256368     * pmax(0, Poro-0.0485233)*pmax(0, -12.4376-Perm)          \
    +2.98519      * pmax(0, 0.0485233-Poro)*pmax(0, -12.4376-Perm)          
    ROM_7_LogArea_15yr = 10 ** ROM_7_LogArea_15yr
    return ROM_7_LogArea_15yr 
#################################################################################### 
# 20 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogArea_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogArea_20yr =+6.79222  -1.74725     * pmax(0, Poro-0.154993)                          \
    +3.12988      * pmax(0, 0.154993-Poro)                          \
    +0.816879     * pmax(0, Perm+14.7726)                           \
    -0.774829    * pmax(0, -14.7726-Perm)                          \
    -0.0001155   * pmax(0, Depth-2389.46)                                    \
    +4.87891      * pmax(0, GeoGrad-0.0385635)                         \
    -6.52293     * pmax(0, 0.0385635-GeoGrad)                         \
    -15.2485     * pmax(0, Poro-0.0752091)*pmax(0, 0.154993-Poro)          \
    +34.0621      * pmax(0, 0.0752091-Poro)*pmax(0, 0.154993-Poro)          \
    +2.30548      * pmax(0, Poro-0.263399)*pmax(0, Poro-0.154993)           \
    -7.36779     * pmax(0, 0.263399-Poro)*pmax(0, Poro-0.154993)           \
    +0.000180616  * pmax(0, Depth-1394.14)                           \
    -0.000304821 * pmax(0, 1394.14-Depth)                           
    ROM_1_LogArea_20yr = 10 ** ROM_1_LogArea_20yr
    return ROM_1_LogArea_20yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogArea_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogArea_20yr =+19.3698  +0.846559     * Perm                                         \
    -3.99476     * pmax(0, Poro-0.134495)                             \
    +5.89665      * pmax(0, 0.134495-Poro)                             \
    -1.04657e-05 * pmax(0, Depth-2344.28)*Perm                           \
    +1.92387e-05  * pmax(0, 2344.28-Depth)*Perm                           \
    -0.405579    * pmax(0, GeoGrad-0.0220961)*Perm                         \
    +0.633022     * pmax(0, 0.0220961-GeoGrad)*Perm                         \
    -0.112402    * pmax(0, Poro-0.0543989)*Perm                         \
    -0.218815    * pmax(0, 0.0543989-Poro)*Perm                         \
    -0.178325    * pmax(0, Poro-0.122772)*pmax(0, Poro-0.0543989)*Perm          \
    +1.80808      * pmax(0, 0.122772-Poro)*pmax(0, Poro-0.0543989)*Perm          \
    -8.28324e-05 * pmax(0, Depth-1362.99)                              \
    -5.51035e-05 * pmax(0, 1362.99-Depth)                              
    ROM_2_LogArea_20yr = 10 ** ROM_2_LogArea_20yr
    return ROM_2_LogArea_20yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogArea_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogArea_20yr =+ 7.52606  + 0.884248     * pmax(0, Perm+14.0318)                          \
    + -0.782457    * pmax(0, -14.0318-Perm)                         \
    + -2.07427     * pmax(0, Poro-0.135424)                         \
    + 3.88585      * pmax(0, 0.135424-Poro)                         \
    + 6.8382e-05   * pmax(0, Depth-2389.27)                          \
    + -0.000214568 * pmax(0, 2389.27-Depth)                          \
    + 5.88681      * pmax(0, GeoGrad-0.022313)                         \
    + -8.73216     * pmax(0, 0.022313-GeoGrad)                         \
    + 2.81162      * pmax(0, Poro-0.178264)*pmax(0, Poro-0.135424)                 \
    + -20.3628     * pmax(0, Poro-0.0523905)*pmax(0, 0.135424-Poro)         \
    + 54.178       * pmax(0, 0.0523905-Poro)*pmax(0, 0.135424-Poro)         \
    + 0.935957     * pmax(0, Perm+14.7684)*pmax(0, 0.135424-Poro)                    
    ROM_3_LogArea_20yr = 10 ** ROM_3_LogArea_20yr
    return ROM_3_LogArea_20yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogArea_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogArea_20yr =+ 7.79611 + 0.959099     * pmax(0, Perm+13.7912)                          \
    + -0.842974    * pmax(0, -13.7912-Perm)                         \
    + -2.42149     * pmax(0, Poro-0.134068)                         \
    + 4.46364      * pmax(0, 0.134068-Poro)                         \
    + 6.89407e-05  * pmax(0, Depth-2383.1)                           \
    + -0.000226223 * pmax(0, 2383.1-Depth)                           \
    + 5.70782      * pmax(0, GeoGrad-0.0301863)                        \
    + -7.17113     * pmax(0, 0.0301863-GeoGrad)                        \
    + 2.80385      * pmax(0, Poro-0.172005)*pmax(0, Poro-0.134068)          \
    + 20.5184      * pmax(0, 0.172005-Poro)*pmax(0, Poro-0.134068)          \
    + 0.192748     * pmax(0, Perm+12.9758)*pmax(0, Poro-0.134068)           \
    + 0.291173     * pmax(0, -12.9758-Perm)*pmax(0, Poro-0.134068)          \
    + -15.8956     * pmax(0, Poro-0.0567747)*pmax(0, 0.134068-Poro)         \
    + 52.2628      * pmax(0, 0.0567747-Poro)*pmax(0, 0.134068-Poro)         
    ROM_4_LogArea_20yr = 10 ** ROM_4_LogArea_20yr
    return ROM_4_LogArea_20yr 
#############
# ROM: 1-10
#############
def ROM_5_LogArea_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogArea_20yr =+7.79705  +0.891694     * pmax(0, Perm+13.7386)                           \
    -0.811227    * pmax(0, -13.7386-Perm)                          \
    -1.39458     * pmax(0, Poro-0.134274)                          \
    +4.17171      * pmax(0, 0.134274-Poro)                          \
    +7.12043e-05  * pmax(0, Depth-2279.91)                           \
    -0.000248957 * pmax(0, 2279.91-Depth)                           \
    +5.73517      * pmax(0, GeoGrad-0.0326267)                         \
    -7.11787     * pmax(0, 0.0326267-GeoGrad)                         \
    +0.336388     * pmax(0, Poro-0.282005)*pmax(0, Perm+13.7386)            \
    +0.821941     * pmax(0, 0.282005-Poro)*pmax(0, Perm+13.7386)            \
    +43.2942      * pmax(0, Poro-0.0826292)*pmax(0, 0.134274-Poro)          \
    +36.6134      * pmax(0, 0.0826292-Poro)*pmax(0, 0.134274-Poro)          
    ROM_5_LogArea_20yr = 10 ** ROM_5_LogArea_20yr
    return ROM_5_LogArea_20yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogArea_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogArea_20yr =+8.37811   +1.06279      * pmax(0, Perm+13.1539)                           \
    -0.913701    * pmax(0, -13.1539-Perm)     -2.35391     * pmax(0, Poro-0.146935)                          \
    +4.40758      * pmax(0, 0.146935-Poro)   +7.58408e-05  * pmax(0, Depth-2404.97)                           \
    -0.000224639 * pmax(0, 2404.97-Depth)  +9.18363      * pmax(0, GeoGrad-0.0330617)                         \
    -7.56186     * pmax(0, 0.0330617-GeoGrad)   -0.0015241   * Thick*pmax(0, Perm+13.1539)                     \
    +3.0181       * pmax(0, Poro-0.191165)*pmax(0, Poro-0.146935)                   \
    -11.2931     * pmax(0, Poro-0.0706691)*pmax(0, 0.146935-Poro)          \
    +42.3317      * pmax(0, 0.0706691-Poro)*pmax(0, 0.146935-Poro)          \
    +0.386709     * pmax(0, Poro-0.186913)*pmax(0, -13.1539-Perm)           \
    -0.700788    * pmax(0, 0.186913-Poro)*pmax(0, -13.1539-Perm)           \
    -0.00166172  * pmax(0, Depth-1587.41)*pmax(0, GeoGrad-0.0330617)           \
    -0.00469234  * pmax(0, 1587.41-Depth)*pmax(0, GeoGrad-0.0330617)           
    ROM_6_LogArea_20yr = 10 ** ROM_6_LogArea_20yr
    return ROM_6_LogArea_20yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogArea_20yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogArea_20yr =+9.22687  +1.09571      * pmax(0, Perm+12.4376)                           \
    -1.07716     * pmax(0, -12.4376-Perm)  -2.07617     * pmax(0, Poro-0.160589)                          \
    +3.50034      * pmax(0, 0.160589-Poro)  +5.81088e-05  * pmax(0, Depth-2944.65)                          \
    -0.000134577 * pmax(0, 2944.65-Depth)     +4.85985      * pmax(0, GeoGrad-0.0390025)                         \
    -7.34382     * pmax(0, 0.0390025-GeoGrad)    -0.0014417   * Thick                                      \
    -0.0023906   * pmax(0, Perm+12.414)*Thick                         \
    +0.00132412   * pmax(0, -12.414-Perm)*Thick                        \
    -6.39056     * pmax(0, Poro-0.106148)*pmax(0, 0.160589-Poro)           \
    +25.2948      * pmax(0, 0.106148-Poro)*pmax(0, 0.160589-Poro)           \
    +2.80918      * pmax(0, Poro-0.299945)*pmax(0, Poro-0.160589)           \
    -4.96143     * pmax(0, 0.299945-Poro)*pmax(0, Poro-0.160589)                 \
    -6.63861e-08 * pmax(0, 1822.78-Depth)*pmax(0, 2944.65-Depth)             \
    +0.264645     * pmax(0, Poro-0.0485233)*pmax(0, -12.4376-Perm)          \
    +2.97707      * pmax(0, 0.0485233-Poro)*pmax(0, -12.4376-Perm)          
    ROM_7_LogArea_20yr = 10 ** ROM_7_LogArea_20yr
    return ROM_7_LogArea_20yr 
#################################################################################### 
# 25 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogArea_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogArea_25yr =+6.9997   -1.70867     * pmax(0, Poro-0.154993)                         \
    +2.23897      * pmax(0, 0.154993-Poro)                         \
    +0.827933     * pmax(0, Perm+14.7726)                          \
    -0.79104     * pmax(0, -14.7726-Perm)                         \
    +6.19011e-05  * pmax(0, Depth-1967.7)                           \
    -0.000251387 * pmax(0, 1967.7-Depth)                           \
    +4.83146      * pmax(0, GeoGrad-0.0385635)                        \
    -6.52633     * pmax(0, 0.0385635-GeoGrad)                                 \
    +28.4699      * pmax(0, 0.113841-Poro)*pmax(0, 0.154993-Poro)          \
    +2.30967      * pmax(0, Poro-0.276576)*pmax(0, Poro-0.154993)          \
    -6.51437     * pmax(0, 0.276576-Poro)*pmax(0, Poro-0.154993)          \
    +2.71609e-06  * Thick*pmax(0, Depth-1967.7)                        
    ROM_1_LogArea_25yr = 10 ** ROM_1_LogArea_25yr
    return ROM_1_LogArea_25yr     
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogArea_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogArea_25yr =+7.75419  +0.939        * pmax(0, Perm+13.8665)                           \
    -0.822258    * pmax(0, -13.8665-Perm)                          \
    -1.4906      * pmax(0, Poro-0.134495)                          \
    +3.51833      * pmax(0, 0.134495-Poro)                          \
    +6.69045e-05  * pmax(0, Depth-2371.91)                           \
    -0.000217614 * pmax(0, 2371.91-Depth)                           \
    +5.73441      * pmax(0, GeoGrad-0.022249)                          \
    -8.65015     * pmax(0, 0.022249-GeoGrad)                                  \
    +47.2327      * pmax(0, 0.0826435-Poro)*pmax(0, 0.134495-Poro)                   \
    -3.04374     * pmax(0, 0.408459-Poro)*pmax(0, Poro-0.134495)           \
    +0.132361     * pmax(0, Poro-0.0860178)*pmax(0, -13.8665-Perm)          \
    -1.59094     * pmax(0, 0.0860178-Poro)*pmax(0, -13.8665-Perm)          
    ROM_2_LogArea_25yr = 10 ** ROM_2_LogArea_25yr
    return ROM_2_LogArea_25yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogArea_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogArea_25yr =+7.60697  +0.896432     * pmax(0, Perm+14.0318)                           \
    -0.786608    * pmax(0, -14.0318-Perm)                          \
    -2.09087     * pmax(0, Poro-0.135424)                          \
    +3.8874       * pmax(0, 0.135424-Poro)                          \
    +6.86358e-05  * pmax(0, Depth-2389.27)                           \
    -0.000215775 * pmax(0, 2389.27-Depth)                           \
    +5.78279      * pmax(0, GeoGrad-0.022313)                          \
    -8.38139     * pmax(0, 0.022313-GeoGrad)                          \
    +2.85412      * pmax(0, Poro-0.176815)*pmax(0, Poro-0.135424)                   \
    -20.396      * pmax(0, Poro-0.0523905)*pmax(0, 0.135424-Poro)          \
    +54.8926      * pmax(0, 0.0523905-Poro)*pmax(0, 0.135424-Poro)          \
    +1.03253      * pmax(0, Perm+14.7684)*pmax(0, 0.135424-Poro)                  
    ROM_3_LogArea_25yr = 10 ** ROM_3_LogArea_25yr
    return ROM_3_LogArea_25yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogArea_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogArea_25yr =+7.83454   +0.916669     * pmax(0, Perm+13.7912)                          \
    -0.814339    * pmax(0, -13.7912-Perm)                         \
    -1.73996     * pmax(0, Poro-0.134068)                         \
    +5.09874      * pmax(0, 0.134068-Poro)                         \
    +6.87723e-05  * pmax(0, Depth-2367.9)                           \
    -0.000231285 * pmax(0, 2367.9-Depth)                           \
    +5.60965      * pmax(0, GeoGrad-0.0299431)                        \
    -7.16859     * pmax(0, 0.0299431-GeoGrad)                        \
    -0.0990413   * pmax(0, Poro-0.281867)*pmax(0, Perm+13.7912)           \
    +0.621352     * pmax(0, 0.281867-Poro)*pmax(0, Perm+13.7912)           \
    +1.72124      * pmax(0, Poro-0.170506)*pmax(0, Poro-0.134068)          \
    +107.796      * pmax(0, 0.170506-Poro)*pmax(0, Poro-0.134068)          
    ROM_4_LogArea_25yr = 10 ** ROM_4_LogArea_25yr
    return ROM_4_LogArea_25yr 
#############
# ROM: 1-10
#############
def ROM_5_LogArea_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogArea_25yr =+7.88197 +0.908176     * pmax(0, Perm+13.7386)                           \
    -0.822642    * pmax(0, -13.7386-Perm)                          \
    -1.41272     * pmax(0, Poro-0.134274)                          \
    +4.24657      * pmax(0, 0.134274-Poro)                          \
    +7.13436e-05  * pmax(0, Depth-2279.91)                           \
    -0.000250732 * pmax(0, 2279.91-Depth)                           \
    +5.83193      * pmax(0, GeoGrad-0.0326267)                         \
    -7.20228     * pmax(0, 0.0326267-GeoGrad)                         \
    +0.335322     * pmax(0, Poro-0.282005)*pmax(0, Perm+13.7386)            \
    +0.865608     * pmax(0, 0.282005-Poro)*pmax(0, Perm+13.7386)            \
    +44.7462      * pmax(0, Poro-0.0826292)*pmax(0, 0.134274-Poro)          \
    +37.4952      * pmax(0, 0.0826292-Poro)*pmax(0, 0.134274-Poro)        
    ROM_5_LogArea_25yr = 10 ** ROM_5_LogArea_25yr
    return ROM_5_LogArea_25yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogArea_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogArea_25yr =+8.47091  +1.12198      * pmax(0, Perm+13.1539)                           \
    -0.959437    * pmax(0, -13.1539-Perm)   -2.48958     * pmax(0, Poro-0.146935)                          \
    +4.39337      * pmax(0, 0.146935-Poro)  +7.55287e-05  * pmax(0, Depth-2404.97)                           \
    -0.000228534 * pmax(0, 2404.97-Depth)    +9.64565      * pmax(0, GeoGrad-0.0330617)                         \
    -7.70961     * pmax(0, 0.0330617-GeoGrad)   -0.00160003  * Thick*pmax(0, Perm+13.1539)                        \
    +3.09923      * pmax(0, Poro-0.191165)*pmax(0, Poro-0.146935)                   \
    -10.7678     * pmax(0, Poro-0.0706691)*pmax(0, 0.146935-Poro)          \
    +40.7059      * pmax(0, 0.0706691-Poro)*pmax(0, 0.146935-Poro)          \
    -0.123854    * pmax(0, Perm+12.7145)*pmax(0, Poro-0.146935)            \
    +0.369478     * pmax(0, -12.7145-Perm)*pmax(0, Poro-0.146935)           \
    -0.0018153   * pmax(0, Depth-1587.41)*pmax(0, GeoGrad-0.0330617)           \
    -0.00406578  * pmax(0, 1587.41-Depth)*pmax(0, GeoGrad-0.0330617)           
    ROM_6_LogArea_25yr = 10 ** ROM_6_LogArea_25yr
    return ROM_6_LogArea_25yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogArea_25yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogArea_25yr =+9.34128  +1.13011      * pmax(0, Perm+12.419)                           \
    -1.09699     * pmax(0, -12.419-Perm)    -2.2603      * pmax(0, Poro-0.160589)                         \
    +4.44243      * pmax(0, 0.160589-Poro)    +6.07356e-05  * pmax(0, Depth-2944.65)                          \
    -0.00013665  * pmax(0, 2944.65-Depth)      +14.8036      * pmax(0, GeoGrad-0.0390025)                        \
    -7.52541     * pmax(0, 0.0390025-GeoGrad)   -0.00151616  * Thick                                     \
    -0.00247689  * pmax(0, Perm+12.414)*Thick   +0.00137785   * pmax(0, -12.414-Perm)*Thick                       \
    +0.294147     * pmax(0, Poro-0.0694696)*pmax(0, -12.419-Perm)          \
    +4.95078      * pmax(0, 0.0694696-Poro)*pmax(0, -12.419-Perm)          \
    +2.40547      * pmax(0, Poro-0.18992)*pmax(0, Poro-0.160589)           \
    +87.6043      * pmax(0, 0.18992-Poro)*pmax(0, Poro-0.160589)                    \
    -6.93618e-08 * pmax(0, 1822.78-Depth)*pmax(0, 2944.65-Depth)            \
    -0.00282612  * Depth*pmax(0, GeoGrad-0.0390025)                     
    ROM_7_LogArea_25yr = 10 ** ROM_7_LogArea_25yr
    return ROM_7_LogArea_25yr 
#################################################################################### 
# 30 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogArea_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogArea_30yr =+7.06261 -1.71516     * pmax(0, Poro-0.154993)                         \
    +2.24391      * pmax(0, 0.154993-Poro)                         \
    +0.83574      * pmax(0, Perm+14.7726)                          \
    -0.792571    * pmax(0, -14.7726-Perm)                         \
    +6.21068e-05  * pmax(0, Depth-1967.7)                           \
    -0.000252598 * pmax(0, 1967.7-Depth)                           \
    +4.85304      * pmax(0, GeoGrad-0.0385635)                        \
    -6.36285     * pmax(0, 0.0385635-GeoGrad)                                 \
    +28.6604      * pmax(0, 0.113841-Poro)*pmax(0, 0.154993-Poro)          \
    +2.36417      * pmax(0, Poro-0.276576)*pmax(0, Poro-0.154993)          \
    -6.57015     * pmax(0, 0.276576-Poro)*pmax(0, Poro-0.154993)          \
    +2.64428e-06  * Thick*pmax(0, Depth-1967.7)                        
    ROM_1_LogArea_30yr = 10 ** ROM_1_LogArea_30yr
    return ROM_1_LogArea_30yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogArea_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogArea_30yr =+7.82867  +0.950421     * pmax(0, Perm+13.8665)                           \
    -0.830998    * pmax(0, -13.8665-Perm)                          \
    -1.87313     * pmax(0, Poro-0.134495)                          \
    +3.49134      * pmax(0, 0.134495-Poro)                          \
    +6.71651e-05  * pmax(0, Depth-2371.91)                           \
    -0.000218664 * pmax(0, 2371.91-Depth)                           \
    +5.66535      * pmax(0, GeoGrad-0.0220961)                         \
    -8.32252     * pmax(0, 0.0220961-GeoGrad)                         \
    -9.98871     * pmax(0, Poro-0.0826435)*pmax(0, 0.134495-Poro)          \
    +48.3297      * pmax(0, 0.0826435-Poro)*pmax(0, 0.134495-Poro)          \
    +2.64271      * pmax(0, Poro-0.28827)*pmax(0, Poro-0.134495)            \
    -4.59459     * pmax(0, 0.28827-Poro)*pmax(0, Poro-0.134495)            \
    +0.153789     * pmax(0, Poro-0.0860178)*pmax(0, -13.8665-Perm)          \
    -1.69432     * pmax(0, 0.0860178-Poro)*pmax(0, -13.8665-Perm)          
    ROM_2_LogArea_30yr = 10 ** ROM_2_LogArea_30yr
    return ROM_2_LogArea_30yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogArea_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogArea_30yr =+7.67081  +0.906689     * pmax(0, Perm+14.0318)                           \
    -0.790961    * pmax(0, -14.0318-Perm)                          \
    -2.10198     * pmax(0, Poro-0.135424)                          \
    +3.89311      * pmax(0, 0.135424-Poro)                          \
    +6.8954e-05   * pmax(0, Depth-2389.27)                           \
    -0.000216907 * pmax(0, 2389.27-Depth)                           \
    +5.75575      * pmax(0, GeoGrad-0.0219125)                         \
    -8.16637     * pmax(0, 0.0219125-GeoGrad)                         \
    +2.88469      * pmax(0, Poro-0.176815)*pmax(0, Poro-0.135424)                     \
    -20.6809     * pmax(0, Poro-0.0523905)*pmax(0, 0.135424-Poro)          \
    +55.5512      * pmax(0, 0.0523905-Poro)*pmax(0, 0.135424-Poro)          \
    +1.12182      * pmax(0, Perm+14.7684)*pmax(0, 0.135424-Poro)                   
    ROM_3_LogArea_30yr = 10 ** ROM_3_LogArea_30yr
    return ROM_3_LogArea_30yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogArea_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogArea_30yr =+7.88284  +0.895477    * pmax(0, Perm+13.8053)                           \
    -0.820653   * pmax(0, -13.8053-Perm)                          \
    -1.38511    * pmax(0, Poro-0.134068)                          \
    +4.18084     * pmax(0, 0.134068-Poro)                          \
    +6.92637e-05 * pmax(0, Depth-2367.9)                            \
    -0.00023243 * pmax(0, 2367.9-Depth)                            \
    +5.82289     * pmax(0, GeoGrad-0.0299431)                         \
    -7.16155    * pmax(0, 0.0299431-GeoGrad)                         \
    +0.349359    * pmax(0, Poro-0.281867)*pmax(0, Perm+13.8053)            \
    +0.947731    * pmax(0, 0.281867-Poro)*pmax(0, Perm+13.8053)            \
    +43.2546     * pmax(0, Poro-0.0818632)*pmax(0, 0.134068-Poro)          \
    +37.214      * pmax(0, 0.0818632-Poro)*pmax(0, 0.134068-Poro)          
    ROM_4_LogArea_30yr = 10 ** ROM_4_LogArea_30yr
    return ROM_4_LogArea_30yr 
#############
# ROM: 1-10
#############
def ROM_5_LogArea_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogArea_30yr =+7.95422  +0.922317     * pmax(0, Perm+13.7386)                           \
    -0.833274    * pmax(0, -13.7386-Perm)                          \
    -1.43209     * pmax(0, Poro-0.134274)                          \
    +4.3061       * pmax(0, 0.134274-Poro)                          \
    +7.14013e-05  * pmax(0, Depth-2279.91)                           \
    -0.000251945 * pmax(0, 2279.91-Depth)                           \
    +5.90448      * pmax(0, GeoGrad-0.0327253)                         \
    -7.2918      * pmax(0, 0.0327253-GeoGrad)                         \
    +0.337447     * pmax(0, Poro-0.282005)*pmax(0, Perm+13.7386)            \
    +0.884662     * pmax(0, 0.282005-Poro)*pmax(0, Perm+13.7386)            \
    +46.4782      * pmax(0, Poro-0.0826292)*pmax(0, 0.134274-Poro)          \
    +38.2886      * pmax(0, 0.0826292-Poro)*pmax(0, 0.134274-Poro)          
    ROM_5_LogArea_30yr = 10 ** ROM_5_LogArea_30yr
    return ROM_5_LogArea_30yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogArea_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogArea_30yr =+8.55253 +1.10135     * pmax(0, Perm+13.1539)                           \
    -0.943863   * pmax(0, -13.1539-Perm)  -2.42261    * pmax(0, Poro-0.149085)                          \
    +4.52428     * pmax(0, 0.149085-Poro)      +7.58478e-05 * pmax(0, Depth-2404.97)                           \
    -0.00022676 * pmax(0, 2404.97-Depth)     +9.95197     * pmax(0, GeoGrad-0.0330617)                         \
    -7.90125    * pmax(0, 0.0330617-GeoGrad)  -0.00160845 * Thick*pmax(0, Perm+13.1539)                        \
    +3.09735     * pmax(0, Poro-0.191165)*pmax(0, Poro-0.149085)                  \
    -11.8888    * pmax(0, Poro-0.0707025)*pmax(0, 0.149085-Poro)          \
    +43.2387     * pmax(0, 0.0707025-Poro)*pmax(0, 0.149085-Poro)          \
    +0.396475    * pmax(0, Poro-0.186913)*pmax(0, -13.1539-Perm)           \
    -0.748584   * pmax(0, 0.186913-Poro)*pmax(0, -13.1539-Perm)           \
    -0.00193584 * pmax(0, Depth-1587.41)*pmax(0, GeoGrad-0.0330617)           \
    -0.00376259 * pmax(0, 1587.41-Depth)*pmax(0, GeoGrad-0.0330617)           
    ROM_6_LogArea_30yr = 10 ** ROM_6_LogArea_30yr
    return ROM_6_LogArea_30yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogArea_30yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogArea_30yr =+9.45912  +1.14102      * pmax(0, Perm+12.419)                           \
    -1.10707     * pmax(0, -12.419-Perm)  -2.2878      * pmax(0, Poro-0.160589)                         \
    +4.42655      * pmax(0, 0.160589-Poro)  +6.4513e-05   * pmax(0, Depth-2944.65)                          \
    -0.000131792 * pmax(0, 2944.65-Depth)    +7.33625      * pmax(0, GeoGrad-0.041565)                         \
    -8.10832     * pmax(0, 0.041565-GeoGrad)   -0.00153798  * Thick                                     \
    -0.00257124  * pmax(0, Perm+12.414)*Thick                        \
    +0.00136048   * pmax(0, -12.414-Perm)*Thick                       \
    +2.52353      * pmax(0, Poro-0.199536)*pmax(0, Poro-0.160589)          \
    +38.0033      * pmax(0, 0.199536-Poro)*pmax(0, Poro-0.160589)          \
    +0.30023      * pmax(0, Poro-0.0765052)*pmax(0, -12.419-Perm)          \
    +4.15026      * pmax(0, 0.0765052-Poro)*pmax(0, -12.419-Perm)                 \
    -6.79778e-08 * pmax(0, 1822.78-Depth)*pmax(0, 2944.65-Depth)            \
    -0.00207659  * pmax(0, GeoGrad-0.0314639)*pmax(0, Depth-2944.65)                  
    ROM_7_LogArea_30yr = 10 ** ROM_7_LogArea_30yr
    return ROM_7_LogArea_30yr 
#################################################################################### 
# 35 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogArea_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogArea_35yr =+7.11102  -1.41558     * pmax(0, Poro-0.154993)                          \
    +3.38388      * pmax(0, 0.154993-Poro)                          \
    +0.843269     * pmax(0, Perm+14.7726)                           \
    -0.797364    * pmax(0, -14.7726-Perm)                          \
    +6.24763e-05  * pmax(0, Depth-1967.7)                            \
    -0.000252088 * pmax(0, 1967.7-Depth)                            \
    +4.488        * pmax(0, GeoGrad-0.0385635)                         \
    -6.33514     * pmax(0, 0.0385635-GeoGrad)                         \
    -15.1094     * pmax(0, Poro-0.0695001)*pmax(0, 0.154993-Poro)          \
    +36.6413      * pmax(0, 0.0695001-Poro)*pmax(0, 0.154993-Poro)          \
    +1.08419      * pmax(0, Poro-0.375389)*pmax(0, Poro-0.154993)           \
    -3.3651      * pmax(0, 0.375389-Poro)*pmax(0, Poro-0.154993)           \
    +2.57881e-06  * Thick*pmax(0, Depth-1967.7)                       
    ROM_1_LogArea_35yr = 10 ** ROM_1_LogArea_35yr
    return ROM_1_LogArea_35yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogArea_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogArea_35yr =+7.64891    +0.906313     * pmax(0, Perm+14.124)                            \
    -0.791409    * pmax(0, -14.124-Perm)                           \
    -1.69123     * pmax(0, Poro-0.134495)                          \
    +18.8725      * pmax(0, 0.134495-Poro)                          \
    +6.73386e-05  * pmax(0, Depth-2371.91)                           \
    -0.000218836 * pmax(0, 2371.91-Depth)                           \
    +5.64076      * pmax(0, GeoGrad-0.0214075)                         \
    -8.26802     * pmax(0, 0.0214075-GeoGrad)                                  \
    +39.2409      * pmax(0, 0.0826435-Poro)*pmax(0, 0.134495-Poro)          \
    +2.46451      * pmax(0, Poro-0.311453)*pmax(0, Poro-0.134495)           \
    -3.93636     * pmax(0, 0.311453-Poro)*pmax(0, Poro-0.134495)           \
    +1.07038      * Perm*pmax(0, 0.134495-Poro)                      
    ROM_2_LogArea_35yr = 10 ** ROM_2_LogArea_35yr
    return ROM_2_LogArea_35yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogArea_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogArea_35yr =+7.72282  +0.918785     * pmax(0, Perm+14.0318)                           \
    -0.795132    * pmax(0, -14.0318-Perm)                          \
    -2.10454     * pmax(0, Poro-0.135424)                          \
    +3.90121      * pmax(0, 0.135424-Poro)                          \
    +7.14062e-05  * pmax(0, Depth-2389.27)                           \
    -0.000179933 * pmax(0, 2389.27-Depth)                           \
    +5.71744      * pmax(0, GeoGrad-0.0219125)                         \
    -7.96319     * pmax(0, 0.0219125-GeoGrad)                         \
    +2.88035      * pmax(0, Poro-0.176815)*pmax(0, Poro-0.135424)                    \
    -20.8193     * pmax(0, Poro-0.0523905)*pmax(0, 0.135424-Poro)          \
    +55.666       * pmax(0, 0.0523905-Poro)*pmax(0, 0.135424-Poro)          \
    +1.22629      * pmax(0, Perm+14.7684)*pmax(0, 0.135424-Poro)                     \
    -1.21361e-07 * pmax(0, Depth-1758.1)*pmax(0, 2389.27-Depth)              \
    -6.54089e-08 * pmax(0, 1758.1-Depth)*pmax(0, 2389.27-Depth)              
    ROM_3_LogArea_35yr = 10 ** ROM_3_LogArea_35yr
    return ROM_3_LogArea_35yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogArea_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogArea_35yr =+7.99163  +1.00503      * pmax(0, Perm+13.8098)                           \
    -0.874301    * pmax(0, -13.8098-Perm)                          \
    -2.56491     * pmax(0, Poro-0.134068)                          \
    +4.68539      * pmax(0, 0.134068-Poro)                          \
    +6.9974e-05   * pmax(0, Depth-2367.9)                            \
    -0.000230406 * pmax(0, 2367.9-Depth)                            \
    +5.82324      * pmax(0, GeoGrad-0.0299431)                         \
    -7.15149     * pmax(0, 0.0299431-GeoGrad)                         \
    +0.24263      * pmax(0, Perm+12.9758)*pmax(0, Poro-0.134068)            \
    +0.35327      * pmax(0, -12.9758-Perm)*pmax(0, Poro-0.134068)           \
    +2.93943      * pmax(0, Poro-0.172005)*pmax(0, Poro-0.134068)           \
    +18.9931      * pmax(0, 0.172005-Poro)*pmax(0, Poro-0.134068)           \
    -17.0044     * pmax(0, Poro-0.0559029)*pmax(0, 0.134068-Poro)          \
    +57.4399      * pmax(0, 0.0559029-Poro)*pmax(0, 0.134068-Poro)          
    ROM_4_LogArea_35yr = 10 ** ROM_4_LogArea_35yr
    return ROM_4_LogArea_35yr 
#############
# ROM: 1-10
#############
def ROM_5_LogArea_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogArea_35yr =+8.01938  +0.933239     * pmax(0, Perm+13.7386)                           \
    -0.843922    * pmax(0, -13.7386-Perm)                          \
    -1.45214     * pmax(0, Poro-0.134274)                          \
    +4.37659      * pmax(0, 0.134274-Poro)                          \
    +7.15054e-05  * pmax(0, Depth-2279.91)                           \
    -0.000251279 * pmax(0, 2279.91-Depth)                           \
    +5.91038      * pmax(0, GeoGrad-0.0331115)                         \
    -7.34613     * pmax(0, 0.0331115-GeoGrad)                         \
    +0.339534     * pmax(0, Poro-0.282005)*pmax(0, Perm+13.7386)            \
    +0.852535     * pmax(0, 0.282005-Poro)*pmax(0, Perm+13.7386)            \
    +46.7948      * pmax(0, Poro-0.0826292)*pmax(0, 0.134274-Poro)          \
    +38.5202      * pmax(0, 0.0826292-Poro)*pmax(0, 0.134274-Poro)        
    ROM_5_LogArea_35yr = 10 ** ROM_5_LogArea_35yr
    return ROM_5_LogArea_35yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogArea_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogArea_35yr =+8.73766  +1.09615      * pmax(0, Perm+13.1384) -0.989945    * pmax(0, -13.1384-Perm)                         \
    -2.39007     * pmax(0, Poro-0.146935)     +4.67051      * pmax(0, 0.146935-Poro)                         \
    +6.76448e-05  * pmax(0, Depth-2412.51)     -0.000220314 * pmax(0, 2412.51-Depth)                          \
    +1.66268      * pmax(0, GeoGrad-0.0454104)   -7.4744      * pmax(0, 0.0454104-GeoGrad)                        \
    -0.0015962   * Thick*pmax(0, Perm+13.1384)                       \
    +2.93719      * pmax(0, Poro-0.191165)*pmax(0, Poro-0.146935)          \
    +13.7375      * pmax(0, 0.191165-Poro)*pmax(0, Poro-0.146935)          \
    -11.4506     * pmax(0, Poro-0.069333)*pmax(0, 0.146935-Poro)          \
    +44.7319      * pmax(0, 0.069333-Poro)*pmax(0, 0.146935-Poro)          \
    +0.395317     * pmax(0, Poro-0.128619)*pmax(0, -13.1384-Perm)          \
    -0.809583    * pmax(0, 0.128619-Poro)*pmax(0, -13.1384-Perm)          
    ROM_6_LogArea_35yr = 10 ** ROM_6_LogArea_35yr
    return ROM_6_LogArea_35yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogArea_35yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogArea_35yr =+9.52837  +0.998144     * pmax(0, Perm+12.4376)                           \
    -1.0427      * pmax(0, -12.4376-Perm)   -2.27841     * pmax(0, Poro-0.160589)                          \
    +4.0891       * pmax(0, 0.160589-Poro)  +4.42674e-05  * pmax(0, Depth-2944.65)                           \
    -0.000115118 * pmax(0, 2944.65-Depth)    +1.59404      * pmax(0, GeoGrad-0.0449745)                         \
    -8.66332     * pmax(0, 0.0449745-GeoGrad)     -0.0178139   * Thick                                      \
    -0.00130867  * Perm*Thick                                   \
    +2.89622      * pmax(0, Poro-0.200527)*pmax(0, Poro-0.160589)                   \
    -12.5801     * pmax(0, Poro-0.0734044)*pmax(0, 0.160589-Poro)          \
    +36.2253      * pmax(0, 0.0734044-Poro)*pmax(0, 0.160589-Poro)          \
    +0.000697215  * pmax(0, Depth-1463.73)*pmax(0, 0.0449745-GeoGrad)           \
    -0.00191914  * pmax(0, 1463.73-Depth)*pmax(0, 0.0449745-GeoGrad)                    \
    -5.66489e-08 * pmax(0, 1888.61-Depth)*pmax(0, 2944.65-Depth)             
    ROM_7_LogArea_35yr = 10 ** ROM_7_LogArea_35yr
    return ROM_7_LogArea_35yr 
#################################################################################### 
# 40 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogArea_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogArea_40yr =+7.16284  -1.66134     * pmax(0, Poro-0.154993)                          \
    +15.8615      * pmax(0, 0.154993-Poro)                          \
    +0.831305     * pmax(0, Perm+14.7726)                           \
    -0.758587    * pmax(0, -14.7726-Perm)                          \
    +5.08349e-05  * pmax(0, Depth-1690.97)                           \
    -0.000206916 * pmax(0, 1690.97-Depth)                           \
    +5.18613      * pmax(0, GeoGrad-0.0329603)                         \
    -6.12242     * pmax(0, 0.0329603-GeoGrad)                         \
    -11.1546     * pmax(0, Poro-0.0695001)*pmax(0, 0.154993-Poro)          \
    +40.6184      * pmax(0, 0.0695001-Poro)*pmax(0, 0.154993-Poro)                  \
    -7.01477e-05 * pmax(0, 3087.83-Depth)                           \
    +2.06667      * pmax(0, Poro-0.278886)*pmax(0, Poro-0.154993)           \
    -5.17708     * pmax(0, 0.278886-Poro)*pmax(0, Poro-0.154993)           \
    +0.852952     * Perm*pmax(0, 0.154993-Poro)                     
    ROM_1_LogArea_40yr = 10 ** ROM_1_LogArea_40yr
    return ROM_1_LogArea_40yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogArea_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogArea_40yr =+7.69555  +0.914224     * pmax(0, Perm+14.124)  -0.795038    * pmax(0, -14.124-Perm)                           \
    -1.73053     * pmax(0, Poro-0.134495)     +19.8214      * pmax(0, 0.134495-Poro)                          \
    +6.75668e-05  * pmax(0, Depth-2371.91)    -0.000219798 * pmax(0, 2371.91-Depth)                           \
    +5.62596      * pmax(0, GeoGrad-0.0210689)   -8.05254     * pmax(0, 0.0210689-GeoGrad)                                 \
    +40.53        * pmax(0, 0.0807082-Poro)*pmax(0, 0.134495-Poro)          \
    +2.53726      * pmax(0, Poro-0.29977)*pmax(0, Poro-0.134495)            \
    -4.11279     * pmax(0, 0.29977-Poro)*pmax(0, Poro-0.134495)            \
    +1.13123      * Perm*pmax(0, 0.134495-Poro)                     
    ROM_2_LogArea_40yr = 10 ** ROM_2_LogArea_40yr
    return ROM_2_LogArea_40yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogArea_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogArea_40yr =+7.78648    +0.942771     * pmax(0, Perm+14.0318)                           \
    -0.869114    * pmax(0, -14.0318-Perm)   -2.23555     * pmax(0, Poro-0.135424)                          \
    +4.55166      * pmax(0, 0.135424-Poro) +7.18367e-05  * pmax(0, Depth-2389.27)                           \
    -0.000181063 * pmax(0, 2389.27-Depth)    +5.74581      * pmax(0, GeoGrad-0.0215654)                         \
    -7.89389     * pmax(0, 0.0215654-GeoGrad)                         \
    +0.296809     * pmax(0, Poro-0.0463671)*pmax(0, -14.0318-Perm)          \
    -6.40153     * pmax(0, 0.0463671-Poro)*pmax(0, -14.0318-Perm)          \
    +2.86662      * pmax(0, Poro-0.176815)*pmax(0, Poro-0.135424)                   \
    -19.7985     * pmax(0, Poro-0.0512223)*pmax(0, 0.135424-Poro)          \
    +79.4508      * pmax(0, 0.0512223-Poro)*pmax(0, 0.135424-Poro)          \
    -1.24962e-07 * pmax(0, Depth-1775.27)*pmax(0, 2389.27-Depth)             \
    -6.26842e-08 * pmax(0, 1775.27-Depth)*pmax(0, 2389.27-Depth)             
    ROM_3_LogArea_40yr = 10 ** ROM_3_LogArea_40yr
    return ROM_3_LogArea_40yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogArea_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogArea_40yr =+8.0404  +1.01003      * pmax(0, Perm+13.8163)                           \
    -0.882396    * pmax(0, -13.8163-Perm)                          \
    -2.5809      * pmax(0, Poro-0.134068)                          \
    +4.73695      * pmax(0, 0.134068-Poro)                          \
    +7.01052e-05  * pmax(0, Depth-2367.9)                            \
    -0.000230598 * pmax(0, 2367.9-Depth)                            \
    +5.84167      * pmax(0, GeoGrad-0.0301863)                         \
    -7.13511     * pmax(0, 0.0301863-GeoGrad)                         \
    +0.302972     * pmax(0, Perm+12.9758)*pmax(0, Poro-0.134068)            \
    +0.354807     * pmax(0, -12.9758-Perm)*pmax(0, Poro-0.134068)           \
    +2.94526      * pmax(0, Poro-0.172005)*pmax(0, Poro-0.134068)           \
    +18.352       * pmax(0, 0.172005-Poro)*pmax(0, Poro-0.134068)           \
    -17.224      * pmax(0, Poro-0.0559029)*pmax(0, 0.134068-Poro)          \
    +57.7338      * pmax(0, 0.0559029-Poro)*pmax(0, 0.134068-Poro)          
    ROM_4_LogArea_40yr = 10 ** ROM_4_LogArea_40yr
    return ROM_4_LogArea_40yr 
#############
# ROM: 1-10
#############
def ROM_5_LogArea_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogArea_40yr =+7.50288  +0.983742     * pmax(0, Perm+14.4093)                           \
    -0.808315    * pmax(0, -14.4093-Perm)                          \
    -2.62892     * pmax(0, Poro-0.134274)                          \
    +4.90118      * pmax(0, 0.134274-Poro)                          \
    +7.11101e-05  * pmax(0, Depth-2378.12)                           \
    -0.000230514 * pmax(0, 2378.12-Depth)                           \
    +5.75385      * pmax(0, GeoGrad-0.0334709)                         \
    -7.41411     * pmax(0, 0.0334709-GeoGrad)                         \
    +0.316071     * pmax(0, Perm+13.2573)*pmax(0, Poro-0.134274)            \
    +0.512421     * pmax(0, -13.2573-Perm)*pmax(0, Poro-0.134274)           \
    +3.13549      * pmax(0, Poro-0.172569)*pmax(0, Poro-0.134274)                   \
    -18.2059     * pmax(0, Poro-0.0549236)*pmax(0, 0.134274-Poro)          \
    +60.4652      * pmax(0, 0.0549236-Poro)*pmax(0, 0.134274-Poro)         
    ROM_5_LogArea_40yr = 10 ** ROM_5_LogArea_40yr
    return ROM_5_LogArea_40yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogArea_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogArea_40yr =+8.88946 +1.01301      * pmax(0, Perm+13.0609)                           \
    -0.967603    * pmax(0, -13.0609-Perm)                          \
    -2.30207     * pmax(0, Poro-0.146935)                          \
    +4.57855      * pmax(0, 0.146935-Poro)                          \
    +7.65244e-05  * pmax(0, Depth-2424.23)                           \
    -0.000146899 * pmax(0, 2424.23-Depth)                           \
    +6.29844      * pmax(0, GeoGrad-0.0455058)                         \
    -8.41051     * pmax(0, 0.0455058-GeoGrad)                         \
    +2.95088      * pmax(0, Poro-0.204289)*pmax(0, Poro-0.146935)                   \
    -1.18413e-06 * Thick*pmax(0, 2424.23-Depth)                        \
    -14.6332     * pmax(0, Poro-0.0632297)*pmax(0, 0.146935-Poro)          \
    +44.9944      * pmax(0, 0.0632297-Poro)*pmax(0, 0.146935-Poro)          \
    -0.00164691  * pmax(0, GeoGrad-0.0300333)*pmax(0, Depth-2424.23)                    
    ROM_6_LogArea_40yr = 10 ** ROM_6_LogArea_40yr
    return ROM_6_LogArea_40yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogArea_40yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogArea_40yr =+9.54424  +0.851735     * pmax(0, Perm+12.4418)                          \
    -0.947052    * pmax(0, -12.4418-Perm) -2.03054     * pmax(0, Poro-0.160589)                         \
    +3.92751      * pmax(0, 0.160589-Poro)   +4.93875e-05  * pmax(0, Depth-2960.87)                          \
    -0.000119306 * pmax(0, 2960.87-Depth)    +5.18692      * pmax(0, GeoGrad-0.0455564)                        \
    -7.90199     * pmax(0, 0.0455564-GeoGrad)     -0.00110495  * Thick                                     \
    -0.00119645  * pmax(0, Poro-0.0750203)*Thick                     \
    +0.056772     * pmax(0, 0.0750203-Poro)*Thick                     \
    +2.44782      * pmax(0, Poro-0.202123)*pmax(0, Poro-0.160589)          \
    +31.7682      * pmax(0, 0.202123-Poro)*pmax(0, Poro-0.160589)          \
    +1.61743e-07  * pmax(0, Depth-1645.87)*Thick                       \
    -1.75935e-06 * pmax(0, 1645.87-Depth)*Thick                       \
    -0.00195689  * pmax(0, GeoGrad-0.0314639)*pmax(0, Depth-2960.87)                   
    ROM_7_LogArea_40yr = 10 ** ROM_7_LogArea_40yr
    return ROM_7_LogArea_40yr 
#################################################################################### 
# 45 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogArea_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogArea_45yr =+7.19097  -1.41965     * pmax(0, Poro-0.154993)                          \
    +3.40131      * pmax(0, 0.154993-Poro)                          \
    +0.853897     * pmax(0, Perm+14.7726)                           \
    -0.771485    * pmax(0, -14.7726-Perm)                          \
    +9.8907e-05   * pmax(0, Depth-1967.7)                            \
    -0.000253416 * pmax(0, 1967.7-Depth)                            \
    +4.44498      * pmax(0, GeoGrad-0.0385635)                         \
    -5.9653      * pmax(0, 0.0385635-GeoGrad)                         \
    -12.6814     * pmax(0, Poro-0.0695001)*pmax(0, 0.154993-Poro)          \
    +37.9058      * pmax(0, 0.0695001-Poro)*pmax(0, 0.154993-Poro)          \
    +1.22608      * pmax(0, Poro-0.375389)*pmax(0, Poro-0.154993)           \
    -3.10826     * pmax(0, 0.375389-Poro)*pmax(0, Poro-0.154993)           \
    -1.09367e-08 * pmax(0, Depth-2324.47)*pmax(0, Depth-1967.7)              \
    -5.16022e-07 * pmax(0, 2324.47-Depth)*pmax(0, Depth-1967.7)             
    ROM_1_LogArea_45yr = 10 ** ROM_1_LogArea_45yr
    return ROM_1_LogArea_45yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogArea_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogArea_45yr =+7.73787   +0.920834     * pmax(0, Perm+14.124)                            \
    -0.799218    * pmax(0, -14.124-Perm)                           \
    -1.73698     * pmax(0, Poro-0.134495)                          \
    +20.341       * pmax(0, 0.134495-Poro)                          \
    +6.78724e-05  * pmax(0, Depth-2371.91)                           \
    -0.000220914 * pmax(0, 2371.91-Depth)                           \
    +5.59154      * pmax(0, GeoGrad-0.0207483)                         \
    -7.92444     * pmax(0, 0.0207483-GeoGrad)                                   \
    +40.8092      * pmax(0, 0.0807082-Poro)*pmax(0, 0.134495-Poro)          \
    +2.55221      * pmax(0, Poro-0.29977)*pmax(0, Poro-0.134495)            \
    -4.18089     * pmax(0, 0.29977-Poro)*pmax(0, Poro-0.134495)            \
    +1.16579      * Perm*pmax(0, 0.134495-Poro)                      
    ROM_2_LogArea_45yr = 10 ** ROM_2_LogArea_45yr
    return ROM_2_LogArea_45yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogArea_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogArea_45yr =+7.83111  +0.950478     * pmax(0, Perm+14.0318)                           \
    -0.876096    * pmax(0, -14.0318-Perm)    -2.27757     * pmax(0, Poro-0.135424)                          \
    +4.70935      * pmax(0, 0.135424-Poro)   +7.19773e-05  * pmax(0, Depth-2389.27)                           \
    -0.000178547 * pmax(0, 2389.27-Depth)     +5.73003      * pmax(0, GeoGrad-0.0213266)                         \
    -7.80233     * pmax(0, 0.0213266-GeoGrad)                         \
    +0.307638     * pmax(0, Poro-0.0463671)*pmax(0, -14.0318-Perm)          \
    -6.80271     * pmax(0, 0.0463671-Poro)*pmax(0, -14.0318-Perm)          \
    +2.91495      * pmax(0, Poro-0.171042)*pmax(0, Poro-0.135424)                    \
    -21.8732     * pmax(0, Poro-0.0479827)*pmax(0, 0.135424-Poro)          \
    +91.7392      * pmax(0, 0.0479827-Poro)*pmax(0, 0.135424-Poro)          \
    -2.46244e-07 * pmax(0, Depth-1898)*pmax(0, 2389.27-Depth)                \
    -5.76916e-08 * pmax(0, 1898-Depth)*pmax(0, 2389.27-Depth)                
    ROM_3_LogArea_45yr = 10 ** ROM_3_LogArea_45yr
    return ROM_3_LogArea_45yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogArea_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogArea_45yr =+8.08105    +0.98802      * pmax(0, Perm+13.8203)                           \
    -0.863304    * pmax(0, -13.8203-Perm)                          \
    -2.32456     * pmax(0, Poro-0.134068)                          \
    +5.17239      * pmax(0, 0.134068-Poro)                          \
    +7.03413e-05  * pmax(0, Depth-2367.9)                            \
    -0.000230639 * pmax(0, 2367.9-Depth)                            \
    +5.83986      * pmax(0, GeoGrad-0.030241)                          \
    -7.22628     * pmax(0, 0.030241-GeoGrad)                          \
    +0.293348     * pmax(0, Poro-0.132927)*pmax(0, -13.8203-Perm)           \
    -1.26315     * pmax(0, 0.132927-Poro)*pmax(0, -13.8203-Perm)           \
    +2.91682      * pmax(0, Poro-0.170506)*pmax(0, Poro-0.134068)           \
    +24.5601      * pmax(0, 0.170506-Poro)*pmax(0, Poro-0.134068)           \
    -17.5849     * pmax(0, Poro-0.0559029)*pmax(0, 0.134068-Poro)          \
    +56.3252      * pmax(0, 0.0559029-Poro)*pmax(0, 0.134068-Poro)         
    ROM_4_LogArea_45yr = 10 ** ROM_4_LogArea_45yr
    return ROM_4_LogArea_45yr 
#############
# ROM: 1-10
#############
def ROM_5_LogArea_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogArea_45yr =+7.55268  +0.984514     * pmax(0, Perm+14.4093)                           \
    -0.822903    * pmax(0, -14.4093-Perm)                          \
    -2.61013     * pmax(0, Poro-0.134274)                          \
    +4.92618      * pmax(0, 0.134274-Poro)                          \
    +7.06506e-05  * pmax(0, Depth-2386.28)                           \
    -0.000228976 * pmax(0, 2386.28-Depth)                           \
    +5.73498      * pmax(0, GeoGrad-0.0336373)                         \
    -7.45203     * pmax(0, 0.0336373-GeoGrad)                         \
    +0.304691     * pmax(0, Perm+13.3007)*pmax(0, Poro-0.134274)            \
    +0.496174     * pmax(0, -13.3007-Perm)*pmax(0, Poro-0.134274)           \
    +3.11593      * pmax(0, Poro-0.172569)*pmax(0, Poro-0.134274)                    \
    -17.3716     * pmax(0, Poro-0.0549236)*pmax(0, 0.134274-Poro)          \
    +60.4701      * pmax(0, 0.0549236-Poro)*pmax(0, 0.134274-Poro)          
    ROM_5_LogArea_45yr = 10 ** ROM_5_LogArea_45yr
    return ROM_5_LogArea_45yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogArea_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogArea_45yr =+8.9459 +0.988903     * pmax(0, Perm+13.0498)                           \
    -0.971285    * pmax(0, -13.0498-Perm)                          \
    -2.29144     * pmax(0, Poro-0.146935)                          \
    +4.51503      * pmax(0, 0.146935-Poro)                          \
    +5.77206e-05  * pmax(0, Depth-2436.2)                            \
    -0.000118652 * pmax(0, 2436.2-Depth)                            \
    +1.98393      * pmax(0, GeoGrad-0.0450806)                         \
    -8.76348     * pmax(0, 0.0450806-GeoGrad)                         \
    -1.18751e-06 * Thick*pmax(0, 2436.2-Depth)                         \
    +2.91621      * pmax(0, Poro-0.203079)*pmax(0, Poro-0.146935)                    \
    -15.0882     * pmax(0, Poro-0.0632297)*pmax(0, 0.146935-Poro)          \
    +44.2714      * pmax(0, 0.0632297-Poro)*pmax(0, 0.146935-Poro)          \
    +0.000664869  * pmax(0, Depth-1240.6)*pmax(0, 0.0450806-GeoGrad)            \
    -0.00996955  * pmax(0, 1240.6-Depth)*pmax(0, 0.0450806-GeoGrad)            
    ROM_6_LogArea_45yr = 10 ** ROM_6_LogArea_45yr
    return ROM_6_LogArea_45yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogArea_45yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogArea_45yr =+9.5564 +1.1073       * pmax(0, Perm+12.4533)                          \
    -0.951949    * pmax(0, -12.4533-Perm)  -1.89216     * pmax(0, Poro-0.162287)                         \
    +3.69001      * pmax(0, 0.162287-Poro)  +3.42358e-05  * pmax(0, Depth-2960.87)                          \
    -0.000110856 * pmax(0, 2960.87-Depth)  -5.88127     * pmax(0, 0.0455564-GeoGrad)                        \
    -0.000744317 * Thick   -0.00184891  * pmax(0, Poro-0.0784163)*Thick                     \
    +0.0559278    * pmax(0, 0.0784163-Poro)*Thick                     \
    +2.06205      * pmax(0, Poro-0.205492)*pmax(0, Poro-0.162287)          \
    +22.8448      * pmax(0, 0.205492-Poro)*pmax(0, Poro-0.162287)          \
    +1.22539e-07  * pmax(0, Depth-1645.87)*Thick                       \
    -1.93847e-06 * pmax(0, 1645.87-Depth)*Thick                       \
    -0.00034407  * Depth*pmax(0, Perm+12.4533)                              \
    -0.000922193 * pmax(0, 4534.55-Depth)*pmax(0, 0.0455564-GeoGrad)          \
    +0.00060081   * Poro*Depth*pmax(0, Perm+12.4533)                    
    ROM_7_LogArea_45yr = 10 ** ROM_7_LogArea_45yr
    return ROM_7_LogArea_45yr 
#################################################################################### 
# 50 years
####################################################################################
#############
# ROM: 0-0.1
#############
def ROM_1_LogArea_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_1_LogArea_50yr =+7.23199   -1.70005     * pmax(0, Poro-0.154993)                          \
    +3.36927      * pmax(0, 0.154993-Poro)                          \
    +0.857203     * pmax(0, Perm+14.7726)                           \
    -0.780922    * pmax(0, -14.7726-Perm)                          \
    +0.000100186  * pmax(0, Depth-1967.7)                            \
    -0.000253739 * pmax(0, 1967.7-Depth)                            \
    +4.627        * pmax(0, GeoGrad-0.0385635)                         \
    -5.8461      * pmax(0, 0.0385635-GeoGrad)                         \
    -14.7585     * pmax(0, Poro-0.0695001)*pmax(0, 0.154993-Poro)          \
    +38.1297      * pmax(0, 0.0695001-Poro)*pmax(0, 0.154993-Poro)          \
    +2.25422      * pmax(0, Poro-0.276576)*pmax(0, Poro-0.154993)           \
    -6.27505     * pmax(0, 0.276576-Poro)*pmax(0, Poro-0.154993)           \
    -1.15022e-08 * pmax(0, Depth-2324.47)*pmax(0, Depth-1967.7)              \
    -5.7869e-07  * pmax(0, 2324.47-Depth)*pmax(0, Depth-1967.7)              
    ROM_1_LogArea_50yr = 10 ** ROM_1_LogArea_50yr
    return ROM_1_LogArea_50yr 
#############
# ROM: 0.05-0.5
############# 
def ROM_2_LogArea_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_2_LogArea_50yr =+7.77851   +0.926274     * pmax(0, Perm+14.124)                            \
    -0.803731    * pmax(0, -14.124-Perm)                           \
    -1.74345     * pmax(0, Poro-0.134495)                          \
    +20.5939      * pmax(0, 0.134495-Poro)                          \
    +6.81302e-05  * pmax(0, Depth-2371.91)                           \
    -0.000221734 * pmax(0, 2371.91-Depth)                           \
    +5.56674      * pmax(0, GeoGrad-0.0208928)                         \
    -7.67734     * pmax(0, 0.0208928-GeoGrad)                                  \
    +40.9564      * pmax(0, 0.0807082-Poro)*pmax(0, 0.134495-Poro)          \
    +2.56528      * pmax(0, Poro-0.29977)*pmax(0, Poro-0.134495)            \
    -4.19759     * pmax(0, 0.29977-Poro)*pmax(0, Poro-0.134495)            \
    +1.18185      * Perm*pmax(0, 0.134495-Poro)                     
    ROM_2_LogArea_50yr = 10 ** ROM_2_LogArea_50yr
    return ROM_2_LogArea_50yr 
#############
# ROM: 0.1-1
############# 
def ROM_3_LogArea_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_3_LogArea_50yr =+7.87111   +0.957349     * pmax(0, Perm+14.0318)                           \
    -0.883646    * pmax(0, -14.0318-Perm)                          \
    -2.27562     * pmax(0, Poro-0.135424)                          \
    +4.74665      * pmax(0, 0.135424-Poro)                          \
    +7.22167e-05  * pmax(0, Depth-2389.27)                           \
    -0.000179613 * pmax(0, 2389.27-Depth)                           \
    +5.72267      * pmax(0, GeoGrad-0.021221)                          \
    -7.69292     * pmax(0, 0.021221-GeoGrad)                          \
    +0.319136     * pmax(0, Poro-0.0463671)*pmax(0, -14.0318-Perm)          \
    -6.73777     * pmax(0, 0.0463671-Poro)*pmax(0, -14.0318-Perm)          \
    +2.93109      * pmax(0, Poro-0.176815)*pmax(0, Poro-0.135424)                    \
    -21.8086     * pmax(0, Poro-0.0479827)*pmax(0, 0.135424-Poro)          \
    +91.6409      * pmax(0, 0.0479827-Poro)*pmax(0, 0.135424-Poro)          \
    -2.13641e-07 * pmax(0, Depth-1872.12)*pmax(0, 2389.27-Depth)             \
    -5.965e-08   * pmax(0, 1872.12-Depth)*pmax(0, 2389.27-Depth)             
    ROM_3_LogArea_50yr = 10 ** ROM_3_LogArea_50yr
    return ROM_3_LogArea_50yr 
#############
# ROM: 0.5-5
############# 
def ROM_4_LogArea_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_4_LogArea_50yr =+ 8.12744    + 0.989924     * pmax(0, Perm+13.827)                           \
    + -0.871535    * pmax(0, -13.827-Perm)                          \
    + -2.33838     * pmax(0, Poro-0.134068)                         \
    + 5.18262      * pmax(0, 0.134068-Poro)                         \
    + 7.011e-05    * pmax(0, Depth-2383.1)                           \
    + -0.000228812 * pmax(0, 2383.1-Depth)                           \
    + 5.81918      * pmax(0, GeoGrad-0.0313561)                        \
    + -7.1347      * pmax(0, 0.0313561-GeoGrad)                        \
    + 0.297907     * pmax(0, Poro-0.132927)*pmax(0, -13.827-Perm)           \
    + -1.23484     * pmax(0, 0.132927-Poro)*pmax(0, -13.827-Perm)           \
    + 2.9331       * pmax(0, Poro-0.170506)*pmax(0, Poro-0.134068)          \
    + 22.4529      * pmax(0, 0.170506-Poro)*pmax(0, Poro-0.134068)          \
    + -17.6022     * pmax(0, Poro-0.0559029)*pmax(0, 0.134068-Poro)         \
    + 56.709       * pmax(0, 0.0559029-Poro)*pmax(0, 0.134068-Poro)       
    ROM_4_LogArea_50yr = 10 ** ROM_4_LogArea_50yr
    return ROM_4_LogArea_50yr 
#############
# ROM: 1-10
#############
def ROM_5_LogArea_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_5_LogArea_50yr =+7.59071    +0.9818       * pmax(0, Perm+14.4169)                           \
    -0.838653    * pmax(0, -14.4169-Perm)                          \
    -2.58524     * pmax(0, Poro-0.134274)                          \
    +4.90338      * pmax(0, 0.134274-Poro)                          \
    +7.01637e-05  * pmax(0, Depth-2386.28)                           \
    -0.000228316 * pmax(0, 2386.28-Depth)                           \
    +5.73997      * pmax(0, GeoGrad-0.0336373)                         \
    -7.4741      * pmax(0, 0.0336373-GeoGrad)                         \
    +0.27407      * pmax(0, Perm+13.3735)*pmax(0, Poro-0.134274)            \
    +0.480633     * pmax(0, -13.3735-Perm)*pmax(0, Poro-0.134274)           \
    +3.09505      * pmax(0, Poro-0.171337)*pmax(0, Poro-0.134274)                   \
    -16.054      * pmax(0, Poro-0.0559029)*pmax(0, 0.134274-Poro)          \
    +58.3115      * pmax(0, 0.0559029-Poro)*pmax(0, 0.134274-Poro)          
    ROM_5_LogArea_50yr = 10 ** ROM_5_LogArea_50yr
    return ROM_5_LogArea_50yr 
#############
# ROM: 5-50
############# 
def ROM_6_LogArea_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_6_LogArea_50yr =+8.96233   +0.945514     * pmax(0, Perm+13.0271)                           \
    -0.98392     * pmax(0, -13.0271-Perm)                          \
    -2.301       * pmax(0, Poro-0.149085)                          \
    +4.46168      * pmax(0, 0.149085-Poro)                          \
    +6.51147e-05  * pmax(0, Depth-2436.2)                            \
    -0.000116014 * pmax(0, 2436.2-Depth)                            \
    +5.42171      * pmax(0, GeoGrad-0.0381185)                         \
    -7.59567     * pmax(0, 0.0381185-GeoGrad)                         \
    -1.25964e-06 * Thick*pmax(0, 2436.2-Depth)                         \
    +2.97183      * pmax(0, Poro-0.206273)*pmax(0, Poro-0.149085)                    \
    -10.9212     * pmax(0, Poro-0.0618619)*pmax(0, 0.149085-Poro)          \
    +41.2767      * pmax(0, 0.0618619-Poro)*pmax(0, 0.149085-Poro)          \
    +0.0990039    * pmax(0, Poro-0.180538)*pmax(0, Perm+13.0271)            \
    -2.23322     * pmax(0, 0.180538-Poro)*pmax(0, Perm+13.0271)            
    ROM_6_LogArea_50yr = 10 ** ROM_6_LogArea_50yr
    return ROM_6_LogArea_50yr 
###########
# ROM: 10-max
########### 
def ROM_7_LogArea_50yr(Depth, Thick, Perm, Poro, GeoGrad): 
    ROM_7_LogArea_50yr =+9.54237 +0.546609     * pmax(0, Perm+12.4588)                                        \
    -0.931851    * pmax(0, -12.4588-Perm)   -1.26737     * pmax(0, Poro-0.164458)                                   \
    +4.59663      * pmax(0, 0.164458-Poro)  +3.47851e-05  * pmax(0, Depth-3086.26)                                   \
    -0.000108674 * pmax(0, 3086.26-Depth)  -8.27151     * pmax(0, 0.0455564-GeoGrad)                                      \
    -0.00499583  * Thick*pmax(0, Poro-0.164458)                                    \
    -3.98653     * pmax(0, Perm+13.1652)*pmax(0, 0.164458-Poro)                         \
    +3.91035      * pmax(0, -13.1652-Perm)*pmax(0, 0.164458-Poro)                                 \
    -0.0329986   * pmax(0, 0.411336-Poro)*Thick*pmax(0, Poro-0.164458)                     \
    -0.0001261   * pmax(0, Depth-1074.12)*pmax(0, Perm+12.4588)                                  \
    +2.03878      * pmax(0, Perm+12.5313)*pmax(0, Poro-0.164458)                         \
    -0.122218    * pmax(0, -12.5313-Perm)*pmax(0, Poro-0.164458)                        \
    +7.58921e-07  * pmax(0, Depth-1766.82)*Thick*pmax(0, Poro-0.164458)                      \
    -9.20507e-06 * pmax(0, 1766.82-Depth)*Thick*pmax(0, Poro-0.164458)                      \
    -0.00791327  * pmax(0, GeoGrad-0.0143965)*pmax(0, Depth-1074.12)*pmax(0, Perm+12.4588)          \
    -0.0808961   * pmax(0, 0.0143965-GeoGrad)*pmax(0, Depth-1074.12)*pmax(0, Perm+12.4588)          \
    -71.0775     * Poro*pmax(0, -13.1652-Perm)*pmax(0, 0.164458-Poro)                     \
    +0.00058976   * pmax(0, Depth-1250.45)*pmax(0, 0.0455564-GeoGrad)                        \
    -0.00962344  * pmax(0, 1250.45-Depth)*pmax(0, 0.0455564-GeoGrad)                      
    ROM_7_LogArea_50yr = 10 ** ROM_7_LogArea_50yr
    return ROM_7_LogArea_50yr