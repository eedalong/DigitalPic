input = open('codes');
output = open('tmp2','w');
for item in input.readlines():
	output.write(item[:-1]);
output.close();
