from utils.reference_generator import WikipediaReferenceGenerator

def main():
    try:
        # Get Google News URL from the user
        google_link = input("Enter the Google News URL: ").strip()

        # Validate input
        if not google_link:
            print("Please enter a valid Google News URL.")
            return

        # Generate Wikipedia reference
        generator = WikipediaReferenceGenerator(google_link)
        reference = generator.generate_reference()

        # Print the generated reference
        print("\nGenerated Wikipedia Reference:")
        print(reference)

        # Copy to clipboard if on MacOS
        try:
            import pyperclip
            pyperclip.copy(reference)
            print("\nThe reference has been copied to your clipboard.")
        except ImportError:
            print("\nIf you want clipboard support, install the 'pyperclip' package.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
