import sys

if (len(sys.argv) < 2):
	print("Invalid arguments")
	print("Provide hex to convert to ascii")
elif (len(sys.argv[1])%2 == 0):
	sys.stdout.write(sys.argv[1].decode('hex'))
else:
	sys.stdout.write((sys.argv[1]+"0").decode('hex'))
