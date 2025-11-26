import tkinter as tk
from tkinter import ttk, messagebox
import json
import urllib.request
import urllib.error
class GitHubRepoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Repository Info - Вариант 6 (Kubernetes)")
        self.root.geometry("600x400")
        # Создаем основной фрейм
        main_frame = ttk.Frame(root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)
        # Заголовок
        title_label = ttk.Label(main_frame, 
                               text="Получение информации о репозитории GitHub\nВариант 6: Kubernetes", 
                               font=("Arial", 14, "bold"),
                               justify=tk.CENTER)
        title_label.pack(pady=15)
        # Поле ввода имени репозитория
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=20)
        ttk.Label(input_frame, text="Имя репозитория:", font=("Arial", 10)).pack(side=tk.LEFT)
        self.repo_entry = ttk.Entry(input_frame, width=25, font=("Arial", 10))
        self.repo_entry.pack(side=tk.LEFT, padx=10)
        self.repo_entry.insert(0, "kubernetes")  # Автоматически подставляем kubernetes
        # Кнопка получения информации
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)
        get_info_button = ttk.Button(button_frame, text="Получить информацию Kubernetes", 
                                   command=self.get_repo_info,
                                   style="Accent.TButton")
        get_info_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = ttk.Button(button_frame, text="Очистить", 
                                command=self.clear_results)
        clear_button.pack(side=tk.LEFT, padx=5)
        # Поле для вывода результата
        result_frame = ttk.LabelFrame(main_frame, text="Результат:", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        self.result_text = tk.Text(result_frame, height=12, width=70, font=("Consolas", 9))
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Статус бар
        self.status_var = tk.StringVar(value="Готов к работе")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(fill=tk.X, pady=(5, 0))
    def make_request(self, url):
        """Выполняет HTTP запрос используя urllib"""
        try:
            self.status_var.set("Выполняется запрос к GitHub API...")
            self.root.update()
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0')
            with urllib.request.urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise Exception("Репозиторий не найден")
            else:
                raise Exception(f"Ошибка API GitHub: {e.code}")
        except urllib.error.URLError as e:
            raise Exception(f"Ошибка подключения к интернету: {str(e)}")
        except Exception as e:
            raise Exception(f"Произошла ошибка: {str(e)}")
        finally:
            self.status_var.set("Готов к работе")
    def get_repo_info(self):
        repo_name = self.repo_entry.get().strip()
        if not repo_name:
            messagebox.showerror("Ошибка", "Введите имя репозитория")
            return
        try:
            # Получаем информацию о репозитории
            repo_url = f"https://api.github.com/repos/{repo_name}/{repo_name}"
            repo_data = self.make_request(repo_url)
            
            # Получаем информацию об owner
            owner_url = repo_data['owner']['url']
            owner_data = self.make_request(owner_url)
            
            # Формируем данные в требуемом формате
            result_data = {
                'company': owner_data.get('company'),
                'created_at': owner_data.get('created_at'),
                'email': owner_data.get('email'),
                'id': owner_data.get('id'),
                'name': owner_data.get('name') or repo_name,
                'url': owner_data.get('url')
            }
            # Выводим результат в текстовое поле
            self.result_text.delete(1.0, tk.END)
            formatted_json = json.dumps(result_data, indent=2, ensure_ascii=False)
            self.result_text.insert(1.0, formatted_json)
            # Сохраняем в файл
            filename = self.save_to_file(result_data, repo_name)
            messagebox.showinfo("Успех", f"Информация о Kubernetes сохранена в файл:\n{filename}")  
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    def save_to_file(self, data, repo_name):
        """Сохраняет данные в JSON файл"""
        filename = f"github_info_{repo_name}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return filename
    def clear_results(self):
        """Очищает поле результатов"""
        self.result_text.delete(1.0, tk.END)
        self.status_var.set("Поле результатов очищено")
def main():
    root = tk.Tk()
    # Стиль для акцентной кнопки
    style = ttk.Style()
    style.configure("Accent.TButton", foreground="blue", font=("Arial", 10, "bold"))
    app = GitHubRepoApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()
