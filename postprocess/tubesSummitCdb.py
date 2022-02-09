# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# destroy renderView1
Delete(renderView1)
del renderView1

# load state
LoadState('<PvSkript>', DataDirectory='<DataDirectory>',
    AMReXBoxLibGridReader3FileNames=['<AMReXBoxLibGridReader3FileNames>'])
print('skript')

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

# set active view
SetActiveView(renderView1)

# find source
aMReXBoxLibGridReader3 = FindSource('AMReXBoxLibGridReader3')

# set active source
SetActiveSource(aMReXBoxLibGridReader3)

# Properties modified on aMReXBoxLibGridReader3
aMReXBoxLibGridReader3.CellArrayStatus = []

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on aMReXBoxLibGridReader3
aMReXBoxLibGridReader3.CellArrayStatus = ['Bx', 'By', 'Bz', 'Ex', 'Ey', 'Ez', 'jx', 'jy', 'jz', 'rho']

# update the view to ensure updated data information
renderView1.Update()

# find source
resampleToImage1 = FindSource('ResampleToImage1')

# set active source
SetActiveSource(resampleToImage1)

# get display properties
resampleToImage1Display = GetDisplayProperties(resampleToImage1, view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=resampleToImage1Display)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=resampleToImage1Display.SliceFunction)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=resampleToImage1Display)

# reset view to fit data
renderView1.ResetCamera()

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'RenderView1_%.6ts%cm.png'
pNG1.Writer.ImageResolution = [500, 500]
pNG1.Writer.Format = 'PNG'

# Properties modified on pNG1.Writer
pNG1.Writer.CameraMode = 'Phi-Theta'

# Properties modified on pNG1.Trigger
pNG1.Trigger.UseStartTimeStep = 1

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on pNG1.Trigger
pNG1.Trigger.UseEndTimeStep = 1

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.00010591363255556098, -2.7970035577731125e-05, 5.460277445390548e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.44762183573101705, 0.5471248639415862, -0.7073111588499755]
renderView1.CameraParallelScale = 5.436905525073885e-05

# save extracts
SaveExtracts(ExtractsOutputDirectory='<CDB>',
    GenerateCinemaSpecification=1)

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.00010591363255556098, -2.7970035577731125e-05, 5.460277445390548e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.44762183573101705, 0.5471248639415862, -0.7073111588499755]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 0.00012778766088545343]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.00010269045465793091, 6.849929924549199e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.0, 0.5000000000000002, -0.8660254037844386]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.00010269045465793095, -5.0077424034430956e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.0, -0.49999999999999967, -0.8660254037844388]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 6.945670167485263e-20, -0.00010936578567439248]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.0, -1.0, -5.857532553913371e-16]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, -0.00010269045465793089, -5.0077424034431085e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.0, -0.5000000000000008, 0.8660254037844383]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, -0.00010269045465793101, 6.849929924549188e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.0, 0.49999999999999917, 0.8660254037844392]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.00010269045465793091, 0.0, 6.849929924549199e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [5.134522732896548e-05, 0.00010269045465793093, 3.885511842551125e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-0.7499999999999999, 0.5000000000000002, -0.43301270189221946]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-5.134522732896543e-05, 0.00010269045465793097, -2.0433243214450247e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-0.7500000000000002, -0.4999999999999997, -0.4330127018922196]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.00010269045465793095, 7.030373462210693e-20, -5.007742403443102e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-5.389951109126102e-16, -1.0, -2.5222625841645313e-16]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-5.134522732896556e-05, -0.00010269045465793091, -2.0433243214450294e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.7499999999999997, -0.5000000000000007, 0.4330127018922193]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [5.1345227328965375e-05, -0.00010269045465793104, 3.885511842551121e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.7500000000000006, 0.4999999999999991, 0.4330127018922195]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.00010269045465793094, 0.0, -5.0077424034430956e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [5.13452273289655e-05, 0.00010269045465793091, -2.043324321445024e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-0.75, 0.5000000000000002, 0.433012701892219]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-5.134522732896544e-05, 0.00010269045465793097, 3.8855118425511205e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-0.7500000000000003, -0.4999999999999997, 0.4330127018922192]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.00010269045465793098, 4.828087799349512e-20, 6.849929924549196e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-4.2919644476521296e-16, -1.0, 7.094984288033657e-17]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-5.134522732896556e-05, -0.00010269045465793093, 3.885511842551124e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.7499999999999998, -0.5000000000000004, -0.43301270189221913]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [5.134522732896541e-05, -0.00010269045465793102, -2.0433243214450233e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.7500000000000004, 0.49999999999999933, -0.4330127018922193]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [1.4521460461813908e-20, 0.0, -0.00010936578567439246]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [7.260730230906957e-21, 0.0001026904546579309, -5.007742403443101e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-1.0605752387249068e-16, 0.5000000000000003, 0.8660254037844386]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-7.260730230906948e-21, 0.00010269045465793094, 6.849929924549192e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-1.0605752387249072e-16, -0.49999999999999967, 0.8660254037844388]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-1.4521460461813908e-20, 7.284483346386983e-20, 0.00012778766088545343]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-8.737044059982583e-32, -1.0, 6.14326584922622e-16]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-7.260730230906968e-21, -0.00010269045465793087, 6.849929924549206e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [1.0605752387249063e-16, -0.5000000000000009, -0.8660254037844383]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [7.260730230906939e-21, -0.000102690454657931, -5.007742403443088e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [1.0605752387249078e-16, 0.49999999999999906, -0.8660254037844393]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.0001026904546579309, 0.0, -5.0077424034431044e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-5.134522732896548e-05, 0.00010269045465793091, -2.0433243214450294e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.7499999999999997, 0.5000000000000002, 0.43301270189221963]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [5.13452273289654e-05, 0.00010269045465793095, 3.8855118425511225e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.7500000000000001, -0.49999999999999956, 0.43301270189221985]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.00010269045465793089, 7.623296525288703e-20, 6.849929924549202e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [5.168779601716475e-16, -1.0, 3.9054094057795733e-16]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [5.134522732896552e-05, -0.00010269045465793085, 3.885511842551131e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-0.7499999999999993, -0.5000000000000009, -0.4330127018922194]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-5.134522732896533e-05, -0.00010269045465793097, -2.04332432144502e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-0.7500000000000002, 0.49999999999999895, -0.43301270189222013]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.00010269045465793091, 0.0, 6.849929924549199e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [-5.134522732896548e-05, 0.00010269045465793093, 3.885511842551125e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.7499999999999999, 0.5000000000000002, -0.43301270189221946]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [5.134522732896543e-05, 0.00010269045465793097, -2.0433243214450247e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [0.7500000000000002, -0.4999999999999997, -0.4330127018922196]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [0.00010269045465793095, 7.030373462210693e-20, -5.007742403443102e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [5.389951109126102e-16, -1.0, -2.5222625841645313e-16]
renderView1.CameraParallelScale = 5.436905525073885e-05

# layout/tab size in pixels
layout1.SetSize(850, 862)

# current camera placement for renderView1
renderView1.CameraPosition = [5.134522732896556e-05, -0.00010269045465793091, -2.0433243214450294e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-0.7499999999999997, -0.5000000000000007, 0.4330127018922193]
renderView1.CameraParallelScale = 5.436905525073885e-05

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(850, 862)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-5.1345227328965375e-05, -0.00010269045465793104, 3.885511842551121e-05]
renderView1.CameraFocalPoint = [0.0, 0.0, 9.21093760553049e-06]
renderView1.CameraViewUp = [-0.7500000000000006, 0.4999999999999991, 0.4330127018922195]
renderView1.CameraParallelScale = 5.436905525073885e-05
