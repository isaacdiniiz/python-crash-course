class User:
    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.kwargs = kwargs

        kwargs['first_name'] = first_name
        kwargs['last_name'] = last_name

    def describe_user(self):
        for key, value in self.kwargs.items():
            print(f'{key}: {value}')
        print('\n')

    def greet_user(self):
        print(f"Greetings, {self.kwargs['first_name']}!\n")


me = User('Isaac', 'Diniz', hobbies='reading and coding')
me.describe_user()
me.greet_user()