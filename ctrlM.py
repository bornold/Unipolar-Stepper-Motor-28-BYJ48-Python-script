import readKey
import motor2

try:
    setup()
    print ("f back j forward")
    while True:
        char = getch()
        if (char == "j"):
            forward()
        elif (char == "f"):
            back()
        else:
            break
finally:
    cleanup()