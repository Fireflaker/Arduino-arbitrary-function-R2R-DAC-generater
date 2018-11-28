from __future__ import print_function
from sympy import *
import numpy
import matplotlib
from matplotlib import pylab, mlab, pyplot
import numpy as np

pyplot.show()

x = Symbol('x') #like varable
init_printing (use_latex='mathjax')

plot= ("5x^3")
from sympy.plotting import plot, plot_parametric

#expr = sin(2*sin(x**3))

expr = sin(x**x)

plot(expr,(x,0,5));

xsample = 4000
precition_float = float(100) #bigger value, more horizontally precise


output = []
output2 = []

for num_float in range(0,xsample):

    (pi*x**2 + x/3).evalf()

    xval_float = (num_float/precition_float)       #culculate
    
    obj_float = expr.subs(x,xval_float)            #culculate expression
    output.append(obj_float)
    
    print('obj=', obj_float)
    print('num=', num_float)
    print('xval=', xval_float)
    

print('output=', output)
print('data length is ', xsample)

print('!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

verticalresolution = float(256)        

y = np.array(output)


for num2_float in range(0,xsample):
    q = verticalresolution/2 + (y[num2_float]) * verticalresolution/2  #half of resolution for abs val
    roundoutput = round(q,0)
    print('multiplied output = ', q)
    print('rounded output = ', roundoutput)
    output2.append(roundoutput)
    
print('the secondary output is', output2)

print('!!!!!!!Part2 job DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

portcode='D'

import sys
sys.stdout.write('.')
sys.stdout.flush()
print('')
print('')
print('')
print('///////////////////////////////Copy from here////////////////////////////////')
print('')
print('void setup() {')
print('noInterrupts();')

print('DDR', end='')
print(portcode, end='')
print(' = ', end='')
print('B11111111;')

print('}')
print('')
print('void loop() {')

for num3 in range(0,xsample):
    
    print('PORT', end='')
    print(portcode, end='')
    print(' = B', end='')
    if(output2[num3])==256:
        (output2[num3])=255
    print(bin(int((output2[num3])))[2:], end='')
    print(';        //Sample=',num3+1, '/', xsample, '  Value=',int((output2[num3])))
    

print('}')
print('')
print('///////////////////////////////Code end////////////////////////////////')
