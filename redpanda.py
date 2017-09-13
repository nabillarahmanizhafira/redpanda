from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_dotenv import DotEnv
from werkzeug.utils import secure_filename
import os


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

	@app.route("/gallery", methods=["GET", "POST"])
	def gallery():
		if request.method == "GET":
			list_files = os.listdir("static/img/upload")
			return render_template('gallery.html', title='Gallery', current_page='Gallery', list_files=list_files)
		elif request.method == "POST":
			file = request.files['file']
			caption = request.form.get('caption')
			filename = secure_filename('upl_' + caption + '_' + file.filename)
			file.save(os.path.join('static/img/upload', filename))
			return redirect('/gallery')


	@app.route("/reproduction", methods=["GET"])
	def reproduction():
		return render_template('reproduction.html', title='Reproduction', current_page='Reproduction')

	@app.route("/habitat", methods=["GET"])
	def habitat():
		return render_template('habitat.html', title='Habitat', current_page='Habitat')

	@app.route("/behavior", methods=["GET"])
	def behavior():
		return render_template('behavior.html', title='Behavior', current_page='Behavior')

	return app


if __name__ == "__main__":
	app = create_app()
	app.run(host=app.config['HOST'], port=int(app.config['PORT']))
