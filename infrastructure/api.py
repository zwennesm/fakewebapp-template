from typing import Dict

from flask import Flask

from application.calc import Calc

app = Flask(__name__)
calc = Calc()


@app.route("/<int:x>/<int:y>")
def hello_world(x: int, y: int) -> Dict[str, int]:
    return {"result": calc.add(x, y)}


if __name__ == "__main__":
    app.run(debug=False)
