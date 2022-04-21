from PIL import Image


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

def pin_images(img1, img2):
    """拼接两个图片"""
    img1w, img1h = img1.size
    img2w, img2h = img2.size
    imgh = img1h + img2h
    imgw = max(img1w, img2w)
    nimg = Image.new('RGB', (imgw, imgh), (256,256,256))
    nimg.paste(img1,(0,0))
    nimg.paste(img2,(0,img1h))
    nimg.show()


# path = "..\chapter1\database\images"
# imgs_path = [path+os.sep+ i for i in os.listdir(path)]

# images = [Image.open(i) for i in imgs_path]

# max_width = get_max_width(images)

# for idx,img in enumerate(images):
#     nimg = pad_image(img, max_width)
#     nimg.save(imgs_path[idx])

# path1 = "E:\数学\多么痛的领悟\chapter1\database\images\Snipaste_2022-04-21_14-46-19.png"
# path2 = "E:\数学\多么痛的领悟\chapter1\database\images\Snipaste_2022-04-21_14-47-29.png"
# pad_image(Image.open(path), 800).save(path)
# pin_images(Image.open(path1), Image.open(path2))