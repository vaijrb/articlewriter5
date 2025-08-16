# Automated Research Article Generator

A comprehensive Python application that automatically generates complete research articles from topic input, complete with literature review, proper citations, and APA7 formatting.

## 🎯 Features

- **Automated Research**: Searches Google Scholar, Semantic Scholar, and arXiv
- **Intelligent Content Generation**: Uses GPT-4 to create academic content
- **Proper Citations**: Automatically generates APA7 format citations and bibliography  
- **Multiple Formats**: Outputs to Word (.docx) and Markdown formats
- **Quality Control**: Includes readability analysis and generation reports
- **Extensible**: Support for QuillBot and SciSpace integration

## 📋 Requirements

- Python 3.8+
- OpenAI API key (required)
- Internet connection for academic database searches

## 🚀 Quick Start

### 1. Installation

```bash
# Clone or download the project files
git clone <repository-url>
cd research-article-generator

# Run setup script
python setup.py
```

### 2. Configuration

```bash
# Copy environment template and add your API keys
cp .env.example .env
# Edit .env with your API keys
# Pre-release Developers - Request for a config.yaml file
```

Required API key:
- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)

Optional API keys (for enhanced features):
- **Semantic Scholar**: [Semantic Scholar API](https://www.semanticscholar.org/product/api)
- **QuillBot**: For content paraphrasing
- **SciSpace**: For content enhancement

### 3. Generate Your First Article

```bash
python research_article_generator.py "artificial intelligence in healthcare"
```

## 📖 Usage

### Basic Usage

```bash
python research_article_generator.py "your research topic"
```

### Advanced Usage

```bash
# Specify custom config and output directory
python research_article_generator.py "machine learning" --config my_config.yaml --output my_results/

# Enable verbose logging
python research_article_generator.py "data science" --verbose
```

### Programmatic Usage

```python
from research_article_generator import ResearchArticleGenerator

# Initialize generator
generator = ResearchArticleGenerator()

# Generate article
result = generator.generate_article("artificial intelligence ethics")

if result["status"] == "success":
    print(f"Generated: {result['title']}")
    print(f"Files: {result['files']}")
```

## 📁 Output Structure

After generation, you'll find:

```
outputs/
├── research_article_20240101_120000.docx    # Main article (Word format)
├── research_article_20240101_120000.md      # Markdown version
└── generation_report_20240101_120000.md     # Quality report
```

### Generated Article Sections

1. **Title Page** - Research-appropriate title
2. **Abstract** - 250-word summary
3. **Keywords** - 5-7 relevant keywords
4. **Introduction** - Context and research question
5. **Literature Review** - Comprehensive analysis of existing research
6. **Methodology** - Research approach and methods
7. **Results** - Findings presentation
8. **Conclusion** - Summary and implications
9. **References** - APA7 formatted bibliography

## ⚙️ Configuration

The `config.yaml` file controls all aspects of generation:

```yaml
# Search settings
search:
  max_papers: 20
  min_citation_count: 5
  search_sources: ["semantic_scholar", "google_scholar", "arxiv"]

# Generation settings  
generation:
  model: "gpt-5-mini"
  temperature: 0.7
  target_word_counts:
    abstract: 250
    introduction: 800
    literature_review: 1500
    # ... etc
```

## 🔧 Customization

### Custom Prompts

Modify the prompt templates in the `ArticleGenerator` class:

```python
def _get_introduction_prompt(self) -> str:
    return """
    Your custom introduction prompt here...
    """
```

### Additional Search Sources

Add new search sources by extending the `PaperSearcher` class:

```python
def search_new_source(self, query: str) -> List[ResearchPaper]:
    # Implement your search logic
    pass
```

### Custom Output Formats

Extend the `DocumentFormatter` class:

```python
def create_latex(self, title: str, sections: List[ArticleSection]) -> str:
    # Implement LaTeX export
    pass
```

## 📊 Quality Features

- **Readability Analysis**: Flesch Reading Ease scoring
- **Citation Tracking**: Ensures proper academic referencing
- **Duplicate Detection**: Removes duplicate papers from literature
- **Content Enhancement**: Optional QuillBot/SciSpace integration
- **Generation Reports**: Detailed quality metrics

## 🤝 Integration Options

### QuillBot Integration
```python
# Automatic paraphrasing to reduce similarity
rewriter = ContentRewriter(config)
enhanced_content = rewriter.rewrite_with_quillbot(original_content)
```

### SciSpace Integration
```python
# Academic writing enhancement
enhanced_content = rewriter.enhance_with_scispace(original_content)
```

## 📚 Academic Sources

The application searches:
- **Semantic Scholar**: 200M+ academic papers
- **Google Scholar**: Comprehensive academic search
- **arXiv**: Preprint repository for cutting-edge research

## ⚠️ Important Notes

### For Journal Submission

1. **Review Generated Content**: Always review and customize the generated article
2. **Verify Citations**: Cross-check all references with original sources  
3. **Add Specifics**: Include your actual research data, methodology details
4. **Plagiarism Check**: Run through plagiarism detection tools
5. **Journal Guidelines**: Adapt formatting to specific journal requirements

### Limitations

- Generated content requires human review and customization
- Methodology section needs adaptation to your specific research
- Results section requires your actual research data
- Some journal-specific formatting may need manual adjustment

## 🛠️ Troubleshooting

### Common Issues

**"No papers found" error:**
```bash
# Try broader search terms
python research_article_generator.py "machine learning" instead of "deep convolutional neural networks for medical image segmentation"
```

**API rate limiting:**
```bash
# Reduce search scope in config.yaml
search:
  max_papers: 10
```

**Memory issues:**
```bash
# Use smaller model or reduce token limits
generation:
  model: "gpt-3.5-turbo"
  max_tokens: 1000
```

## 📈 Performance Tips

1. **Use Specific Topics**: More specific = better results
2. **Configure Search Sources**: Enable all sources for comprehensive coverage
3. **Optimize Word Counts**: Adjust target lengths per journal requirements
4. **Use API Keys**: Semantic Scholar API key improves search quality

## 🔄 Updates and Maintenance

The application includes automatic configuration management and graceful error handling. Update dependencies regularly:

```bash
pip install -r requirements.txt --upgrade
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues, feature requests, or questions:
1. Check the troubleshooting section
2. Review configuration settings
3. Ensure API keys are properly set
4. Check logs for detailed error messages

## 🎯 Roadmap

- [ ] PDF generation with LaTeX support
- [ ] Integration with more academic databases
- [ ] Advanced plagiarism detection
- [ ] Multi-language support
- [ ] Web interface
- [ ] Collaborative editing features

---

**⚡ Ready to revolutionize your research workflow? Generate your first article in minutes!**