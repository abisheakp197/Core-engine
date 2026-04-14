class Plugin:
    def run(self, data: dict) -> dict:
        raise NotImplementedError("Plugin must implement run()")
