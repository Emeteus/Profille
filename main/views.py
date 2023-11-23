import random
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


def index(request):
    singers = [
        {'id': 1, 'codde': 'сoldplay', 'name': 'Coldplay', 'genre': 'Рок', 'lead_singers': 'Кріс Мартін',
         'followers': '25,5 млн.'},

        {'id': 2, 'codde': 'queen', 'name': 'Queen', 'genre': 'Рок', 'lead_singers': 'Фредді Меркюрі',
         'followers': '40 млн.'},

        {'id': 3, 'codde': 'the-beatles', 'name': 'The Beatles', 'genre': 'Рок', 'lead_singers': 'Джон Леннон',
         'followers': '38 млн.'},

        {'id': 4, 'codde': 'twenty-one-pilots', 'name': 'Twenty One Pilots', 'genre': 'Реп',
         'lead_singers': 'Тайлер Джозеф', 'followers': '8,6 млн.'},

        {'id': 5, 'codde': 'exo', 'name': 'Exo', 'genre': 'K-pop', 'lead_singers': ' Сю Ман', 'followers': '10,8 млн.'},

        {'id': 6, 'codde': 'maroon5', 'name': 'Maroon 5', 'genre': 'Поп-рок', 'lead_singers': 'Адам Левін',
         'followers': '8,8 млн.'},

        {'id': 7, 'codde': 'imagine-dragons', 'name': 'Imagine Dragons', 'genre': 'Iнді-рок',
         'lead_singers': 'Ден Рейнольдс', 'followers': '7,8 млн.'},

        {'id': 8, 'codde': 'adele', 'name': 'Adele', 'genre': 'R&B', 'lead_singers': 'Адель', 'followers': '55,6 млн.'},
    ]

    random_singer = random.choice(singers)

    return render(request, 'main/index.html', {'random_singer': random_singer, 'singers': singers})



def singer_detail(request, codde):
    singers = [
        {'id': 1, 'codde': 'сoldplay', 'name': 'Coldplay', 'genre': 'Рок', 'lead_singers': 'Кріс Мартін', 'followers': '25,5 млн.'},

        {'id': 2, 'codde': 'queen', 'name': 'Queen', 'genre': 'Рок', 'lead_singers': 'Фредді Меркюрі', 'followers': '40 млн.'},

        {'id': 3, 'codde': 'the-beatles', 'name': 'The Beatles', 'genre': 'Рок', 'lead_singers': 'Джон Леннон', 'followers': '38 млн.'},

        {'id': 4, 'codde': 'twenty-one-pilots', 'name': 'Twenty One Pilots', 'genre': 'Реп', 'lead_singers': 'Тайлер Джозеф', 'followers': '8,6 млн.'},

        {'id': 5, 'codde': 'exo', 'name': 'Exo', 'genre': 'K-pop', 'lead_singers': ' Сю Ман', 'followers': '10,8 млн.'},

        {'id': 6, 'codde': 'maroon5', 'name': 'Maroon 5', 'genre': 'Поп-рок', 'lead_singers': 'Адам Левін', 'followers': '8,8 млн.'},

        {'id': 7, 'codde': 'imagine-dragons', 'name': 'Imagine Dragons', 'genre': 'Iнді-рок', 'lead_singers': 'Ден Рейнольдс', 'followers': '7,8 млн.'},

        {'id': 8, 'codde': 'adele', 'name': 'Adele', 'genre': 'R&B', 'lead_singers': 'Адель', 'followers': '55,6 млн.'},
    ]

    singer = None
    for s in singers:
        if s['codde'] == codde:
            singer = s
            break

    if singer is None:
        return render(request, 'main/404.html', status=404)

    return render(request, 'main/singer_detail.html', {'singer': singer})

