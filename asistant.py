from config import Model, Transcriber, Voice, PhoneNumberManager

class Assistant:
    def __init__(self, model: Model, transcriber: Transcriber, voice: Voice, phone_manager: PhoneNumberManager):
        self.model = model
        self.transcriber = transcriber
        self.voice = voice
        self.phone_manager = phone_manager

    def assign_phone_number(self, phone_number: str):
        config = self.phone_manager.get_phone_number(phone_number)
        config.assigned_assistant = self

    def unassign_phone_number(self, phone_number: str):
        config = self.phone_manager.get_phone_number(phone_number)
        config.assigned_assistant = None

    def __repr__(self):
        return (f"Assistant(model={self.model!r}, transcriber={self.transcriber!r}, "
                f"voice={self.voice!r}, phone_manager={self.phone_manager!r})")
