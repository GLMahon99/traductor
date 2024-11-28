
#traductor de ingles a español utilzando googletrans

from googletrans import Translator

# Crear un objeto traductor
translator = Translator()

# Texto en inglés a traducir
text_to_translate = input('ingresa texto a traducir: ')

# Traducir al español
translated_text = translator.translate(text_to_translate, src='en', dest='es')

# Imprimir el texto traducido
print(f"Texto en inglés: {text_to_translate}")
print(f"Texto en español: {translated_text.text}")