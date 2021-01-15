from flask import Flask, request, jsonify
from flask_cors import CORS
from django.utils.crypto import get_random_string

app = Flask(__name__)
CORS(app)

users = { 
    'users_list' :
    [
        { 
            'id': 'xyz789',
            'name': 'Charlie',
            'job': 'Janitor',
        },
        {
            'id': 'abc123', 
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id': 'ppp222', 
            'name': 'Mac',
            'job': 'Professor',
        }, 
        {
            'id': 'yat999', 
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id': 'zap555', 
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}


@app.route('/users/<id>')
def get_user(id):
    if id :
        for user in users['users_list']:
            if user['id'] == id:
                return user
        return ({})
    return users

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')

        if search_username and search_job:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username and user['job'] == search_job:
                    subdict['users_list'].append(user)
            return subdict

        elif search_username:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict

        elif search_job:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['job'] == search_job:
                    subdict['users_list'].append(user)
            return subdict
        return users

#Method for adding an entry
#Returns the new user object and code 201 on success
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = get_random_string(length=6, allowed_chars=u'abcdefghijklmnopqrstuvwxyz1234567890')
        users['users_list'].append(userToAdd)
        resp = jsonify(userToAdd)
        resp.status_code = 201 #successful add 
        return resp

#Method for deleting an entry
#Returns True and code 200 on success
    elif request.method == 'DELETE':
        userToDelete = request.get_json()
        users['users_list'].remove(userToDelete)
        resp = jsonify(success=True)
        resp.status_code = 200 #successful delete
        return resp