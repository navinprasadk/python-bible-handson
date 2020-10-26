#email slicer project
#get email id from user
email = input("what is your email address?:").strip()

#get username from mail id
username = email[:email.index("@")]

#slice domain name
domain = email[email.index("@")+1:]

#format message
output = "Your username is {} and your domain is {}".format(username,domain)

#display message
print(output)
