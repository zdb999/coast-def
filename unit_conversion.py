
# This must run on import

# set up for unit conversion
# everything is based off meters internally

convert_table = {'m':1}
convert_table['km'] = 0.001
convert_table['cm'] = 100.
convert_table['mm'] = 1000.
convert_table['ft'] = 3.28084
convert_table['feet'] = 3.28084
convert_table['in'] = 39.37008
convert_table['yrd'] = 1.09361
convert_table['yards'] = 1.09361
convert_table['mi'] = 0.00062137121212121
convert_table['miles'] = 0.00062137121212121
convert_table['nmi'] = 0.000539955174946
convert_table['nautical mile'] = 0.000539955174946


def convert_unit(value, from_unit, to_unit):
	"""Convert distance units from one unit to another.

	Args:
		value (float or int): The value to be converted.
		from_unit (str): The short name of the value's unit.
		to_unit (str): The short name of the desired unit.

    Returns:
		float: The value in its new units.
	"""

	# Check for bad inputs

	assert from_unit in convert_table, "Unfortunately, {} is not a unit we know.".format(from_unit)
	assert to_unit in convert_table, "Unfortunately, {} is not a unit we know.".format(to_unit)
	
	#Convert to meters then to desired unit

	meters = float(value) / convert_table[from_unit]
	return meters * convert_table[to_unit]
