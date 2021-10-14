from django.shortcuts import render
import requests


def get_from_github(request):
    user = {}
    repo_list = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url1 = f'https://api.github.com/users/{username}'
        url2 = f'https://api.github.com/users/{username}/repos'
        response_username = requests.get(url1)
        good_resp = (response_username.status_code == 200)
        response_username_repos = requests.get(url2)
        user = response_username.json()
        user['exist'] = good_resp
        repo_list = response_username_repos.json()
    return render(request, 'index.html', {'user': user, 'repo_list': repo_list})

