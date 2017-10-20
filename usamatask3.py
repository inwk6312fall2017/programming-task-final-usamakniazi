file = open("running-config.cfg")
file2 = open("conf.txt", "w")
for line in file:
 file2.write(line.replace('172', '192'))
