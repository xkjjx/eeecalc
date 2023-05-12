import src.eeeCalc.filter as f
import src.eeeCalc.phasors as p
import src.eeeCalc.transferFunctionPlot as tplt



testfilter = f.LPF(-1,-20,8400,8500)
testfilter.implementChebyshevTypeI()
testfilter.getPoles()
print(testfilter)
t = testfilter.getTransferFunction()

tplt.transferFunctionPlot(t,lowerLog=3,upperLog=4,Hz=True)

