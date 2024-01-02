import os
from pxr import Usd, UsdGeom

# This script creates a new USD stage, adds a transform and a sphere to it,
# prints the stage contents, saves the stage to disk, and then loads the stage in usdview.

# Create a new USD stage with the filename "hello_world.usda"
stage = Usd.Stage.CreateNew("hello_world.usda")

# Define a new transform at the path "/ball_transform" on the stage
xformPrim = UsdGeom.Xform.Define(stage, "/ball_transform")

# Define a new sphere at the path "/ball_transform/ball_mesh" on the stage
spherePrim = UsdGeom.Sphere.Define(stage, "/ball_transform/ball_mesh")

# Export the stage to a string and print it, to show the stage contents
print(stage.GetRootLayer().ExportToString())

# Save the stage to disk
stage.GetRootLayer().Save()

# Use the os.system function to call the usdview command, which will load the stage from the file "hello_world.usda"
os.system("usdview hello_world.usda")
