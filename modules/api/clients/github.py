import requests


class GitHub:
    def get_user(self, username):
        url = "https://api.github.com/users/" + username
        r = requests.get(f"{url}")
        body = r.json()

        return body

    def search_repo(self,name):
        r = requests.get(f"https://api.github.com/search/repositories?q={name}")
        body = r.json()

        return body

    # non-autentificated user get info about existed user
    def get_user_contextual_info(self,username):
        r = requests.get(f"https://api.github.com/users/{username}/hovercard")
        body = r.json()

        return body

    # test for Lists all the emojis available to use on GitHub
    def get_list_emojis(self):
        r = requests.get(f"https://api.github.com/emojis")
        body = r.json()

        return body

    # test for List commits
    def get_list_commits(self, username, repo):
        r = requests.get(f"https://api.github.com/repos/{username}/{repo}/commits")
        body = r.json()

        return body

    # test for non-exist user (previors)
    def get_non_exist_user(self,username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body
