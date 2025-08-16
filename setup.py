#!/usr/bin/env python3
"""
Setup script for Automated Research Article Generator
"""

import os
import sys
import subprocess
from pathlib import Path

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def setup_directories():
    """Create necessary directories"""
    print("📁 Setting up directories...")
    directories = ["outputs", "templates", "cache"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"   ✅ Created: {directory}/")

def setup_environment():
    """Setup environment variables"""
    print("🔧 Setting up environment...")
    
    env_template = """# Automated Research Article Generator Environment Variables
# Copy this to .env and fill in your API keys

# Required: OpenAI API Key (get from https://platform.openai.com/api-keys)
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Semantic Scholar API Key (get from https://www.semanticscholar.org/product/api)
SEMANTIC_SCHOLAR_API_KEY=your_semantic_scholar_key_here

# Optional: QuillBot API Key (for paraphrasing)
QUILLBOT_API_KEY=your_quillbot_key_here

# Optional: SciSpace API Key (for enhancement)
SCISPACE_API_KEY=your_scispace_key_here
"""
    
    env_file = Path(".env.example")
    if not env_file.exists():
        with open(env_file, 'w') as f:
            f.write(env_template)
        print(f"   ✅ Created: {env_file}")
        print("   📝 Please copy .env.example to .env and add your API keys")
    
def download_nltk_data():
    """Download required NLTK data"""
    print("📚 Downloading NLTK data...")
    import nltk
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("   ✅ NLTK data downloaded")
    except Exception as e:
        print(f"   ⚠️ NLTK download warning: {e}")

def create_sample_config():
    """Create sample configuration if it doesn't exist"""
    config_file = Path("config.yaml")
    if config_file.exists():
        print("   ✅ Config file already exists")
        return
    
    # The config.yaml content is already created in the artifacts
    print("   ✅ Default config.yaml will be created on first run")

def run_test():
    """Run a simple test"""
    print("🧪 Running basic test...")
    try:
        # Test imports
        import openai
        import scholarly
        import nltk
        from docx import Document
        print("   ✅ All core dependencies imported successfully")
        
        # Test basic functionality
        from research_article_generator import ResearchArticleGenerator
        print("   ✅ Main application imports successfully")
        
        return True
    except ImportError as e:
        print(f"   ❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"   ⚠️ Test warning: {e}")
        return True

def main():
    """Main setup function"""
    print("🚀 Setting up Automated Research Article Generator\n")
    
    try:
        install_requirements()
        setup_directories()
        setup_environment()
        download_nltk_data()
        create_sample_config()
        
        print("\n🎉 Setup completed successfully!")
        
        if run_test():
            print("\n✅ System ready! You can now:")
            print("   1. Add your API keys to .env file")
            print("   2. Run: python research_article_generator.py 'your research topic'")
            print("   3. Review generated articles in outputs/ directory")
        else:
            print("\n⚠️ Setup completed with warnings. Please check error messages above.")
            
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()