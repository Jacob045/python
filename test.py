from scipy.optimize import curve_fit
import numpy as np
 
xdata = [0.1738, 0.0325, 0.0135, 0.0058, 0.0028]
ydata = [11.313, 15.953, 21.599, 33.212, 54.098]
 
### define the fit functions, y = a * x^b ###
def target_func(x, a, b):
    return a*(x**b)

 
### curve fit ###
popt, pcov  = curve_fit(target_func, xdata, ydata)
 
### Calculate R Square ###
calc_ydata = [target_func(i, popt[0], popt[1]) for i in xdata]
res_ydata  = np.array(ydata) - np.array(calc_ydata)
ss_res     = np.sum(res_ydata**2)
ss_tot     = np.sum((ydata - np.mean(ydata))**2)
r_squared  = 1 - (ss_res / ss_tot)
 
### Output results ###
print("a = %f  b = %f   R2 = %f"%(popt[0], popt[1], r_squared))
print(ydata, calc_ydata)
print()
