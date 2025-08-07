from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home.html')
def news_list(request):
	from .models import News
	news = News.objects.all()
	return render(request, 'news_list.html', {'news': news})
def player_list(request):
	from .models import Player
	players = Player.objects.all()
	return render(request, 'player_list.html', {'players': players})
def about(request):
	return render(request, 'about.html')
def contact(request):
	return render(request, 'contact.html')
def news_detail(request, news_id):
	from .models import News
	news = News.objects.get(id=news_id)
	return render(request, 'news_detail.html', {'news': news})
def player_detail(request, player_id):
	from .models import Player
	player = Player.objects.get(id=player_id)
	return render(request, 'player_detail.html', {'player': player})