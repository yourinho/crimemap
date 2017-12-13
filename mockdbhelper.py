class MockDBHelper:

    def connect(self, database="crimemap"):
        pass

    def get_all_inputs(self):
        return []

    def get_all_crimes(self):
        return [{'latitude': 59.93196566631549,
                 'longitude': 30.364151000976562,
                 'date': "2000-01-01",
                 'category': "mugging",
                 'description': "mock description"}]

    def add_input(self, data):
        pass

    def add_crime(self, category, date, latitude, longitude, description):
        pass

    def clear_all(self):
        pass

