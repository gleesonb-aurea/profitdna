# ProfitDNA Analyzer

A powerful tool that analyzes product ideas and generates structured revenue strategies using AI-driven insights.

## Features

- Revenue Strategy Analysis
- Implementation Strategy Generation
- Financial Summary and Projections
- AI-powered Market Analysis
- Automated Strategy Generation

## Prerequisites

- Python 3.8+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/profitdna.git
cd profitdna
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run main.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter your OpenAI API key in the sidebar

4. Input your product description and click "Analyze Product"

## Project Structure

```
profitdna/
├── main.py             # Main Streamlit application
├── ai_analyzer.py      # AI analysis logic
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## License

MIT License - see LICENSE file for details
