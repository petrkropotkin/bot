from django.shortcuts import render,redirect,render_to_response
import random


from django import forms

class AnswerForm(forms.Form):
	user = forms.CharField(max_length=100,label='Human')



# Create your views here.
def index(request):
	list_of_greetings = ["What's up?" ,"Hello bro, how are you?","Good day Sir!",
                     "How are you doing?","How are you doing these days?","Nice seeing you!","What do you do for a living?",
                     "What is your name?","What a surprise. I haven't seen you in a long time.",
                     "Enjoy your stay with us.","So where are you from?","What do you mean?",
                      "How have you been?"]


	
	list_of_topic = list_of_greetings
	random_member = random.randint(0, len(list_of_topic) - 1)
	word = list_of_topic[random_member]

	

	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			# answer = form.cleaned_data['user']
			
			
			return redirect('/')
	else:
		form = AnswerForm()
	return render(request,'bot_app/index.html',{'form':form, 'word':word})
	
		
	

	# used_word = set()
	# if word not in used_word:
	# 	used_word.add(word)
	# 	if len(used_word) == len(list_of_topic):
	# 		used_word.clear()

		
	