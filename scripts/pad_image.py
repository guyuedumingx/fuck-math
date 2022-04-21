from PIL import Image
import os

def pad_image(image, to_width):
    iw, ih = image.size
    nimg = Image.new('RGB', (to_width, ih), (256,256,256))
    nimg.paste(image,(0,0)) 
    return nimg

path = "E:\数学\多么痛的领悟\chapter1\database\images"
imgs_path = [path+os.sep+ i for i in os.listdir(path)]

images = [Image.open(i) for i in imgs_path]

def get_max_width(images):
    max_width, _ = images[0].size;
    for img in images:
        width, _ = img.size;
        if max_width < width:
            max_width = width
    return max_width

max_width = get_max_width(images)

for idx,img in enumerate(images):
    nimg = pad_image(img, max_width)
    nimg.save(imgs_path[idx])