import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

dic = {row.letter: row.code for (index, row) in data.iterrows()}

name_wrong = True
while name_wrong:
    try:
        user_name = input("Enter your name: ").upper()
        result = [dic[let] for let in user_name]

    except KeyError:
        print("Your name only contains letters, doesn't it?")

    else:
        name_wrong = False
        print(result)
