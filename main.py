import argparse
from github import Github


class GithubHandler:
    def __init__(self, name, token, org_name):
        self.name = name
        self.token = token
        self.org_name = org_name
        self.git = Github(token)
        self.user = self.git.get_user(self.name)
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

    parser.add_argument("-n", "--name", help="Username for login.")
    parser.add_argument("-t", "--token", help="Token for API access.")
    parser.add_argument("-o", "--org", help="Name of organization.")
    parser.add_argument("-r", "--repo", help="Name of code repository.")

    parser.add_argument("-c", "--create", dest="create", action="store_const", const="create", help="Create code repository.")
    parser.add_argument("-d", "--delete", dest="delete", action="store_const", const="delete", help="Delete code repository.")

    args = parser.parse_args()

    gh = GithubHandler(args.name, args.token, args.org)
    if args.create:
        gh.create_org_repo(args.repo)
    elif args.delete:
        gh.delete_org_repo(args.repo)


if __name__ == '__main__':
    main()
