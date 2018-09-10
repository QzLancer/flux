#! Flux2D 11.2
newProject()

SketcherOption[1].magnetizationGrid=MagnetizationGrid(gridActivation='OUI',lengthGridCell=10.0,cellSubdivision=10,subdivisionPoint=10)

openSketcher2dContext()

closeSketcher2dContext()

buildFaces()

lastInstance = SymmetryYaxis(physicalType=SymmetryNotDefined(),
              position='0')

lastInstance = CoordSysCartesian(name='CoordSys_1',
                  parentCoordSys=Local(coordSys=CoordSys['XY1']),
                  origin=['0',
                          '0'],
                  rotationAngles=RotationAngles(angleZ='0'),
                  visibility=Visibility['VISIBLE'])

CoordSysCartesian['COORDSYS_1'].delete()
lastInstance = ParameterGeom(name='THICK : Thickness of the upper magnetic circuit',
              expression='8')

lastInstance = ParameterGeom(name='DIST : Distance between the mobile and the fixed coordinate system',
              expression='0')

lastInstance = CoordSysCartesian(name='FIXED',
                  parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
                                             angleUnit=AngleUnit['DEGREE']),
                  origin=['0',
                          '0'],
                  rotationAngles=RotationAngles(angleZ='0'),
                  visibility=Visibility['VISIBLE'])

lastInstance = CoordSysCartesian(name='MOBILE',
                  parentCoordSys=Local(coordSys=CoordSys['FIXED']),
                  origin=['0',
                          'DIST'],
                  rotationAngles=RotationAngles(angleZ='0'),
                  visibility=Visibility['VISIBLE'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['5',
                      '-20.5'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['3',
                      '-20.5'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['3',
                      '-31'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['32',
                      '-31'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['32',
                      '-24'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['32',
                      '23+THICK'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['15',
                      '23+THICK'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['15',
                      '23'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['32-THICK/2',
                      '23'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['32-THICK/2',
                      '-24'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['14.5',
                      '-24'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['14.5',
                      '-11'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['32',
                      '23'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

Point[3].color=Color['Black']


Point[3].color=Color['White']


lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[1],
                      Point[2]],
            nature=Nature['STANDARD'])

LineSegment[1].delete()
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[1],
                      Point[2]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[2],
                      Point[3]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[3],
                      Point[4]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[4],
                      Point[5]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[5],
                      Point[6]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[6],
                      Point[7]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[7],
                      Point[8]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[9],
                      Point[8]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[13],
                      Point[9]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[9],
                      Point[10]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[5],
                      Point[10]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[10],
                      Point[11]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[11],
                      Point[12]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[12],
                      Point[1]],
            nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['25',
                      '-23'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['17',
                      '-23'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['17',
                      '22'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['FIXED'],
                 uvw=['25',
                      '22'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

LineSegment[5,6,7,8,9,10,11,12,13,14].delete()
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[5],
                      Point[13]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[13],
                      Point[6]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[6],
                      Point[7]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[7],
                      Point[8]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[9],
                      Point[8]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[13],
                      Point[9]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[9],
                      Point[10]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[5],
                      Point[10]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[10],
                      Point[11]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[11],
                      Point[12]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[12],
                      Point[1]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[15],
                      Point[14]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[14],
                      Point[17]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[17],
                      Point[16]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[16],
                      Point[15]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

saveProjectAs('D:/Onedrive/Flux_Learning/2D_Case1.FLU')

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MOBILE'],
                 uvw=['5',
                      '-13.5'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MOBILE'],
                 uvw=['3',
                      '-13.5'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MOBILE'],
                 uvw=['3',
                      '26'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MOBILE'],
                 uvw=['8',
                      '31.5'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MOBILE'],
                 uvw=['8',
                      '46.5'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MOBILE'],
                 uvw=['14.5',
                      '46.5'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MOBILE'],
                 uvw=['14.5',
                      '-4'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MOBILE'],
                 uvw=['0',
                      '-13.5'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['MOBILE'],
                 uvw=['0',
                      '46.5'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[18],
                      Point[19]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[19],
                      Point[20]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[20],
                      Point[21]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[21],
                      Point[22]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[22],
                      Point[23]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[23],
                      Point[24]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[24],
                      Point[18]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[19],
                      Point[25]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[25],
                      Point[26]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[26],
                      Point[22]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

saveProject()

lastInstance = InfiniteBoxDisc(DISCOID=['75',
                         '110'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[29],
                      Point[26]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[25],
                      Point[27]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

saveProject()

buildFaces()

buildFaces()

FaceAutomatic[ALL].delete()
buildFaces()

FaceAutomatic[8].setVisible()

FaceAutomatic[8].setVisible()

meshDomain()

AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.5)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow())))


AidedMesh[1].synchronize()

lastInstance = MeshPoint(name='MP_IB',
          lengthUnit=LengthUnit['MILLIMETER'],
          value='12.25',
          color=Color['Cyan'])

lastInstance = MeshPoint(name='MP_AG',
          lengthUnit=LengthUnit['MILLIMETER'],
          value='1',
          color=Color['Red'])

PointCoordinates[19].assignMeshPoint(meshPoint=MeshPoint['MP_AG'])

PointCoordinates[18].assignMeshPoint(meshPoint=MeshPoint['MP_AG'])

PointCoordinates[24].assignMeshPoint(meshPoint=MeshPoint['MP_AG'])

PointCoordinates[12].assignMeshPoint(meshPoint=MeshPoint['MP_AG'])

PointCoordinates[1].assignMeshPoint(meshPoint=MeshPoint['MP_AG'])

PointCoordinates[2].assignMeshPoint(meshPoint=MeshPoint['MP_AG'])

PointInfiniteBox[27].assignMeshPoint(meshPoint=MeshPoint['MP_IB'])

PointInfiniteBox[30].assignMeshPoint(meshPoint=MeshPoint['MP_IB'])

PointInfiniteBox[31].assignMeshPoint(meshPoint=MeshPoint['MP_IB'])

PointInfiniteBox[28].assignMeshPoint(meshPoint=MeshPoint['MP_IB'])

PointInfiniteBox[29].assignMeshPoint(meshPoint=MeshPoint['MP_IB'])

PointInfiniteBox[32].assignMeshPoint(meshPoint=MeshPoint['MP_IB'])

lastInstance = RelaxLineNull(name='RELAXLINE_NULL : Null relaxation on lines',
              color=Color['Turquoise'])

RelaxLineLow['AIDED_RELAXLINE'].delete()
LineSegment[1].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[2].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[3].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[4].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[5].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[6].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[7].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[8].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[9].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[11].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[13].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[14].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[15].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[20].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[26].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[25].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[24].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[23].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[22].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

LineSegment[21].assignRelaxLine(relaxLine=RelaxLine['RELAXLINE_NULL'])

meshDomain()

lastInstance = ApplicationMagneticDC2D(domain2D=Domain2DAxisymetric(),
                        coilCoefficient=CoilCoefficientAutomatic())

Symmetry['SymmetryYaxis_1'].physicalType=SymmetryTangentMagFields()


lastInstance = MechanicalSetFixed(name='FIXED_PART')

lastInstance = MechanicalSetCompressibleRemeshing(name='COMPRESSIBLE_PART')

lastInstance = MechanicalSetTranslation1Axis(name='MOBILE_PART',
                              kinematics=LinearMultiStatic(),
                              translationAxis=TranslationYAxis(coordSys=CoordSys['XY1']))

lastInstance = Material(name='STEEL',
         propertyBH=PropertyBhNonlinearJmu(initialMur='500',
                                           js='1.9'),
         propertyJE=PropertyJeLinear(rho='2e-7'))

lastInstance = CurrentStrandedCoil(name='CoilConductor : Current source of coil',
                    rmsModulus='1800')

lastInstance = RegionFace(name='AIR',
           magneticDC2D=MagneticDC2DFaceVacuum(),
           color=Color['Turquoise'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['COMPRESSIBLE_PART'])

lastInstance = RegionFace(name='AIR_MOBILE',
           magneticDC2D=MagneticDC2DFaceVacuum(),
           color=Color['Turquoise'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['MOBILE_PART'])

lastInstance = RegionFace(name='CORE',
           magneticDC2D=MagneticDC2DFaceMagnetic(material=Material['STEEL']),
           color=Color['Cyan'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['MOBILE_PART'])

lastInstance = RegionFace(name='MAG_CIR',
           magneticDC2D=MagneticDC2DFaceMagnetic(material=Material['STEEL']),
           color=Color['Cyan'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['FIXED_PART'])

lastInstance = RegionFace(name='INIFINITE',
           magneticDC2D=MagneticDC2DFaceVacuum(),
           color=Color['Turquoise'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['FIXED_PART'])

lastInstance = RegionFace(name='COIL',
           magneticDC2D=MagneticDC2DFaceCoilConductor(coilConductor=CoilConductor2DPositive(turnNumber='1',
                                                                                            seriesParallel=AllInSeries(),
                                                                                            electricComponent=CoilConductor['COILCONDUCTOR'])),
           color=Color['Red'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['FIXED_PART'])

lastInstance = RegionLine(name='LINE_AG',
           magneticDC2D=MagneticDC2DLineAirGap(thickness='3e-6'),
           color=Color['Cyan'],
           visibility=Visibility['VISIBLE'],
           mechanicalSet=MechanicalSet['FIXED_PART'])

LineSegment[10,12].assignRegion(region=RegionLine['LINE_AG'])

assignRegionToFaces(face=[Face[7]],
                    region=RegionFace['AIR_MOBILE'])

assignRegionToFaces(face=[Face[6]],
                    region=RegionFace['COIL'])

assignRegionToFaces(face=[Face[5]],
                    region=RegionFace['COIL'])

assignRegionToFaces(face=[Face[4],
                          Face[3],
                          Face[2]],
                    region=RegionFace['MAG_CIR'])

assignRegionToFaces(face=[Face[1]],
                    region=RegionFace['AIR'])

Face[6].region=RegionFace['CORE']


RegionFace['INFINITE'].delete()
result = checkPhysic()

startMacroTransaction()
RegionFace['INFINITE'].magneticDC2D=MagneticDC2DFaceVacuum()

RegionFace['INFINITE'].mechanicalSet=MechanicalSet['FIXED_PART']

endMacroTransaction()

result = checkPhysic()

saveProject()

