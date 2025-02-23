import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class PizzariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizzaria Delícia")
        self.root.geometry("400x400")

        self.total = 0
        self.pedido = {}

        self.tela_apresentacao()

    def carregar_imagem(self, caminho):
        """Carrega e redimensiona uma imagem para ser usada no fundo."""
        imagem = Image.open(caminho)
        imagem = imagem.resize((400, 400))
        return ImageTk.PhotoImage(imagem)

    def clear_screen(self):
        """Remove todos os widgets da tela."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def tela_apresentacao(self):
        """Tela inicial com apresentação de 3 segundos."""
        self.clear_screen()
        self.bg_image = self.carregar_imagem("pizzaria.jpg")

        canvas = tk.Canvas(self.root, width=400, height=400)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        canvas.create_text(200, 50, text="Bem-vindo à Pizzaria Delícia!", font=("Arial", 20), fill="white")

        self.root.after(3000, self.tela_login)

    def tela_login(self):
        """Tela de login simples."""
        self.clear_screen()
        self.bg_image = self.carregar_imagem("login.jpg")

        canvas = tk.Canvas(self.root, width=400, height=400)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        tk.Label(self.root, text="Usuário:", font=("Arial", 12)).place(x=100, y=150)
        self.entry_usuario = tk.Entry(self.root)
        self.entry_usuario.place(x=180, y=150)

        btn_login = tk.Button(self.root, text="Entrar", command=self.tela_opcoes)
        btn_login.place(x=160, y=200)

    def tela_opcoes(self):
        """Tela principal com opções de Pizzas, Salgados e Bebidas."""
        self.clear_screen()
        self.bg_image = self.carregar_imagem("menu.jpg")

        canvas = tk.Canvas(self.root, width=400, height=400)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        tk.Button(self.root, text="🍕 Pizzas", command=self.tela_pizzas).place(x=160, y=100)
        tk.Button(self.root, text="🥐 Salgados", command=self.tela_salgados).place(x=150, y=150)
        tk.Button(self.root, text="🥤 Bebidas", command=self.tela_bebidas).place(x=160, y=200)
        tk.Button(self.root, text="🛒 Finalizar Pedido", command=self.tela_pagamento).place(x=135, y=250)

    def atualizar_pedido(self, item, preco, label_total):
        """Adiciona ou remove itens do pedido."""
        if item in self.pedido:
            self.pedido[item] += 1
        else:
            self.pedido[item] = 1
        self.total += preco
        label_total.config(text=f"Total: R$ {self.total:.2f}")

    def remover_pedido(self, item, preco, label_total):
        """Remove itens do pedido."""
        if item in self.pedido and self.pedido[item] > 0:
            self.pedido[item] -= 1
            self.total -= preco
            label_total.config(text=f"Total: R$ {self.total:.2f}")

    def tela_pizzas(self):
        """Tela de pizzas."""
        self.clear_screen()
        tk.Label(self.root, text="Escolha sua Pizza", font=("Arial", 14)).pack()
        label_total = tk.Label(self.root, text=f"Total: R$ {self.total:.2f}", font=("Arial", 12))
        label_total.pack()

        itens = [("Calabresa", 25), ("Mussarela", 23), ("Frango c/ Catupiry", 27)]
        for item, preco in itens:
            frame = tk.Frame(self.root)
            frame.pack()
            tk.Label(frame, text=item).pack(side="left")
            tk.Button(frame, text="+", command=lambda i=item, p=preco: self.atualizar_pedido(i, p, label_total)).pack(side="left")
            tk.Button(frame, text="-", command=lambda i=item, p=preco: self.remover_pedido(i, p, label_total)).pack(side="left")

        tk.Button(self.root, text="Voltar", command=self.tela_opcoes).pack()

    def tela_salgados(self):
        """Tela de salgados."""
        self.clear_screen()
        tk.Label(self.root, text="Escolha seu Salgado", font=("Arial", 14)).pack()
        label_total = tk.Label(self.root, text=f"Total: R$ {self.total:.2f}", font=("Arial", 12))
        label_total.pack()

        itens = [("Coxinha", 5), ("Empada", 4), ("Esfirra", 6)]
        for item, preco in itens:
            frame = tk.Frame(self.root)
            frame.pack()
            tk.Label(frame, text=item).pack(side="left")
            tk.Button(frame, text="+", command=lambda i=item, p=preco: self.atualizar_pedido(i, p, label_total)).pack(side="left")
            tk.Button(frame, text="-", command=lambda i=item, p=preco: self.remover_pedido(i, p, label_total)).pack(side="left")

        tk.Button(self.root, text="Voltar", command=self.tela_opcoes).pack()

    def tela_bebidas(self):
        """Tela de bebidas."""
        self.clear_screen()
        tk.Label(self.root, text="Escolha sua Bebida", font=("Arial", 14)).pack()
        label_total = tk.Label(self.root, text=f"Total: R$ {self.total:.2f}", font=("Arial", 12))
        label_total.pack()

        itens = [("Refrigerante", 8), ("Suco", 6), ("Água", 3)]
        for item, preco in itens:
            frame = tk.Frame(self.root)
            frame.pack()
            tk.Label(frame, text=item).pack(side="left")
            tk.Button(frame, text="+", command=lambda i=item, p=preco: self.atualizar_pedido(i, p, label_total)).pack(side="left")
            tk.Button(frame, text="-", command=lambda i=item, p=preco: self.remover_pedido(i, p, label_total)).pack(side="left")

        tk.Button(self.root, text="Voltar", command=self.tela_opcoes).pack()

    def tela_pagamento(self):
        """Tela de pagamento."""
        self.clear_screen()
        tk.Label(self.root, text=f"Total a pagar: R$ {self.total:.2f}", font=("Arial", 14)).pack()
        tk.Button(self.root, text="Confirmar Pedido", command=self.tela_agradecimento).pack()
        tk.Button(self.root, text="Voltar", command=self.tela_opcoes).pack()

    def tela_agradecimento(self):
        """Tela final com mensagem de agradecimento."""
        self.clear_screen()
        tk.Label(self.root, text="Obrigado pelo seu pedido!", font=("Arial", 16)).pack()
        tk.Button(self.root, text="Voltar ao Menu", command=self.tela_opcoes).pack()

root = tk.Tk()
app = PizzariaApp(root)
root.mainloop()
