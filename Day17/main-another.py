""# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class User:
    def __init__(self, user_id,user_username): #init constructor func olarak çalışıyor.
        print("cagirildim")
        self.id=user_id
        self.username=user_username
        self.followers=0
        self.following =0

    def follow(self, user):
        user.followers+=1
        self.following+=1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    user_1 = User("001","berkay")
    user_2 = User("002","kemal")

    user_1.follow(user_2)
    print(user_1.followers)
    print(user_1.following)
    print(user_2.followers)
    print(user_2.following)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
