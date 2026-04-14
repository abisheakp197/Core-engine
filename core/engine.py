class Engine:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin):
        if not hasattr(plugin, "run"):
            raise TypeError("Plugin must implement run() method")
        self.plugins.append(plugin)

    def execute(self, data: dict) -> dict:
        if not isinstance(data, dict):
            raise ValueError("Input data must be a dictionary")

        for plugin in self.plugins:
            try:
                data = plugin.run(data)
            except Exception as e:
                return {
                    "error": str(e),
                    "failed_plugin": plugin.__class__.__name__
                }

        return data
