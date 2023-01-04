from django.shortcuts import render, reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def main_view(request):
    template_name = 'cooking_calc/index.html'

    pages = dict()
    for k in DATA.keys():
        pages[k] = "{0}?dish={1}".format(reverse("calc"), k)

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def calc_view(request):
    template_name = 'cooking_calc/calc.html'
    dish = request.GET.get('dish')
    servings  = request.GET.get('servings', 1)

    if dish in DATA:
        recipe = {k: v * servings for k, v in DATA[dish].items()}
    else:
        return render(request, 'cooking_calc/404.html')

    context = {
        'recipe': recipe,
        'servings': servings,
        'dish': dish,
    }
    return render(request, template_name, context)