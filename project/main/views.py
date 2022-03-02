from django.shortcuts import render

# Create your views here.
def get_menu_context():
    return [
        {'url_name': 'index'},
        {'url_name': 'time', 'name': 'Добавить данные', 'name1': 'Просмотрр карты'},
    ]
def index_page(request):
    context = {
        'pagename': 'Главная',
        'author': 'балбесы',
        'menu': get_menu_context(),
    }
    return render(request, 'pages/index.html', context)
def add_page(request):
    context = {
        'pagename': 'Главная',
        'author': 'балбесы',
        'menu': get_menu_context(),
    }
    return render(request, 'pages/index.html', context)
