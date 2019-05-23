import unittest

from python_repos import PythonRepos


class PythonRepoTestCase(unittest.TestCase):

    def test_status_code(self):
        pr = PythonRepos()
        pr.make_api_call()
        status_code = pr.status_code

        assert status_code == 200, f"Status code is {status_code}"

    def test_total_repos_is_greater_than_1000(self):
        pr = PythonRepos()
        pr.store_response()
        total_repos = pr.total_repos

        assert total_repos > 1000, f"Number of repos is {total_repos}"


unittest.main()
