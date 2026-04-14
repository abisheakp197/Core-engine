from core.engine import Engine
from plugins.file_plugin import FileListPlugin

def main():
    engine = Engine()
    engine.register_plugin(FileListPlugin())

    input_data = {
        "folder": "/storage/emulated/0/Download"
    }

    result = engine.execute(input_data)
    print(result)

if __name__ == "__main__":
    main()
