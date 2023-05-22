import customtkinter as ctk


class Main(ctk.CTk):

    def __init__(self):

        super().__init__()
        self.title('calculator')

        self.font = ctk.CTkFont('consolas', 30)
        self.expr = ''

        self.entry = ctk.CTkEntry(self, state=ctk.DISABLED, font=self.font)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='we')

        self.add_btn(1, 0, '7')
        self.add_btn(1, 1, '8')
        self.add_btn(1, 2, '9')
        self.add_btn(1, 3, '+', True)

        self.add_btn(2, 0, '4')
        self.add_btn(2, 1, '5')
        self.add_btn(2, 2, '6')
        self.add_btn(2, 3, '-', True)

        self.add_btn(3, 0, '1')
        self.add_btn(3, 1, '2')
        self.add_btn(3, 2, '3')
        self.add_btn(3, 3, '/', True)

        self.add_btn(4, 0, 'CE', command=self.clear)
        self.add_btn(4, 1, '0')
        self.add_btn(4, 2, '=', True, command=self.equal)
        self.add_btn(4, 3, '*', True)

    def add_btn(self, row, column, text, is_act=False, command=None):

        if is_act: col = None
        else: col = '#343638'
        if not command: command = lambda: self.insert(text)
        ctk.CTkButton(self, text=text, command=command, fg_color=col, width=50, height=50, font=self.font).grid(row=row, column=column, padx=5, pady=5)

    def insert(self, text):

        self.entry.configure(state=ctk.NORMAL)
        self.expr += text
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, self.expr)
        self.entry.configure(state=ctk.DISABLED)

    def clear(self):

        self.entry.configure(state=ctk.NORMAL)
        self.entry.delete(0, ctk.END)
        self.expr = ''
        self.entry.configure(state=ctk.DISABLED)

    def equal(self):

        self.entry.configure(state=ctk.NORMAL)
        self.entry.delete(0, ctk.END)
        try:
            result = eval(self.expr)
        except:
            result = 'ERROR'
        self.expr = ''
        self.entry.insert(0, str(result))
        self.entry.configure(state=ctk.DISABLED)


if __name__ == '__main__':
    main = Main()
    main.mainloop()
