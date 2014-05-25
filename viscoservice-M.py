#!/usr/bin/env python

# re-calculates pump characteristics for viscous fluids - Hydraulic Institute Coeff
# BEP - Best Efficiency Point
# metric units

# D. Djokic, 2014

import numpy as np

visco = float(raw_input("Enter new fluid viscosity in cSt: "))
sg = float(raw_input ("Specific Gravity: "))

inpfilename = raw_input("Input Filename with original data - METRIC units: ")
data = coords = np.loadtxt(inpfilename, dtype=float, comments="#", delimiter=',', converters=None, skiprows=1, usecols=(1,2,3,4), unpack=False, ndmin=0)

# arrays to store data
Q=[]
H=[]
Eff=[]
HPow=[]

for pnts in range (0,4):
	Q.append(data[pnts,0])
	H.append(data[pnts,1])
	Eff.append(data[pnts,2])
	HPow.append(data[pnts,3])

QBEP=Q[2]
HBEP=H[2]


# calculating pseudocapacity

pseudo = 1.95*(visco**0.5)*(0.04739*((HBEP/0.3048)**0.25739) *((QBEP/0.227)**0.5))**0.5

# Hydraulic Institute Polynomial Coeffs

DEff = [1.0522, -3.512E-2, -9.0394E-4, 2.2218E-4, -1.198E-5, 1.9895E-7]
DQ = [0.9873, 9.019E-3, -1.6233E-3, 7.7233E-5, -2.0258E-6, 2.1009E-8]
DH06 = [1.0103, -4.6061E-3, 2.4091E-4, -1.6912E-5, 3.2459E-7, -1.16611E-9]
DH08 = [1.0167, -8.3641E-3, 5.1288E-4, -2.9941E-5, 6.1644E-7, -4.0487E-9]
DH10 = [1.0045, -2.664E-3, -6.8292E-4, 4.9706E-5, -1.6522E-6, 1.9172E-8]
DH12 = [1.0175, -7.8654E-3, -5.6018E-4, 5.4967E-5, -1.9035E-6, 2.1615E-8]

# calculating HI Coeffs.
CEff1=[]
CQ1=[]
CH061=[]
CH081=[]
CH101=[]
CH121=[]
CH=[]

for i in range(0,6):
	CEff1.append(DEff[i]*pseudo**i)
	CQ1.append(DQ[i]*pseudo**i)
	CH061.append(DH06[i]*pseudo**i)
	CH081.append(DH08[i]*pseudo**i)
	CH101.append(DH10[i]*pseudo**i)
	CH121.append(DH12[i]*pseudo**i)

CEff=sum(CEff1)
CQ = sum(CQ1)
CH.append(sum(CH061))
CH.append(sum(CH081))
CH.append(sum(CH101))
CH.append(sum(CH121))

QVisco=[]
HVisco=[]
EffVisco=[]
HPowVisco=[]

for pnts in range (0,4):
	QVisco.append(CQ*Q[pnts])
	EffVisco.append(CEff*Eff[pnts])
	HVisco.append(CH[pnts]*H[pnts])
	HPowVisco.append(QVisco[pnts]*HVisco[pnts]*sg/(3960*EffVisco[pnts]))

# writing results to input file

BEPCapacity=[60,80,100,120]

fn = open(inpfilename, "a")
fn. write("\n")
fn.write("Fluid Viscosity [cSt]")
fn.write(",")
fn.write (str(visco))
fn.write("\n")
fn.write("Fluid Specific Gravity")
fn.write(",")
fn.write(str(sg))
fn.write("\n")
fn.write("% BEP Capacity,Q[cum/h], H[m], Efficiency[%], Power[kW]")

for cnt in range (0,4):
	fn.write("\n")
	fn.write(str(BEPCapacity[cnt]))
	fn.write(",")
	fn.write(str(QVisco[cnt]))
	fn.write(",")
	fn.write(str(HVisco[cnt]))
	fn.write(",")
	fn.write(str(EffVisco[cnt]))
	fn.write(',')
	fn.write(str(HPowVisco[cnt]))

fn.close()