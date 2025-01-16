from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth import authenticate, login, logout  # Make sure login is imported

# Signup View
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            return redirect("login")
        else:
            return render(request, "signup.html", {"error": "Username already exists."})
    return render(request, "signup.html")

# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("chat")
        else:
            return render(request, "login.html", {"error": "Invalid credentials."})
    return render(request, "login.html")

# Logout View
def user_logout(request):
    logout(request)
    return redirect("login")

# Chat View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.db.models import Q

@login_required
def chat_view(request):
    user = request.user
    recipient_username = request.GET.get('recipient')  # Get recipient from query parameter
    recipient = None
    messages = []

    # Check if the recipient is passed in the URL
    if recipient_username:
        try:
            recipient = User.objects.get(username=recipient_username)
            
            # Fetch messages between the logged-in user and the selected recipient
            messages = Message.objects.filter(
                (Q(sender=user) & Q(receiver=recipient)) |
                (Q(sender=recipient) & Q(receiver=user))
            ).order_by('timestamp')

        except User.DoesNotExist:
            recipient = None

    # If no recipient is selected, you might want to show an error message or prompt to select a user
    if not recipient:
        # You can display an alert or a message that no recipient is selected
        return render(request, 'chat.html', {
            'user': user,
            'users': User.objects.exclude(username=user.username),
            'messages': [],
            'recipient': None,
            'error_message': 'Please select a user to chat with.'
        })

    if request.method == 'POST':
        message_content = request.POST.get('message')
        if recipient and message_content:
            # Create a new message if a recipient and message content are provided
            Message.objects.create(sender=user, receiver=recipient, content=message_content)
            return redirect(f'?recipient={recipient.username}')  # Reload the page with the recipient selected

    return render(request, 'chat.html', {
        'user': user,
        'users': User.objects.exclude(username=user.username),
        'messages': messages,
        'recipient': recipient,
    })

    # Render the chat page with the recipient and messages
    return render(request, 'chat.html', {
        'user': user,
        'users': users,
        'messages': messages,
        'recipient': recipient,
    })
