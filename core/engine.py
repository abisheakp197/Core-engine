class Engine:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin):
        if not hasattr(plugin, "run"):
            raise TypeError("Plugin must implement run()")
        self.plugins.append(plugin)

    def execute(self, data: dict) -> dict:
        if not isinstance(data, dict):
            raise ValueError("Input must be a dictionary")

        for plugin in self.plugins:
            data = plugin.run(data)

        return data
