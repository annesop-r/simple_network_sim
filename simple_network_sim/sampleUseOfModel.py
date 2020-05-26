import copy
import random
import sys
import matplotlib.pyplot as plt

from . import common, network_of_populations as ss

numInfected = 10
def cumulative(plot):
        cumPl = []
        cumPl.append(plot[0])
        for i in range(1, len(plot)):
            cumPl.append(plot[i] + cumPl[i-1])
        return cumPl
    
truth = []
for line in open(sys.argv[5]):
        truth.append(int(line.strip()))

for infectVal in [0.2, 0.3, 0.4]:

    
    
    basicPlots = []
    

    
    time = 40
    numTrials = 10
    trialIndex= 0
    
    for region in ["S00133635"]:
        network = ss.createNetworkOfPopulation(sys.argv[1], sys.argv[2], sys.argv[3], infectVal)
        initialState = copy.deepcopy(network.states[0])
        print("trial starting - " + str(trialIndex))
        network.states[0] = initialState
        ageDistribution = {"m": 1.0}
        ss.exposeRegions([region], numInfected, ageDistribution, network.states[0])
        basicPlots.append(ss.basicSimulationInternalAgeStructure(network, time))
        trialIndex = trialIndex +1
    
    for plot in basicPlots:
        plt.plot(cumulative(plot), color = 'purple', alpha=0.2)
    
    plt.plot(common.generateMeanCumulativePlot(basicPlots), color ='dodgerblue', label='basic')
    plt.plot(common.generateMeanPlot(basicPlots), color ='red', label='basic')
    plt.plot(truth, color ='black', label='basic')
    
    plt.savefig("mat_" + str(infectVal) + "_"+ sys.argv[4])
    plt.clf()
