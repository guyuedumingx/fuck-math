from PIL import Image
import os


def pad_image(image, to_width):
    """统一文件夹内图片的宽度，谨慎使用"""
    iw, ih = image.size
    #用白色填充
    nimg = Image.new('RGB', (to_width, ih), (256,256,256))
    nimg.paste(image,(0,0)) 
    return nimg

def get_max_width(images):
    """获取图片最大宽度"""
    max_width = 0
    for img in images:
        width, _ = img.size
        if max_width < width:
            max_width = width
    return max_width


path = "..\chapter1\database\images"
imgs_path = [path+os.sep+ i for i in os.listdir(path)]

images = [Image.open(i) for i in imgs_path]

max_width = get_max_width(images)

for idx,img in enumerate(images):
    nimg = pad_image(img, max_width)
    nimg.save(imgs_path[idx])