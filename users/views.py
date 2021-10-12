from django.shortcuts import render
import requests


def get_from_github(request):
    user = {}
    repo_list = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url1 = f'https://api.github.com/users/{username}'
        url2 = f'https://api.github.com/users/{username}/repos'
        response1 = requests.get(url1)
        response2 = requests.get(url2)
        user = response1.json()
        repo_list = response2.json()
    return render(request, 'index.html', {'user': user, 'repo_list': repo_list})

