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



def smart_notes_view(request: HttpRequest):
    if request.method == 'POST':
        notes = request.POST.get('notes', '').strip()
        if notes:
            prompt = f"""
            DO NOT USE * SYMBOL

            You are an advanced academic reasoning system designed to transform messy student notes
            into precise, structured, high-retention learning material. Your output must be conceptually
            accurate, logically connected, and pedagogically optimized. First perform a silent reasoning
            and verification pass to ensure scientific correctness and conceptual clarity. Identify and
            correct any factual, logical, or conceptual errors before producing output. Do not reveal
            your reasoning.

            Output must strictly follow this structure and order with no deviations:

            Clean Notes: Rewrite the content into clear, concise, logically ordered bullet points,
            progressing from fundamental concepts to advanced ones, emphasizing causal relationships
            and conceptual flow.

            Concept Summary: Write 3–6 sentences explaining the core ideas, underlying mechanisms,
            purpose, and real-world relevance using simple but precise language.

            Concept Graph: Generate a causal and dependency-based knowledge graph using the format
            “Concept A → relationship → Concept B”. Focus on mechanisms, energy flow, dependencies,
            and transformations. Avoid location-only links unless essential.

            Key Definitions: List all essential terms with simple definitions and one intuitive example each.
            Definitions must prioritize understanding, not memorization.

            Active Recall Questions: Generate exactly 3 easy, 3 medium, and 3 hard questions that test
            conceptual understanding, causal reasoning, and application. Avoid definition-only questions.
            Write the answers for these questions in the end of your response.

            Misconceptions: Identify common student misunderstandings, explain why they occur, why they are
            wrong, and how to avoid them.

            Compression: Produce exactly 10 dense, information-rich lines that preserve at least 90% of the
            total learning value. Each line must contain a distinct core idea. No filler, no repetition, no vagueness.

            Rules: Be precise. Be rigorous. Enforce conceptual correctness. Prioritize causal understanding over memorization.
            Avoid redundancy. Maintain strict format discipline. If scientific inaccuracies appear in the input, they must be corrected.

            Input:
            {notes}
            """
            response = chat(
                model='llama3.2',
                messages=[{'role': 'user', 'content': prompt}]
            )
            return render(request, 'myapp/smart_notes.html', {'output': response.message.content})

    return render(request, 'myapp/smart_notes.html', {})

def about(request):
    return render(request, 'myapp/about-us.html')

def contact(request):
    return render(request, 'myapp/contact-us.html')

def demo(request):
    return render(request, 'myapp/demo.html')

def profile_view(request):
    return render(request, 'myapp/profile.html')