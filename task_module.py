def send_task(task_name: str, deadline: str) -> str:
    """
    Отправить задачу в таск-трекер.

    :param task_name: Название задачи.
    :param deadline: Дата и время дедлайна в формате ISO 8601.
    :return: Строка с подтверждением.
    """
    return f"Задача '{task_name}' добавлена с дедлайном {deadline}."
