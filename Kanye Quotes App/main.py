from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, background="white")
canvas = Canvas(width=300, height=414, background="white", highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 220, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 24, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,padx=0,pady=0,bd=0, relief="flat")
# kanye_button.grid(row=1, column=0)

kanye_label = Label(image=kanye_img,background="white", borderwidth=0)
kanye_label.grid(row=1, column=0)

kanye_label.bind("<Button-1>", lambda e: get_quote())




window.mainloop()