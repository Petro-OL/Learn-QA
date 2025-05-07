import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'
    # print(r)

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    # print(r['total_count'])

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0
    # print(r)

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0
    # print(r)

# ==== additional tests =========================

# test for: non-autentificated user get info about existed user
@pytest.mark.api
def test_get_noauth_user_contextual_info(github_api):
    user = github_api.get_user_contextual_info('Petro-OL')
    assert user['message'] == 'Requires authentication'
    # print(user)

# test for Lists all the emojis available to use on GitHub
@pytest.mark.api
def test_get_all_emojis(github_api):
    req = github_api.get_list_emojis()
    assert len(req) >= 0

# test for Lists commits
@pytest.mark.api
def test_get_list_commits(github_api):
    ret = github_api.get_list_commits("Petro-OL", "Learn-QA")
    assert len(ret) >= 0
    assert ret[0]['commit']['author']['name'] == 'Petro Oliinyk'
