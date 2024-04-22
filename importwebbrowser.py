import webbrowser

choice=int(input("1.whatsapp\n 2.youtube\n 3.instagram\n 4.facebook\n enter your choice:"))
           
if choice == 1:
    webbrowser.open("https://web.whatsapp.com/")
elif choice == 2:
    webbrowser.open("https://www.youtube.com/")
elif choice == 3:
    webbrowser.open ("https://www.instagram.com/")
elif choice == 4:
    webbrowser.open("https://www.facebook.com/")

else:
    print("invalid choice")
     