from kunUZ.models import Category, Yangiliklar


def head_categories(request):
    return {"head_categories": Category.objects.order_by("id")}


def head_news(requests):
    return {"head_news": Yangiliklar.objects.order_by('-id')}

