from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
def pic4():
    window = Tk()
    window.title("Открытие изображения")
    image = Image.open("проигрыш_картинка.jpg")
    image = image.resize((500,500))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(window,image=photo)
    image_label.pack()
    continue_button = Button(window,text ="Попробывать заного", width=20)
    continue_button.pack(side="bottom",pady=30)
    window.mainloop()
    return image_label