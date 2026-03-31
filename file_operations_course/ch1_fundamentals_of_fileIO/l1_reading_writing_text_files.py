from pathlib import Path

def write_txt_file():
    BASE_DIR = Path(__file__).parent # Get the directory of the current file
    chat_log = BASE_DIR / "transcripts" / "03-19-2026_chat_log.txt" # Define the path to the chat log file

    # example chat bot conv
    chat_history = [
        "User: Hi there!",
        "Bot: Hello! How can I help?",
        "User: What can you do?",
        "Bot: I can answer questions, provide information, and have conversations.",
        "User: Cool!",
        "Bot: Is there anything specific you'd like to know?",
    ]

    file = open(chat_log, "w") # Open the file in write mode)
    for line in chat_history:
        file.write(line + "\n") # Write each line to the file with a newline character
    file.close() # Close the file after writing

    print(f"Chat history has been saved to {chat_log}.")

    file = open(chat_log, "r") # Open the file in read mode
    contents = file.read() # Read the contents of the file
    file.close() # Close the file after reading

    print("\nTranscript Preview:\n")
    print(contents) # Print the contents of the file

    return chat_log

if __name__ == "__main__":
    write_txt_file()