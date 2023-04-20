import weather as w
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Current temperature (F) in Croghan, NY")
        self.minsize(400, 300)

        self.btn1 = ctk.CTkButton(
            master=self, command=self.button_callback, text='Get the weather')
        self.btn1.pack(padx=20, pady=20)

        self.txtbx1 = ctk.CTkTextbox(master=self)
        self.txtbx1.pack(padx=20, pady=20)

    def button_callback(self):
        current_weather = w.Weather()
        self.txtbx1.delete("1.0", ctk.END)  # "line.column"
        message = f"At {current_weather.current_time},\nthe temperature in Croghan, NY\nis {current_weather.get_temp_f()} degrees Fahrenheit."
        self.txtbx1.insert("insert", message, "n/a")


if __name__ == "__main__":
    app = App()
    app.mainloop()
