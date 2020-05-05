import sqlite3
from datetime import datetime
import requests

def import_gists_to_database(db, username, commit=True):
    cursor = db.cursor()
    api_url = 'https://api.github.com/users/{}/gists' .format(username)
    #print(api_url)
    r = requests.get(api_url)
    print(r.status_code)
    r.raise_for_status()
    gists_data = r.json()
    for idx,vals in enumerate(gists_data):
        q = '''INSERT INTO gists
            VALUES ({id}, '{git_id}', '{html_url}',
                    '{git_pull_url}', '{git_push_url}', '{commits_url}',
                    '{forks_url}', {public}, '{created_at}',
                    '{updated_at}', {comments}, '{comments_url}'
                    );''' .format(id=idx, git_id=vals['id'], 
                                html_url=vals['html_url'], 
                                git_pull_url=vals['git_pull_url'], 
                                git_push_url=vals['git_push_url'], 
                                commits_url=vals['commits_url'], 
                                forks_url=vals['forks_url'], 
                                public=vals['public'], 
                                created_at=vals['created_at'],
                                updated_at=vals['updated_at'], 
                                comments=vals['comments'],
                                comments_url=vals['comments_url']
                                )
        cursor.execute(q)
    if commit == True:
        db.commit()
    return
