# -(0)
from PIL import Image
# -(/0)

# -(1)
img = Image.open("flowers.jpg")
# -(/1)

# -(2)
img2 = img.crop((0, 0, 100, 100))
# -(/2)
img2.save("img2.jpg")

# -(3)
width = img.size[0]
height = img.size[1]
img3 = img.crop(
    (
        width - 100,
        height - 100,
        width,
        height
    )
)
# -(/3)
img3.save("img3.jpg")

# -(4)
half_the_width = img.size[0] / 2
half_the_height = img.size[1] / 2
img4 = img.crop(
    (
        half_the_width - 50,
        half_the_height - 75,
        half_the_width + 50,
        half_the_height + 75
    )
)
# -(/4)
img4.save("img4.jpg")

# -(5)
longer_side = max(img.size)
horizontal_padding = (longer_side - img.size[0]) / 2
vertical_padding = (longer_side - img.size[1]) / 2
img5 = img.crop(
    (
        -horizontal_padding,
        -vertical_padding,
        img.size[0] + horizontal_padding,
        img.size[1] + vertical_padding
    )
)
# -(/5)
img5.save("img5.jpg")
