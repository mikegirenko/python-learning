import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

URL = 'https://api.github.com/search/repositories?q=language:python&sort=stars'


class PythonRepos:

    def __init__(self):
        self.repo_dicts = []
        self.status_code = None
        self.total_repos = None

    def make_api_call(self):
        # Make API call and store response
        url = URL
        r = requests.get(url)
        self.status_code = r.status_code
        print('Status code:', self.status_code)
        return r

    def store_response(self):
        # Store response in a variable
        response = self.make_api_call()
        response_dict = response.json()
        self.total_repos = response_dict['total_count']
        print('Total repositories:', self.total_repos)
        return response_dict

    def explore_information(self):
        # Explore information about repositories
        repo = self.store_response()
        self.repo_dicts = repo['items']
        print('Repositories returned:', len(self.repo_dicts))
        return self.repo_dicts

    def populate_names(self):
        names = []
        repo_dicts = self.explore_information()
        for repo_dict in repo_dicts:
            names.append(repo_dict['name'])
        return names

    def populate_plot_dictionaries(self):
        plot_dicts = []
        repo_dicts = self.repo_dicts
        for repo_dict in repo_dicts:
            plot_dict = {
                'value': repo_dict['stargazers_count']
            }
            plot_dicts.append(plot_dict)
        return plot_dicts

    def make_vizio(self):
        # Make visualization
        my_style = LS('#333366', base_style=LCS)
        chart = pygal.Bar(style=my_style, x_label_rotation=45,
                          show_legend=False)
        chart.force_uri_protocol = 'http'
        chart.title = 'Most-Starred Python Projects on GitHub'
        x_labels = self.populate_names()
        chart.x_labels = x_labels

        populate_plot_dictionaries = self.populate_plot_dictionaries()
        chart.add('', populate_plot_dictionaries)
        chart.render_to_file('python_repos.svg')


pr = PythonRepos()
pr.make_vizio()
