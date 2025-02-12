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


me = User('Isaac', 'Diniz', hobbies='reading and coding')
me.describe_user()
me.greet_user()

for _ in range(5):
    me.increment_login_attempts()
    print(f"{me.first_name} has {me.login_attempts} login attempts.")
    
me.reset_login_attempts()
print(f"\n{me.first_name} has {me.login_attempts} login attempts")