import customtkinter as ctk
import random

with open('versiculos.txt', 'r', encoding='utf-8') as arquivo:
    versiculos = [linha.strip() for linha in arquivo]

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gerador de Versiculos Biblicos")
        self.geometry("400x300")
        self.resizable(False, False)

        # Configura as colunas e linhas da grade
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Cria o label e o botão
        self.label = ctk.CTkLabel(self, text="Seu Versiculo do dia:", wraplength=350)
        self.label.configure(font=("Arial", 14))
        self.label.grid(row=0, column=1, padx=10, pady=10)

        self.button = ctk.CTkButton(self, text="Gerar", command=self.generate_text)
        self.button.grid(row=1, column=1, padx=10, pady=10)

        self.versiculos = versiculos
        self.versiculo_escolhido = ""

    def generate_text(self):
        if len(self.versiculos) > 0:
            self.versiculo_escolhido = random.choice(self.versiculos)
            self.label.configure(text=self.versiculo_escolhido)
        else:
            self.label.configure(text="Não há mais versículos disponíveis")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()