from datetime import datetime, timedelta

def get_schedule_progress(start_day, start_time, end_day, end_time):
    start_dt = datetime.combine(start_day, start_time)
    end_dt = datetime.combine(end_day, end_time)
    now = datetime.now()

    if now <= start_dt:
        return 0
    elif now >= end_dt:
        return 100
    else:
        total_duration = (end_dt - start_dt).total_seconds()
        elapsed = (now - start_dt).total_seconds()
        return int((elapsed / total_duration) * 100)
