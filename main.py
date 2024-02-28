import json
import os
import random
from json import JSONDecodeError

from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


USERS = []


app = Flask(__name__)


@app.route('/promotion')
def promotion():
    phrase_list = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return '</br>'.join(phrase_list)


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/img.png" alt="здесь должна была быть картинка, но не нашлась">
                    <br>Вот она какая планета</br>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/img.png" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-dark" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнём с марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/login_form_style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <center>
                            <h1>Анкета претендента на <br> участие в миссии</h1>
                            </center>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="mb-3">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    </div>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="row gy-3">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="education">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                         </div>
                                        <div class="form-group">
                                            <label for="about">Какая у вас профессия?</label>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" value="Инженер-исследователь" id="research_engineer" name="profession">
                                                <label class="form-check-label" for="research_engineer">Инженер-исследователь</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" value="Инженер-строитель" id="civil_engineer" name="profession">
                                                <label class="form-check-label" for="civil_engineer">Инженер-строитель</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" value="Пилот" id="pilot" name="profession">
                                                <label class="form-check-label" for="pilot">Пилот</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" value="Метеоролог" id="meteorologist" name="profession">
                                                <label class="form-check-label" for="meteorologist">Метеоролог</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" value="Инженер по жизнеобеспечению" id="life_support_engineer" name="profession">
                                                <label class="form-check-label" for="life_support_engineer">Инженер по жизнеобеспечению</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" value="Инженер по радиационной защите" id="radiation_protection_engineer" name="profession">
                                                <label class="form-check-label" for="radiation_protection_engineer">Инженер по радиационной защите</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" value="Врач" id="doctor" name="profession">
                                                <label class="form-check-label" for="doctor">Врач</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" value="Экзобиолог" id="exobiologist" name="profession">
                                                <label class="form-check-label" for="exobiologist">Экзобиолог</label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему вы хотите принять участие в миссии</label>
                                            <textarea class="form-control" id="about" rows="3" name="motivation"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group">
                                            <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="ready">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                            </div>
                                        </div>
                                        <div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        professions = list(map(lambda x: x.lower(), request.form.getlist("profession")))
        file = f'/static/img/user{len(USERS) + 1}.png'
        with open(file, 'wb') as f:
            if request.files['file']:
                f.write(request.files['file'].read())
            else:
                with open('static/img/default.png', 'rb') as d:
                    data = d.read()
                f.write(data)
        user_dict = {
            "name": request.form['name'],
            'surname': request.form['surname'],
            "education": request.form['education'],
            "profession": ', '.join(professions),
            "sex": request.form['sex'],
            "motivation": request.form['motivation'],
            "ready": True if request.form['ready'] == 'on' else False,
            "img_src": file
        }
        with open('templates/members.json', encoding='utf-8') as f:
            try:
                users = json.load(f)
            except JSONDecodeError:
                users = []
        users.append(user_dict)
        with open('templates/members.json', 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=4, ensure_ascii=False)
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planet_name(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name}</h1>
                    <h2>Эта планета близка к Земле;</h2>
                    </div>
                    <div class="alert alert-success" role="alert">
                      На ней много необходимых ресурсов;
                    </div>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      На ней есть вода и атмосфера;
                    </div>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      На ней есть небольшое магнитное поле;
                    </div>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Наконец, она просто красива!
                    </div>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname};</h2>
                    </div>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <h2>составляет {rating}!</h2>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form_style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <center>
                                <h1>Загрузка фотографии</h1>
                                <h2>для участия в миссии</h2>
                            </center>
                            <form class="file_form" method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <div class="mb-3">
                                        <label for="photo">Приложите фотографию</label>
                                    </div>
                                    <div class="mb-3">
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                </div>
                                <div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </div>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        if request.files['file']:
            file = request.files['file']
            with open('static/img/image.png', 'wb') as f:
                f.write(file.read())
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form_style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <center>
                                    <h1>Загрузка фотографии</h1>
                                    <h2>для участия в миссии</h2>
                                </center>
                                <form class="file_form" method="post" enctype="multipart/form-data">
                                    <div class="row gy-2">
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div>
                                            <img src="/static/img/image.png" class="img-fluid" alt="photo">
                                        </div>
                                        <div>
                                            <button type="submit" class="btn btn-primary">Отправить</button>
                                        </div>
                                    </div>
                                </form>
                              </body>
                            </html>'''


@app.route('/carousel')
def carousel():
    imgs = ["static/img/img_1.png", "static/img/img_2.png", "static/img/img_3.png"]
    return render_template("carousel.html", imgs=imgs)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def profession(prof):
    return render_template('prof.html', title="http://127.0.0.1:8080/training/" + prof, prof=prof.lower())


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', title="http://127.0.0.1:8080/training/" + list, list=list)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    return render_template('table.html', title=f"http://127.0.0.1:8080/table/{sex}/{age}", sex=sex, age=int(age))


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    with open("templates/members.json", encoding='utf-8') as f:
        try:
            users = json.load(f)
        except JSONDecodeError:
            users = []
    if users:
        user = random.choice(users)
        return render_template('auto_answer.html', title="Анкета", user=user)
    else:
        return "У вас нет анкет"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/member', methods=['GET', 'POST'])
def member():
    with open('templates/members.json', encoding='utf-8') as f:
        try:
            users = json.load(f)
        except JSONDecodeError:
            users = []
    if users:
        user = random.choice(users)
        professions = user['profession']
        initials = user['name'] + ' ' + user['surname']
        # img_src = user["img_src"]
        img_src = "/static/img/image.png"
        print(professions)
        return render_template('member.html', title="http://127.0.0.1:8080/member", initials=initials, prof=professions, img=img_src)
    else:
        return "Отсутствуют члены экипажа"


@app.route('/distribution', methods=['GET', 'POST'])
def distribution():
    user_list = ['Ридли Скотт', 'Энди Уир']
    return render_template('distribution.html', title="http://127.0.0.1:8080/distribution", user_list=user_list)


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    imges = []
    ind = 1
    while os.path.exists(f"static/img/img_{ind}.png"):
        imges.append(f"static/img/img_{ind}.png")
        ind += 1
    print(imges)
    if request.method == 'GET':
        return render_template('galery.html', title="Красная планета", imges=imges)
    elif request.method == 'POST':
        if request.files['file']:
            file = request.files['file']
            with open(f'static/img/img_{len(imges) + 1}.png', 'wb') as f:
                f.write(file.read())
            imges.append(f'/static/img/img_{len(imges) + 1}.png')
            print(imges)
            return render_template('galery.html', title="Красная планета", imges=imges)



class LoginForm(FlaskForm):
    astronaut_id = StringField('id астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    capitan_id = StringField('id капитана', validators=[DataRequired()])
    capitan_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(port=8080, host='127.0.0.1')