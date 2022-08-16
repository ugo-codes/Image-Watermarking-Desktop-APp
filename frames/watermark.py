from tkinter import Frame, Button
from frames.start_page import logo_watermark


class Watermark(Frame):

    def __init__(self, parent, function):
        # initializes the super constructor
        Frame.__init__(self, parent)
        self.config(bg="blue")

        self.function = function

        # creates a button to add to the window
        # sets the text, width and the function to be called when the button is clicked
        text_watermark_button = Button(self, text="Text Watermark", width=20,
                                       command=lambda: self.function("TextWatermark"))
        logo_watermark_button = Button(self, text="Logo Watermark", width=20, command=self.watermark)
        back = Button(self, text="Back", command=lambda: function("StartPage"))
        # sets the location of the button on the window
        text_watermark_button.place(x=10, y=200)
        logo_watermark_button.place(x=360, y=200)
        back.place(x=0, y=0)

    def watermark(self):
        """
        This method calls the function responsible for adding the watermark image and goes back to the start page
        :return: None
        """
        logo_watermark()
        self.function("StartPage")
