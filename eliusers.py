#!/usr/bin/env python3
import argparse
import sys
print('''
███████╗██╗     ██╗██╗   ██╗███████╗███████╗██████╗ ███████╗
██╔════╝██║     ██║██║   ██║██╔════╝██╔════╝██╔══██╗██╔════╝
█████╗  ██║     ██║██║   ██║███████╗█████╗  ██████╔╝███████╗
██╔══╝  ██║     ██║██║   ██║╚════██║██╔══╝  ██╔══██╗╚════██║
███████╗███████╗██║╚██████╔╝███████║███████╗██║  ██║███████║
╚══════╝╚══════╝╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝
		by: Rentix Eliyahu
	''')
example_text = ('''\
python3 eliusers.py -w <wordlist>
python3 eliusers.py --wordlist /home/eli/users.txt > output.txt
''')
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=example_text)
parser.add_argument('--wordlist', '-w', help='Path for the wordlist file.')
args = parser.parse_args()
if args.wordlist:
	try:
		wordlist = str(args.wordlist)
		with open (wordlist, 'r') as word:
			w = word.readlines()
			for line in w:
				name = line.rsplit(' ',1)
				first = name[0]
				first = first.rstrip("\n")
				last = name[1]
				last = last.rstrip("\n")
				first = first.lower()
				last = last.lower()
				print (first+last[0])
				print (first+'.'+last[0])
				print (first+'.'+last[0:3])
				print (first+last[0:3])
				print (first[0]+last)
				print (first[0]+'.'+last)
				print (first[0]+'.'+last[0:3])
				print (first+last)
				print (first+'.'+last)
				print (first[0]+last[0:3])
				print (first[0:3]+last[0])
				print (first[0:3]+'.'+last[0])
				print (first[0:3]+last[0:3])
				print (first[0:3]+'.'+last[0:3])
				print (first[0:3]+last)
				print (first[0:3]+'.'+last)
				first = name[1]
				last = name[0]
				first = first.rstrip("\n")
				first = first.lower()
				last = last.lower()
				last = last.rstrip("\n")
				print (first+last[0])
				print (first+'.'+last[0])
				print (first+'.'+last[0:3])
				print (first+last[0:3])
				print (first[0]+last)
				print (first[0]+'.'+last)
				print (first[0]+'.'+last[0:3])
				print (first+last)
				print (first+'.'+last)
				print (first[0]+last[0:3])
				print (first[0:3]+last[0])
				print (first[0:3]+'.'+last[0])
				print (first[0:3]+last[0:3])
				print (first[0:3]+'.'+last[0:3])
				print (first[0:3]+last)
				print (first[0:3]+'.'+last)
	except:
		print ('nice man you fucked it up. no users for you. check ur payload u fuck.')
