import openai

# OpenAI API keyni o'rnatamiz
openai.api_key = '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'

# Foydalanayotgan modelni aniqlaymiz
engine = 'text-davinci-002'

# Suhbatlashish funksiyasini yaratamiz
def chat_with_gpt(prompt):  
    # GPT-3 API orqali suhbatlashamiz
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=60, # ko'proq so'zlar uchun qiymatni o'zgartiramiz
        n=1,
        stop="-EOF-", # to'xtatish belgisini qo'yamiz
        temperature=0.7, # javobning yorqinligini o'zgartiramiz
    )

    # API javobini olish
    message = response.choices[0].text
    return message.strip()

# Foydalanuvchidan keladigan savollarni qabul qilish
while True:
    prompt = input('Siz: ')

    # Suhbatlashish funksiyasini chaqirib, javobni olish
    response = chat_with_gpt(prompt)

    # GPT-3 javobini chiqaramiz
    print('AI: ' + response)

