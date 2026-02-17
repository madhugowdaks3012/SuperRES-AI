import torch
import numpy as np
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet


def load_model(scale=4):
    """
    Load Real-ESRGAN model (x4)
    """

    model = RRDBNet(
        num_in_ch=3,
        num_out_ch=3,
        num_feat=64,
        num_block=23,
        num_grow_ch=32,
        scale=scale,
    )

    # Official pretrained weights
    model_url = "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth"

    upsampler = RealESRGANer(
        scale=scale,
        model_path=model_url,
        model=model,
        tile=0,
        tile_pad=10,
        pre_pad=0,
        half=False,
        device=torch.device("cpu"),  # CPU safe
    )

    return upsampler


def enhance_image(upsampler, img, scale=4):
    """
    Enhance image using Real-ESRGAN
    """

    if img is None:
        raise ValueError("Image is None")

    if not isinstance(img, np.ndarray):
        raise ValueError("Image must be numpy array")

    output, _ = upsampler.enhance(img, outscale=scale)

    return output
