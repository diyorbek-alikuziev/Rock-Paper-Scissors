import random
from art import rock, paper, scissors
print("Tosh-qog'oz-qaychi o'yiniga xush kelibsiz!")
img = [rock, paper, scissors]
you = int(input("Qaysi birini tanlaysiz? iltimos raqam kiriting: tosh(0) qog'oz(1) qaychi(2): "))
komputer = random.randint(0, 2)
while you > 2 or you < 0:
  you = int(input("Siz qoidani buzdingiz, qayta kiriting: "))
if you == 0 and komputer == 2:
  print(f"Siz toshni tanladingiz: {rock}kompyuter esa qaychini tanladi: {scissors}siz yutdingiz.")
elif you == 2 and komputer == 0:
  print(f"Siz qaychini tanladingiz: {scissors}kompyuter esa toshni tanladi: {rock}siz yutqazdingiz.")
elif you > komputer:
  if you == 1:
    print(f"Siz qog'ozni tanladingiz: {paper}kompyuter esa toshni tanladi: {rock}siz yutdingiz.")
  else:
    print(f"Siz qaychini tanladingiz: {scissors}kompyuter esa toshni tanladi: {paper}siz yutdingiz.")
elif you < komputer:
  if you == 0:
    print(f"Siz toshni tanladingiz: {rock}kompyuter esa qog'ozni tanladi: {paper}siz yutqazdingiz.")
  else:
    print(f"Siz qog'ozni tanladingiz: {paper}kompyuter esa qaychini tanladi: {scissors}siz yutqazdingiz.")
else:
  if you == 0:
    print(f"Siz toshni tanladingiz: {rock}kompyuter ham toshni tanladi: {rock}durrang.")
  elif you == 1:
    print(f"Siz qog'ozni tanladingiz: {paper}kompyuter ham qog'ozni tanladi: {paper}durrang.")
  else:
    print(f"Siz qaychini tanladingiz: {scissors}kompyuter ham qaychini tanladi: {scissors}durrang.")
