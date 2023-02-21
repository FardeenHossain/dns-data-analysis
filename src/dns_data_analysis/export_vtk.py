import vtk

# Create the 3D field data (example)
field_data = vtk.vtkImageData()
field_data.SetDimensions(10, 10, 10)
field_data.AllocateScalars(vtk.VTK_FLOAT, 1)
for i in range(10):
    for j in range(10):
        for k in range(10):
            field_data.SetScalarComponentFromFloat(i, j, k, 0, i * j * k)

# Create a VTK writer and set the output file name
writer = vtk.vtkXMLImageDataWriter()
writer.SetFileName("output.vti")

# Set the input data to the writer
writer.SetInputData(field_data)

# Write the output file
writer.Write()
