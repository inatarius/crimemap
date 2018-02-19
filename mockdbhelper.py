class MockDBHelper:

    def connect(self, database="crimemap"):
        pass

    def add_crime(self, category, date, latitude, longtitude, description):
        pass

    def get_all_crimes(self):
        return [{
        'latitude': -33.334324,
        'longtitude': 45.234234,
        'date': "1900-01-01",
        'category': "mugging",
        'description': "some description"
        }]