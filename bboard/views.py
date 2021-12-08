#from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Bb
from .models import Rubric

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    contex = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render (request, 'bboard/by_rubric.html', contex)

def index(request):
    # template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    contex = {'bbs':bbs, 'rubrics':rubrics}
    # context = {'bbs': bbs}

    return render(request, 'bboard/index.html', contex)

