import customtkinter
import tkinter as tk
import subprocess

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app_width = 350
app_height = 280

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x_position = (screen_width - app_width) // 2
y_position = (screen_height - app_height) // 2

app.geometry(f"{app_width}x{app_height}+{x_position}+{y_position}")
app.resizable(False, False)
app.title("Brightness ControlPro")

main_title = customtkinter.CTkLabel(
    app, text="Adjust Brightness for Application", font=("Arial", 18), anchor="w"
)
main_title.pack(pady=20, padx=10, anchor="w")

title_1 = customtkinter.CTkLabel(app, text="WhatsApp", font=("Arial", 15))
title_1.place(x=10, y=80)


def whatsApp_BtnClick():
    current_text = whatsApp_apply.cget("text")
    if current_text == "Apply":
        print("Apply WhatsApp")
        whatsApp_apply.configure(text="Dispose")

    elif current_text == "Dispose":
        print("Dispose WhatsApp")
        whatsApp_apply.configure(text="Apply")


whatsApp_apply = customtkinter.CTkButton(
    app, text="Apply", font=("Arial", 15), command=whatsApp_BtnClick
)
whatsApp_apply.place(x=150, y=80)

title_2 = customtkinter.CTkLabel(app, text="Telegram", font=("Arial", 15))
title_2.place(x=10, y=130)


def telegram_BtnClick():
    current_text = telegram_apply.cget("text")
    if current_text == "Apply":
        print("Telegram Apply")
        telegram_apply.configure(text="Dispose")

    elif current_text == "Dispose":
        print("Dispose Telegram")
        telegram_apply.configure(text="Apply")


telegram_apply = customtkinter.CTkButton(
    app, text="Apply", font=("Arial", 15), command=telegram_BtnClick
)
telegram_apply.place(x=150, y=130)

app.mainloop()
