from config import Model, Transcriber, Voice, PhoneNumberConfig, PhoneNumberManager
from asistant import Assistant

def main():
    # Crear instancias de configuración
    model = Model("Hello", "OpenAI", "GPT-4", "system_prompt")
    transcriber = Transcriber("Deepgram", "en", "transcriber_model")
    voice = Voice("Azure", "voice_name", "voice_model")
    phone_manager = PhoneNumberManager()
    
    # Crear un asistente
    assistant = Assistant(model, transcriber, voice, phone_manager)
    
    # Crear y agregar un número de teléfono
    phone_config = PhoneNumberConfig("+1234567890", "sid_123", "token_123", "My Label")
    phone_manager.add_phone_number(phone_config)
    
    # Asignar el asistente al número de teléfono
    assistant.assign_phone_number("+1234567890")
    
    # Imprimir el asistente con todos sus datos
    print("\n--- Assistant ---")
    print(assistant)
    
    print("\n--- Phone Number Manager ---")
    print(phone_config.account_sid)

if __name__ == "__main__":
    main()
