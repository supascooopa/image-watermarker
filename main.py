from tkinter import *
import tkinter.filedialog as fd
from PIL import ImageTk, Image
from water_marker import creating_watermarked_img

window = Tk()
def browse_file_system():
    global pic_file_name
    pic_file_name = fd.askopenfilename()
    image = ImageTk.PhotoImage(Image.open(pic_file_name))
    picture_label.configure(image=image)
    picture_label.image = image
    water_mark_btn = Button(text="watermarker", command=lambda arg1=pic_file_name,
                                                               arg2="hello world!": creating_watermarked_img(arg1,
                                                                                                             arg2))
    water_mark_btn.grid(row=2)


window.rowconfigure(3, minsize=50, weight=1)
window.columnconfigure(3, minsize=50, weight=1)
right_frame = Frame(window, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)


browse_button = Button(text="Browse files", command=browse_file_system)
browse_button.grid(row=3, column=0)

# load image to be "edited"
place_holder_image = ImageTk.PhotoImage(Image.open("Unknown.jpeg"))
# Display image in right_frame
picture_label = Label(right_frame, image=place_holder_image)
picture_label.grid(row=0, column=0, padx=5, pady=5)
mainloop()


