from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
def pic3():
    window = Tk()
    window.title("Открытие изображения")
    image = Image.open("3_история.jpg")
    image = image.resize((500,500))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(window,image=photo)
    image_label.pack()
    continue_button = Button(window,text ="Продолжить", width=20)
    continue_button.pack(side="bottom",pady=30)
    window.mainloop()
    return image_label