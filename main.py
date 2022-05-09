import argparse
import configparser
from github import Github


class GithubHandler:
    def __init__(self, name, token, org_name):
        self.name = name
        self.token = token
        self.org_name = org_name
        self.git = Github(token)
        self.user = self.git.get_user()
        if org_name:
            self.organization = self.git.get_organization(self.org_name)

    @staticmethod
    def __create_repo(repo_type, repo_name):
        repo_type.create_repo(
            repo_name,
            allow_rebase_merge=True,
            auto_init=False,
            description='this is a public test',
            has_issues=True,
            has_projects=False,
            has_wiki=False,
            private=False,
        )

    @staticmethod
    def __delete_repo(repo_type, repo_name):
        repo = repo_type.get_repo(repo_name)
        repo.delete()

    def create_org_repo(self, repo_name):
        self.__create_repo(self.organization, repo_name)

    def create_user_repo(self, repo_name):
        self.__create_repo(self.user, repo_name)

    def delete_org_repo(self, repo_name):
        self.__delete_repo(self.organization, repo_name)

    def delete_user_repo(self, repo_name):
        self.__delete_repo(self.user, repo_name)


def main():
    parser = argparse.ArgumentParser()
    config = configparser.ConfigParser()
    ghconfig = 'gh.ini'

    config.read(ghconfig)

    if 'github.org' not in config.sections():
        print(f"No populated {ghconfig} github config file found. Exiting.")
        exit(1)

    parser.add_argument("-r", "--repo", help="Name of code repository.")

    parser.add_argument("-c", "--create", dest="create", action="store_const", const="create", help="Create code repository.")
    parser.add_argument("-d", "--delete", dest="delete", action="store_const", const="delete", help="Delete code repository.")

    args = parser.parse_args()

    user = config['github.org']['User']
    token = config['github.org']['Token']
    org = config['github.org']['Organization']

    if not user or not token:
        print(f"No proper GitHub username and/or token was found, please check {ghconfig} exists and is populated. Exiting.")
        exit(1)

    gh = GithubHandler(user, token, org)
    create = gh.create_org_repo if org else gh.create_user_repo
    delete = gh.delete_org_repo if org else gh.delete_user_repo

    if args.create:
        create(args.repo)
    elif args.delete:
        delete(args.repo)


if __name__ == '__main__':
    main()
