# A basic program that asks a user for some information, and prints the information back to the user

# Asker asks for your name, age, address, phone, and prints it back

def asker():
    print "=================================" * 5
    name = raw_input("Hello what is your name? ")
    age = raw_input("How old are you? ")
    address = raw_input("Where are you based? ")
    phone = raw_input("Your phone: ")
    print ("Your name is %s, and you are %s years old, living at %s and i can reach you on %s." % (name, age, address, phone))

def main():
    return asker()

main()
