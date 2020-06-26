
import numpy as np
import random



MissionFailureProb = 0.01
SpacecraftFailureProb = 0.0078125
DeltaSpacecraftFailureProb = 0.00390625
Loops = 1000000
SatFailuresCount = 0
MissionFailuresCount = 0
ComputedMissionFailureProb = 0
PrecisionThresshold = 0.000001

#For verification purposes
OneFailureOnly = False

SpacecraftArray = np.zeros((9, 34))


TestArray = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]])


def CheckFailure(ArrayToCheck):
	for y in range(0, ArrayToCheck.shape[0]):
		for x in range(0, ArrayToCheck.shape[1]):
			if ArrayToCheck[y,x] == 1 and np.sum(ArrayToCheck[y,x-2:x+2]) > 1:
				return 1
			if ArrayToCheck[y,1] == 1 and ArrayToCheck[y,2] == 1:
				return 1
			if ArrayToCheck[y,1] == 1 or ArrayToCheck[y,2] == 1 and ArrayToCheck[y,-1] == 1:
				return 1
			if ArrayToCheck[y,1] == 1 and ArrayToCheck[y,-1] == 1 or ArrayToCheck[y,-2] == 1:
				return 1    
			if np.sum(ArrayToCheck[y-1:y+1,x]) > 1:
				return 1
			if np.sum(ArrayToCheck[0,::]) >= 1 and np.sum(ArrayToCheck[8,::]) >= 1:
				return 1
			if OneFailureOnly == True and ArrayToCheck[y,x] == 1:
				return 1
	return 0

print("The test is:", CheckFailure(TestArray))

while DeltaSpacecraftFailureProb > PrecisionThresshold:
	MissionFailuresCount = 0
	print("Repeating with probability",SpacecraftFailureProb) 
	for i in range(0,Loops):
		SpacecraftArray.fill(0)
		for x in range(0, SpacecraftArray.shape[0]):
			for y in range(0, SpacecraftArray.shape[1]):
				RandNumb = random.uniform(0, 1)
				if RandNumb < SpacecraftFailureProb:
					SpacecraftArray[x,y] = 1
					SatFailuresCount = SatFailuresCount + 1
		MissionFailuresCount = MissionFailuresCount + CheckFailure(SpacecraftArray)
	print("MissionFailuresCount",MissionFailuresCount)
	ComputedMissionFailureProb = MissionFailuresCount/Loops

	if ComputedMissionFailureProb > MissionFailureProb:
		SpacecraftFailureProb = SpacecraftFailureProb - DeltaSpacecraftFailureProb
	if ComputedMissionFailureProb < MissionFailureProb:
		SpacecraftFailureProb = SpacecraftFailureProb + DeltaSpacecraftFailureProb
	DeltaSpacecraftFailureProb = DeltaSpacecraftFailureProb/2
	print("SpacecraftFailureProb", SpacecraftFailureProb)
	print("ComputedMissionFailureProb", ComputedMissionFailureProb)


print("**************************************")
print("Finished, Reached precision thresshold")
print("**************************************")
print("SpacecraftFailureProb", SpacecraftFailureProb)
print("ComputedMissionFailureProb", ComputedMissionFailureProb)









	



