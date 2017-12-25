# coding:utf-8

import face_recognition
from PIL import Image

img_path = "human.jpg"
hat_img_path = "hat.png"

image = face_recognition.load_image_file(img_path)
face_locations = face_recognition.face_locations(image)

print "%d face found" % len(face_locations)

human_img = Image.open(img_path)
# TODO: what is this part do
human_img = human_img.convert("RGBA")

hat_img = Image.open(hat_img_path)
hat_img = hat_img.convert("RGBA")

for face_location in face_locations:
    top, right, bottom, left = face_location
    top -= 10

    # length and height of human head
    head_h = bottom - top
    head_l = right -left

    hat_img = hat_img.resize( (head_l, head_h) )
    hat_region = hat_img

    human_region = (left, top - head_h, right, top)

    human_img.paste(hat_region, human_region, mask = hat_img)

human_img.show()
human_img.save("test.png")
