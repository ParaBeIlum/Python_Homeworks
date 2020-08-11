import random
from colorama import init
init(autoreset=True)


class Bcolors:
    GN = '\033[32m'  # green
    Y = '\033[93m'  # yellow
    R = '\033[91m'  # red

# encoder
list_encoder = '''%Ёеуъ? 2v#;<\9}иЧRЯfA№e4УАЖn|=ёюя`ИLBНМ_ЪC0~ZwIHбпr'cbdqдgзВ"$Dэlхй,С-XF{Os(:БTжГ6zшЬJьkрpKEШЮХ]uGнЩ[YДQРт)W5N8U.7фxФ/ЛV!чiS1tЕТ3мjоЗmг^aвЭщPцскКПО&hMыа@yлЙoЦ+>*Ы'''
# encoder2
list_encoder2 = '''豸果禾申若念页祭瓜鸟龟足守电麦危幸曲実委用苦玄走武州巻立直虍捨网表岸各釆印担枚耒皮玉甩底瓦具述取而羊肉糸承因在艮性缶赤生考採並老長豕至甲机矛官向効府周件制版穴協板舌済定臼参宝石居波自角貝泣成呼共行令刷枝昔玊交白宇受岩法舟西龙季拝甘乳存襾耳再固艸宙血見聿次里治灰婦目身非禸田司米放宅妻衣刻由卒羽争邑供寺招的全券式舛虫酉毒宿届河'''
# list_encoder3
list_encoder3 = '''表昔龙石各守交枝具刻邑次瓦赤穴州周委協見担曲婦豸羽艮司危寺立府玄券参宝釆页的受乳武宅印呼玉艸在自岸令非老甩述実甲河波法皮糸由成宇白鸟虫虍麦舌申网定固制聿取甘妻宙幸巻缶岩龟承禸直存放生襾供豕共治舟身衣全泣貝耒官耳再刷矛走向果目玊若舛効考用念版电苦式机並長西居足酉羊性灰肉血瓜季臼件拝届毒里至禾米而争枚招行卒因角板底田祭採済捨宿'''
# encoder4
list_encoder4 = '''向米里存糸禾苦果次玉招成巻周届酉非卒河乳承禸定宇治述曲白供司老念目豕式波刻実羊泣府法瓜武舌釆网版玊聿石襾舟直具宅採再角妻虍毒缶血争鸟刷衣行寺官虫肉甘板長因危取耒印底協在足岩西自済臼豸季皮制甩艸龙龟矛考艮昔瓦見受用宿身各居邑祭並枝拝若走申全捨放岸由令舛呼电委券宝幸生担宙表穴効枚交机玄甲性赤件共耳立羽的麦而州婦灰貝至守固页参田'''

# new key
def key():
    w = list_encoder
    q = ''.join(random.sample(w, len(w)))
    print('')
    print(Bcolors.GN + q)

def enc():
    while True:
        b = input('\n' + 'Введите текст для encoder: '+'\n')
        if b == '':
            print(Bcolors.R + "Ничего не введено!")
            continue

        h = b + list_encoder
        if len(list_encoder) != len(set(h)):
            print(Bcolors.R + 'Символы в ключе не найдены!')
            continue
        print(Bcolors.GN + '\n' + 'Зашифрованный текст:' + '\n')

        i = 1
        for c in b:
            encoder = ''
            y = list_encoder.index(c)
            if i % 3 == 0:
                encoder += list_encoder4[y]
            elif i % 2 == 0:
                encoder += list_encoder3[y]
            else:
                encoder += list_encoder2[y]
            i += 1
            print(encoder, end="")
        break

def dec():
    while True:
        m = input('\n' + 'Введите текст для decoder: '+'\n')
        if m == '':
            print(Bcolors.R + "Ничего не введено!")
            continue

        t = m + list_encoder2
        if len(list_encoder2) != len(set(t)):
            print(Bcolors.R + 'Символы в ключе не найдены!')
            continue
        print(Bcolors.GN + '\n' + 'Расшифрованный текст:' + '\n')

        i = 1
        for x in m:
            decoder = ''
            if i % 3 == 0:
                y = list_encoder4.index(x)
                decoder += list_encoder[y]
            elif i % 2 == 0:
                y = list_encoder3.index(x)
                decoder += list_encoder[y]
            else:
                y = list_encoder2.index(x)
                decoder += list_encoder[y]
            i += 1
            print(decoder, end="")
        break

while True:
    text_vybor = input('Выберите действие:'+'\n')
    if text_vybor == "1":
        enc()
        break
    elif text_vybor == "2":
        dec()
        break
    elif text_vybor == "3":
        key()
        break
    elif text_vybor == "4":
        readme()
        break
    else:
        print(Bcolors.R + "Введите 1,2,3 или 4!")

print(Bcolors.Y + "\n\nДля выхода нажмите Enter")
input()

