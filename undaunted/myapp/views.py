from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from ollama import chat

# Create your views here.

class LandingView(TemplateView):
    template_name = 'myapp/landing.html'


class DashboardView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'myapp/dashboard.html', context)


def ai_view(request: HttpRequest):
    if request.method == 'POST':
        gpa = request.POST.get('gpa')
        sat = request.POST.get('sat')
        rank = request.POST.get('ranking')
        ecs = request.POST.get('extracurriculars')
        essay = request.POST.get('essay')
        hs_courses = request.POST.get('hs_coursework')
        response = chat(
            model='llama3.2',
            messages=[{'role': 'user',
                       'content': 'You are an elite college admissions evaluator reviewing a student application.'
                                  'Your job is not to encourage, reassure, or soften feedback. Your job is to assess competitiveness with cold realism and professional ruthlessness.'
                                  'Assume the student wants the truth, even if it stings.'
                                  'dont use * symbol'
                                  'start by evaluating the application overall from 1 to 10'
                                  'Describe strengths, weaknesses and recommendations for improvement in 180-300 words'
                                  'You are given the following inputs:'
                                  'GPA: {}, SAT: {}, Ranking: {}, Extracurriculars: {}, Essay: {}, hs courses: {}'.format(gpa, sat, rank, ecs, essay, hs_courses)
                       }],
        )
        return render(request, 'myapp/app_eval.html', {'gpa': gpa, 'response': response.message.content, 'ranking': rank, 'sat': sat})
    return render(request, 'myapp/app_eval.html')

def image_testing_view(request: HttpRequest):
    if request.method == 'POST':
        img = request.FILES['image']

        response = chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': 'What is in this image?',
                'images': [img.read()]
            }]
        )

        return render(request, 'myapp/vision_ai.html', {
            'response': response.message.content
        })

    return render(request, 'myapp/vision_ai.html')


