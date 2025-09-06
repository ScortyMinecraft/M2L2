import telebot
import random
import os
import requests
from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)

# Наш банк заданий
TASKS = [
    "Сдай 10 батареек в специальный пункт приема. 🔋",
    "Сдай 5 пластиковых бутылок на переработку. ♻️",
    "Купи продукты сегодня без одноразового пластикового пакета. 🛍️",
    "Приготовь домашнее средство для уборки (из уксуса или соды). 🧼",
    "Откажись от одноразовой трубочки в кафе или купи многоразовую. 🥤",
    "Найди ближайший контейнер для сбора стекла и сдай туда бутылки. 🍾",
    "Потрать 15 минут, чтобы разобрать небольшой ящик с макулатурой. 📦",
    "Купи хотя бы один овощ/фрукт без упаковки на развес. 🍎",
    "Используй обе стороны листа бумаги при печати или рисовании. 📄",
    "Почини одну сломанную вещь вместо того, чтобы выбрасывать. 🛠️"
]

# Список похвал и достижений
ACHIEVEMENTS = [
    "Ты — супергерой планеты! 🌍✨",
    "Мастер экологичности! 🏆",
    "Повелитель переработки! ♻️👑",
    "Защитник природы! 🌿🛡️",
    "Эко-легенда! 🤩",
    "Ты делаешь мир чище! 💫",
    "Великий избавитель от мусора! 🗑️⚡",
]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
Привет! 🌱 Я экологичный бот, который даёт задание! За выполнение заданий я даю тебе достижение)

Вот что я умею:
/task - Получить случайное экозадание
/done - Сообщить о выполнении задания
/mission - Узнать о нашей миссии
/refuse - Отказаться от задания (я бы не советовал это делать)

Просто напиши мне что-нибудь! 😊
    """
    bot.reply_to(message, welcome_text)

# Обработчик команды /task
@bot.message_handler(commands=['task'])
def give_task(message):
    random_task = random.choice(TASKS)
    task_message = f"🚀 Твое задание на сегодня:\n\n{random_task}\n\nНапиши мне 'сделал' когда выполнишь!"
    bot.reply_to(message, task_message)

# Обработчик команды /done
@bot.message_handler(commands=['done'])
def task_done(message):
    random_praise = random.choice(ACHIEVEMENTS)
    celebration_message = f"""
🎉 Поздравляю! Задание выполнено!

{random_praise}

Ты стал на шаг ближе к экологичному образу жизни! 🌟

Хочешь еще задание? Напиши /task
    """
    bot.reply_to(message, celebration_message)

# Обработчик команды /mission
@bot.message_handler(commands=['mission'])
def send_mission(message):
    mission_text = """
Наша миссия: 🌍
Помогать людям небольшими шагами уменьшать количество отходов.
Каждое маленькое действие имеет значение!
Вместе мы можем сделать планету чище. 💚
    """
    bot.reply_to(message, mission_text)

@bot.message_handler(commands=['refuse'])
def send_refuse(message):
    refuse_text = """
Ах ты негодяй! Грешник! НЕ ПОРТЬ ПЛАНЕТУ!!! ПОЗАБОТЬСЯ О МИРЕ И ОКРУЖАЮЩЕЙ СРЕДЕ!!!
    """
    bot.reply_to(message, refuse_text)

# Обработчик обычных текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_text = message.text.lower()
    
    if any(word in user_text for word in ['привет', 'hello', 'hi', 'start']):
        send_welcome(message)
    elif any(word in user_text for word in ['задание', 'задачу', 'task', 'что делать']):
        give_task(message)
    elif any(word in user_text for word in ['сделал', 'выполнил', 'готово', 'done', 'готов', 'успех']):
        task_done(message)
    elif any(word in user_text for word in ['миссия', 'цель', 'mission']):
        send_mission(message)
    elif any(word in user_text for word in ['не выполнил', 'цель не выполнена', 'не хочу', 'отказ','фу']):
        send_refuse(message)
    else:
        bot.reply_to(message, "Не понял тебя 😊 Напиши /task для задания или /done когда выполнишь!")

bot.polling()
