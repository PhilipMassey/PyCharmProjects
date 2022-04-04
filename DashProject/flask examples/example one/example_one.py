import views
from flask import Flask

app = Flask(__name__)
#app = Flask(__name__, template_folder='templates', static_folder='static')

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/other', view_func=views.other)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
