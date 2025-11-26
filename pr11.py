import tkinter as tk
from tkinter import ttk, messagebox, filedialog
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # 1. Название приложения: ФИО автора
        self.title("Роньшина Валерия Игоревна")
        self.geometry("600x400")
        # Создание вкладок
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        # Первая вкладка - калькулятор
        self.create_calculator_tab()
        # Вторая вкладка - чекбоксы
        self.create_checkboxes_tab()
        # Третья вкладка - работа с текстом
        self.create_text_tab()
    def create_calculator_tab(self):
        """Создание вкладки с калькулятором"""
        calc_frame = ttk.Frame(self.notebook)
        self.notebook.add(calc_frame, text="Калькулятор")
        # Поля для ввода чисел
        ttk.Label(calc_frame, text="Первое число:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.num1_entry = ttk.Entry(calc_frame)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(calc_frame, text="Второе число:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.num2_entry = ttk.Entry(calc_frame)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)
        # Выпадающий список операций
        ttk.Label(calc_frame, text="Операция:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.operation_var = tk.StringVar(value="+")
        operations = ["+", "-", "*", "/"]
        self.operation_combo = ttk.Combobox(calc_frame, textvariable=self.operation_var, 
                                           values=operations, state="readonly")
        self.operation_combo.grid(row=2, column=1, padx=10, pady=10)
        # Кнопка вычисления
        calc_button = ttk.Button(calc_frame, text="Вычислить", command=self.calculate)
        calc_button.grid(row=3, column=0, columnspan=2, pady=20)
        # Поле для результата
        ttk.Label(calc_frame, text="Результат:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.result_label = ttk.Label(calc_frame, text="", font=("Arial", 12, "bold"))
        self.result_label.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    def calculate(self):
        """Выполнение вычислений"""
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Деление на ноль!")
                result = num1 / num2
            self.result_label.config(text=f"{result:.2f}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа!")
        except ZeroDivisionError as e:
            messagebox.showerror("Ошибка", str(e))
    def create_checkboxes_tab(self):
        """Создание вкладки с чекбоксами"""
        check_frame = ttk.Frame(self.notebook)
        self.notebook.add(check_frame, text="Чекбоксы")
        # Переменные для чекбоксов
        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()
        # Создание чекбоксов
        self.check1 = ttk.Checkbutton(check_frame, text="Первый", variable=self.var1)
        self.check2 = ttk.Checkbutton(check_frame, text="Второй", variable=self.var2)
        self.check3 = ttk.Checkbutton(check_frame, text="Третий", variable=self.var3)
        # Размещение чекбоксов
        self.check1.pack(pady=15)
        self.check2.pack(pady=15)
        self.check3.pack(pady=15)
        # Кнопка для показа выбора
        show_button = ttk.Button(check_frame, text="Показать выбор", command=self.show_selection)
        show_button.pack(pady=20)
    def show_selection(self):
        """Показ выбранных чекбоксов во всплывающем окне"""
        selected = []
        if self.var1.get():
            selected.append("Первый")
        if self.var2.get():
            selected.append("Второй")
        if self.var3.get():
            selected.append("Третий")
        if selected:
            message = f"Вы выбрали: {', '.join(selected)}"
        else:
            message = "Вы ничего не выбрали"
        messagebox.showinfo("Ваш выбор", message)
    def create_text_tab(self):
        """Создание вкладки для работы с текстом"""
        text_frame = ttk.Frame(self.notebook)
        self.notebook.add(text_frame, text="Текст")
        # Создание меню
        menubar = tk.Menu(text_frame)
        self.file_menu = tk.Menu(menubar, tearoff=0)
        self.file_menu.add_command(label="Загрузить из файла", command=self.load_from_file)
        self.file_menu.add_command(label="Сохранить в файл", command=self.save_to_file)
        menubar.add_cascade(label="Файл", menu=self.file_menu)
        # Текстовое поле
        self.text_widget = tk.Text(text_frame, wrap=tk.WORD, width=60, height=15)
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.text_widget.yview)
        self.text_widget.configure(yscrollcommand=scrollbar.set)
        # Размещение элементов
        self.text_widget.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y", pady=10)
        # Установка меню
        self.config(menu=menubar)
    def load_from_file(self):
        """Загрузка текста из файла"""
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_widget.delete(1.0, tk.END)
                    self.text_widget.insert(1.0, content)
                messagebox.showinfo("Успех", "Файл успешно загружен!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {str(e)}")
    def save_to_file(self):
        """Сохранение текста в файл"""
        file_path = filedialog.asksaveasfilename(
            title="Сохранить файл",
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        if file_path:
            try:
                content = self.text_widget.get(1.0, tk.END)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                messagebox.showinfo("Успех", "Файл успешно сохранен!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")
# Запуск приложения
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
