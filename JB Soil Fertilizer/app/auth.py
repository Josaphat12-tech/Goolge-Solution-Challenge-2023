import shelve


def login():
    with shelve.open('users') as db:
        if 'username' not in db:
            db['username'] = ['admin', 'user']
            db['password'] = ['123456789', 'user']
        print(db['username'])
        print(db['password'])

        temp1 = input("username: ")
        temp2 = input("password: ")
        flag = False
        for i in range(len(db['username'])):
            if temp1 == db['username'][i] and temp2 == db['password'][i]:
                flag = True
                break

        if flag:
            print("login success")
            # window.location.replace('Code/Web%20Application/src/home.html');
        else:
            print("Invalid Credentials")


def signup():
    with shelve.open('users') as db:
        if 'username' not in db:
            db['username'] = ['admin', 'user']
            db['password'] = ['123456789', 'user']
        temp1 = input("username: ")
        temp2 = input("password: ")

        if temp1 and temp2:
            flag = True
            for i in range(len(db['username'])):
                if temp1 == db['username'][i]:
                    flag = False
                    break

            if flag:
                db['username'].append(temp1)
                db['password'].append(temp2)
                print("Account Created")
                # window.location.replace('index.html');
            else:
                print("Username Already Exists")
        else:
            print("Fill the Sign Up form completly")


def forgot():
    with shelve.open('users') as db:
        if 'username' not in db:
            db['username'] = ['admin', 'user']
            db['password'] = ['123456789', 'user']
        temp1 = input("username: ")
        temp2 = input("password: ")

        flag = False
        for i in range(len(db['username'])):
            if temp1 == db['username'][i]:
                db['password'][i] = temp2
                flag = True
                break

        if flag:
            print("Password Changed")
            # window.location.replace('index.html')
        else:
            print("No User Found")
