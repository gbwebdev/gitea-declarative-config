"""Gitea Organization
"""
from typing import List

from gitea_declarative_config.model.repo import Repo

class Organization:
  """Gitea organization
  """
  def __init__(self, json: dict):
    """Init an organsization object.

    Args:
        json (dict): A json returned by the API.
    """
    self._avatar_url: str = None
    self._description: str = None
    self._email: str = None
    self._full_name: str = None
    self._id: int = None
    self._location: str = None
    self._name: str = None
    self._repo_admin_change_team_access: bool = None
    self._visibility: str = None
    self._website: str = None

    self._teams = None
    self._repos: List[Repo] = []

    if json != {} :
      self._init_from_json(json)

  def _init_from_json(self, json: dict):
    """Init all attributes from a json returned by the API

    Args:
        json (dict): from a json returned by the API
    """
    self.avatar_url = json['avatar_url']
    self.description = json['description']
    self.email = json['email']
    self.full_name = json['full_name']
    self.id = json['id']
    self.location = json['location']
    self.name = json['name']
    self.repo_admin_change_team_access = json['repo_admin_change_team_access']
    self.visibility = json['visibility']
    self.website = json['website']

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self._avatar_url == other._avatar_url \
        and self._description == other._description \
        and self._email == other._email \
        and self._full_name == other._full_name \
        and self._id == other._id \
        and self._location == other._location \
        and self._name == other._name \
        and self._repo_admin_change_team_access == other._repo_admin_change_team_access \
        and self._visibility == other._visibility \
        and self._website == other._website 
    else:
        return False


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
  def repo_admin_change_team_access(self) -> bool:
    """repo_admin_change_team_access

    Returns:
        bool: repo_admin_change_team_access
    """
    return self._repo_admin_change_team_access

  @repo_admin_change_team_access.setter
  def repo_admin_change_team_access(self, repo_admin_change_team_access: bool):
    """repo_admin_change_team_access

    Args:
        repo_admin_change_team_access (bool): repo_admin_change_team_access
    """
    self._repo_admin_change_team_access = repo_admin_change_team_access

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
    assert visibility in ['public', 'private', 'limited']
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
