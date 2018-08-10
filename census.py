"""
@author: Jennifer "Jenny" Bloom
Created on Mon Aug 31 17:17:03 2015
Assignment #1 Part 1

This assignment calculates projected population in one year based on current
rates of change for birth, death, and immigration. 
"""
# Modules of interest:
#import math

# Variables of interest:
br = 1/8    #birth rate per second, growth 
dr = 1/13   #death rate per second, shrink
ir = 1/40   #immigration rate per second, growth
pop_orig = 318892103 #original population
spy = 60*60*24*365  #seconds per year, an approximation

"""
rate_o_change is in population for 1 yr, seconds per year multiplied by the
function of birth rate plus immigration rate (both growth) subtracting death.
This is used to calculate projected population (pop_final), rounded to include 
whole persons, not fractions of persons.
"""
rate_o_change = round(spy*(br+ir-dr)) #round up to incorporate fractions
pop_final = int(rate_o_change + pop_orig) #final projected population 
print("The population will be", pop_final)

