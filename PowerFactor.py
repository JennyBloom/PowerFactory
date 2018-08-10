"""
Jenny Bloom
08/28/2015
Assignment #1 Part 2
This assignment calculates the power factor used to charge customers
rates based on real and reactive power usage. 
"""

"""
The power factor is a ratio used to quantify the amount of power 
provided to users, measuring flow of real power in relation to the
apparent power in the circuit.
Power Factor = Real Power (kW) / Apparent Power (kVA) = (kW) / 
(sqrt((kW)^2 + (kVAr)^2)
"""
import math

real_power = float(input("Enter the Real Power" ))
reactive_power = float(input("Enter the Reactive Power"))
apparent_power = pow(real_power, 2) + pow(reactive_power, 2)

power_factor = round(((real_power) / math.sqrt(apparent_power))*100)

print("The power factor is %i" %power_factor + "%")
# The % is a placemarker inside a string, the .i is integer placeholder.
# The + "%" allows the percent sign to come after the power factor.
# The round() was used in HW1 Part 1
