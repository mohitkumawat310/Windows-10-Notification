from win10toast import ToastNotifier

test = ToastNotifier()

test.show_toast("Test", "I hope it will work", duration=5)

print("It worked")
