import yaml

class ConfigReader:
    def __init__(self, path):
        self.path = path

    def getTimer(self, id):
        with self.path.open() as file:
            content = yaml.safe_dump(file)