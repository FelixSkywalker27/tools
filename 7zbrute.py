from argparse import ArgumentParser
import itertools
import subprocess

chars = "0123456789" ##abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
		
def main():
	argp = ArgumentParser()
	argp.add_argument('-f', '--file', dest='file', required=True, help='Path of file')
	args = argp.parse_args()
	file = args.file
	i = 4;
	searching = True
	while i<10 and searching:
		p = itertools.combinations_with_replacement(chars, i)
		for e in p:
			password = "".join(e)
			r = subprocess.getoutput('"C:\\Program Files\\7-Zip\\7z.exe" e '+file+" -p"+password)
			if not "Wrong password?" in r:
				print("\n\n [+] " + "Password found!!" + " %s\n" % password)
				exit()
			else:
				print(password)
		i = i+1
	return

		
if __name__ == "__main__":
	main()