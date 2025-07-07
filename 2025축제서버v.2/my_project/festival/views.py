from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Information, Participant
import urllib.parse
from django.shortcuts import render




def success_view(request):
    return render(request, 'festival/success.html')

def login_page(request):
    return render(request, 'festival/login.html')

def main_page(request):
    participant = Participant.objects.all
    return render(request,'festival/main.html', {'participant': participant})


def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        vote = request.POST.get('vote')

        information = get_object_or_404(Information, name = name, number = number)

        information.vote = vote
        information.save()

        return redirect('/success/')
    return render(request, 'festival/success.html')



def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')

        if not name or not number:
            return HttpResponse("이름과 번호를 입력해 주세요.", status=400)

        user = Information.objects.filter(name= name, number= number).first()
        name = urllib.parse.quote(name)

        if user:
            response = redirect('/mainpage/')
            response.set_cookie('name', name, httponly= False, max_age=1800)
            response.set_cookie('number', number, max_age=1800)
            return response
        else:
            return HttpResponse("이름 또는 번호가 잘못되었습니다.", status=401)
    return render(request, 'festival/main.html')

def result (request):
    vote1_result = Information.objects.filter(vote=1).count()
    vote2_result = Information.objects.filter(vote=2).count()
    participant = Participant.objects.get(id = 1)
    if vote1_result > vote2_result:
        text = f"{participant.participant1}, {vote1_result} : {participant.participant2}, {vote2_result}으로 {participant.participant1}가 이겼습니다"
    elif vote1_result == vote2_result:
        text = f"{participant.participant1}, {vote1_result} : {participant.participant2}, {vote2_result}으로 무승부입니다"
    else:
        text = f"{participant.participant1}, {vote1_result} : {participant.participant2}, {vote2_result}으로 {participant.participant2}가 이겼습니다"
    return render(request, 'festival/result.html', {'text' : text})

def reset (request):
    Information.objects.update(vote = None)
    vote1_result = Information.objects.filter(vote=1).count()
    vote2_result = Information.objects.filter(vote=2).count()
    text = f"1번 투표 {vote1_result}, 2번 투표 {vote2_result} 리셋 결과"
    return render(request, 'festival/result.html', {'text': text})