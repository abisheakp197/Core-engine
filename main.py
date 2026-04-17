import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from plugins.file_plugin import FileListPlugin
from plugins.filter_plugin import FileFilterPlugin
from plugins.rule_plugin import RulePlugin
from plugins.action_plugin import ActionPlugin
from plugins.undo_plugin import UndoPlugin


def main():
    data = {
        "type": "file",
        "folder": "/storage/emulated/0/Download",
        "extension": ".txt",
        "undo": False
    }

    file_list = FileListPlugin()
    data = file_list.run(data)
    print("LOG:", data)

    file_filter = FileFilterPlugin()
    data = file_filter.run(data)
    print("LOG:", data)

    rule = RulePlugin()
    data = rule.run(data)
    print("LOG:", data)

    if data.get("action") == "TXT_FILES_FOUND":
        action = ActionPlugin()
        data = action.run(data)
        print("LOG:", data)

    if data.get("undo") is True:
        undo = UndoPlugin()
        data = undo.run(data)
        print("LOG:", data)

    print("\nFINAL OUTPUT:")
    print(data)


if __name__ == "__main__":
    main()
