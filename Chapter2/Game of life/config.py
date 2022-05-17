InitConfig = open("confige.txt", 'rb')

l = list(InitConfig.read())
t = ()
config = []
for i in range(1,10,2):
	config.append((l[i-1],l[i]))
	
print(config[:10])

# [(14, 17), (21, 27), (10, 1), (12, 21), (10, 14), (9, 25), (1, 19), (17, 11), (12, 24), (17, 29)]