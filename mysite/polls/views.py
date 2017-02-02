from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question, Choice
# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = { 'latest_question_list': latest_question_list }	
	#output = ', '.join([p.question_text for p in latest_question_list])
    	#return HttpResponse(output)
	return render(request,'polls/index.html',context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = { 'question': question }
	return render(request, 'polls/detail.html', context)
    	#return HttpResponse("You are at the detail page for poll " + question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:		
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		context = {
			'question' : question,
			'error_message': "You didn't pick anything!",
			  }
		return render(request, 'polls/detail.html', context)
	else:
		selected_choice.votes +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    	#return HttpResponse("You are at the page that gets the HTTP POST.")

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)    
	return HttpResponse("This page will showus which one is most popular.")
