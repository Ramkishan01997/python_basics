import win32com.client

def read_outlook_emails(folder_name="Inbox", num_emails=10):
    try:
        # Initialize the Outlook application
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

        # Access the folder (e.g., Inbox)
        inbox = outlook.Folders.Item(1).Folders[folder_name]
        
        # Fetch the items (emails) in the folder
        messages = inbox.Items
        messages.Sort("[ReceivedTime]", True)  # Sort emails by received time (newest first)

        print(f"Reading the latest {num_emails} emails from the {folder_name} folder...\n")

        for i, message in enumerate(messages[:num_emails], 1):
            try:
                print(f"Email {i}:")
                print(f"Subject: {message.Subject}")
                print(f"Sender: {message.SenderName}")
                print(f"Received: {message.ReceivedTime}")
                print(f"Body: {message.Body[:100]}...")  # Print first 100 characters of the email body
                print("-" * 50)
            except Exception as e:
                print(f"Error reading email {i}: {e}")
    except Exception as e:
        print(f"Error accessing Outlook: {e}")

# Call the function to read emails
read_outlook_emails()
