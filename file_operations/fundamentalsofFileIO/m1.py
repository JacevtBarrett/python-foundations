# example chat bot conv
chat_history = [
    "User: Hi there!",
    "Bot: Hello! How can I help?",
    "User: What can you do?",
    "Bot: I can answer questions, provide information, and have conversations.",
    "User: Cool!",
    "Bot: Is there anything specific you'd like to know?",
]

# define the file path
file_path = "transcripts/03-19-2026_chat_log.txt"

file = open(file_path, "w") # Open the file in write mode)
for line in chat_history:
    file.write(line + "\n") # Write each line to the file with a newline character
file.close() # Close the file after writing

print(f"Chat history has been saved to {file_path}")

file = open(file_path, "r") # Open the file in read mode
contents = file.read() # Read the contents of the file
file.close() # Close the file after reading

print("\nTranscript Preview:\n")
print(contents) # Print the contents of the file