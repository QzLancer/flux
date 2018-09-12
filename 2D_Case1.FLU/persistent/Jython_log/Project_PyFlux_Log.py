#! Tue Sep 11 13:53:45 CST 2018 loadProject('D:/Flux_Learning/2D_Case1.FLU')

Scenario['CASE1_SC_1'].deleteAllResults()

selectCurrentStep(activeScenario=Scenario['CASE1_SC'],
                  parameterValue=['DIST=0.0'])

Scenario['CASE1_SC_1'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

selectCurrentStep(activeScenario=Scenario['CASE1_SC'],
                  parameterValue=['DIST=0.0'])

Scenario['CASE1_SC'].deleteAllResults()

Scenario['CASE1_SC_1'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

Scenario['CASE1_SC_1'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

Scenario['CASE1_SC'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

Scenario['CASE1_SC_1'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

startMacroTransaction()
Scenario['CASE1_SC_1'].adaptive=EverAdaptive()
endMacroTransaction()

Scenario['CASE1_SC_1'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

Scenario(name='CASE1_SC_2',
         refinement=InactivatedAdaptive())

startMacroTransaction()

Scenario['CASE1_SC_2'].addPilot(pilot=MultiValues(parameter=VariationParameter['DIST'],
                                                  intervals=[IntervalStepNumber(minValue=0.0,
                                                                                maxValue=-6.5,
                                                                                stepNumber=2)]))

endMacroTransaction()

Scenario['CASE1_SC_2'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

Scenario['CASE1_SC'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

deleteMesh()

meshDomain()

checkMesh()

result = checkPhysic()

