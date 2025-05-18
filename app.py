from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route("/")
def index():
    return """
    <html>
      <head>
        <title>DevSecOps Project - Omer JAVAID</title>
        <style>
          body {
            background-color: #121212;
            color: #ffffff;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 80px;
          }
          h1 {
            color: #00d4ff;
          }
          a {
            color: #ffd700;
            text-decoration: none;
            font-weight: bold;
          }
        </style>
      </head>
      <body>
        <h1>🚀 DevSecOps Project by Omer JAVAID</h1>
        <p>This cloud app is containerized with Docker and monitored using Prometheus + Grafana.</p>
        <p>Hosted on AWS EC2 | Managed with Terraform | Secured with Trivy</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
