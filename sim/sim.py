# Calculates the population of a region over a number of years based on 
#   initial population, fertility rate and death rate.  It currently assumes
#   there is an equal number of males and females in the country.

# Simulates as many years as are in the dataframe.  
# Columns in the input df:
#   - year - year to simulate
# 	- frt - fertility rate as babies/population
# 	- drt - death rate as deaths/population
#   - mig - total migrants
# Returns the same df plus a 'pop' column.   Note that
#   pop[N+1] is based on the parameters for year N

def sim_df (df):

