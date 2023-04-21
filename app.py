import weather as w
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # self.title("The Weather in Three Cities")

        self.main_frame = ctk.CTkFrame(self, width=1020, height=951)
        self.main_frame.grid_columnconfigure(0, minsize=600)
        self.main_frame.grid_columnconfigure(1, minsize=600)
        self.main_frame.grid()

        self.drop_down = ctk.CTkOptionMenu(
            self.main_frame, width=300, values=['Lowville', 'Watertown', 'Rochester'], font=('Helvetica bold', 30), command=self.send_value)
        self.drop_down.grid(row=0, column=0, padx=0, pady=0)
        self.city = 'Lowville'

        self.btn1 = ctk.CTkButton(self.main_frame, width=300, command=self.button_callback,
                                  text='Get temps', font=('Helvetica bold', 30))
        self.btn1.grid(row=0, column=1, padx=0, pady=0)

        self.data_frame = ctk.CTkFrame(self.main_frame)
        self.data_frame.grid_columnconfigure(0, minsize=350)
        self.data_frame.grid_columnconfigure(1, minsize=350)
        self.data_frame.grid_columnconfigure(2, minsize=350)
        self.data_frame.grid(columnspan=2, padx=20)

        #!  0
        self.lbl0 = ctk.CTkLabel(self.data_frame, text='low', font=(
            'Helvetica bold', 30))
        self.lbl0.grid(row=0, column=0, padx=0, pady=200)

        #!  1
        self.lbl1 = ctk.CTkLabel(self.data_frame, text='current', font=(
            'Helvetica bold', 50))
        self.lbl1.grid(row=0, column=1, padx=0, pady=200)

        #!  2
        self.lbl2 = ctk.CTkLabel(self.data_frame, text='high', font=(
            'Helvetica bold', 30))
        self.lbl2.grid(row=0, column=2, padx=0, pady=200)

        print(self.main_frame.winfo_width())
        print(self.main_frame.winfo_height())

    def button_callback(self):
        current_weather = w.Weather(self.city)

        self.lbl0.configure(text=f'{current_weather.get_list_f()[0]}F')
        self.lbl1.configure(text=f'{current_weather.get_list_f()[1]}F')
        self.lbl2.configure(text=f'{current_weather.get_list_f()[2]}F')

        print(self.winfo_width())
        print(self.winfo_height())

    def send_value(self, city):
        self.city = city


if __name__ == "__main__":
    app = App()
    app.mainloop()
