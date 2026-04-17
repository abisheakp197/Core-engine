from core.plugin import Plugin

class FileFilterPlugin(Plugin):
    def run(self, data: dict) -> dict:
        extension = data.get("extension")

        if not extension:
            return data

        files = data.get("files", [])

        filtered = [f for f in files if f.endswith(extension)]

        data["filtered_files"] = filtered
        data["filtered_count"] = len(filtered)

        return data
