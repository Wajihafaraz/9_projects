import time
# COUNTDOWN TIMER
# sb se phle user se input lenge hours, minute , seconds
hours=int(input("Enter an hours: "))
minutes=int(input("Enter a minutes: "))
seconds=int(input("Enter a seconds: "))

# Total seconds calculate karenge
Total_secs=(hours*3600) + (minutes*60) + seconds
# print(Total_secs)

# Countdown start 
while Total_secs > 0:
    hour = Total_secs // 3600  #floor division take decimal na ae
    minute = ( Total_secs % 3600 ) // 60  #iise humne minute nikale hn divide by 60 se
    second= (Total_secs % 60)

# Countdown ko formatted way me print karna

    print(f"🧭Time left: {hour:02}: {minute:02}:{second:02} ", end="\r") 
# end ka use isliye kiya he k result ek hi line me update ho yani jb timer chalte to next line me na jae aur r ka us isliye kiya he k jb ek dafa timer chale to cursor peche ajae aur purani value erase hojae aur new update hojae
    time.sleep(1)
    Total_secs-=1

print("\n ⏰Time's up!")    
























# # 45500sec\
# total_sec=37500
# hrs=total_sec//3600
# print(hrs) #1 hour

# remaining_sec=total_sec % 3600
# print(remaining_sec)  #900 se

# mins = remaining_sec // 60 # 15 mint
# print(mins)

# secs=remaining_sec % 60
# print(secs)

