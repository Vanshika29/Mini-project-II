from tkinter import Button,Canvas
from PIL import ImageTk,Image
from vir_mouse import main_virtual_mouse
import gesture
import tkinter

main_window = tkinter.Tk()
main_window.geometry("670x400")

my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\hp\\Downloads\\miniprojeect_gesture_recognition-master\\background1.png"))


my_label = tkinter.Label(image=my_img)
my_label.pack()


main_window.iconbitmap("C:\\Users\\hp\\Downloads\\miniprojeect_gesture_recognition-master\\icon.ico")
main_window.title("Gesture Recognition")


def virtual_mouse(event):
    def open(event):
        main_virtual_mouse()
    
    vir_mouse_window = tkinter.Tk()
    vir_mouse_window.geometry("500x200")
    vir_mouse_window.title("Virtual Mouse")
    tkinter.Label(vir_mouse_window,text="virtual mouse ---> Press Q to exit or --> Click on the Close Button").pack()

   

    b11 = tkinter.Button(vir_mouse_window,text="Click To Use",bg='blue',fg='white')
    b11.bind("<Button-1>",open)
    b11.config( height = 3, width = 50 )
    b11.pack(pady=10)
    
    
    bclose = tkinter.Button(vir_mouse_window,text="Close",command=vir_mouse_window.destroy,bg='red',fg='white')
    bclose.config(height=3,width=25)
    bclose.pack()


def gesture_recog_a(event):
    def open(event):
        gesture.gesture_recog()
    
  

    gesture_window = tkinter.Tk()
    gesture_window.geometry("500x200")
    gesture_window.title("Gesture Recognition")
    tkinter.Label(gesture_window,text="Gesture recognition ---> Press Q to exit or ---> Click on the Close Button").pack()
    b22 = tkinter.Button(gesture_window,text="Click To Use",bg='green',fg='white')
    b22.bind("<Button-1>",open)
    b22.config( height = 3, width = 50 )
    
    b22.pack(pady=10)

    bclose = tkinter.Button(gesture_window,text="Close",command=gesture_window.destroy,bg='red',fg='white')
    bclose.config(height=3,width=25)
    bclose.pack()
    





b1 = tkinter.Button(main_window,text="Virtual Mouse",bg='blue',fg='white')
b1.bind("<Button-1>",virtual_mouse)
b1.config( height = 2, width = 25 )
b1.pack(pady=10)
b1.place(relx = .9, rely = .1, anchor = 'ne')

b2 = tkinter.Button(main_window,text="Gesture Recognition",bg='green',fg='white')
b2.bind("<Button-1>",gesture_recog_a)
b2.config( height = 2, width = 25 )
b2.pack(pady=10)
b2.place(relx = .9, rely = .3, anchor = 'ne')


bclose_main = tkinter.Button(main_window,text="Close",command=main_window.quit,bg='red',fg='white')
bclose_main.config(height=1,width=15)
bclose_main.pack()
bclose_main.place(relx = .85, rely = .5, anchor = 'ne')

main_window.minsize(400,200)
main_window.mainloop()
