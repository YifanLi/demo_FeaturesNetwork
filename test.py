# filename:test.py, only for Intel internal
# The tool is a simple demo to define test cases scope, for "BIOS Feature Affinity Study" 

from sys import argv, exit, stdout, stderr

global Nval,Pval,Lval,Ival

# arguments process function
def exit_with_help():
	print("""\
Usage: %s TargetCase InitWeight IterationTimes IncreaseWeight

This script tool can find out these cases which are closely related with target node or case.

inputs:
TargetCase/Node - base on the case index, e.g. 1~10 for Demo
InitWeight      - the weight value selected for derectly connected neighbor case
IterationTimes  - the times of iteration, e.g. 3,5,...
IncreaseWeight  - the weight value should be increased on scale, like +0.1
                  for each iteration.
                  
outputs:
- the expected cases(index number) will be returned.

----- by Yifan
""" % argv[0])
	exit(1)
	
# get quantity of lines(cases) in file		
def getLineNum():
    f = open('test.csv')
    lineNum = 0
    for line in f:
        lineNum=lineNum+1
    f.close()
    return lineNum
    
# get the X Line's string
def getXLine(line):
    f = open('test.csv')
    lines=""
    for x in range(line):
        lines = f.readline()
    f.close()
    return lines
# search the X line to find out the expected value(case)
def searchXLine(line,height,index_list,ln):
    linestr = getXLine(line)
    for x in range(0,getLineNum()):
        c = linestr.split(',')[x]
        if float(c)>=height and index_list[x]==0:
            # mark the case in index_list 
            index_list[x]=ln+1
            print("%s iteration --> %d" %(ln,(x+1)))
                   
argc = len(argv)
if argc != 5:
	exit_with_help()
	
# transform arguments to available type
Nval = int(argv[1])
Pval = float(argv[2])
Lval = int(argv[3])
Ival = float(argv[4])

n = getLineNum()
# retain a list to indicate the accessed nodes  
index_list = [0]*n

index_list[Nval-1]=1
#linestr = getXLine(Nval)
#index_list[Nval]=1
print("Base on the parameters, the following cases should be executed:")
print("-----")
for l in range(Lval):
      for index,item in enumerate(index_list):
          if item == l+1: searchXLine((index+1),(Pval+Ival*l),index_list,l+1)

print("Hi, the iteration finished or no more availale nodes fulfill the need.")
         
            
        


        
    

