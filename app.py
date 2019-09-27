import os
from flask import Flask, redirect
import rq_dashboard
from rq_dashboard.cli import add_basic_auth

app = Flask(__name__)
app.config.from_object(rq_dashboard.default_settings)
app.config["RQ_DASHBOARD_REDIS_URL"] = os.environ.get("RQ_DASHBOARD_REDIS_URL")

add_basic_auth(
    blueprint=rq_dashboard.blueprint,
    username=os.environ.get("RQ_DASHBOARD_USERNAME"),
    password=os.environ.get("RQ_DASHBOARD_PASSWORD"),
)

app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")


@app.route("/")
def root():
    return redirect("/rq", code=302)


if __name__ == "__main__":
    app.run()
