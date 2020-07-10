database = ['Debaditya','Debangan','Pallabini','Pradeep','Pankaj','Manasi','Sujata']
admin = ['Debaditya','Debangan','Pallabini']

print("Enter username")
user = input("")

if user in database:
    print(f"Welcome back {user}")
    print("Want to continue ?")
    ans = input("")
    if ans == 'yes' and ans =='yes':
        print("Checking Permissions")
        if user in admin:
            print("Access Granted")
        elif user not in admin:
            print("Access Denied")
    elif ans == "No" and ans=='no':
        print('Thanks for trying out the beta version')
else:
    print("User Not Found!")
