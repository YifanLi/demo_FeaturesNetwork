This directory includes these files:

1. test.py demo script
2. test.csv file for features/cases relationship weight data storage.
3. Demo.jpg show the cases-network.

NOTE: Please Install Python before run test.py, add the path of python.exe and .py into Environment Variables.

Introduction
===============
This demo script test.py is for test scope definition.

For selected targetcase and initial weight value, it follows the links and iterates to find out the needed nodes.


Usage
===============
Note: Opent the directory in cmd line for Windows.

test.py TargetCase InitWeight IterationTimes IncreaseWeight

inputs:
TargetCase/Node - base on the case index, e.g. 1~10 for Demo
InitWeight      - the weight value selected for derectly connected neighbor case
IterationTimes  - the times of iteration, e.g. 3,5,...
IncreaseWeight  - the weight value should be increased on scale, like +0.1
                  for each iteration.
                  
outputs:
- the expected cases(index number) will be returned.

Example
===============

> test.py 3 0.5 3 0.1

> test.py 5 0.3 4 0.2



----- by Yifan, 2012/04/17