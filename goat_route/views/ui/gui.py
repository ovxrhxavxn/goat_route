import PIL.Image
import customtkinter as CTk
from pathlib import WindowsPath

from .interfaces import IGUI

class MainWindowGUI(IGUI, CTk.CTk):

    def __init__(self):

        super().__init__()

        self.geometry("460x640")  # Устанавливаем размеры окна
        self.title('G.O.A.T Route')  # Устанавливаем заголовок окна
        self.resizable(False, False)  # Запрещаем изменение размеров окна
        self.iconbitmap(WindowsPath("views\\ui\\resources\\icon.ico").resolve())

        # Устанавливаем тему по умолчанию "Dark"
        CTk.set_appearance_mode("Dark")

        # Загружаем логотип и добавляем его в окно
        self.logo = CTk.CTkImage(

            dark_image=PIL.Image.open(WindowsPath("views\\ui\\resources\\logo.png").resolve()),
            size=(160, 160)

            )
        
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 0))

        # Создаем фрейм для ввода данных
        self.input_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.input_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.entry_list = []  # Список для хранения текстовых полей ввода

        self.max_entries = 8  # Максимальное количество панелей ввода

        # Добавляем первую панель ввода
        self._add_input_entry()

        # Добавляем текст "KirovChist" между первой панелью ввода и логотипом
        self.kirovchist_label = CTk.CTkLabel(master=self, text="© Киров & Чистяков", fg_color="transparent")
        self.kirovchist_label.grid(row=2, column=0, padx=(20, 20), pady=(10, 0))

        # Создаем фрейм для настроек
        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=3, column=0, padx=(20, 20), pady=(20, 0), sticky="ew")

        # Добавляем радиокнопки в фрейм настроек
        self.radio_var = CTk.StringVar()  # Переменная для связи радиокнопок между собой

        self._radio_options = [

            CTk.CTkRadioButton(master=self.settings_frame, text="On Foot",
                                                 variable=self.radio_var, value="On Foot"),

            CTk.CTkRadioButton(master=self.settings_frame, text="Car",
                                                 variable=self.radio_var, value="Car"),

            CTk.CTkRadioButton(master=self.settings_frame, text="Public Transport",
                                                 variable=self.radio_var, value="Public Transport")
        ]

        for i, radio_option in enumerate(self._radio_options):
            radio_option.grid(row=0, column=i, padx=(0, 10), sticky="ew")

        # Добавляем кнопку "Генерировать путь" и привязываем ее к методу generate_path
        self.generate_path_button = CTk.CTkButton(master=self, text="Генерировать путь", command=None)
        self.generate_path_button.grid(row=4, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

    def _add_input_entry(self):

        """Метод для добавления нового текстового поля ввода"""
        
        if len(self.entry_list) < self.max_entries:  # Проверяем, что количество полей меньше максимального
            new_entry_frame = CTk.CTkFrame(master=self.input_frame, fg_color="transparent")
            new_entry_frame.grid(row=len(self.entry_list), column=0, padx=(0, 0), pady=(5, 5), sticky="ew")

            new_entry = CTk.CTkEntry(master=new_entry_frame, width=300)
            new_entry.grid(row=0, column=0, padx=(0, 20))

            self.entry_list.append(new_entry)  # Добавляем новое поле ввода в список

            # Добавляем кнопку "+" для добавления новых полей ввода
            self.btn_add = CTk.CTkButton(master=new_entry_frame, text="+", width=100,
                                         command=self._add_input_entry)
            self.btn_add.grid(row=0, column=1)

            if len(self.entry_list) == self.max_entries:  # Отключаем кнопку, если достигнут максимум
                self.btn_add.configure(state="disabled")

    def init(self):
        self.mainloop()