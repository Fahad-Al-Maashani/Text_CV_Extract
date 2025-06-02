# Text_CV_Extract
Extract Text from images
Create a Google Cloud project and enable Vision API.

pip install google-cloud-vision

You can install the following packages using pip:

pip install pytesseract pillow

Download the installer from Tesseract GitHub

If you plan to structure the extracted text automatically, consider installing additional libraries:


pip install beautifulsoup4 lxml

beautifulsoup4: Helps parse and format extracted text into structured HTML.

lxml: Improves handling of XML and HTML files.

## try this one for testing 
##
. Using Python Flask to Generate a Web Page
Instead of generating static HTML, create a Flask app to display the extracted CV dynamically.

Setup:
sh
pip install flask
Example:
python
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