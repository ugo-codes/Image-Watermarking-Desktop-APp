from tkinter import Frame, Canvas, Button, filedialog, simpledialog, messagebox
from imaging import open_image, add_text_watermark, add_logo_watermark, save_image

canvas = canvas_image = image = None


def text_watermark(text: str, font_family: str, font_size: int, font_color: tuple):
    """
    This method receives the text and how to format the text then passes it to the method for adding it as watermark
    then update the canvas to show the image
    to the image at the top left of the image
    :param text: (str) the text to be written on the image
    :param font_family: (str) The font the text should be written in
    :param font_size: (int) the size of the font
    :param font_color: (tuple) the color of the font in ((RBG), hexcode)
    :return: (PhotoImage) an image format that can be used by tkinter
    """
    global image
    image = add_text_watermark(text, font_family, font_size, font_color)
    update_canvas()


def logo_watermark():
    """
    This method adds a logo to the picture as watermark then updates the canvas to show the image
    :return: None
    """
    global image
    file_path = open_file_dialog()
    image = add_logo_watermark(file_path)
    update_canvas()


def update_canvas():
    """
    This method updates the canvas to show the image
    :return: None
    """
    canvas.itemconfig(canvas_image, image=image)


def open_file_dialog():
    """
    Tis method opens a file dialog to select an image file, returns the file path as string
    :return: (str) the file path to the image file
    """
    # opens a file dialog to open a file
    # sets the title of the file dialog to pick an Image
    filename = filedialog.askopenfilename(title="Pick An Image", filetypes=[("Image Files", ".png .jpg")])
    if filename is None:
        return
    # returns the path to the file as string
    return filename


def pick_image():
    """
    This image displays the image that was selected on the canvas
    :return: None
    """
    global image
    file_path = open_file_dialog()
    # if no file was picked, don't do anything
    if file_path is None:
        return

    image = open_image(file_path)
    # create canvas to view the
    update_canvas()


def add_watermark(function):
    """
    This method switches to the frame responsible for adding the watermark
    :param function: the function to be called for the changing of the frame visible
    :return: None
    """
    # if no image is selected do nothing
    if image is None:
        # show a dialog box
        messagebox.showinfo(title="Info", message="Pick an Image")
        return

    # the function responsible of changing the visible frame
    function("Watermark")


def save():
    """
    This method opens up a file dialog to know where to save the image file, ask for the file name then calls the method
    for saving the image then passes the directory and the filename as arguments
    :return: None
    """

    # dialog to know where to save the file
    directory = filedialog.askdirectory()
    # dialog to know the file name
    filename = simpledialog.askstring(title="hr", prompt="Hello")
    # method responsible for saving the image
    save_image(f"{directory}/{filename}.png")


class StartPage(Frame):

    def __init__(self, parent, function):
        global canvas, canvas_image
        # initializes the constructor of the super class
        Frame.__init__(self, parent)
        # configure the frame
        # sets the x and y padding, background color
        self.config(padx=10, pady=10, bg="red")

        # create a canvas where we can draw an Image
        canvas = Canvas(self, width=500, height=300)
        # # this will draw an image on top of the canvas
        canvas_image = canvas.create_image(250, 150)
        # # sets the location of the canvas on the grid
        canvas.grid(row=0, column=0, columnspan=2)

        # creates a button to add to the window
        # sets the text, width and the function to be called when the button is clicked
        select_image = Button(self, text="Open Image", width=20, command=pick_image)
        watermark_image = Button(self, text="Add Watermark", width=20, command=lambda: add_watermark(function))
        save_button = Button(self, text="Save Image", width=20, command=save)
        # sets the location of the button on the window
        select_image.grid(row=1, column=0, pady=10)
        watermark_image.grid(row=1, column=1, pady=10)
        save_button.grid(row=2, column=0)
