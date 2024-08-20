import unittest
from config import Model, Transcriber, Voice, PhoneNumberConfig, PhoneNumberManager
from asistant import Assistant

class TestModel(unittest.TestCase):
    def test_model_initialization(self):
        model = Model("Hello", "provider_a", "model_x", "system_prompt")
        self.assertEqual(model.first_message, "Hello")
        self.assertEqual(model.provider, "provider_a")
        self.assertEqual(model.model, "model_x")
        self.assertEqual(model.system_prompt, "system_prompt")

class TestTranscriber(unittest.TestCase):
    def test_transcriber_initialization(self):
        transcriber = Transcriber("provider_b", "en", "model_y")
        self.assertEqual(transcriber.provider, "provider_b")
        self.assertEqual(transcriber.lang, "en")
        self.assertEqual(transcriber.model, "model_y")

class TestVoice(unittest.TestCase):
    def test_voice_initialization(self):
        voice = Voice("provider_c", "voice_a", "model_z")
        self.assertEqual(voice.provider, "provider_c")
        self.assertEqual(voice.voice, "voice_a")
        self.assertEqual(voice.model, "model_z")

class TestPhoneNumberConfig(unittest.TestCase):
    def test_phone_number_config_initialization(self):
        config = PhoneNumberConfig("+1234567890", "sid_123", "token_123", "My Label")
        self.assertEqual(config.phone_number, "+1234567890")
        self.assertEqual(config.account_sid, "sid_123")
        self.assertEqual(config.auth_token, "token_123")
        self.assertEqual(config.label, "My Label")
        self.assertIsNone(config.assigned_assistant)

class TestPhoneNumberManager(unittest.TestCase):
    def test_phone_number_manager(self):
        manager = PhoneNumberManager()
        config = PhoneNumberConfig("+1234567890", "sid_123", "token_123", "My Label")
        manager.add_phone_number(config)
        self.assertEqual(len(manager.phone_numbers), 1)

        fetched_config = manager.get_phone_number("+1234567890")
        self.assertEqual(fetched_config, config)

        manager.remove_phone_number("+1234567890")  # Assuming this method exists
        self.assertEqual(len(manager.phone_numbers), 0)

class TestAssistant(unittest.TestCase):
    def test_assistant_initialization(self):
        model = Model("Hello", "provider_a", "model_x", "system_prompt")
        transcriber = Transcriber("provider_b", "en", "model_y")
        voice = Voice("provider_c", "voice_a", "model_z")
        phone_manager = PhoneNumberManager()
        assistant = Assistant(model, transcriber, voice, phone_manager)

        self.assertEqual(assistant.model, model)
        self.assertEqual(assistant.transcriber, transcriber)
        self.assertEqual(assistant.voice, voice)
        self.assertEqual(assistant.phone_manager, phone_manager)

    def test_assign_unassign_phone_number(self):
        phone_manager = PhoneNumberManager()
        model = Model("Hello", "provider_a", "model_x", "system_prompt")
        transcriber = Transcriber("provider_b", "en", "model_y")
        voice = Voice("provider_c", "voice_a", "model_z")
        assistant = Assistant(model, transcriber, voice, phone_manager)

        config = PhoneNumberConfig("+1234567890", "sid_123", "token_123", "My Label")
        phone_manager.add_phone_number(config)

        assistant.assign_phone_number("+1234567890")
        self.assertEqual(config.assigned_assistant, assistant)

        assistant.unassign_phone_number("+1234567890")
        self.assertIsNone(config.assigned_assistant)

if __name__ == '__main__':
    unittest.main()
