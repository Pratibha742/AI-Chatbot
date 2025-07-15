from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .ai_logics import get_bot_response
from .forms import CustomRegisterForm,CustomLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from . models import ChatMessage
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy





# Create your views here.
def landing_page(request):
    return render(request, 'chatbot/landing.html')

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegisterForm()

    return render(request, 'chatbot/register.html', {'form': form})

# @login_required
# def chat_redirect_required(request):
#     session = ChatSession.objects.create(user=request.user, title="New Chat")
#     return redirect('chat_Page',session_id=session.id)


@login_required
def chat_page(request):
    history = ChatMessage.objects.filter(user=request.user).order_by("timestamp")
    return render(request, "chatbot/chat.html", {"chat_history": history})

@csrf_exempt
@login_required
def chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        bot_response = get_bot_response(user_message)

        # Save to database
        ChatMessage.objects.create(
            user=request.user,
            message=user_message,
            response=bot_response
        )

        return JsonResponse({"response": bot_response})

    return JsonResponse({"error": "Only POST allowed"})


class CustomLoginView(LoginView):
    template_name = 'chatbot/login.html'
    authentication_form = CustomLoginForm

    def get(self, request, *args, **kwargs):
        # Clear any leftover messages before showing the login page
        storage = messages.get_messages(request)
        for _ in storage:
            pass  # this simply clears the message queue
        return super().get(request, *args, **kwargs)


    def form_invalid(self, form):
        messages.error(self.request, "Invalid credentials or account does not exist.")
        return super().form_invalid(form)
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


