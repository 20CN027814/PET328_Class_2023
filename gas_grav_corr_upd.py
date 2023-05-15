co2_comp=input('what is the co2 composition')
n2_comp=input('what is the n2 composition')
h2s_comp=input('what is the h2s composition')
h2o_comp=input('what is the h2o composition')
gas gravity=input('what is the standard gas gravity')

#convert inputs to numerals
co2_comp=float(co2_comp)
n2_comp=float(n2_comp)
h2s_comp=float(h2o_comp)
h2o_comp=float(h2o_comp)
gas_gravity=float(gas_gravity)

#the if statement
if co2_comp=0.12 or n2_comp=0.03 or h2s_comp=0:
    corr_gas_gravity=((gas_gravity)-(1.1767*yh2s)-(1.5196*yco2)-(0.9672*yn2))/(1-yh2s-yco2-yn2)
    print('the corrected gas gravity is',corr_gas_gravity)

#determing pseudocritical pressure and pseudo critical temperature
p_pch=756.8-131.0*corr_gas_gravity-3.6*corr_gas_gravity**2
t_pch=169.2+349.5*corr_gas_gravity-74.0*corr_gas_gravity**2

#displaying the results
print( 'The hydrocarbon pseudo-critical pressure is',pseudo_pre,'psia')
print('The hydrocarbon pseudo-critical temperature is',pseudo_temp,'deg Rankine')

#determing pseudoreduced pressure and pseudoreduced temperature
pseudo_red_pre=(1-yh2s-yco2-yn2)*pseudo_pre + 1306*yh2s+1071*yco2+493.1*yn2
pseudo_red_temp=(1-yh2s-yco2-yn2)*pseudo_temp+672.35*yh2s+547.58*yco2+227.16*yn2

#displaying the results
print( 'The hydrocarbon pseudo-reduced pressure is',pseudo_red_pre,'psia')
print( 'The hydrocarbon pseudo-reduced temperatureis',pseudo_red_temp,'deg Rankine')
               
