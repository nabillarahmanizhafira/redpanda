from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_dotenv import DotEnv

def create_app():
	env = DotEnv()
	app = Flask(__name__)
	env.init_app(app)
	env.eval(keys={
		'DEBUG': bool,
		'TESTING': bool
	})


	@app.route("/", methods=['GET', 'POST'])
	def index():
		"""
			Render the view of index page.
		"""

		return render_template('index.html', title='RedPanda', current_page='RedPanda')


	@app.errorhandler(404)
	def page_not_found_error(err):
		"""
		Render the view of error 404 page
		"""
		return render_template('404.html', title='RedPanda not found', current_page='404')

	@app.errorhandler(500)
	def internal_server_error(err):
		"""
		Render the view of error 500 page
		"""
		return render_template('500.html', title='RedPanda internal server error', current_page='500')


	return app


if __name__ == "__main__":
	app = create_app()
	app.run(host=app.config['HOST'], port=int(app.config['PORT']))
