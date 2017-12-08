from flask import Flask, request
# from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webservice():
    if request.method == 'POST':
        data_received = request.headers
        print data_received
    else:
        if request.args.get("q") == "Ping":
            return 'OK'
        elif request.args.get("q") == "Name":
            return 'Bapi Raj Loya'
        elif request.args.get("q") == "Referrer":
            return 'LinkedIn'
        elif request.args.get("q") == 'Email Address':
            return 'bapir.loya@gmail.com'
        elif request.args.get("q") == "Phone":
            return '469-556-6805'
        elif request.args.get("q") == "Position":
            return 'Devops Engineer'
        elif request.args.get("q") == "Resume":
            return "https://www.dropbox.com/s/i9xkyjqzvnhjmjs/BAPI%20RAJ%20LOYA_devops_new_cv.pdf?dl=0"
        elif request.args.get("q") == "Source":
             return "https://github.com/bapi24/flask-brealtime.git"
        elif request.args.get("q") == "Puzzle":
            return "ABCD\nA=><>\nB<=<>\nC>>=>\nD<<<="
        elif request.args.get("q") == "Years":
            return "3 years "
        elif request.args.get("q") == "Degree":
            return "Masters in Information Technology Management(Uiversity of Texas at Dallas) and Bachelors in Information Technology(Manipal University)"
        elif request.args.get("q") == "Status":
            return "Yes"

if __name__ == '__main__':
    app.run(host)
