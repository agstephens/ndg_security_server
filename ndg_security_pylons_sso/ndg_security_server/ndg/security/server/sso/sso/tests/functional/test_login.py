from ndg.security.server.sso.sso.tests import *

class TestLoginController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='login'))
        # Test response...
