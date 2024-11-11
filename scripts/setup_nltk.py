import nltk
import ssl


def download_nltk_data():
    """Download required NLTK data packages"""
    try:
        # Create an unverified context to avoid SSL issues
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        # Download required NLTK data
        packages = [
            'punkt',
            'stopwords',
            'wordnet',
            'averaged_perceptron_tagger'
        ]

        for package in packages:
            print(f"Downloading {package}...")
            nltk.download(package)

        print("\nAll NLTK packages downloaded successfully!")

    except Exception as e:
        print(f"Error downloading NLTK data: {str(e)}")
        print("\nAlternative manual installation:")
        print("1. Open Python console")
        print("2. Run the following commands:")
        print("   import nltk")
        print("   nltk.download('punkt')")
        print("   nltk.download('stopwords')")
        print("   nltk.download('wordnet')")
        print("   nltk.download('averaged_perceptron_tagger')")


if __name__ == "__main__":
    download_nltk_data()