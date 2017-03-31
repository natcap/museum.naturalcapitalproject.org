import subprocess

import webapp2

MUSEUM = 'museum.naturalcapitalproject.org'
REPO = 'https://bitbucket.org/natcap/%s' % MUSEUM
DEST_DIR = 'museum_repo'


class Main(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Updating museum')

        subprocess.call('hg clone {repo} -u tip {dest}'.format(
            repo=REPO, dest=DEST_DIR), shell=True)
        subprocess.call('gsutil rsync -d ./* gs://%s' % MUSEUM,
                        shell=True)


app = webapp2.WSGIApplication([
    ('/', Main),
], debug=True)
