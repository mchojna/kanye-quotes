import requests
import tkinter as tk


def new_quote():
    quote = requests.get(url=link)
    quote = quote.json()["quote"]
    canvas.itemconfig(kanye_quote, text=f"{quote}")


link = "https://api.kanye.rest"

root = tk.Tk()
root.minsize(width=400, height=650)
root.title("Kanye Says...")

quote_img = tk.PhotoImage(file="background.png")

canvas = tk.Canvas(width=600, height=800, bg="white")
canvas.create_image(200, 400, image=quote_img)
kanye_quote = canvas.create_text(200, 375, text="", font=("Ariel", 24, "bold"), width=245, justify="left")

new_quote()

canvas.place(x=0, y=-150)

kanye_img = tk.PhotoImage(file="kanye.png")
kanye_button = tk.Button(image=kanye_img, bg="white", borderwidth=0, highlightthickness=0, command=new_quote)
kanye_button.place(x=150, y=465)

root.mainloop()