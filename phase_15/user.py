class User:

    def __init__(
        self,
        user_id,
        username,
        password,
        role
    ):

        self.id = user_id

        self.username = username

        self.password = password

        self.role = role


    def is_admin(self):

        return (
            self.role == "admin"
        )