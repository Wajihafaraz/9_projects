import random,string

user_password=int(input("How many passwords you want?  "))
Length= int(input("Enter a length of password you want: "))

# Password banane ke liye characters collect karna

characters = string.ascii_letters + string.digits + string.punctuation



for _ in range(user_password):# 5 dafa chalega loop agar user ne 5 dia
    password = ("").join(random.choice(characters) for _ in range(Length))

    print(f"Generated password🔐 {password}")
     
