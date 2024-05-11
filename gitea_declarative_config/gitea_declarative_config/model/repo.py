"""Gitea Repo
"""

class Repo:
  """Gitea Repo
  """

  def __init__(self, json: dict):
    """Init a repo object

    Args:
        json (dict): A json returned by the API.
    """
    self._allow_merge_commits: bool = None
    self._allow_rebase: bool = None
    self._allow_rebase_explicit: bool = None
    self._allow_rebase_update: bool = None
    self._allow_squash_merge: bool = None
    self._archived: bool = None
    self._avatar_url: str = None
    self._clone_url: str = None
    self._created_at: str = None
    self._default_allow_maintainer_edit: bool = None
    self._default_branch: str = None
    self._default_delete_branch_after_merge: bool = None
    self._default_merge_style: str = None
    self._description: str = None
    self._empty: bool = None
    self._external_tracker: dict = None
    self._external_wiki: dict = None
    self._fork: bool = None
    self._full_name: str = None
    self._has_actions: bool = None
    self._has_issues: bool = None
    self._has_packages: bool = None
    self._has_projects: bool = None
    self._has_pull_requests: bool = None
    self._has_releases: bool = None
    self._has_wiki: bool = None
    self._html_url: str = None
    self._id: int = None
    self._ignore_whitespace_conflicts: bool = None
    self._internal: bool = None
    self._internal_tracker: dict = None
    self._language: str = None
    self._languages_url: str = None
    self._link: str = None
    self._mirror: bool = None
    self._mirror_interval: str = None
    self._name: str = None
    self._original_url: str = None
    self._owner: str = None
    self._parent: str = None
    self._permissions: dict = None
    self._private: bool = None
    self._repo_transfer: dict = None
    self._ssh_url: str = None
    self._template: bool = None
    self._url: str = None
    self._website: str = None
    # self._archived_at: str = None
    # self._forks_count: int = None
    # self._mirror_updated: str = None
    # self._open_issues_count: int = None
    # self._open_pr_counter: int = None
    # self._release_counter: int = None
    # self._size: int = None
    # self._stars_count: int = None
    # self._updated_at: str = None
    # self._watchers_count: int = None

    if json != {} :
      self._init_from_json(json)

  def _init_from_json(self, json: dict):
    """Init all attributes from a json returned by the API

    Args:
        json (dict): from a json returned by the API
    """
    self.allow_merge_commits = json['allow_merge_commits']
    self.allow_rebase = json['allow_rebase']
    self.allow_rebase_explicit = json['allow_rebase_explicit']
    self.allow_rebase_update = json['allow_rebase_update']
    self.allow_squash_merge = json['allow_squash_merge']
    self.archived = json['archived']
    self.avatar_url = json['avatar_url']
    self.clone_url = json['clone_url']
    self.created_at = json['created_at']
    self.default_allow_maintainer_edit = json['default_allow_maintainer_edit']
    self.default_branch = json['default_branch']
    self.default_delete_branch_after_merge = json['default_delete_branch_after_merge']
    self.default_merge_style = json['default_merge_style']
    self.description = json['description']
    self.empty = json['empty']
    self.external_tracker = json['external_tracker']
    self.external_wiki = json['external_wiki']
    self.fork = json['fork']
    self.full_name = json['full_name']
    self.has_actions = json['has_actions']
    self.has_issues = json['has_issues']
    self.has_packages = json['has_packages']
    self.has_projects = json['has_projects']
    self.has_pull_requests = json['has_pull_requests']
    self.has_releases = json['has_releases']
    self.has_wiki = json['has_wiki']
    self.html_url = json['html_url']
    self.id = json['id']
    self.ignore_whitespace_conflicts = json['ignore_whitespace_conflicts']
    self.internal = json['internal']
    self.internal_tracker = json['internal_tracker']
    self.language = json['language']
    self.languages_url = json['languages_url']
    self.link = json['link']
    self.mirror = json['mirror']
    self.mirror_interval = json['mirror_interval']
    self.name = json['name']
    self.original_url = json['original_url']
    self.owner = json['owner']
    self.parent = json['parent']
    self.permissions = json['permissions']
    self.private = json['private']
    self.repo_transfer = json['repo_transfer']
    self.ssh_url = json['ssh_url']
    self.template = json['template']
    self.url = json['url']
    self.website = json['website']

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.allow_merge_commits == other.allow_merge_commits and \
        self.allow_rebase == other.allow_rebase and \
        self.allow_rebase_explicit == other.allow_rebase_explicit and \
        self.allow_rebase_update == other.allow_rebase_update and \
        self.allow_squash_merge == other.allow_squash_merge and \
        self.archived == other.archived and \
        self.avatar_url == other.avatar_url and \
        self.clone_url == other.clone_url and \
        self.created_at == other.created_at and \
        self.default_allow_maintainer_edit == other.default_allow_maintainer_edit and \
        self.default_branch == other.default_branch and \
        self.default_delete_branch_after_merge == other.default_delete_branch_after_merge and \
        self.default_merge_style == other.default_merge_style and \
        self.description == other.description and \
        self.empty == other.empty and \
        self.external_tracker == other.external_tracker and \
        self.external_wiki == other.external_wiki and \
        self.fork == other.fork and \
        self.full_name == other.full_name and \
        self.has_actions == other.has_actions and \
        self.has_issues == other.has_issues and \
        self.has_packages == other.has_packages and \
        self.has_projects == other.has_projects and \
        self.has_pull_requests == other.has_pull_requests and \
        self.has_releases == other.has_releases and \
        self.has_wiki == other.has_wiki and \
        self.html_url == other.html_url and \
        self.id == other.id and \
        self.ignore_whitespace_conflicts == other.ignore_whitespace_conflicts and \
        self.internal == other.internal and \
        self.internal_tracker == other.internal_tracker and \
        self.language == other.language and \
        self.languages_url == other.languages_url and \
        self.link == other.link and \
        self.mirror == other.mirror and \
        self.mirror_interval == other.mirror_interval and \
        self.name == other.name and \
        self.original_url == other.original_url and \
        self.owner == other.owner and \
        self.parent == other.parent and \
        self.permissions == other.permissions and \
        self.private == other.private and \
        self.repo_transfer == other.repo_transfer and \
        self.ssh_url == other.ssh_url and \
        self.template == other.template and \
        self.url == other.url and \
        self.website == other.website
    else:
      return False



  @property
  def allow_merge_commits(self) -> bool:
    """allow_merge_commits

    Returns:
        bool: allow_merge_commits
    """
    return self._allow_merge_commits

  @allow_merge_commits.setter
  def allow_merge_commits(self, allow_merge_commits: bool):
    """allow_merge_commits

    Args:
        allow_merge_commits (bool): allow_merge_commits
    """
    self._allow_merge_commits = allow_merge_commits

  @property
  def allow_rebase(self) -> bool:
    """allow_rebase

    Returns:
        bool: allow_rebase
    """
    return self._allow_rebase

  @allow_rebase.setter
  def allow_rebase(self, allow_rebase: bool):
    """allow_rebase

    Args:
        allow_rebase (bool): allow_rebase
    """
    self._allow_rebase = allow_rebase

  @property
  def allow_rebase_explicit(self) -> bool:
    """allow_rebase_explicit

    Returns:
        bool: allow_rebase_explicit
    """
    return self._allow_rebase_explicit

  @allow_rebase_explicit.setter
  def allow_rebase_explicit(self, allow_rebase_explicit: bool):
    """allow_rebase_explicit

    Args:
        allow_rebase_explicit (bool): allow_rebase_explicit
    """
    self._allow_rebase_explicit = allow_rebase_explicit

  @property
  def allow_rebase_update(self) -> bool:
    """allow_rebase_update

    Returns:
        bool: allow_rebase_update
    """
    return self._allow_rebase_update

  @allow_rebase_update.setter
  def allow_rebase_update(self, allow_rebase_update: bool):
    """allow_rebase_update

    Args:
        allow_rebase_update (bool): allow_rebase_update
    """
    self._allow_rebase_update = allow_rebase_update

  @property
  def allow_squash_merge(self) -> bool:
    """allow_squash_merge

    Returns:
        bool: allow_squash_merge
    """
    return self._allow_squash_merge

  @allow_squash_merge.setter
  def allow_squash_merge(self, allow_squash_merge: bool):
    """allow_squash_merge

    Args:
        allow_squash_merge (bool): allow_squash_merge
    """
    self._allow_squash_merge = allow_squash_merge

  @property
  def archived(self) -> bool:
    """archived

    Returns:
        bool: archived
    """
    return self._archived

  @archived.setter
  def archived(self, archived: bool):
    """archived

    Args:
        archived (bool): archived
    """
    self._archived = archived

  @property
  def avatar_url(self) -> str:
    """avatar_url

    Returns:
        str: avatar_url
    """
    return self._avatar_url

  @avatar_url.setter
  def avatar_url(self, avatar_url: str):
    """avatar_url

    Args:
        avatar_url (str): avatar_url
    """
    self._avatar_url = avatar_url

  @property
  def clone_url(self) -> str:
    """clone_url

    Returns:
        str: clone_url
    """
    return self._clone_url

  @clone_url.setter
  def clone_url(self, clone_url: str):
    """clone_url

    Args:
        clone_url (str): clone_url
    """
    self._clone_url = clone_url

  @property
  def created_at(self) -> str:
    """created_at

    Returns:
        str: created_at
    """
    return self._created_at

  @created_at.setter
  def created_at(self, created_at: str):
    """created_at

    Args:
        created_at (str): created_at
    """
    self._created_at = created_at

  @property
  def default_allow_maintainer_edit(self) -> bool:
    """default_allow_maintainer_edit

    Returns:
        bool: default_allow_maintainer_edit
    """
    return self._default_allow_maintainer_edit

  @default_allow_maintainer_edit.setter
  def default_allow_maintainer_edit(self, default_allow_maintainer_edit: bool):
    """default_allow_maintainer_edit

    Args:
        default_allow_maintainer_edit (bool): default_allow_maintainer_edit
    """
    self._default_allow_maintainer_edit = default_allow_maintainer_edit

  @property
  def default_branch(self) -> str:
    """default_branch

    Returns:
        str: default_branch
    """
    return self._default_branch

  @default_branch.setter
  def default_branch(self, default_branch: str):
    """default_branch

    Args:
        default_branch (str): default_branch
    """
    self._default_branch = default_branch

  @property
  def default_delete_branch_after_merge(self) -> bool:
    """default_delete_branch_after_merge

    Returns:
        bool: default_delete_branch_after_merge
    """
    return self._default_delete_branch_after_merge

  @default_delete_branch_after_merge.setter
  def default_delete_branch_after_merge(self, default_delete_branch_after_merge: bool):
    """default_delete_branch_after_merge

    Args:
        default_delete_branch_after_merge (bool): default_delete_branch_after_merge
    """
    self._default_delete_branch_after_merge = default_delete_branch_after_merge

  @property
  def default_merge_style(self) -> str:
    """default_merge_style

    Returns:
        str: default_merge_style
    """
    return self._default_merge_style

  @default_merge_style.setter
  def default_merge_style(self, default_merge_style: str):
    """default_merge_style

    Args:
        default_merge_style (str): default_merge_style
    """
    self._default_merge_style = default_merge_style

  @property
  def description(self) -> str:
    """description

    Returns:
        str: description
    """
    return self._description

  @description.setter
  def description(self, description: str):
    """description

    Args:
        description (str): description
    """
    self._description = description

  @property
  def empty(self) -> bool:
    """empty

    Returns:
        bool: empty
    """
    return self._empty

  @empty.setter
  def empty(self, empty: bool):
    """empty

    Args:
        empty (bool): empty
    """
    self._empty = empty

  @property
  def external_tracker(self) -> dict:
    """external_tracker

    Returns:
        dict: external_tracker
    """
    return self._external_tracker

  @external_tracker.setter
  def external_tracker(self, external_tracker: dict):
    """external_tracker

    Args:
        external_tracker (dict): external_tracker
    """
    self._external_tracker = external_tracker

  @property
  def external_wiki(self) -> dict:
    """external_wiki

    Returns:
        dict: external_wiki
    """
    return self._external_wiki

  @external_wiki.setter
  def external_wiki(self, external_wiki: dict):
    """external_wiki

    Args:
        external_wiki (dict): external_wiki
    """
    self._external_wiki = external_wiki

  @property
  def fork(self) -> bool:
    """fork

    Returns:
        bool: fork
    """
    return self._fork

  @fork.setter
  def fork(self, fork: bool):
    """fork

    Args:
        fork (bool): fork
    """
    self._fork = fork

  @property
  def full_name(self) -> str:
    """full_name

    Returns:
        str: full_name
    """
    return self._full_name

  @full_name.setter
  def full_name(self, full_name: str):
    """full_name

    Args:
        full_name (str): full_name
    """
    self._full_name = full_name

  @property
  def has_actions(self) -> bool:
    """has_actions

    Returns:
        bool: has_actions
    """
    return self._has_actions

  @has_actions.setter
  def has_actions(self, has_actions: bool):
    """has_actions

    Args:
        has_actions (bool): has_actions
    """
    self._has_actions = has_actions

  @property
  def has_issues(self) -> bool:
    """has_issues

    Returns:
        bool: has_issues
    """
    return self._has_issues

  @has_issues.setter
  def has_issues(self, has_issues: bool):
    """has_issues

    Args:
        has_issues (bool): has_issues
    """
    self._has_issues = has_issues

  @property
  def has_packages(self) -> bool:
    """has_packages

    Returns:
        bool: has_packages
    """
    return self._has_packages

  @has_packages.setter
  def has_packages(self, has_packages: bool):
    """has_packages

    Args:
        has_packages (bool): has_packages
    """
    self._has_packages = has_packages

  @property
  def has_projects(self) -> bool:
    """has_projects

    Returns:
        bool: has_projects
    """
    return self._has_projects

  @has_projects.setter
  def has_projects(self, has_projects: bool):
    """has_projects

    Args:
        has_projects (bool): has_projects
    """
    self._has_projects = has_projects

  @property
  def has_pull_requests(self) -> bool:
    """has_pull_requests

    Returns:
        bool: has_pull_requests
    """
    return self._has_pull_requests

  @has_pull_requests.setter
  def has_pull_requests(self, has_pull_requests: bool):
    """has_pull_requests

    Args:
        has_pull_requests (bool): has_pull_requests
    """
    self._has_pull_requests = has_pull_requests

  @property
  def has_releases(self) -> bool:
    """has_releases

    Returns:
        bool: has_releases
    """
    return self._has_releases

  @has_releases.setter
  def has_releases(self, has_releases: bool):
    """has_releases

    Args:
        has_releases (bool): has_releases
    """
    self._has_releases = has_releases

  @property
  def has_wiki(self) -> bool:
    """has_wiki

    Returns:
        bool: has_wiki
    """
    return self._has_wiki

  @has_wiki.setter
  def has_wiki(self, has_wiki: bool):
    """has_wiki

    Args:
        has_wiki (bool): has_wiki
    """
    self._has_wiki = has_wiki

  @property
  def html_url(self) -> str:
    """html_url

    Returns:
        str: html_url
    """
    return self._html_url

  @html_url.setter
  def html_url(self, html_url: str):
    """html_url

    Args:
        html_url (str): html_url
    """
    self._html_url = html_url

  @property
  def id(self) -> int:
    """id

    Returns:
        int: id
    """
    return self._id

  @id.setter
  def id(self, id: int):
    """id

    Args:
        id (int): id
    """
    self._id = id

  @property
  def ignore_whitespace_conflicts(self) -> bool:
    """ignore_whitespace_conflicts

    Returns:
        bool: ignore_whitespace_conflicts
    """
    return self._ignore_whitespace_conflicts

  @ignore_whitespace_conflicts.setter
  def ignore_whitespace_conflicts(self, ignore_whitespace_conflicts: bool):
    """ignore_whitespace_conflicts

    Args:
        ignore_whitespace_conflicts (bool): ignore_whitespace_conflicts
    """
    self._ignore_whitespace_conflicts = ignore_whitespace_conflicts

  @property
  def internal(self) -> bool:
    """internal

    Returns:
        bool: internal
    """
    return self._internal

  @internal.setter
  def internal(self, internal: bool):
    """internal

    Args:
        internal (bool): internal
    """
    self._internal = internal

  @property
  def internal_tracker(self) -> dict:
    """internal_tracker

    Returns:
        dict: internal_tracker
    """
    return self._internal_tracker

  @internal_tracker.setter
  def internal_tracker(self, internal_tracker: dict):
    """internal_tracker

    Args:
        internal_tracker (dict): internal_tracker
    """
    self._internal_tracker = internal_tracker

  @property
  def language(self) -> str:
    """language

    Returns:
        str: language
    """
    return self._language

  @language.setter
  def language(self, language: str):
    """language

    Args:
        language (str): language
    """
    self._language = language

  @property
  def languages_url(self) -> str:
    """languages_url

    Returns:
        str: languages_url
    """
    return self._languages_url

  @languages_url.setter
  def languages_url(self, languages_url: str):
    """languages_url

    Args:
        languages_url (str): languages_url
    """
    self._languages_url = languages_url

  @property
  def link(self) -> str:
    """link

    Returns:
        str: link
    """
    return self._link

  @link.setter
  def link(self, link: str):
    """link

    Args:
        link (str): link
    """
    self._link = link

  @property
  def mirror(self) -> bool:
    """mirror

    Returns:
        bool: mirror
    """
    return self._mirror

  @mirror.setter
  def mirror(self, mirror: bool):
    """mirror

    Args:
        mirror (bool): mirror
    """
    self._mirror = mirror

  @property
  def mirror_interval(self) -> str:
    """mirror_interval

    Returns:
        str: mirror_interval
    """
    return self._mirror_interval

  @mirror_interval.setter
  def mirror_interval(self, mirror_interval: str):
    """mirror_interval

    Args:
        mirror_interval (str): mirror_interval
    """
    self._mirror_interval = mirror_interval

  @property
  def name(self) -> str:
    """name

    Returns:
        str: name
    """
    return self._name

  @name.setter
  def name(self, name: str):
    """name

    Args:
        name (str): name
    """
    self._name = name

  @property
  def original_url(self) -> str:
    """original_url

    Returns:
        str: original_url
    """
    return self._original_url

  @original_url.setter
  def original_url(self, original_url: str):
    """original_url

    Args:
        original_url (str): original_url
    """
    self._original_url = original_url

  @property
  def owner(self) -> str:
    """owner

    Returns:
        str: owner
    """
    return self._owner

  @owner.setter
  def owner(self, owner: str):
    """owner

    Args:
        owner (str): owner
    """
    self._owner = owner

  @property
  def parent(self) -> str:
    """parent

    Returns:
        str: parent
    """
    return self._parent

  @parent.setter
  def parent(self, parent: str):
    """parent

    Args:
        parent (str): parent
    """
    self._parent = parent

  @property
  def permissions(self) -> dict:
    """permissions

    Returns:
        dict: permissions
    """
    return self._permissions

  @permissions.setter
  def permissions(self, permissions: dict):
    """permissions

    Args:
        permissions (dict): permissions
    """
    self._permissions = permissions

  @property
  def private(self) -> bool:
    """private

    Returns:
        bool: private
    """
    return self._private

  @private.setter
  def private(self, private: bool):
    """private

    Args:
        private (bool): private
    """
    self._private = private

  @property
  def repo_transfer(self) -> dict:
    """repo_transfer

    Returns:
        dict: repo_transfer
    """
    return self._repo_transfer

  @repo_transfer.setter
  def repo_transfer(self, repo_transfer: dict):
    """repo_transfer

    Args:
        repo_transfer (dict): repo_transfer
    """
    self._repo_transfer = repo_transfer

  @property
  def ssh_url(self) -> str:
    """ssh_url

    Returns:
        str: ssh_url
    """
    return self._ssh_url

  @ssh_url.setter
  def ssh_url(self, ssh_url: str):
    """ssh_url

    Args:
        ssh_url (str): ssh_url
    """
    self._ssh_url = ssh_url

  @property
  def template(self) -> bool:
    """template

    Returns:
        bool: template
    """
    return self._template

  @template.setter
  def template(self, template: bool):
    """template

    Args:
        template (bool): template
    """
    self._template = template

  @property
  def url(self) -> str:
    """url

    Returns:
        str: url
    """
    return self._url

  @url.setter
  def url(self, url: str):
    """url

    Args:
        url (str): url
    """
    self._url = url

  @property
  def website(self) -> str:
    """website

    Returns:
        str: website
    """
    return self._website

  @website.setter
  def website(self, website: str):
    """website

    Args:
        website (str): website
    """
    self._website = website












# allow_merge_commits
# allow_rebase
# allow_rebase_explicit
# allow_rebase_update
# allow_squash_merge
# archived
# avatar_url
# clone_url
# created_at
# default_allow_maintainer_edit
# default_branch
# default_delete_branch_after_merge
# default_merge_style
# description
# empty
# external_tracker
# external_wiki
# fork
# full_name
# has_actions
# has_issues
# has_packages
# has_projects
# has_pull_requests
# has_releases
# has_wiki
# html_url
# id
# ignore_whitespace_conflicts
# internal
# internal_tracker
# language
# languages_url
# link
# mirror
# mirror_interval
# name
# original_url
# owner
# parent
# permissions
# private
# repo_transfer
# ssh_url
# template
# url
# website