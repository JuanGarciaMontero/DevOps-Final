import pytest
from flask_testing import TestCase
from app import create_app, db
from app.models import Data

class TestRoutes(TestCase):
    def create_app(self):
        app = create_app("testing")  # Utiliza la configuración de prueba
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_insert_data(self):
        response = self.client.post("/data", json={"name": "TestName"})
        self.assert200(response)
        data = Data.query.filter_by(name="TestName").first()
        self.assertIsNotNone(data)

    # Agrega más pruebas según sea necesario

if __name__ == "__main__":
    pytest.main()