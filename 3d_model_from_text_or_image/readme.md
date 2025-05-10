# Photo/Text to 3D Model Generator

This project converts a photo or text prompt into a 3D model (.obj) and provides a live visualization using `pyrender`. It's powered by OpenAI's Shape-E and basic 3D extrusion logic for images.

---

## Steps to Run

1. **Clone the repo and install dependencies**:

    ```bash
    git clone https://github.com/openai/shap-e.git
    cd 3d_model_from_text_or_image
    pip install -r requirements.txt
    ```

2. **Run the program**:

    ```bash
    python main.py
    ```

3. **Choose a mode**:

    - For images, provide a path like: `input/sample.png`
    - For text, type a prompt like: `a toy car`, `a spaceship`, etc.

4. **Outputs**:

    - A 3D `.obj` file in the `output/` directory.
    - A live 3D visualization rendered via a simple GUI.

---

## Libraries Used

- `torch` — Deep learning backend for Shape-E
- `shap-e` — OpenAI's library for 3D generation from text
- `rembg` — For background removal from images
- `Pillow`, `numpy`, `scikit-image` — For image processing and contour extraction
- `trimesh`, `pyrender`, `matplotlib` — 3D mesh handling and rendering
- `ipywidgets` — Required by Shape-E's utilities

---

## Thought Process

- **Text → 3D**: Used OpenAI's Shape-E diffusion model to sample latents and generate a 3D `.obj` file from prompts.
- **Image → 3D**: Removed background, extracted contours from the binary mask, and extruded the 2D shape to create a mesh.
- **Visualization**: Used `pyrender` to show the generated 3D object in an interactive viewer.
- **Optimization**: Parameters like `karras_steps`, `guidance_scale`, and `s_churn` were tuned to balance speed and visual quality under 1.5 hours of runtime.
