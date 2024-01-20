import customtkinter
from src.view import mainViewFrame


class LoginViewFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # create login frame
        # self.login_frame = customtkinter.CTkFrame(self, corner_radius=0,)
        # self.login_frame.grid(row=0, column=0, sticky="ns")
        
        self.login_label = customtkinter.CTkLabel(
            self, text="Login FShd",
            font=customtkinter.CTkFont(size=20, weight="bold"))
        
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        
        self.username_entry = customtkinter.CTkEntry(self, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        
        self.password_entry = customtkinter.CTkEntry(self, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        
        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        
        #Main Frame
        self.main_frame = mainViewFrame.MainViewFrame(self.master)
        
    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())
        self.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=20,pady=20)  # show main frame