import pandas as pd
from llm_interface import call_intelligence
from utils import get_progress_bar
from agents import PlannerAgent, ExecutorAgent, AuditorAgent
from datetime import datetime

class MeetingIntelligenceSystem:
    def __init__(self):
        self.registry = []
        self.audit_trail = []
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.auditor = AuditorAgent()

    def process_cycle(self, meeting_text):
        try:
            if meeting_text and meeting_text.strip():
                history = "\n".join([f"ID {t['ID']}: {t['Decision']}" for t in self.registry])
                prompt = f"""
                Analyze this transcript: '{meeting_text}'
                Existing Registry: {history if history else "Empty"}

                LOGIC RULES:
                1. Extract every unique action item.
                2. If a task says "after", "once finished", or "then", identify the 'dep_id'.
                3. SEQUENCING: Task B follows Task A → Task B's dep_id = Task A ID.

                Return ONLY JSON:
                {{
                    "decisions": [
                        {{"decision": "string", "owner": "string", "priority": "High/Med/Low", "dep_id": int_or_null}}
                    ]
                }}
                """
                data = call_intelligence(prompt)

                for d in data.get("decisions", []):
                    new_id = len(self.registry) + 1
                    self.registry.append({
                        "ID": new_id,
                        "Decision": d.get("decision", "Action Item"),
                        "Owner": d.get("owner") or "Unassigned",
                        "Priority": d.get("priority", "Med"),
                        "Status": "⚪ Pending",
                        "Progress": 0,
                        "Dependency": d.get("dep_id")
                    })
                    self.planner.log(self.audit_trail, new_id)

            for _ in range(2):
                for item in self.registry:
                    dep_id = item.get("Dependency")
                    blocked = False
                    if dep_id is not None:
                        parent = next((x for x in self.registry if x["ID"] == int(dep_id)), None)
                        if parent and parent["Progress"] < 100:
                            blocked = True
                            item["Status"] = f"🔴 Stalled (ID:{dep_id})"

                    if not blocked:
                        if "Pending" in item["Status"] or "Stalled" in item["Status"]:
                            item["Status"] = "🔵 In Progress"
                            item["Progress"] = 20
                            self.executor.start(self.audit_trail, item["ID"])
                        elif item["Status"] == "🔵 In Progress":
                            item["Progress"] = min(item["Progress"] + 40, 100)
                            if item["Progress"] == 100:
                                item["Status"] = "🟢 Resolved"
                                self.auditor.verify(self.audit_trail, item["ID"])

            df_tasks = pd.DataFrame(self.registry)
            if not df_tasks.empty:
                df_tasks["Progress"] = df_tasks["Progress"].apply(get_progress_bar)

            df_logs = pd.DataFrame(self.audit_trail)
            return df_tasks, df_logs

        except Exception as e:
            return pd.DataFrame([{"Error": str(e)}]), pd.DataFrame()

    def reset(self):
        self.registry, self.audit_trail = [], []
        return pd.DataFrame(), pd.DataFrame()
