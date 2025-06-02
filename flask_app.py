##install flask  pip install flask
##this will jsut convert the cv data into a generated html file showing below.
from flask import Flask, render_template_string

app = Flask(__name__)

cv_data = {
    "name": "John Doe",
    "title": "Software Engineer",
    "experience": ["XYZ Corp (2020-Present)", "ABC Tech (2019-2020)"]
}

html_template = """
<!DOCTYPE html>
<html>
<head><title>{{ name }}</title></head>
<body>
<h1>{{ name }}</h1>
<h2>{{ title }}</h2>
<h3>Experience</h3>
<ul>
{% for job in experience %}
<li>{{ job }}</li>
{% endfor %}
</ul>
</body>
</html>
"""

@app.route("/")
def display_cv():
    return render_template_string(html_template, **cv_data)

if __name__ == "__main__":
    app.run(debug=True)
