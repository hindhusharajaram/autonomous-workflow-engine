from datetime import datetime

class PlannerAgent:
    def log(self, audit_trail, task_id):
        audit_trail.append({
            "Time": datetime.now().strftime("%H:%M"),
            "Agent": "🧠 Planner",
            "Action": f"Indexed Decision #{task_id}"
        })

class ExecutorAgent:
    def start(self, audit_trail, task_id):
        audit_trail.append({
            "Time": datetime.now().strftime("%H:%M"),
            "Agent": "⚙️ Executor",
            "Action": f"Initiated Task #{task_id}"
        })

class AuditorAgent:
    def verify(self, audit_trail, task_id):
        audit_trail.append({
            "Time": datetime.now().strftime("%H:%M"),
            "Agent": "🏁 Auditor",
            "Action": f"Verified Task #{task_id}"
        })
