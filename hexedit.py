import sys

if (len(sys.argv) < 2):
	print("Invalid arguments")
	print("Provide hex to convert to ascii")
else:
	sys.stdout.write(sys.argv[1].decode('hex'))
