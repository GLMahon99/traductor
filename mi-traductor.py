
#traductor de ingles a español utilzando googletrans
from googletrans import Translator

# Crear un objeto traductor
translator = Translator()

# Pedir al usuario que seleccione el idioma de destino
select_lang_translate = input('Selecciona el idioma de destino (por ejemplo, "es" para español, "en" para inglés, "fr" para francés): ')

# Texto en inglés a traducir
text_to_translate = input('Ingresa el texto a traducir: ')

# Traducir al idioma seleccionado
translated_text = translator.translate(text_to_translate, dest=select_lang_translate)

# Imprimir el texto traducido
print(f"Texto original: {text_to_translate}")
print(f"Texto traducido ({select_lang_translate}): {translated_text.text}")
