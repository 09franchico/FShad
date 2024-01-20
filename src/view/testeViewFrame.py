import customtkinter
from src.view import inputViewFrame
from src.view import logViewFrame
from src.view import terminalViewFrame


class TestViewFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        
        # self.terminalFrame = terminalViewFrame.TerminalViewFrame(master=self)
        # self.terminalFrame.grid(row=0, column=0, padx=5, pady=5, sticky="new")
        
        # self.inputFrame = inputViewFrame.InputViewFrame(master=self)
        # self.inputFrame.grid(row=1, column=1, padx=5, pady=5,sticky="nswe")
    
        
        # self.logFrame = logViewFrame.LogViewFrame(master=self)
        # self.logFrame.grid(row=1, column=2, padx=5, pady=5,sticky="nsew")
        
        
        
        