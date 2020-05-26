# CurrentlyInUse
def generateMeanPlot(listOfPlots):
    meanForPlot = []
    # print(listOfPlots)
    for i in range(len(listOfPlots[0])):
        sumTot = 0
        for j in range(len(listOfPlots)):
            sumTot = sumTot + listOfPlots[j][i]
        meanForPlot.append(float(sumTot)/len(listOfPlots))
    return meanForPlot

def generateMeanCumulativePlot(listOfPlots):
    meanForPlot = []
    # print(listOfPlots)
    for i in range(len(listOfPlots[0])):
        sumTot = 0
        for j in range(len(listOfPlots)):
            sumTot = sumTot + listOfPlots[j][i]
        meanForPlot.append(float(sumTot)/len(listOfPlots))
    cumulative = []
    cumulative.append(meanForPlot[0])
    for i in range(1, len(meanForPlot)):
        cumulative.append( meanForPlot[i] + cumulative[i-1])
    return cumulative
