from flask import Flask, render_template, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdlkj123'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/flashing')
def flashing():
  flash('Sucesso', 'success')
  return render_template('flashing.html')

@app.route('/hello/<name>')
def hello(name):
  flash(f'Bem-vindo, {name}!', 'info')
  return render_template('hello.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')