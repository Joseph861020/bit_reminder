from datetime import datetime, timedelta
from typing import Dict


class ReminderModule:
    def __init__(self):
        self.reminders = {}

    def set_reminder(self, event_datetime: datetime, reminder_time: timedelta, details: str) -> str:
        """
        Устанавливает напоминание о событии.
        :param event_datetime: Дата и время события.
        :param reminder_time: Время до события, когда нужно напомнить.
        :param details: Описание напоминания.
        :return: Сообщение о результате.
        """
        reminder_datetime = event_datetime - reminder_time
        self.reminders[reminder_datetime] = details
        return f"Напоминание установлено: {details} за {reminder_time} до {event_datetime}"

    def check_reminders(self) -> Dict[datetime, str]:
        """
        Проверяет все напоминания и возвращает те, которые нужно показать.
        :return: Словарь активных напоминаний.
        """
        now = datetime.now()
        due_reminders = {dt: msg for dt, msg in self.reminders.items() if dt <= now}
        return due_reminders
