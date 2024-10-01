# import sys
# from utils.reference_generator import WikipediaReferenceGenerator

# def run_cli():
#     if len(sys.argv) != 2:
#         print("Usage: python main.py <Google News URL>")
#         sys.exit(1)

#     google_news_url = sys.argv[1]

#     try:
#         generator = WikipediaReferenceGenerator(google_news_url)
#         reference = generator.generate_reference()
#         print("\nGenerated Reference:")
#         print(reference)
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# if __name__ == "__main__":
#     run_cli()


# previous version below

# from gui import run_gui

# if __name__ == "__main__":
#     run_gui()