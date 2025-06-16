# Data Formats

## Worldwide Population - 2019-2020

- both sexes, all ages
- global and all countries
	- global marked 
	- list of countries in ??
	
## Starting data

What date in the year is the data taken?
- WPP2019 - always July 1
- WPP2022 - includes Jan 1 and July 1, but most in July 1.  Using July 1.
- 

## BMGF dataset

Scenarios:

- Slower Met Need and Education (-1)
- Reference (0)
- Faster Met Need and Education (1)
- Fastest Met Need and Education (2)
- SDG Met Need and Education (3)

## UN 2019 dataset

Scenarios:

- low
- medium
- high

Original columns:  Variant	Region	Notes	Country code	Type	Parent code

## UN 2022 dataset

Scenarios:

- low
- medium
- high 
- (others not currently used)

Original columns:  Index	Variant	Region, subregion, country or area *	Notes	Location code	ISO3 Alpha-code	ISO2 Alpha-code	SDMX code**	Type	Parent code

Note:  UN2019 and UN2022 have the same list of 235 countries

Format:
- originally stored as one set of values per region per year
- deleted top rows and unused columns by hand
- deleted Index, ISO, Alpha and SMDX code, change "Region,..." to "Region"
- changed "Total..." to "population"
- changed 'Year' to 'year'

## Wittgenstein dataset



