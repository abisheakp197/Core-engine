import os
import json
from core.plugin import Plugin

class UndoPlugin(Plugin):
    def run(self, data: dict) -> dict:
        if not data.get("undo"):
            return data

        folder = data.get("folder")
        undo_file = os.path.join(folder, "undo_log.json")

        if not os.path.exists(undo_file):
            data["undo_status"] = "No undo file found"
            return data

        with open(undo_file, "r") as f:
            undo_map = json.load(f)

        restored = []

        for new_name, original_name in undo_map.items():
            new_path = os.path.join(folder, new_name)
            original_path = os.path.join(folder, original_name)

            try:
                if os.path.exists(new_path):
                    os.rename(new_path, original_path)
                    restored.append(original_name)
            except Exception as e:
                return {"error": str(e)}

        data["restored_files"] = restored
        data["undo_status"] = "SUCCESS"

        return data
