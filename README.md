# Бот Напоминаний

Этот проект представляет собой бота, который использует API OpenAI для обработки текстовых команд и выполнения различных задач, таких как планирование встреч, установка напоминаний и создание задач.

## Описание

Бот выполняет следующие функции:
- **Планирование встреч**: Позволяет пользователю планировать встречи на определенные даты и время.
- **Установка напоминаний**: Позволяет пользователю установить напоминания о важных событиях.
- **Создание задач**: Позволяет пользователю создавать задачи для выполнения.

## Требования

Для работы бота вам потребуется:
- Python 3.7 или новее
- Установленные зависимости из `requirements.txt`
- API-ключ от OpenAI

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/ваш-пользователь/бот-напоминаний.git
2. Перейдите в каталог проекта:

    ```bash
    cd бот-напоминаний
    ```
3. Создайте и активируйте виртуальное окружение:
    
    ```bash
    
    python -m venv .venv

    source .venv/bin/activate  # Для Windows используйте .venv\Scripts\activate
    ```
4. Установите зависимости:

   ```bash
   
   pip install -r requirements.txt
   ```
5. Создайте файл .env и добавьте ваш OpenAI API-ключ:

   ```env
   
   OPENAI_API_KEY=ваш_ключ_здесь
   ```
## Использование
Для запуска бота используйте команду:

   ```bash
   
   python main.py
   ```
Бот будет запущен и будет ожидать ввода сообщений. Введите команду, например, "Планирую встречу на 2024-08-07 в 10:00 с клиентом", и бот обработает ее.

### Примеры команд
* Планирование встречи:

   Введите: Планирую встречу на 2024-08-07 в 10:00 с клиентом

   Ответ: Команда обработана. Встреча запланирована.

* Установка напоминания:
   
   Введите: Напомни мне о встрече через 1 час
   
   Ответ: Команда обработана. Напоминание установлено.

* Создание задачи:

   Введите: Создать задачу по подготовке отчета
   
   Ответ: Команда обработана. Задача создана.