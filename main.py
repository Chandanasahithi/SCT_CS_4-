from datetime import datetime

print("=" * 55)
print("         ADVANCED KEYSTROKE LOGGER")
print("=" * 55)

# Open log file
log_file = open("keystrokes.txt", "a")

# Add session header
log_file.write("\n")
log_file.write("=" * 50 + "\n")
log_file.write("Session Started: " + str(datetime.now()) + "\n")
log_file.write("=" * 50 + "\n")

print("\nStart typing below.")
print("Type 'exit' to stop the logger.\n")

while True:

    # User input
    text = input("Enter Text: ")

    # Stop condition
    if text.lower() == "exit":
        break

    # Current timestamp
    timestamp = datetime.now()

    # Save with timestamp
    log_entry = f"[{timestamp}] {text}\n"

    log_file.write(log_entry)

# Close file
log_file.write("\nSession Ended.\n")
log_file.close()

print("\nKeystrokes logged successfully!")
print("Logs saved in 'keystrokes.txt'")




to check the saved keystrokes code is
with open("keystrokes.txt", "r") as file:
    print(file.read())