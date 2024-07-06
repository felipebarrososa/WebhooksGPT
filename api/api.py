from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configure a API key do OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Extrair a mensagem do lead
    user_message = data.get('message')

    # Enviar a mensagem para o GPT
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=150
    )

    # Extrair a resposta do GPT
    gpt_response = response.choices[0].text.strip()

    # Retornar a resposta em formato JSON
    return jsonify({"response": gpt_response})

if __name__ == '__main__':
    app.run(port=5000)
