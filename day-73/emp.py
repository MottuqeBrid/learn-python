class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __len__(self):
        return len(self.name)

    def __str__(self) -> str:
        return f"Name: {self.name}, ID: {self.id}"

    def __repr__(self) -> str:
        return f"Employee(name={self.name}, id={self.id})"

    def __call__(self):
        print(f"Name: {self.name}, ID: {self.id}")
