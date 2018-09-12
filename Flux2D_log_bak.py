#! Flux2D 11.2
loadProject('D:/Flux_Learning/2D_Case1.FLU')

Scenario(name='CASE1_SC : Multi-static Kinematic model',
         refinement=InactivatedAdaptive())

startMacroTransaction()

Scenario['CASE1_SC'].addPilot(pilot=MultiValues(parameter=VariationParameter['DIST'],
                                                intervals=[IntervalStepNumber(minValue=0.0,
                                                                              maxValue=6.5,
                                                                              stepNumber=2)]))

endMacroTransaction()

Scenario['CASE1_SC'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

saveProject()

IsolineSpatialGroup['4_ISOLIN_NO_INFINITE'].displayIsoline()

IsolineSpatialGroup['4_ISOLIN_NO_INFINITE'].maskIsoline()

IsovalueSpatialGroup['4_ISOVAL_NO_INFINITE'].displayIsovalue()

IsovalueSpatialGroup['4_ISOVAL_NO_INFINITE'].maskIsovalue()

PathStraightLine2PTS(name='Path_1',
                     pathDiscretization=IntervalPathDiscretization(intervalNumber=15),
                     regionFace='AIR',
                     color=Color['White'],
                     visibility=Visibility['VISIBLE'],
                     mechanicalSet=MechanicalSet['FIXED_PART'],
                     startPoint=PathPoint(coordSys=CoordSys['FIXED'],
                                          uvw=['0', '-20.5+3.5+DIST/2']),
                     endPoint=PathPoint(coordSys=CoordSys['FIXED'],
                                        uvw=['5', '-20.5+3.5+DIST/2']))


PathStraightLine2PTS(name='PATH_2',
                     pathDiscretization=IntervalPathDiscretization(intervalNumber=35),
                     regionFace='AIR',
                     color=Color['White'],
                     visibility=Visibility['VISIBLE'],
                     mechanicalSet=MechanicalSet['FIXED_PART'],
                     startPoint=PathPoint(coordSys=CoordSys['FIXED'],
                                          uvw=['5', '-20.5+3.5+DIST/2']),
                     endPoint=PathPoint(coordSys=CoordSys['FIXED'],
                                        uvw=['14.5', '-11+3.5+DIST/2']),
                     previousPath=Path['PATH_1'])


Path[2].setInvisible()

Path[3].setInvisible()

Path['PATH_1'].visibility=Visibility['VISIBLE']


cleanInvalidPaths()

cleanInvalidPaths()

PathStraightLine2PTS(name='Path_1',
                     pathDiscretization=IntervalPathDiscretization(intervalNumber=15),
                     regionFace='AIR',
                     color=Color['White'],
                     visibility=Visibility['VISIBLE'],
                     startPoint=PathPoint(coordSys=CoordSys['FIXED'],
                                          uvw=['0', '-20.5+3.5+DIST/2']),
                     endPoint=PathPoint(coordSys=CoordSys['FIXED'],
                                        uvw=['5', '-20.5+3.5+DIST/2']))


PathStraightLine2PTS(name='PATH_2',
                     pathDiscretization=IntervalPathDiscretization(intervalNumber=35),
                     regionFace='AIR',
                     color=Color['White'],
                     visibility=Visibility['VISIBLE'],
                     startPoint=PathPoint(coordSys=CoordSys['FIXED'],
                                          uvw=['5', '-20.5+3.5+DIST/2']),
                     endPoint=PathPoint(coordSys=CoordSys['FIXED'],
                                        uvw=['14.5', '-11+3.5+DIST/2']),
                     previousPath=Path['PATH_1'])


lastInstance = CompoundPath(name='AIRGAP',
             paths=[Path['PATH_1'],
                    Path['PATH_2']],
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

cleanInvalidPaths()

selectCurrentStep(activeScenario=Scenario['CASE1_SC'],
                  parameterValue=['DIST=0.0'])

lastInstance = PropArrowPath(name='ARR_PATH',
              compoundPath=[CompoundPath['AIRGAP']],
              formula='B')

saveProject()

ArrowSpatialGroup['4_ARROWS_NO_INFINITE'].maskArrow()

Scenario(name='CASE1_SC_1',
         refinement=InactivatedAdaptive())

startMacroTransaction()

Scenario['CASE1_SC_1'].addPilot(pilot=MultiValues(parameter=VariationParameter['DIST'],
                                                  intervals=[IntervalStepNumber(minValue=0.0,
                                                                                maxValue=-6.5,
                                                                                stepNumber=2)]))

endMacroTransaction()

Scenario['CASE1_SC_1'].solve(projectName='D:/Flux_Learning/2D_Case1.FLU')

selectCurrentStep(activeScenario=Scenario['CASE1_SC_1'],
                  parameterValue=['DIST=0.0'])

EvolutiveCurve2D(name='FORCE_VS_DIST',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['DIST'],
                                                                                 limitMin=-6.5,
                                                                                 limitMax=0.0)]),
                 formula=['ForceElecMag(MOBILE_PART)'])

saveProject()

exit()
