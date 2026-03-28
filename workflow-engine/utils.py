def get_progress_bar(pct):
    filled = int(pct / 10)
    bar = "█" * filled + "░" * (10 - filled)
    return f"{bar} {pct}%"
