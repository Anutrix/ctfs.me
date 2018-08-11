import os

for i in range(332,0,-1):
	command1 = 'fcrackzip -u -D -p "rockyou.txt" level'+str(i)+'.zip'
	data = os.popen(command1).readlines()
	print('level'+str(i)+'.zip',data)
	s = ""
	for j in data:
		s+=j
	start = s.find('pw == ')+6
	end = s.find('\n',start)	
	password = s[start:end]
	command2 = 'unzip -P '+ password + ' level'+str(i)+'.zip'
	os.system(command2)