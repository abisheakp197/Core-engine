from core.plugin import Plugin

class RulePlugin(Plugin):
    def run(self, data: dict) -> dict:
        count = data.get("filtered_count", 0)

        if count > 0:
            data["action"] = "TXT_FILES_FOUND"
        else:
            data["action"] = "NO_TXT_FILES"

        return data

