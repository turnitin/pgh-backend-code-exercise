import sys
import unittest

import requests

BASE = None


class VerifyStudents(unittest.TestCase):
    def get(self, query_args={}):
        return requests.get(self.url(), params=query_args)

    def post(self, body_dict={}):
        return requests.post(self.url(), json=body_dict)

    def url(self):
        return BASE + self.path()

    def assert_post_not_ok(self, body_dict, msg):
        self.assert_response_not_between(self.post(body_dict), 200, 300, msg)

    def assert_response_between(self, response, low, high, msg):
        status = response.status_code
        if status not in range(low, high):
            self.fail(msg + ', expected status between {} and {}, got {}'.format(low, high, status))

    def assert_response_not_between(self, response, low, high, msg):
        status = response.status_code
        if status in range(low, high):
            self.fail(msg + ', expected status NOT between {} and {}, got {}'.format(low, high, status))


class VerifyCreate(VerifyStudents):
    def path(self):
        return '/students'

    def valid_student(self, updates={}):
        student = {
            'email': 'pusheen@example.com',
            'first_name': 'Push',
            'last_name': 'Een',
        }
        student.update(updates)
        return student

    def test_fail_missing_last_name(self):
        doc = self.valid_student({'last_name': None})
        self.assert_post_not_ok(doc, 'Expected error with no last name')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python {} url-of-solution".format(sys.argv[0]))
        sys.exit(1)

    BASE = sys.argv[1].rstrip('/')

    # lop this off so unittest doesn't try to do something with it
    del(sys.argv[1])

    try:
        response = requests.get(BASE + '/')
        if response.status_code >= 400:
            print("FAIL: Health check got bad status ({}), not continuing".format(response.status_code))
            sys.exit(1)
    except requests.RequestException as e:
        print("FAIL: Caught exception with health check -- {}".format(e))
        sys.exit(1)

    print("OK: Health check")
    unittest.main(verbosity=2)
