from django.shortcuts import render

# Create your views here.
def index(request):
    pass

@app.route('/forgot_password', methods=['GET', 'POST'])

def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        token = s.dumps(email, salt='email-confirm')

        msg = Message('Password Reset Request', sender='your_email@example.com', recipients=[email])
        link = url_for('reset_password', token=token, _external=True)
        msg.body = f'Your link to reset your password is {link}'
        mail.send(msg)

        flash('A password reset link has been sent to your email.', 'info')
        return redirect(url_for('forgot_password'))

    return render_template('forgot_password.html')
