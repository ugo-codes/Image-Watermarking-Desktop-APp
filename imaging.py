from PIL import ImageTk, Image, ImageDraw, ImageFont
from matplotlib import font_manager

image = None


def add_text_watermark(text: str, font_family: str, font_size: int, font_color: tuple):
    """
    This method receives the text and how to format the text then adds the text
    to the image at the top left of the image
    :param text: (str) the text to be written on the image
    :param font_family: (str) The font the text should be written in
    :param font_size: (int) the size of the font
    :param font_color: (tuple) the color of the font in ((RBG), hexcode)
    :return: (PhotoImage) an image format that can be used by tkinter
    """
    global image
    # if the image variable is empty don't do anything
    if image is None:
        return
    # create a variable and set it to the image
    watermark_image = image
    # creates a board on the image where we can draw on
    draw = ImageDraw.Draw(watermark_image)
    # create a font from a string
    font = font_manager.FontProperties(family=font_family)
    # crete a file from the font string
    file = font_manager.findfont(font)
    # create a font that can be written on the board from the font file
    font = ImageFont.truetype(file, font_size * 2)

    # draw the text on the board
    # specify the position, the text to be drawn, the text color, the font
    draw.text((0, 0), text, fill=font_color[0], font=font)

    # replaces the global image with the watermarked image
    image = watermark_image

    # returns the watermarked image
    return ImageTk.PhotoImage(image)


def get_image(image_path: str):
    """
    This method takes a string to the location of an image, and  opens the image in PIL.Image format
    :param image_path: (str) the path to the location of an image on the computer
    :return: PIL.Image
    """
    # select the image from a folder
    x = image_path

    # if no image was selected, don't go further
    if len(x) == 0:
        return

    # opens the image and returns it
    return Image.open(x)


def add_logo_watermark(image_path: str):
    global image

    if image is None:
        return

    # get the image to be watermarked
    watermark = get_image(image_path)
    watermark.thumbnail((500, 100))

    copied_image = image

    copied_image.paste(watermark, (300, 200))

    image = copied_image

    return ImageTk.PhotoImage(image)


def open_image(image_path: str):
    """
    This method takes a string to the location of an image, then converts the image
    to a format readable by tkinter for display
    :param image_path: (str) the path to the location of an image on the computer
    :return: (ImageTk.PhotoImage) an image redable by tkinter for display on the canvas
    """
    global image

    image = get_image(image_path)

    if image is None:
        return
    # resize the image and ensures the image is still of high quality if the image is bigger than
    # the canvas
    if image.size[0] > 500 or image.size[1] > 300:
        image = image.resize((500, 300), Image.ANTIALIAS)

    # The PhotoImage enables the image to be added to a widget to be seen on the window eg a canvas
    return ImageTk.PhotoImage(image)


def save_image(file_name: str):
    """
    This method receives the path to the directly and save the image to the directly
    :param file_name: (str) the path to a directly
    :return: None
    """
    if image is None:
        return
    image.save(file_name)
