import os
import maya.cmds as cmds

def create_blendshape(base, target):
    cmds.select(target, base, r=True)
    blendshape = cmds.blendShape(n="{}_to_{}".format(base, target))[0]
    print("Created blendShape: {}_to_{}".format(base, target))
    return blendshape

def duplicate_and_blend(source, target):
    cmds.select(source, r=True)
    duplicate = cmds.duplicate(n="{}_DUPLICATE".format(source))[0]
    cmds.select(cl=True)
    create_blendshape(duplicate, target)

def convert_inbetweens_to_blendshapes():
    selection = cmds.ls(sl=True)
    if len(selection) < 2:
        cmds.error("Please select at least two objects: the start shape and one or more in-between shapes.")
        return
    
    start_shape = selection[0]
    blendshapes = selection[1:]
    
    print("Start Shape: {}".format(start_shape))
    print("Blendshapes: {}".format(blendshapes))
    
    # Create blendshape from start_shape to the first in-between shape
    create_blendshape(start_shape, blendshapes[0])
    
    # Iterate over the blendshapes and create duplicates and blendshapes as needed
    for i in range(len(blendshapes) - 1):
        duplicate_and_blend(blendshapes[i], blendshapes[i + 1])
    
    print("Blendshapes and duplicates created successfully.")

# Execute the function to ensure it runs
convert_inbetweens_to_blendshapes()
