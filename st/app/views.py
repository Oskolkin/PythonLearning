from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
QUESTIONS = [
    {
        "title": f"Title #{i}",
        "text": f"This is text for question #{i}",  
        "number": i,
    } for i in range (1000)
]

def ask(request):
    return render(request, "ask.html")

def question(request, i:int):
    return render(request, "question_page.html", {"question": QUESTIONS[i]})

def TagIndex(request):
    return render(request, "TagIndex.html", {"questions": QUESTIONS})

def question_35(request):
    return render(request, "TagIndex.html")

def logIn(request):
    return render(request, "logIn.html")

def registration(request):
    return render(request, "registration.html")

def settings(request):
    return render(request, "settings.html")

def index(request):
    # Ваш список вопросов
    QUESTIONS = [
        {
            "title": f"Title #{i}",
            "text": f"This is text for question #{i}",  
            "number": i,
        } for i in range(1000)
    ]

    # Создаем Paginator с 5 вопросами на страницу
    paginator = Paginator(QUESTIONS, 5)

    # Получаем номер страницы из запроса (например, ?page=2)
    page_number = request.GET.get('page')

    try:
        # Получаем объект страницы
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page не число, возвращаем первую страницу
        page = paginator.page(1)
    except EmptyPage:
        # Если страница пуста (например, page=9999), возвращаем последнюю страницу
        page = paginator.page(paginator.num_pages)

    # Передаем страницу в шаблон
    return render(request, 'index.html', {'page': page})