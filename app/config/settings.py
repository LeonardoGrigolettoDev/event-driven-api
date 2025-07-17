import os

class Settings:
    def __init__(self):
        self.env = os.getenv('ENV', 'development')
        self.debug = os.getenv('DEBUG', 'True') == 'True'
        # Adicione outras configurações conforme necessário
