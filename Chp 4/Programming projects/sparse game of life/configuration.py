

def configuration(name):
	configure = {	
		"LWS":[[(0,0),(0,2),(1,3),(2,3),(3,3),(4,3),(4,2),(4,1),(3,0),
				(0,10),(0,12),(1,13),(2,13),(3,13),(4,13),(4,12),(4,11),(3,10)],(95,10)],
		# "SLIDER":[]

		"SLIDER GUN":[[(1,5),(2,5),(1,6),(2,6),(35,3),(36,3),(35,4),(36,4),\

				(11,5),(11,6),(11,7),(12,4),(13,3),(14,3),(16,4),
				(17,5),(17,6),(17,7),(15,6),(18,6),(16,8),(14,9),
				(13,9),(12,8),\

				(21,3),(21,4),(21,5),(22,3),(22,4),(22,5),(23,2),
				(23,6),(25,1),(25,2),(25,6),(25,7)],(50,10)]

	}
	if name.upper() in configure.keys():
		return configure[name.upper()]
	return configure["LWS"]

if __name__ == '__main__':
	
	configure = configuration("lws")
	(row, col), configure = configure[1], configure[0]
	print(row, col, configure)