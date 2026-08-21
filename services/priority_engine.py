from datetime import datetime


def calculate_priority(task):
    """
    Calculate a priority score from 0-100.

    Higher score = more urgent.
    """

    score = 0

    # Existing manual priority
    manual_priority = task.priority or 3

    priority_points = {
        1: 40,
        2: 30,
        3: 20,
        4: 10,
        5: 5
    }

    score += priority_points.get(
        manual_priority,
        20
    )

    # Deadline pressure
    if task.deadline:

        now = datetime.now()
        hours_remaining = (
            task.deadline - now
        ).total_seconds() / 3600

        if hours_remaining <= 0:
            score += 50

        elif hours_remaining <= 6:
            score += 45

        elif hours_remaining <= 24:
            score += 35

        elif hours_remaining <= 72:
            score += 25

        elif hours_remaining <= 168:
            score += 15

        else:
            score += 5

    # Large tasks deserve earlier attention
    if task.estimated_minutes:

        if task.estimated_minutes >= 240:
            score += 10

        elif task.estimated_minutes >= 120:
            score += 7

        elif task.estimated_minutes >= 60:
            score += 4

    return min(score, 100)
def rank_tasks(tasks):
    """
    Return tasks ordered by calculated priority.
    """

    ranked = []

    for task in tasks:
        score = calculate_priority(task)

        ranked.append(
            (task, score)
        )

    ranked.sort(
        key=lambda item: item[1],
        reverse=True
    )

    return ranked