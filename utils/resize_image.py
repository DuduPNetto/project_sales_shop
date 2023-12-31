import os

from django.conf import settings
from PIL import Image


def resize_image(img, new_width=800):
    img_path = os.path.join(settings.MEDIA_ROOT, img.name)
    img_pil = Image.open(img_path)

    original_width, original_height = img_pil.size

    if original_width <= new_width:
        img_pil.close()
        return

    new_heigth = round((new_width * original_height) / original_width)
    new_img = img_pil.resize((new_width, new_heigth), Image.LANCZOS)
    new_img.save(img_path, optimize=True, quality=85)
