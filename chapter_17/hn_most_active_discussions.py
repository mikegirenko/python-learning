import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code', r.status_code)

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

title, comments = [], []
for submission_dict in submission_dicts:
    title.append(submission_dict['title'])
    comments.append(submission_dict['comments'])

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most active discussions currently happening on Hacker News'
chart.x_labels = title
chart.add('', comments)
chart.render_to_file('hn_most_active_discussions.svg')
