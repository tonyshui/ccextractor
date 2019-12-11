import sys
import srt

def censor(text, word):
    return text.replace(word, '[bleep]')

def main():
	srt = open(sys.argv[1],"r").read()
	blacklist = open(sys.argv[2], "r").read()
	# print(srt)
	# print(blacklist)
	for expletive in blacklist.split():
		print('censoring for: ' + expletive)
		srt = censor(srt, expletive)
		print('text now looks like this:\n' + srt)

	print('done censoring! final text:\n' + srt)

if __name__ == "__main__":
	main()

