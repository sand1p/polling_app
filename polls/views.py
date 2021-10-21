from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Question
from django.core import serializers
from .serializers import Questionserializer
from rest_framework.decorators import api_view

def index(request):
    return HttpResponse("Hello django world !!")

@api_view(['GET', 'POST', 'DELETE'])
def list_questions(request,question_id):
    if request.method == 'GET':
        Question.objects.all()
        question_serializer = Questionserializer(Question, many=True)

        return JsonResponse(question_serializer.data,safe=False)
    elif request.method== 'DELETE':
        question = Question.objects.get(pk=question_id)
        question.delete()
        JsonResponse("{Deleted questionwith id }")

def retrive_questions(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    # output = ', '.join([q.question_text for q in latest_question_list])
    serializer = Questionserializer(latest_question_list)
    json_output = serializer.data
    return HttpResponse(json_output)

def detail(request, question_id):
    return HttpResponse("You're looking at the question %s," % question_id)

def results(request, question_id):
    response="You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
            return HttpResponse("For question:{}, \n you didn't select a choice".format(question))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




