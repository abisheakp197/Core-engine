import os
from core.plugin import Plugin

import os
from core.plugin import Plugin


class FileListPlugin(Plugin):
    def run(self, data: dict) -> dict:
        folder = data.get("folder")

        if not folder:
            raise ValueError("Missing 'folder' in input")

        if not os.path.exists(folder):
            raise FileNotFoundError(f"Folder not found: {folder}")

        files = os.listdir(folder)

        data["files"] = files
        data["file_count"] = len(files)

        return data
