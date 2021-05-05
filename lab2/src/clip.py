import vtk

# Read raw dataset
reader = vtk.vtkImageReader()
reader.SetFileName("../dataset/BostonTeapot.raw")
reader.SetDataByteOrderToBigEndian()
reader.SetNumberOfScalarComponents(1)
reader.SetFileDimensionality(3)
reader.SetDataExtent(0, 255, 0, 255, 0, 177)
reader.SetDataScalarTypeToUnsignedChar()
reader.Update()

contour = vtk.vtkContourFilter()
contour.SetInputConnection(reader.GetOutputPort())
contour.GenerateValues(2, 30, 255)


plane = vtk.vtkPlane()
plane.SetOrigin(160, 150, 140)
plane.SetNormal(0.0, -0.35, -0.9)

clipper = vtk.vtkClipPolyData()
clipper.SetInputConnection(contour.GetOutputPort())
clipper.SetClipFunction(plane)
clipper.SetValue(0)
clipper.Update()

mapper = vtk.vtkDataSetMapper()
mapper.SetInputConnection(clipper.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1.0, 1.0, 1.0)

renderer = vtk.vtkRenderer()
renderer.SetBackground(0.3, 0.3, 0.3)
renderer.AddActor(actor)

render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("teapot")
render_window.SetSize(800, 800)
render_window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)
interactor.Initialize()
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
render_window.Render()
interactor.Start()
