import os
import json
from core.plugin import Plugin

class ActionPlugin(Plugin):
    def run(self, data: dict) -> dict:
        action = data.get("action")

        if action == "TXT_FILES_FOUND":
            folder = data.get("folder")
            files = data.get("filtered_files", [])

            renamed = []
            undo_map = {}

            for file in files:

                # ✅ SMART RULE: skip already renamed files
                if file.startswith("renamed_"):
                    print(f"SKIP (already renamed): {file}")
                    continue

                old_path = os.path.join(folder, file)
                new_name = f"renamed_{file}"
                new_path = os.path.join(folder, new_name)

                try:
                    os.rename(old_path, new_path)
                    renamed.append(new_name)

                    # Save mapping for undo
                    undo_map[new_name] = file

                except Exception as e:
                    return {"error": str(e)}

            # Save undo log
            undo_file = os.path.join(folder, "undo_log.json")
            with open(undo_file, "w") as f:
                json.dump(undo_map, f, indent=4)

            data["renamed_files"] = renamed
            data["undo_file"] = undo_file

        return data
