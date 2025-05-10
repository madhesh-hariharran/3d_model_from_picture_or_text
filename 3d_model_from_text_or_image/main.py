from utils.image_to_3d import process_image_to_3d
from utils.text_to_3d import process_text_to_3d
from utils.visualize import render_model

mode=input("Choose mode (photo/text):").strip().lower()

if mode=="photo":
    img_path=input("image path:")
    process_image_to_3d(img_path)
    render_model('output/image_model.obj')

elif mode=="text":
    prompt=input("text prompt:")
    process_text_to_3d(prompt)
    render_model('output/text_model.obj')
    
else:
    print("Invalid input.give 'photo' or 'text'")
