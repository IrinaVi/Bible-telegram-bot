import os
import telebot
from telebot import types
from freebible import read_web
import re
import random

web = read_web()

dkt = {'Genesis': {'abbr': 'Gen', 'chapters_number': 50}, 'Leviticus': {'abbr': 'Lev', 'chapters_number': 27}, '1Chronicles': {'abbr': '1 Chron', 'chapters_number': 29}, 'Deuteronomy': {'abbr': 'Deut', 'chapters_number': 34}, 'Judges': {'abbr': 'Judg', 'chapters_number': 21}, '1Samuel': {'abbr': '1 Sam', 'chapters_number': 31}, '1Kings': {'abbr': '1 Kgs', 'chapters_number': 22}, 'Ezra': {'abbr': 'Ezra', 'chapters_number': 10}, 'Esther': {'abbr': 'Esth', 'chapters_number': 10}, 'Psalms': {'abbr': 'Pslm', 'chapters_number': 150}, 'Ecclesiastes': {'abbr': 'Eccles', 'chapters_number': 12}, 'Jeremiah': {'abbr': 'Jer', 'chapters_number': 52}, 'Daniel': {'abbr': 'Dan', 'chapters_number': 12}, 'Joel': {'abbr': 'Joel', 'chapters_number': 3}, 'Jonah': {'abbr': 'Jnh', 'chapters_number': 4}, 'Nahum': {'abbr': 'Nah', 'chapters_number': 3}, 'Zephaniah': {'abbr': 'Zeph', 'chapters_number': 3}, 'Exodus': {'abbr': 'Exo', 'chapters_number': 40}, 'Numbers': {'abbr': 'Num', 'chapters_number': 36}, 'Joshua': {'abbr': 'Josh', 'chapters_number': 24}, 'Ruth': {'abbr': 'Rth', 'chapters_number': 4}, '2Samuel': {'abbr': '2 Sam', 'chapters_number': 24}, '2Kings': {'abbr': '2 Kgs', 'chapters_number': 25}, '2Chronicles': {'abbr': '2 Chron', 'chapters_number': 36}, 'Nehemiah': {'abbr': 'Neh', 'chapters_number': 13}, 'Job': {'abbr': 'Job', 'chapters_number': 42}, 'Proverbs': {'abbr': 'Prov', 'chapters_number': 31}, 'Song of Songs': {'abbr': 'Song', 'chapters_number': 8}, 'Isaiah': {'abbr': 'Isa', 'chapters_number': 66}, 'Lamentations': {'abbr': 'Lam', 'chapters_number': 5}, 'Ezekial': {'abbr': 'Ezek', 'chapters_number': 48}, 'Hosea': {'abbr': 'Hos', 'chapters_number': 14}, 'Amos': {'abbr': 'Amos', 'chapters_number': 9}, 'Micah': {'abbr': 'Micah', 'chapters_number': 7}, 'Habakkuk': {'abbr': 'Hab', 'chapters_number': 3}, 'Haggai': {'abbr': 'Haggai', 'chapters_number': 2}, 'Malachi': {'abbr': 'Mal', 'chapters_number': 4}, 'Obadiah': {'abbr': 'Obad', 'chapters_number': 1}, 'Zechariah': {'abbr': 'Zech', 'chapters_number': 14}, 'Matthew': {'abbr': 'Matt', 'chapters_number': 28}, 'Mark': {'abbr': 'Mrk', 'chapters_number': 16}, 'Luke': {'abbr': 'Luk', 'chapters_number': 24}, 'John': {'abbr': 'John', 'chapters_number': 21}, 'Acts': {'abbr': 'Acts', 'chapters_number': 28}, 'Romans': {'abbr': 'Rom', 'chapters_number': 16}, '1Corinthians': {'abbr': '1 Cor', 'chapters_number': 16}, '2Corinthians': {'abbr': '2 Cor', 'chapters_number': 13}, 'Galatians': {'abbr': 'Gal', 'chapters_number': 6}, 'Ephesians': {'abbr': 'Ephes', 'chapters_number': 6}, 'Philippians': {'abbr': 'Phil', 'chapters_number': 4}, 'Colossians': {'abbr': 'Col', 'chapters_number': 4}, '1Thessalonians': {'abbr': '1 Thess', 'chapters_number': 5}, '2Thessalonians': {'abbr': '2 Thess', 'chapters_number': 3}, '1Timothy': {'abbr': '1 Tim', 'chapters_number': 6}, '2 Timothy': {'abbr': '2 Tim', 'chapters_number': 4}, 'Titus': {'abbr': 'Titus', 'chapters_number': 3}, 'Philemon': {'abbr': 'Philem', 'chapters_number': 1}, 'Hebrews': {'abbr': 'Hebrews', 'chapters_number': 13}, 'James': {'abbr': 'James', 'chapters_number': 5}, '1Peter': {'abbr': '1 Pet', 'chapters_number': 5}, '2Peter': {'abbr': '2 Pet', 'chapters_number': 3}, '1John': {'abbr': '1 John', 'chapters_number': 5}, '2John': {'abbr': '2 John', 'chapters_number': 1}, '3John': {'abbr': '3 John', 'chapters_number': 1}, 'Jude': {'abbr': 'Jude', 'chapters_number': 1}, 'Revelation': {'abbr': 'Rev', 'chapters_number': 22}}
list_of_books = ['Genesis', 'Leviticus', '1Chronicles', '2Chronicles', 'Deuteronomy', 'Judges', '1Samuel', '2Samuel', '1Kings', '2Kings', 'Ezra', 'Esther',
                 'Psalms', 'Ecclesiastes', 'Jeremiah', 'Daniel', 'Joel', 'Jonah', 'Nahum', 'Zephaniah', 'Exodus', 'Numbers',
                 'Joshua', 'Ruth', 'Nehemiah', 'Job', 'Proverbs', 'Song of Songs', 'Isaiah',
                 'Lamentations', 'Ezekial', 'Hosea', 'Amos', 'Micah', 'Habakkuk', 'Haggai', 'Malachi', 'Obadiah', 'Zechariah',
                 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1Corinthians', '2Corinthians', 'Galatians', 'Ephesians',
                 'Philippians', 'Colossians', '1Thessalonians', '2Thessalonians', '1Timothy', '2Timothy', 'Titus', 'Philemon',
                 'Hebrews', 'James', '1Peter', '2Peter', '1John', '2John', '3John', 'Jude', 'Revelation']

API_KEY = os.environ['TELEGRAM_API']

#create bot:
bot = telebot.TeleBot(API_KEY)

#KEY - FIRST STEP, SEND LIST OF BOOKS
@bot.message_handler(commands=['Bible', 'Back'])
def send_book(msg):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn_verse = types.KeyboardButton("/Verse")
    markup.add(btn_verse)
    for key,value in dkt.items():
        btn = types.KeyboardButton(f"/{key}")
        markup.add(btn)
    bot.send_message(chat_id=msg.chat.id, text="Choose which book you would like to read or Verse for random Verse:", reply_markup=markup)

@bot.message_handler(commands=["Verse"])
def random_verse(msg):
    random_chapter_name = random.choice(list_of_books)
    abbreviation = dkt[random_chapter_name]['abbr']
    chapter_number = random.randint(1,dkt[random_chapter_name]['chapters_number'])
    verses_number = len(web[abbreviation][chapter_number])
    random_verse_number = random.randint(1,verses_number)
    random_verse = web[abbreviation][chapter_number][random_verse_number]
    bot.send_message(chat_id=msg.chat.id, text=random_verse)


#SEND LIST OF BOOKS WITH CHAPTERS
@bot.message_handler(commands=list_of_books)
def send_chapter_numbers(msg):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    inter = msg.text
    chapter = inter.replace("/","")
    number_of_chapters = dkt[chapter]['chapters_number']
    back_btn = types.KeyboardButton("/Back")
    markup.add(back_btn)
    for n in range(1, number_of_chapters+1):
        btn = types.KeyboardButton(f"/{chapter}, {n}")
        markup.add(btn)
    bot.send_message(chat_id=msg.chat.id, text="Choose chapter to read or press Back", reply_markup=markup)

#SEND NEXT PART. NEXT SHOULD BE WIHOUT SLASH
@bot.message_handler(content_types=['text'])
def send_next_chapter(msg):
    if re.search(r"^NEXT\W", msg.text):
        message = msg.text.replace("/", "").split(",")
        abbriviation = message[1]
        chapter_number = int(message[2])
        count = int(message[3])
        chapter_length = len(web[abbriviation][chapter_number])
        current_chapter = ""
        for i in range(count+1,count+5):
            if i > chapter_length:
                break
            else:
                current_chapter += str(web[abbriviation][chapter_number][i])

        bot.send_message(msg.chat.id, current_chapter)

        if i > chapter_length:
            send_book(msg)

        else:
            markup = types.ReplyKeyboardMarkup(row_width=1)
            btn = types.KeyboardButton(f"NEXT,{abbriviation},{chapter_number},{i}")
            back_btn = types.KeyboardButton("/Back")
            markup.add(btn)
            markup.add(back_btn)
            bot.send_message(chat_id=msg.chat.id, text="Press Next to read next part or go back", reply_markup=markup)

    else:
        message = msg.text.replace("/","").split(",")

        chapter_number = int(message[1].strip())
        chapter_name = message[0].strip()
        abbriviation = dkt[chapter_name]['abbr']

        chapter_length = len(web[abbriviation][chapter_number])

        current_chapter = ""
        for i in range(1,5):
            if i > chapter_length:
                break
            else:
                current_chapter += str(web[abbriviation][chapter_number][i])

        bot.send_message(msg.chat.id, current_chapter)

        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn = types.KeyboardButton(f"NEXT,{abbriviation},{chapter_number},{i}")
        back_btn = types.KeyboardButton("/Back")
        markup.add(btn)
        markup.add(back_btn)
        bot.send_message(chat_id=msg.chat.id, text="Press Next to read next part or go back", reply_markup=markup)

#make the bot listen:
bot.polling(none_stop=True)

