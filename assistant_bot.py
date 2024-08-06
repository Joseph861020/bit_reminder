import openai

from calendar_module import CalendarModule
from reminder_module import ReminderModule
from task_tracker_module import TaskTrackerModule


class AssistantBot:  # Already appropriately named
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key
        self.calendar_module = CalendarModule()
        self.reminder_module = ReminderModule()
        self.task_tracker_module = TaskTrackerModule()

    def extract_keywords_and_params(self, message: str):
        try:
            response = openai.ChatCompletion.create(
                messages=[{"role": "user", "content": message}],
                model="gpt-3.5-turbo"
            )
            content = response.choices[0].message['content'].strip()

            if "встречу" in content:
                return {"command": "schedule_meeting"}, {"details": content}
            elif "напомни" in content:
                return {"command": "set_reminder"}, {"details": content}
            elif "задачу" in content:
                return {"command": "create_task"}, {"details": content}
            else:
                return {"command": "unknown"}, {"details": content}

        except openai.error.OpenAIError as e:
            return {"command": "error"}, {"details": f"Произошла ошибка: {str(e)}"}

    def process_message(self, message: str) -> str:
        keywords, params = self.extract_keywords_and_params(message)
        command = keywords.get("command")

        if command == "schedule_meeting":
            return self.calendar_module.schedule_meeting(params)
        elif command == "set_reminder":
            return self.reminder_module.set_reminder(params)
        elif command == "create_task":
            return self.task_tracker_module.create_task(params)
        else:
            return "Неизвестная команда."
