class User:
    
    
    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.kwargs = kwargs
        self.login_attempts = 0

        kwargs['first_name'] = first_name
        kwargs['last_name'] = last_name

    def describe_user(self):
        for key, value in self.kwargs.items():
            print(f'{key}: {value}')
        print('\n')

    def greet_user(self):
        print(f"Greetings, {self.kwargs['first_name']}!\n")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):


    def __init__(self, first_name, last_name, privileges, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = privileges
        kwargs['privileges'] = privileges

    def show_privileges(self):
        for value in self.privileges:
            print(f"- {value}")


admin = Admin('Isaac', 'Diniz', ['can add post', 'can delete post', 'can ban user'])

admin.describe_user()
admin.show_privileges()