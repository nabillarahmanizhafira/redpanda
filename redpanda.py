from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_dotenv import DotEnv
from flask_mail import Mail
from flask_mail import Message
from form import FeedbackForm

def create_app():
	env = DotEnv()
	app = Flask(__name__)
	env.init_app(app)
	env.eval(keys={
		'DEBUG': bool,
		'TESTING': bool
	})
	mail = Mail(app)
	mail.init_app(app)

	@app.route("/", methods=['GET', 'POST'])
	def index():
		"""
			Render the view of index page.
		"""
		form = FeedbackForm()
		return render_template('index.html', title='Tri Sinergi Mitra', current_page='TSM', form=form)

	@app.route("/send_feedback", methods=['POST'])
	def send_feedback():
		"""
			Do action with python form
		"""
		if request.method == 'POST' :
			#result = request.form
			result = request.form['email']
			msg_subject = "You got an email from {} / {} - {}".format(request.form['email'], request.form['full_name'], request.form['subject'])
			msg_body = request.form['body']
			send_email(msg_subject,'trisinergim@gmail.com', ['trisinergim@gmail.com'], msg_body)
			return redirect(url_for('index'))
		else:
			flash('The message has not been sent due to unknown failure')
			return redirect(url_for('index'))

	def send_email(subject, sender, recipients, text_body):
		msg = Message(subject, sender=sender, recipients=recipients)
		msg.body = text_body
		mail.send(msg)
		return

	@app.errorhandler(404)
	def page_not_found_error(err):
		"""
		Render the view of error 404 page
		"""
		return render_template('404.html', title='TSM not found', current_page='404')

	@app.errorhandler(500)
	def internal_server_error(err):
		"""
		Render the view of error 500 page
		"""
		return render_template('500.html', title='TSM internal server error', current_page='500')


	return app


if __name__ == "__main__":
	app = create_app()
	app.run(host=app.config['HOST'], port=int(app.config['PORT']))