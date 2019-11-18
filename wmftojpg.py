from PIL import Image
from wand.image import Image as wima

path_in = "/home/gryfin/Pobrane/epigrafe - portable/"
path_out = "/home/gryfin/Pulpit/"
image_name = "C.25"
ext_in = ".wmf"
ext_out = ".pdf"
# Image.open(path_in + image_name + ext_in).save(path_out + image_name + ext_out)

with wima(filename=path_in + image_name + ext_in) as img:
    img.save(filename=path_out + image_name + ext_out)
