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

Scenario['CASE1_SC_2'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

selectCurrentStep(activeScenario=Scenario['CASE1_SC_2'],
                  parameterValue=['DIST=-6.5'])

selectCurrentStep(activeScenario=Scenario['CASE1_SC_2'],
                  parameterValue=['DIST=0.0'])

saveProjectAs('2D_Case2.FLU')

DeleteCurrentApplication()

lastInstance = ApplicationMagneticTransient2D(domain2D=Domain2DAxisymetric(),
                               coilCoefficient=CoilCoefficientAutomatic(),
                               transientInitialization=TransientInitializationZeroInitialSolution())

DeleteElectricCircuit(deleteStrandedConductor='NO')

importCircuit(filename='2D_Case2_log1.xcir',
              importValue=1,
              ImportFELink=1)


lastInstance = VariationParameterPilot(name='K_SPRING',
                        referenceValue=0.0)

startMacroTransaction()
MechanicalSet['MOBILE_PART'].kinematics=LinearCoupledLoad(initialVelocity='0',
                                                          initialPosition='0',
                                                          internalCharacteristics=LinearLoadCoefficients(mass='0.25',
                                                                                                         friction=LinearFrictionCoefficients(constantFriction='0',
                                                                                                                                             viscousCoefficient='0',
                                                                                                                                             squareSpeedCoefficient='0'),
                                                                                                         spring=LinearSpring(springConstant='K_SPRING',
                                                                                                                             equilibriumPosition='0')),
                                                          externalCharacteristics=LinearLoadCoefficients(mass='0',
                                                                                                         friction=LinearFrictionCoefficients(constantFriction='0',
                                                                                                                                             viscousCoefficient='0',
                                                                                                                                             squareSpeedCoefficient='0')),
                                                          minimalStop=LinearStop(position='-6.5e-3'),
                                                          maximalStop=LinearStop(position='0'))

MechanicalSet['MOBILE_PART'].translationAxis=TranslationYAxis(coordSys=CoordSys['FIXED'])

endMacroTransaction()

RegionFace['COIL'].magneticTransient2D=MagneticTransient2DFaceCoilConductor(coilConductor=CoilConductor2DPositive(turnNumber='225',
                                                                                                                  seriesParallel=AllInSeries(),
                                                                                                                  electricComponent=CoilConductor['COILCONDUCTOR_1']))


RegionFace['CORE'].magneticTransient2D=MagneticTransient2DFaceSolidConductor(material=Material['STEEL'],
                                                                             circuitType=NoCircuit())


RegionFace['MAG_CIR'].magneticTransient2D=MagneticTransient2DFaceSolidConductor(material=Material['STEEL'],
                                                                                circuitType=NoCircuit())


RegionFace['AIR'].magneticTransient2D=MagneticTransient2DFaceVacuum()


RegionFace['AIR_MOBILE'].magneticTransient2D=MagneticTransient2DFaceVacuum()


RegionFace['INFINITE'].magneticTransient2D=MagneticTransient2DFaceVacuum()


RegionLine['LINE_AG'].magneticTransient2D=MagneticTransient2DLineAirGap(thickness='3e-6')


Scenario(name='CASE2_SC : Coupled load kinematic model')

startMacroTransaction()

Scenario['CASE2_SC'].addPilot(pilot=MultiValues(parameter=VariationParameter['TIME'],
                                                intervals=[IntervalStepValue(minValue=0.0,
                                                                             maxValue=0.015,
                                                                             stepValue=0.001),
                                                           IntervalStepValue(minValue=0.015,
                                                                             maxValue=0.0155,
                                                                             stepValue=1.0E-4),
                                                           IntervalStepValue(minValue=0.0155,
                                                                             maxValue=0.017,
                                                                             stepValue=0.001),
                                                           IntervalStepValue(minValue=0.017,
                                                                             maxValue=0.0175,
                                                                             stepValue=1.0E-4),
                                                           IntervalStepValue(minValue=0.0175,
                                                                             maxValue=0.02,
                                                                             stepValue=0.001),
                                                           IntervalStepValue(minValue=0.02,
                                                                             maxValue=0.05,
                                                                             stepValue=0.005),
                                                           IntervalStepValue(minValue=0.05,
                                                                             maxValue=0.1,
                                                                             stepValue=0.01)]))

Scenario['CASE2_SC'].addPilot(pilot=MultiValues(parameter=VariationParameter['K_SPRING'],
                                                intervals=[IntervalStepNumber(minValue=0.0,
                                                                              maxValue=10000.0,
                                                                              stepNumber=2)]))

endMacroTransaction()

Scenario['CASE2_SC'].solve(projectName='2D_Case2.FLU')

meshDomain()

Scenario['CASE2_SC'].solve(projectName='2D_Case2.FLU')

CurrentStrandedCoil['COILCONDUCTOR'].delete()
Scenario['CASE2_SC'].solve(projectName='2D_Case2.FLU')

result = checkPhysic()

MechanicalSet['MOBILE_PART'].translationAxis=TranslationYAxis(coordSys=CoordSys['XY1'])


result = checkPhysic()

RegionFace['INIFINITE'].delete()
result = checkPhysic()

Scenario['CASE2_SC'].solve(projectName='2D_Case2.FLU')

EvolutiveCurve2D(name='EvolutiveCurve2D_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['K_SPRING'],
                                                                             currentValue=0.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['TIME'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=0.1)]),
                 formula=['I(COILCONDUCTOR_1)'])

EvolutiveCurve2D(name='FORCE_VERSUS_TIME',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['K_SPRING'],
                                                                             currentValue=0.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['TIME'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=0.1)]),
                 formula=['ForceElecMag(MOBILE_PART)'])

EvolutiveCurve2D(name='EvolutiveCurve2D_2',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['K_SPRING'],
                                                                             currentValue=0.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['TIME'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=0.1)]),
                 formula=['LinSpeed(MOBILE_PART)'])

lastInstance = SensorPredefinedMagneticFlux(name='FLUX',
                             support=ComputationSupportCoilConductorMagneticFlux(coilConductor=[CoilConductor['COILCONDUCTOR_1']]))

evaluateSensors()

EvolutiveCurve2D(name='FLUX_VERSUS_TIME',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['K_SPRING'],
                                                                             currentValue=0.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['TIME'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=0.1)]),
                 formula=['FLUX'])

saveProject()

