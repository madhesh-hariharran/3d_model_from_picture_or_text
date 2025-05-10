import torch
import os
from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
from shap_e.models.download import load_model, load_config
from shap_e.util.notebooks import decode_latent_mesh

def process_text_to_3d(prompt):
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    #load models
    xm=load_model('transmitter', device=device)
    model=load_model('text300M', device=device)
    diffusion=diffusion_from_config(load_config('diffusion'))

    batch_size=1
    guidance_scale=15

    latents=sample_latents(
        batch_size=batch_size,
        model=model,
        diffusion=diffusion,
        guidance_scale=guidance_scale,
        model_kwargs=dict(texts=[prompt]*batch_size),
        progress=True,
        clip_denoised=True,
        use_fp16=True,
        use_karras=True,
        karras_steps=20,
        sigma_min=1e-3,
        sigma_max=160,
        s_churn=1,
    )

    os.makedirs("output", exist_ok=True)
    output_path="output/text_model.obj"

    t=decode_latent_mesh(xm, latents[0]).tri_mesh()

    with open(output_path, 'w') as f:
        t.write_obj(f)

    print(f"[INFO] 3D model saved to: {output_path}")
