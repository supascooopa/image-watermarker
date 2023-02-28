from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def creating_watermarked_img(file: str, phrase: str = "hello world"):
    """Creates a image file with given file as base and a phrase to water-mark it on
    file: path to an image file
    phrase: a phrase to water-mark an image with"""
    org_image = Image.open(file)
    watermark_txt = phrase

    # copying original image
    copy_image = org_image.copy().convert("RGBA")

    # transparent text creator
    # make a blank image for the text, initialized to transparent text color
    txt_image = Image.new('RGBA', copy_image.size, (255, 255, 255, 0))
    # get a drawing context
    drawn_text = ImageDraw.Draw(txt_image)
    # picking a font
    font = ImageFont.load_default()
    # drawn text
    drawn_text.text((0, 0), watermark_txt, fill=(0, 0, 0, 15), font=font)

    combined = Image.alpha_composite(copy_image, txt_image)
    combined.save("new123.png")



