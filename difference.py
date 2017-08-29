import codecs
import sys

def Diff(file1, file2):
	a = {}
	with codecs.open('out/same.txt','w','utf8') as out1:
		with codecs.open('out/diff.txt','w','utf8') as out2:
			with codecs.open(file1,'r','utf8') as source1:
				for line in source1.readlines():
					line = line.strip('\n')
					line = line.strip('\r')
					a[line] = 0

			with codecs.open(file2,'r','utf8') as source2:
				for line in source2.readlines():
					line = line.strip('\n')
					line = line.strip('\r')
					if line in a:
						a[line] += 1
						out1.writelines(line + '\n')
					else:
						out2.writelines(line + '\n')

			for k,v in a.items():
				if v == 0:
					out2.writelines(k + '\n')

if __name__=='__main__':
	if len(sys.argv) < 3:
		print('there is some question')
	else:
		Diff(sys.argv[1], sys.argv[2])
