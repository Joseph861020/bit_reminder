from datetime import datetime
from typing import Dict


class CalendarModule:
    def __init__(self):
        self.events = {}

    def add_event(self, date: str, time: str, details: str) -> str:
        """
        Добавляет событие в календарь.
        :param date: Дата события в формате YYYY-MM-DD.
        :param time: Время события в формате HH:MM.
        :param details: Описание события.
        :return: Сообщение о результате.
        """
        event_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        self.events[event_datetime] = details
        return f"Событие добавлено: {details} на {event_datetime}"

    def list_events(self) -> Dict[datetime, str]:
        """
        Возвращает список всех событий в календаре.
        :return: Словарь событий.
        """
        return self.events
