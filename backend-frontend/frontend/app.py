import json
import urllib.request
import urllib.parse

from flask import Flask, render_template, url_for, request, redirect, Blueprint


endpoint = 'http://undernginx/pastebin/api'


app = Flask(__name__)
bp = Blueprint('mybp', __name__, 
               static_folder='static',
               static_url_path='/pastebin/static',
               template_folder='templates',
               url_prefix='/pastebin')


@bp.route(f'/', methods=['GET'])
@bp.route(f'/index.html', methods=['GET'])
def get_index():
    count_pastes = 0
    url = f'{endpoint}/pastes/'
    data = None
    headers = {'Accept': 'application/json'}
    method = 'GET'
    req = urllib.request.Request(url=url,
                                 data=data,
                                 headers=headers,
                                 method=method)
    with urllib.request.urlopen(req) as f:
        data = json.loads(f.read())
        count_pastes = len(data)

    return render_template('index.html',
                           count_pastes=count_pastes)


app.register_blueprint(bp)
