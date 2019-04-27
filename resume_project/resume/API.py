import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from resume_project.resume import models
# в бд нужно сохранить переменные:
'''
fullname
avatar_url
orgs - это словарь
followers
repos_count
repos_dict_with_full_info - это словарь
----------------



доп задание:

в конце функциии генерятся 2 фотки строками:
plt.savefig('demo.png')
plt.savefig('demo2.png')

сохраняй их в директорию аля так:
plt.savefig('directoryforimages/user/demo2.png')

и настрой функцию по их отдаче по ссылке

'''


def github(usr_id,username, site_username):
    #check user dictory

    command = 'ls static/users_dir | grep ' + site_username

    if os.system(command) == 256:
        print("NO USER DIR\nUSER: " + site_username)
        command = "mkdir static/users_dir/" + site_username
        os.system(command)
    else:
        print("FOUND USER DIR\nUSER: " + site_username)

    client_id_and_secret = '?client_id=ea92b1a1958dd3d3e965&client_secret=2ee1ba9e4052deae4c79ba5c2b43cc0cadda2636'

    url = 'https://api.github.com/users/' + str(username) + client_id_and_secret
    req = requests.get(url)
    main_json = req.json()
    # getting avatar
    avatar_url = main_json['avatar_url']
    # ------------------
    # getting full name
    full_name = main_json['name']
    # ------------------
    # getting user organisations
    url_orgs = 'https://api.github.com/users/' + str(username) + '/orgs' + client_id_and_secret
    req = requests.get(url_orgs)
    req_json = req.json()
    orgs = []
    for i in req_json:
        orgs.append({'org_name': i['login'], 'avatar_url': i['avatar_url'], 'description': i['description']})
    # ------------------
    # getting followers
    followers_json = (
        requests.get('https://api.github.com/users/' + username + '/followers' + client_id_and_secret)).json()
    followers = (len(followers_json))
    # ------------------
    # getting repos full information
    repos_json = (requests.get('https://api.github.com/users/' + username + '/repos' + client_id_and_secret)).json()
    repos_count = len(repos_json)

    repos_dict_with_full_info = []
    for repo in repos_json:
        contributors_json = (requests.get('https://api.github.com/repos/' + username + '/' + repo[
            'name'] + '/contributors' + client_id_and_secret)).json()
        repo_info_json = (
            requests.get('https://api.github.com/repos/' + username + '/' + repo['name'] + client_id_and_secret)).json()

        try:
            my_dict = {'name': repo['name'], 'language': repo_info_json['language'],
                       'commits': contributors_json[0]['contributions'], 'stars': repo_info_json['stargazers_count']}

            repos_dict_with_full_info.append(my_dict)
        except:
            pass

    # ----------------------------------
    langs = []
    stars = []
    for i in repos_dict_with_full_info:
        if str(i['stars']) != '0':
            langs.append(i['name'])
            stars.append(int(i['stars']))

    # Pie chart
    labels = langs
    sizes = stars
    # colors
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#99cccc']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title('Repositories with the highest star-rates')
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()

    image_save_filename = 'static/users_dir/' + site_username + '/demo.png'
    plt.savefig(image_save_filename)

    langs = []
    stars = []
    for i in repos_dict_with_full_info:
        if str(i['stars']) != '0':
            if i['language'] in langs:
                stars[langs.index(i['language'])] += int(i['stars'])
            else:
                langs.append(i['language'])
                stars.append(int(i['stars']))

    # Pie chart
    labels = langs
    sizes = stars
    # colors

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.2f%%', startangle=90)
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title('Most starred languages')
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()

    image_save_filename = 'static/users_dir/' + site_username + '/demo2.png'
    plt.savefig(image_save_filename)

    u = models.GithubConnectedUsers.objects.create(id = '',
    authorid = '',
    fullname = '',
    avatarurl = '',
    orgs = '',
    followers = '',
    repos_dict_with_full_info = '',
    client_ID_and_secret = '')
    u.save()

#github('jonkykong')