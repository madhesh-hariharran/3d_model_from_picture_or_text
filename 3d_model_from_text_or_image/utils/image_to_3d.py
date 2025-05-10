from rembg import remove
from PIL import Image
import numpy as np
import trimesh
from skimage import measure

def process_image_to_3d(img_path):
    #convert image to RGBA
    input_img=Image.open(img_path).convert("RGBA")

    #remove background
    output_img=remove(input_img)
    output_img.save("output/removed_bg.png")

    #grayscale and binary mask
    gray=output_img.convert("L")
    mask_np=np.array(gray)
    mask_binary=mask_np > 0 

    contours=measure.find_contours(mask_binary.astype(np.uint8), 0.8)

    if not contours:
        raise ValueError("no contours found in the mask")

    #contours to 2D paths
    entities=[]
    vertices=[]

    for contour in contours:
        contour=np.flip(contour, axis=1) 
        start_idx=len(vertices)
        vertices.extend(contour)
        for i in range(len(contour) - 1):
            entities.append(trimesh.path.entities.Line([start_idx + i, start_idx + i + 1]))

    #create a Path2D from entities and vertices
    path=trimesh.path.Path2D(entities=entities, vertices=vertices)

    #extrude the 2D path to 3D mesh
    meshes=path.extrude(height=5.0)

    if isinstance(meshes, list):
        combined_mesh=trimesh.util.concatenate(meshes)
    else:
        combined_mesh=meshes

    combined_mesh.export('output/image_model.obj')
    print("3D model saved to output/image_model.obj")
