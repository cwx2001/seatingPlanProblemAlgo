# seatingPlanProblemAlgo
Repo of Python code implementation for the Nearest Neighbour Algorithm with 2-Opt mechanism to solve the Seating Plan Problem 

=============================================
SEATING PLAN PROBLEM ALGORITHM: NEARESTNEIGHBOUR AND 2-OPT ALGORITHM
=============================================

There are 3 ways of using the program, depending of the method of data input:

--------------------------------------
Data input through console inputs
--------------------------------------
How to use:
1. Set isUserInput boolean to True
2. Console prompts user to input amount of seats to be assigned, enter desired int value (recommended value = 5).
3. Console prompts user to input names of people to be assigned to seats, enter desired String value.
4. Console prompts user to input relationship values between two people, enter desired int value between 0 to 100.
	Note: value 50 to indicate neutral relationship, 0 for low comfortability and 100 for high comfortability
	If no error messages show in console, continue.


--SKIP TO ALGORITHM PROCESS SECTION AT THIS POINT--

--------------------------------------
Data input through variables
--------------------------------------
Code for sample test data seaterName, relMatrix is already provided. 
Reference seaterName and relMatrix to substitute desired data.
Skip to algorithm process on discretion.

How to use:
1. Set isUserInput boolean to False
--SKIP TO ALGORITHM PROCESS SECTION IF TEST DATA UNCHANGED--
2. Create variable of list for names of people to be assigned to seats
3. Create variable of numPy array for relationship value adjacency matrix
4. Pass variable into verifyRelationsMatrix() method in order of (matrix, nameList)
	Do not change variable name of returned output.
	If no error messages show in console, continue.


--SKIP TO ALGORITHM PROCESS SECTION AT THIS POINT--

--------------------------------------
Random Data input
--------------------------------------
Code to generate random matrix is provided as comments .
uncomment line 
	relMatrixDict = createRandomRelationsMatrix(200) 
to use.

How to use:
1. Set isUserInput boolean to False
2. Uncomment (Remove # symbol) from line below to use:
		#relMatrixDict = createRandomRelationsMatrix(200) 
	Note: recomment line (Add # symbol) at start of line to disable use.
3. Replace value 200 with desired data size of int value.

--SKIP TO ALGORITHM PROCESS SECTION AT THIS POINT--

=============================================
ALGORITHM PROCESS
=============================================
Code to process matrix and form route is already provided. Skip to visualisation section on discretion.

--------------------------------------
algorithm process 1
--------------------------------------

	routeDict = nearestNeigbour(matrix, origin)

1. This method produces a route based on output from Data input section.
2. Pass the output from Data input section as matrix, and desired origin node as origin.
3. origin is index of a person chosen as a origin node (int value)
4. Method produces output of routeDict which is a dict containing route (list), cost (int) and matrix (pandas.DataFrame)
5. Method prints the CPU execution time of the process in console.

--------------------------------------
algorithm process 2
--------------------------------------
		
	routeDict = twoOpt(route)

1. This method produces a route based on output from algorithm process 1.
2. Pass the output from algorithm process 1 (as it is) as route.
	Note: it is possible to pass in a route that has not went through process 1, provided that data is valid
4. Method produces output of routeDict which is a dict containing route (list), cost (int) and matrix (pandas.DataFrame)
5. Method prints the CPU execution time of the process in console.

=============================================
VISUALISATION
=============================================
Code to visualise result for algorithm process 1 and algorithm process 2 is already provided. Skip on discretion.

	drawSeats(route)

1. This method produces a visualisation of the final result in the console.
2. Pass output from algorithm process into route for visualisation.
	Note: it is possible to pass in a route that has only went through algorithm process 1.
3. Visualisation includes relationship value adjacency matrix, produced optimal route, and its cost.


=============================================
SAMPLE TEST DATA
=============================================
Sample test data to be used for testing purposes. Copy and paste into code by replacing the existing array.

test data 1:
[
[0, 45, 45, 55, 60],
[45, 0, 30, 45, 65],
[45, 30, 0, 10, 30],
[55, 45, 10, 0, 90],
[60, 65, 30, 90, 0]
]

test data 2:
[
[0, 15, 75, 55, 80],
[15, 0, 30, 45, 65],
[75, 30, 0, 10, 30],
[55, 45, 10, 0, 90],
[80, 65, 30, 90, 0]
]
