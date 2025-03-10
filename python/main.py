from app import create_app, db
from flasgger import Swagger

app = create_app()
swagger = Swagger(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)