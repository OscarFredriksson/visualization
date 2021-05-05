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

# Fill in the rest such that the important parts of the dataset is visualized

# Create suitable filter(s)

# Map the enriched data from the filter(s) to the appropriate visualization model(s)

# Create corresponding actors(s) for each mapping

# Create renderer and attach actor(s)

# Create render window and connect to renderer

# Create interactor, connect to render window, and

contour1 = vtk.vtkContourFilter()
contour1.SetInputConnection(reader.GetOutputPort())
contour1.GenerateValues(2, 0.0, 30)


mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(contour1.GetOutputPort())

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor(1.0, 1.0, 1.0)
actor1.GetProperty().SetOpacity(0.2)

contour2 = vtk.vtkContourFilter()
contour2.SetInputConnection(reader.GetOutputPort())
contour2.GenerateValues(2, 0.0, 130)

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(contour2.GetOutputPort())

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(1, 0.75, 0)
actor2.GetMapper().ScalarVisibilityOff()

renderer = vtk.vtkRenderer()
renderer.SetBackground(0.3, 0.3, 0.3)
renderer.AddActor(actor1)
renderer.AddActor(actor2)

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
