class Dog:
    """ Simples tentativa de modelar um cachorro """


    def __init__(self, name, age):
        """ Inicializa os atributos de nome e idade """
        self.name = name
        self.age = age

    def sit(self):
        """ Simula um cachorro sentando em resposta a um comando """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """ Simula um cachorro rolando em resposta a um comando """
        print(f"{self.name} rolled over!")

my_dog = Dog('Toby', 10)
my_dog.sit()
my_dog.roll_over()