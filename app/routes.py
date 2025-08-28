from flask import jsonify, render_template, request

def register_routes(app):

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/api/json")
    def json_data():
        data = {"message": "Hello from JSON endpoint"}
        return jsonify(data)

    @app.route("/api/xml")
    def xml_data():
        xml_response = """<?xml version="1.0"?><message>Hello from XML endpoint</message>"""
        return app.response_class(xml_response, mimetype='application/xml')

    @app.route("/api/csv")
    def csv_data():
        csv_response = "name,age\nAlice,25\nBob,30"
        return app.response_class(csv_response, mimetype='text/csv')
