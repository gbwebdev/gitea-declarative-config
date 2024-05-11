"""Gitea User
"""

class User:
  """Gitea User
  """

  def __init__(self, json: dict):
    """Init a user object

    Args:
        json (dict): A json returned by the API.
    """
    self._active: bool = None
    self._avatar_url: str = None
    self._created: str = None
    self._description: str = None
    self._email: str = None
    self._followers_count: int = None
    self._following_count: int = None
    self._full_name: str = None
    self._id: int = None
    self._is_admin: bool = None
    self._language: str = None
    self._last_login: str = None
    self._location: str = None
    self._login: str = None
    self._login_name: str = None
    self._prohibit_login: bool = None
    self._restricted: bool = None
    self._starred_repos_count: int = None
    self._visibility: str = None
    self._website: str = None

    if json != {} :
      self._init_from_json(json)

  def _init_from_json(self, json: dict):
    """Init all attributes from a json returned by the API

    Args:
        json (dict): from a json returned by the API
    """
    self.active = json['active']
    self.avatar_url = json['avatar_url']
    self.created = json['created']
    self.description = json['description']
    self.email = json['email']
    self.followers_count = json['followers_count']
    self.following_count = json['following_count']
    self.full_name = json['full_name']
    self.id = json['id']
    self.is_admin = json['is_admin']
    self.language = json['language']
    self.last_login = json['last_login']
    self.location = json['location']
    self.login = json['login']
    self.login_name = json['login_name']
    self.prohibit_login = json['prohibit_login']
    self.restricted = json['restricted']
    self.starred_repos_count = json['starred_repos_count']
    self.visibility = json['visibility']
    self.website = json['website']

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self._active == other.active and \
        self._avatar_url == other.avatar_url and \
        self._created == other.created and \
        self._description == other.description and \
        self._email == other.email and \
        self._followers_count == other.followers_count and \
        self._following_count == other.following_count and \
        self._full_name == other.full_name and \
        self._id == other.id and \
        self._is_admin == other.is_admin and \
        self._language == other.language and \
        self._last_login == other.last_login and \
        self._location == other.location and \
        self._login == other.login and \
        self._login_name == other.login_name and \
        self._prohibit_login == other.prohibit_login and \
        self._restricted == other.restricted and \
        self._starred_repos_count == other.starred_repos_count and \
        self._visibility == other.visibility and \
        self._website == other.website
    else:
      return False

  @property
  def active(self) -> bool:
    """active

    Returns:
        bool: active
    """
    return self._active

  @active.setter
  def active(self, active: bool):
    """active

    Args:
        active (bool): active
    """
    self._active = active

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
  def created(self) -> str:
    """created

    Returns:
        str: created
    """
    return self._created

  @created.setter
  def created(self, created: str):
    """created

    Args:
        created (str): created
    """
    self._created = created

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
  def email(self) -> str:
    """email

    Returns:
        str: email
    """
    return self._email

  @email.setter
  def email(self, email: str):
    """email

    Args:
        email (str): email
    """
    self._email = email

  @property
  def followers_count(self) -> int:
    """followers_count

    Returns:
        int: followers_count
    """
    return self._followers_count

  @followers_count.setter
  def followers_count(self, followers_count: int):
    """followers_count

    Args:
        followers_count (int): followers_count
    """
    self._followers_count = followers_count

  @property
  def following_count(self) -> int:
    """following_count

    Returns:
        int: following_count
    """
    return self._following_count

  @following_count.setter
  def following_count(self, following_count: int):
    """following_count

    Args:
        following_count (int): following_count
    """
    self._following_count = following_count

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
  def is_admin(self) -> bool:
    """is_admin

    Returns:
        bool: is_admin
    """
    return self._is_admin

  @is_admin.setter
  def is_admin(self, is_admin: bool):
    """is_admin

    Args:
        is_admin (bool): is_admin
    """
    self._is_admin = is_admin

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
  def last_login(self) -> str:
    """last_login

    Returns:
        str: last_login
    """
    return self._last_login

  @last_login.setter
  def last_login(self, last_login: str):
    """last_login

    Args:
        last_login (str): last_login
    """
    self._last_login = last_login

  @property
  def location(self) -> str:
    """location

    Returns:
        str: location
    """
    return self._location

  @location.setter
  def location(self, location: str):
    """location

    Args:
        location (str): location
    """
    self._location = location

  @property
  def login(self) -> str:
    """login

    Returns:
        str: login
    """
    return self._login

  @login.setter
  def login(self, login: str):
    """login

    Args:
        login (str): login
    """
    self._login = login

  @property
  def login_name(self) -> str:
    """login_name

    Returns:
        str: login_name
    """
    return self._login_name

  @login_name.setter
  def login_name(self, login_name: str):
    """login_name

    Args:
        login_name (str): login_name
    """
    self._login_name = login_name

  @property
  def prohibit_login(self) -> bool:
    """prohibit_login

    Returns:
        bool: prohibit_login
    """
    return self._prohibit_login

  @prohibit_login.setter
  def prohibit_login(self, prohibit_login: bool):
    """prohibit_login

    Args:
        prohibit_login (bool): prohibit_login
    """
    self._prohibit_login = prohibit_login

  @property
  def restricted(self) -> bool:
    """restricted

    Returns:
        bool: restricted
    """
    return self._restricted

  @restricted.setter
  def restricted(self, restricted: bool):
    """restricted

    Args:
        restricted (bool): restricted
    """
    self._restricted = restricted

  @property
  def starred_repos_count(self) -> int:
    """starred_repos_count

    Returns:
        int: starred_repos_count
    """
    return self._starred_repos_count

  @starred_repos_count.setter
  def starred_repos_count(self, starred_repos_count: int):
    """starred_repos_count

    Args:
        starred_repos_count (int): starred_repos_count
    """
    self._starred_repos_count = starred_repos_count

  @property
  def visibility(self) -> str:
    """visibility

    Returns:
        str: visibility
    """
    return self._visibility

  @visibility.setter
  def visibility(self, visibility: str):
    """visibility

    Args:
        visibility (str): visibility
    """
    self._visibility = visibility

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
