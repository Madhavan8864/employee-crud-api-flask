from flask import Flask

from config.database import create_table

from routes.employee_routes import employee_bp
from routes.web_routes import web_bp

app = Flask(
    __name__,
    template_folder="templates"
)

create_table()

app.register_blueprint(employee_bp)
app.register_blueprint(web_bp)


@app.errorhandler(404)
def page_not_found(error):

    from flask import render_template

    return render_template(
        "404.html"
    ), 404


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )