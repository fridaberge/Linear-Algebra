#klasse for kortene
class Kort:
    def __init__(self, tall, type):
        self.tall = tall
        self.type = type

    def __str__(self):
        return f"{self.tall}({self.type})"