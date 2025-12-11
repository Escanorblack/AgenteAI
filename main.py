import google.generativeai as genai
import sys

API_KEY ="AIzaSyDKNb1pNPhxkJyxO3n3-7kpXdBiAsFMNDs"

try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    print(f"Erro na configuração da API: {e}")
    sys.exit(1)

    print("Iniciando o AI")

try:
    model = genai.GenerativeModel(model_name="gemini-2.5-flash")
except Exception as e:
    print(f"Erro ao inicializar o modelo: {e}")
    sys.exit(1)

print("Gerando o Conteudo ......")
response = model.generate_content (input("Digite sua pergunta para o AI: "))

print("\n --- Resposta do AI ---")
print(response.text)
print("----------")