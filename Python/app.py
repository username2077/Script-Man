from bottle import run, route, template


@route('/')
def hello_world():
	return '<h1>Hello world!</h1>'

# dynamic url
@route('/blog/<id>')
def blog(id):
	return f'<h1>This is blog:{id}</h1>'

# get & post method
@route('/posted', method='POST')
def posted():
	return '<h1>Posted</h1>'

# template system
@route('/index')
def index():
	return template('index', name = 'Eryngium')

# query system
@route('/query')
def query():
	

if __name__ == '__main__':
	# debug for bottle error msg, reloader for bottle server restart
	run(debug=True, reloader=True)