# config.py

class Model:
    def __init__(self, first_message: str, provider: str, model: str, system_prompt: str):
        self.first_message = first_message
        self.provider = provider
        self.model = model
        self.system_prompt = system_prompt

class Transcriber:
    def __init__(self, provider: str, lang: str, model: str):
        self.provider = provider
        self.lang = lang
        self.model = model

class Voice:
    def __init__(self, provider: str, voice: str, model: str):
        self.provider = provider
        self.voice = voice
        self.model = model

class PhoneNumberConfig:
    def __init__(self, phone_number: str, account_sid: str, auth_token: str, label: str):
        self.phone_number = phone_number
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.label = label
        self.assigned_assistant = None  # Tipo: Assistant, inicialmente None

class PhoneNumberManager:
    def __init__(self):
        self.phone_numbers = []

    def add_phone_number(self, config: PhoneNumberConfig):
        self.phone_numbers.append(config)

    def get_phone_number(self, phone_number: str) -> PhoneNumberConfig:
        for config in self.phone_numbers:
            if config.phone_number == phone_number:
                return config
        raise ValueError("Phone number not found")

    def remove_phone_number(self, phone_number: str):
        config = self.get_phone_number(phone_number)
        self.phone_numbers.remove(config)

    def assign_assistant(self, phone_number: str, assistant: 'Assistant'): # type: ignore
        config = self.get_phone_number(phone_number)
        config.assigned_assistant = assistant

    def unassign_assistant(self, phone_number: str):
        config = self.get_phone_number(phone_number)
        config.assigned_assistant = None
