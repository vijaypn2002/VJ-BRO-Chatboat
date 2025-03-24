from django.shortcuts import render
from .gemini_helper import generate_gemini_response

def chat_with_gemini(request):
    response_text = ""
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            response_text = generate_gemini_response(prompt)
    return render(request, "chat.html", {"response": response_text})
