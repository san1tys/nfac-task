class UserManager:

    def __init__(self):
        self.users = {}
        self.next_id = 1

    def addUser(self, name: str) -> int:
        if not name:
            raise ValueError("Имя пользователя не может быть пустым")
        user_id = self.next_id
        self.users[user_id] = name
        self.next_id += 1
        return user_id

    def getUser(self, user_id: int) -> str:
        return self.users.get(user_id)

    def deleteUser(self, user_id: int) -> bool:
        return self.users.pop(user_id, None) is not None

    def findUserByName(self, name: str) -> list[int]:
        return [
            user_id for user_id, user_name in self.users.items() if user_name == name
        ]

    def __str__(self) -> str:
        return f"UserManager(users={self.users})"


# userManager = UserManager()

# id1 = userManager.addUser("Jarasar")
# id2 = userManager.addUser("Adil")
# id3 = userManager.addUser("Jarasar")

# print(userManager.getUser(id1))  # Вернет "Jarasar"
# print(userManager.getUser(id2))  # Вернет "Adil"
# print(userManager.getUser(999))  # Вернет None

# print(userManager.findUserByName("Jarasar"))  # Вернет [id1, id3]
# print(userManager.findUserByName("Baha"))  # Вернет []

# print(userManager.deleteUser(id2))  # Вернет True
# print(userManager.deleteUser(999))  # Вернет False

# print(userManager.getUser(id2))  # Вернет None

# print(userManager)  # UserManager(users={1: 'Jarasar', 3: 'Jarasar'})
