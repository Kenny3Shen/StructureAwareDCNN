from PIL import Image

img = Image.open("./log/img/3.png")
img.convert('L').save("./dataset/val/gt_gray/3.png")
img.convert('1').save("./dataset/val/image_gray/3.png")