import trimesh
import pyrender
import matplotlib.pyplot as plt

def render_model(path):
    mesh=trimesh.load(path)
    scene=pyrender.Scene()
    scene.add(pyrender.Mesh.from_trimesh(mesh))
    pyrender.Viewer(scene, use_raymond_lighting=True)
