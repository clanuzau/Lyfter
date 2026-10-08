"""
Student: Cesar Lanuza Urbina
Program : This code demonstrates the use of abstract base classes (ABCs) in Python to define a user system with different roles and permissions. 
The `User` class is an abstract base class that requires subclasses to implement the `get_role` and `has_permission` methods. 
The `AdminUser` and `RegularUser` classes inherit from `User` and provide specific implementations for these methods.
"""

from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name):
        # Store the name shared by all user types.
        self.name = name

    @abstractmethod
    def get_role(self):
        # Subclasses must define their role.
        pass

    @abstractmethod
    def has_permission(self, permission):
        # Subclasses must define which permissions they grant.
        pass


class AdminUser(User):
    def get_role(self):
        # Identify this user as an administrator.
        return "admin"

    def has_permission(self, permission):
        # Administrators have every permission.
        return True


class RegularUser(User):
    def get_role(self):
        # Identify this user as a regular user.
        return "regular"

    def has_permission(self, permission):
        # Regular users only have read permission.
        return permission == "read"


def main():
    # Create the example users and validate their roles and permissions.
    user1 = AdminUser("Carlos")
    user2 = RegularUser("Andrea")

    assert user1.get_role() == "admin"
    assert user2.get_role() == "regular"
    assert user1.has_permission("read") is True
    assert user1.has_permission("delete") is True
    assert user2.has_permission("read") is True
    assert user2.has_permission("delete") is False
    assert user2.has_permission("write") is False

    # Display each user's name and delete permission result.
    print()
    print(f"{user1.name}: permiso para eliminar = {user1.has_permission('delete')}")
    print(f"{user2.name}: permiso para eliminar = {user2.has_permission('delete')}")
    print()


if __name__ == "__main__":
    main()
