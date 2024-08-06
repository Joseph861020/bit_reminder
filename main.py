import os

import openai
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Инициализация клиента OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY не установлен в переменных окружения.")

openai.api_key = api_key


class SimpleBot:
    def __init__(self):
        pass

    def extract_keywords_and_params(self, message: str):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use GPT-3.5-turbo model
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            content = response.choices[0].message['content'].strip()

            # Простой пример парсинга ответа
            if "встречу" in content:
                return {"command": "schedule_meeting"}, {"details": content}
            elif "напомни" in content:
                return {"command": "set_reminder"}, {"details": content}
            elif "задачу" in content:
                return {"command": "create_task"}, {"details": content}
            else:
                return {"command": "unknown"}, {"details": content}

        except openai.OpenAIError as e:
            # Catching all OpenAI errors
            print("API error:", e)
            return {"command": "error"}, {"details": f"Произошла ошибка: {str(e)}"}

    def process_message(self, message: str) -> str:
        keywords, params = self.extract_keywords_and_params(message)
        command = keywords.get("command")

        if command == "schedule_meeting":
            return "Команда обработана. Встреча запланирована."
        elif command == "set_reminder":
            return "Команда обработана. Напоминание установлено."
        elif command == "create_task":
            return "Команда обработана. Задача создана."
        elif command == "error":
            return f"Ошибка: {params['details']}"
        else:
            return "Неизвестная команда."


def main():
    bot = SimpleBot()
    print("Бот запущен. Введите 'exit' для завершения работы.")
    while True:
        message = input("Введите сообщение: ")
        if message.lower() == 'exit':
            break
        response = bot.process_message(message)
        print(f"Ответ бота: {response}")


if __name__ == "__main__":
    main()
