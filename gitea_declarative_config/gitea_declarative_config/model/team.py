"""Gitea Team
"""

class Team:
  """Gitea Team
  """

  VALID_UNITS = [
    "repo.code",
    "repo.issues",
    "repo.ext_issues",
    "repo.wiki", 
    "repo.pulls",
    "repo.releases",
    "repo.projects",
    "repo.ext_wiki" ] 
  
  VALID_PERMISSIONS = [
    'none',
    'read',
    'write',
    'admin',
    'owner' ]

  def __init__(self, json: dict):
    """Init a team object from a json returned by the API

    Args:
        json (dict): A json returned by the API.
    """
    self._id = json['id']
    self._name = json['name']
    self._description = json['description']
    self._includes_all_repositories = json['includes_all_repositories']
    self._can_create_org_repo = json['can_create_org_repo']
    self._organization  = json['organization']
    self._permission = json['permission']
    self._units = json['units']
    self._units_map = json['units_map']

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self._id == other.id and \
        self._name == other.name and \
        self._description == other.description and \
        self._includes_all_repositories == other.includes_all_repositories and \
        self._can_create_org_repo == other.can_create_org_repo and \
        self._organization == other.organization and \
        self._permission == other.permission and \
        self._units == other.units and \
        self._units_map == other.units_map
    else:
      return False

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
  def includes_all_repositories(self) -> bool:
    """includes_all_repositories

    Returns:
        bool: includes_all_repositories
    """
    return self._includes_all_repositories

  @includes_all_repositories.setter
  def includes_all_repositories(self, includes_all_repositories: bool):
    """includes_all_repositories

    Args:
        includes_all_repositories (bool): includes_all_repositories
    """
    self._includes_all_repositories = includes_all_repositories

  @property
  def can_create_org_repo(self) -> bool:
    """can_create_org_repo

    Returns:
        bool: can_create_org_repo
    """
    return self._can_create_org_repo

  @can_create_org_repo.setter
  def can_create_org_repo(self, can_create_org_repo: bool):
    """can_create_org_repo

    Args:
        can_create_org_repo (bool): can_create_org_repo
    """
    self._can_create_org_repo = can_create_org_repo

  @property
  def organization(self) -> str:
    """organization

    Returns:
        str: organization
    """
    return self._organization

  @organization.setter
  def organization(self, organization: str):
    """organization

    Args:
        organization (str): organization
    """
    self._organization = organization

  @property
  def permission(self) -> bool:
    """permission

    Returns:
        bool: permission
    """
    return self._permission

  @permission.setter
  def permission(self, permission: bool):
    """permission

    Args:
        permission (bool): permission
    """
    assert permission in Team.VALID_PERMISSIONS, "Invalid permission"
    self._permission = permission

  @property
  def units(self) -> list:
    """units

    Returns:
        list: units
    """
    return self._units

  @units.setter
  def units(self, units: list):
    """units

    Args:
        units (list): units
    """
    assert all(item in Team.VALID_UNITS for item in units), "Invalid units"
    self._units = units

  @property
  def units_map(self) -> dict:
    """units_map

    Returns:
        dict: units_map
    """
    return self._units_map

  @units_map.setter
  def units_map(self, units_map: dict):
    """units_map

    Args:
        units_map (dict): units_map
    """
    assert all(item in Team.VALID_UNITS for item in units_map.keys()), "Invalid units"
    assert all(item in Team.VALID_PERMISSIONS for item in units_map.values()), "Invalid permissions"
    self._units_map = units_map
