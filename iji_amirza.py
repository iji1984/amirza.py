# iji(irajpooladvand@gmail.com)
import os
import sqlite3
from itertools import permutations
# اگر فایل کلمات در مسیر جاری وجود داشته باشه حدف میکنه
if os.path.exists("amirza_words.txt"):
    os.remove("amirza_words.txt")
# فایل دیتابیس کلمات فارسی رو لوود میکنه و داخل لیست کلمات فارسی میریزه
db = 'persian_word.db'
con = sqlite3.connect(db)
cur = con.cursor()
cur.execute('SELECT entry FROM mdx')
rows = cur.fetchall()
persian_words = []
for row in rows:
    persian_words.append(row[0])

# فانکشن برای جدا کردن تمام حروف بهم چسبیده و تبدیل به تمام حالتهای ممکن با تابع permutations
def word_separator(word, i):
    word_list = []
    for w in word:
        word_list.append(w)
    word_list = list(permutations(word_list, i))
    return word_list

# فانکشن برای تبدیل لیست به رشته
def list2word(user_list):
    counter = 0
    output_list = []
    for c in range(len(user_list)):
        if ("".join(user_list[c])) in persian_words and ("".join(user_list[c])) not in output_list:
            output_list.append("".join(user_list[counter]))
        counter += 1
    return output_list

# فانکشن برای تبدیل الف به آ
def capital_letters(s):
    s = s.replace('ا', 'آ')
    return s

# فانکشن برای شمردن طول کلمه وارد شده
def check_len_user(user_c):
    return len(user_c)

# گرفتن ورودی از کاربر و جستجو در دیتابیس و در صورت وجود داشتن اضافه کردن به فایل آمیرزا تکست
user_character = input('enter your characters please : ')
if 'ا' in user_character:
    count = check_len_user(user_character)
    while count > 2:
        user_character_separator = (word_separator(capital_letters(user_character), count))
        with open("amirza_words.txt", "a") as f:
            print(list2word(user_character_separator), file=f)
            print(140 * "*", "\n", file=f)
        count -= 1

count = check_len_user(user_character)
while count > 2:
    user_character_separator = word_separator(user_character, count)
    with open("amirza_words.txt", "a") as f:
        print(list2word(user_character_separator), file=f)
        print(140 * "*", "\n", file=f)
    count -= 1
