import os
from urllib.parse import urlparse

import git


class GitRepo:
    def __init__(self, path: str, remote: str, branch: str = 'master'):
        self.branch = branch if len(branch) > 0 else 'master'

        path = os.path.normpath(path)
        os.mkdir(path) if not os.path.isdir(path) else None
        self.path = path

        try:
            self.repo = git.repo.Repo(path)
        except git.InvalidGitRepositoryError:
            self.repo = git.repo.Repo.init(path)

        if 'origin' not in [str(x) for x in self.repo.remotes] and self._check_url(remote):
            self.repo.create_remote('origin', remote)
        for r in self.repo.remotes:
            r: git.Remote
            if r.name != 'origin':
                self.repo.delete_remote(r.name)
            else:
                if remote.lower() not in [x.lower() for x in r.urls]:
                    r.add_url(remote)
                for url in r.urls:
                    if str(url).lower() != remote.lower():
                        self.repo.remote(r.name).delete_url(url)

    @staticmethod
    def _check_url(url: str):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc, result.path])
        except:
            return False

    def check_repo(self):
        remote = self.repo.remote('origin')
        remote.update()

        if len(remote.refs) > 0:
            r_shas = [str(x.commit) for x in remote.refs if str(x.remote_head) == self.branch]
        else:
            r_shas = []

        l_sha = self.repo.head.is_valid()
        l_sha = len([x for x in self.repo.refs if not isinstance(x, git.RemoteReference)]) > 0 and l_sha
        l_sha = str(self.repo.head.commit) if l_sha else None

        return l_sha in r_shas and len(remote.refs) > 0 and len(r_shas) > 0

    def update_repo(self):
        if not self.check_repo():
            remote = self.repo.remote('origin')
            remote.update()
            remote.fetch(self.branch)
            return len(remote.pull(self.branch)) > 0
        else:
            return False

