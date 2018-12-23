from flask import render_template, redirect, url_for, flash

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        content = form.content.data
        message = Message(name=name, content=content)
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
