#!/usr/bin/env python
# pump hand calculations
import inout
import math
import numpy as np
import warnings
import matplotlib.pyplot as plt

print ("1 - Shaft power")
print ("2 - NPSHa and Cavitation")
print ("3 - Centrifugal Pump Curve")
calc = inout.get_integer("Input 1, 2 or 3: ", 0)
if calc==1:
	print ("Calculating shaft power")
	density=inout.get_float("Input density of fluid in [kg/cum] or '0' for fresh water: ", 1000)
	flow=inout.get_float("Input flow of the pump [cum/h] or '0' for 150 cum/h: ", 150)
	head=inout.get_float("Input differental head [m] or '0' for 30 m: ",30)
	efficiency=inout.get_float("Input pump efficiency or '0' for 0.6: ", 0.6)
	rpm = inout.get_float("Input pump speed (rpm) or '0' for 1500", 1500)
	power=9.81*flow*head*density/(3.6*10**6)
	shaft_power=power/efficiency
	print ("Power = %f kW") %power
	print ("Shaft Power = %f kW") %shaft_power
	
elif calc==2:
	print ("Calculating Net Positive Suction Head available - NPSHa")
	density=inout.get_float("Input density of fluid in [kg/cum] or '0' for fresh water: ", 1000)
	abs_pressure=inout.get_float("Input absolute pressure on surface (atmnosferic+gauge) [kPa a] or '0' for 101.3: ",101.3)
	head_loss=inout.get_float("Input headloss in suction pipe [m] or '0' for 1.2 m: ", 1.2)
	flow=inout.get_float("Input flow of the pump [cum/h] or '0' for 150 cum/h: ", 150)
	dia=inout.get_float("Input pipe ND [mm] or '0' for 50mm: ", 50)
	vapour=inout.get_float("Input vapour pressure of fluid [kPa] or '0' for water @20 degC: ", 2.4)
	elevation=inout.get_float("Height of water surface ABOVE pump centre line [m] or '0' for 1.5 m: ",1.5)
	Area=(math.pi*(dia/1000)**2)/4  #pipe area in meters
	velocity=(flow/Area)/3600 #in m/s
	NPSHa=(abs_pressure-vapour)/(9.81*density)-head_loss+elevation
	print("NPSHa= %f") %NPSHa
	print("Note: NPSHa must be greater than NPSHr(equired)")
	print("For NPSHr refer to maker's Data Sheet")
	criter=abs_pressure/(9.81*density)-vapour/(9.81*density)-head_loss-velocity**2/(2*9.81)+elevation
	if criter >0:
		print ("No cavitation in Pump Suction line - safe")
	else:
		print ("Cavitation will take place!!! Try to optimize suction line by lowering losses, increasing NB or alike") 
elif calc==3:	
	print ("Calculating Pump Curve based on minimum 3 points")
	no_pnts=inout.get_integer("Number of points to fit curve: ", 3)
	if no_pnts < 3:
		print("Not possible to fit parabola with less than 3 points")
	else:
		flow=[]
		loss=[]
		for i in range (0, no_pnts):
			print ("Point %r") %i
			fl=inout.get_float("Enter flow: ", 0)
			lo=inout.get_float("Enter loss: ",0)
			Flow=flow.append(fl)
			Loss=loss.append(lo)
		warnings.simplefilter('ignore', np.RankWarning)
		coeffs=np.polyfit(flow, loss, 2)
		print(coeffs)
		print("H=%f*Q**2+%f*Q+%f") %(coeffs[0], coeffs[1], coeffs[2])
		plt.title("Pump Headloss as function of Flow")
		plt.plot(flow, loss)
		plt.show()
else:
	print("Wrong selection")