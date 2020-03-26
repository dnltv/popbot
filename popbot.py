import telebot
from config import TG_TOKEN


bot = telebot.TeleBot(TG_TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Услуги 🤝', 'Стоимость💰', 'Сроки⏳', 'Контакты☎', 'Инфо📣')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте!🙌 Вы попали на страничку телеграм-бота оценщика Попова Ильи Александровича. Нажмите кнопку внизу диалога и выберите, что конкретно Вас интересует👇👇👇', reply_markup=keyboard1)


services = ['услуги 🤝','услуги','направления']
price = ['стоимость💰', 'стоимость', 'цена', 'цены', 'прайс', 'price', 'стоимость услуг', 'цена на услуги', 'цена за услуги']
deadlines = ['сроки⏳', 'сроки',]
contacts = ['контакты☎', 'контакты', 'contact', 'contacts']
info = ['инфо📣', 'инфо', 'информация', 'info', 'information', 'help', '/help', '\help']
phone_num = ['тел', 'телефон', 'номер', 'номер телефона', 'контактный телефон', 'контактный номер', 'контактный номер телефона', 'phone', 'phone number', 'contact phone', 'contact num', 'contact number', 'number']
mail = ['почта', 'адрес почты', 'адрес электронной почты', 'электронная почта', 'mail', 'mail adress', 'email', 'e-mail']
site = ['сайт', 'вебсайт', 'веб-сайт', 'адрес сайта', 'адрес вебсайта', 'адрес веб-сайта', 'site', 'website', 'web-site']
adress = ['адрес', 'адрес офиса', 'офис', 'adress', 'adres', 'office', 'ofice']
work_time = ['время', 'время работы', 'режим', 'режим работы', 'график', 'график работы', 'рабочее время', 'рабочие часы', 'time', 'deadlines', 'working time']
tnx = ['спасибо', 'большое спасибо', 'спасибо большое' 'спасибо тебе', 'спс', 'благодарю', 'от души', 'tnx', 'thx', 'thanks', 'thank you']
bye = ['пока', 'прощай', 'до свидания', 'досвидания', 'bye', 'bye-bye', 'goodbye', 'good bye']
hello = ['привет', 'пт', 'прив', 'салют','здравствуй', 'здравствуйте', 'приветствую']
insult = ['дурак', 'придурок', 'тупой', 'чмо', 'болван', 'дебил', 'урод']

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() in services:
        bot.send_message(message.chat.id, '🤝 Оценщик Попов Илья Александрович предоставляет следующие услуги: \n\n🏬🚙Оценка недвижимого и движимого имущества;\n\n🏦Оценка бизнеса; \n\n📈Оценка убытков; \n\n🧾Оценка ценных бумаг; \n\n🗺Оспаривание кадастровой стоимости; \n\n👨‍🎓Оценка нематериальных активов и объектов интеллектуальной собственности; \n\n⚖Судебная экспертиза.')
    elif message.text.lower() in price:
        bot.send_message(message.chat.id, '💰Стоимость стандартных услуг по оценке: \n\n🏠Квартира 2500 руб. ; \n\n🏡Дом 7000 руб. ; \n\n🏢Коммерческая недвижимость от 7000 руб. ; \n\n💻Оборудование от 1000 руб.; \n\n🚘Транспортные средства от 2000 руб. ; \n\n🏭Стоимость предприятия от 40000 руб. ; \n\n👨‍🎓Нематериальные активы и объекты интеллектуальной собственности от 20000 руб. \n\nДля более подробной информации позвоните по телефону 📞 +79194944233, либо напишите на почту 📧 popov27111987@gmail.com')
    elif message.text.lower() in deadlines:
        bot.send_message(message.chat.id, '⏳Стандратные сроки оценки: \n\n🏠Квартира 1-2 дня; \n\n🏡Дом до 3х дней; \n\n🏢Коммерческая недвижимость до 3х дней; \n\n💻Оценка оборудования до 2х дней; \n\n🚘Оценка транспортных средств до 3х дней; \n\n🏭Оценка предприятий - по согласованию; \n\n👨‍🎓Оценка интеллектуальных и иных прав - по согласованию. \n\nДля более подробной информации позвоните по телефону 📞 +79194944233, либо напишите на почту 📧 popov27111987@gmail.com')
    elif message.text.lower() in contacts:
        bot.send_message(message.chat.id, '☎ Телефон для связи: +79194944233. \n\n📧Адрес электронной почты: popov27111987@gmail.com. \n\n🖥Сайт: http://appraise.tilda.ws')
    elif message.text.lower() in info:
        bot.send_message(message.chat.id, '✍ Просто введите команду(слово) по интересующей Вас теме и я предоставлю информацию! \n\nНапример: услуги, стоимость, сроки, контакты, номер, адрес, почта. \n\nЛибо нажмите на значок, расположенный справа в строке ввода👇')
    elif message.text.lower() in phone_num:
        bot.send_message(message.chat.id, '📞 +79194944233')
    elif message.text.lower() in mail:
        bot.send_message(message.chat.id, '📧 popov27111987@gmail.com')
    elif message.text.lower() in site:
        bot.send_message(message.chat.id, '🖥 http://appraise.tilda.ws')
    elif message.text.lower() in adress:
        bot.send_message(message.chat.id, '🏙 г. Пермь, ул. Мира 11')
    elif message.text.lower() in work_time:
        bot.send_message(message.chat.id, '⏰ Режим работы: пн-пт c 10:00 до 18:00')
    elif message.text.lower() in hello:
        bot.send_message(message.chat.id, 'Приветствую Вас ещё раз!🤚')
    elif message.text.lower() in bye:
        bot.send_message(message.chat.id, 'Всего хорошего! Обращайтесь ещё 😉')
    elif message.text.lower() in tnx:
        bot.send_message(message.chat.id, 'Не за что, я всего лишь выполняю свою работу!🤗')
    elif message.text.lower() in insult:
        bot.send_message(message.chat.id, '\nНе понимаю, почему Вы так решили!🤔 \n\nЯ всего лишь чат-бот!')
   
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    else :
        bot.send_message(message.chat.id, 'Прошу прощения, я Вас не понимаю🤔 Введите "инфо" , чтобы увидеть список доступных команд.')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()