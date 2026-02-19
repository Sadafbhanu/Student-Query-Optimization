
## Student Query Understanding (Q1 – Thinkplus Tech Assessment)

This project implements **Problem Statement Q1: Student Query Understanding** from the Thinkplus AI/ML Engineer assessment.  
Given a natural-language student query (e.g., “I don’t understand backpropagation”), the system predicts:

- **intent**: one of `Explanation`, `Example`, `Doubt clarification`, `Revision`
- **topic**: e.g., `Backpropagation`, `Optimization`, `Neural Networks`, etc.
- **difficulty_level**: one of `Beginner`, `Intermediate`, `Advanced`

Under the hood, it combines **sentence embeddings**, **classical ML classifiers**, and an optional **LLM refinement step**.

### 1. Setup

1. Create and activate a Python environment (3.10+ recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Data

The core training data is a small synthetic dataset of labeled, student-style queries:

- File: `data/student_queries_labeled.csv`
- Columns: `text`, `intent`, `topic`, `difficulty`

You can (re)generate this dataset using:

```bash
python -m src.data_prep
```

The synthetic generation procedure, assumptions, and limitations are documented in the technical write-up (not included here).

### 3. Training the models

Train the intent, topic, and difficulty classifiers on sentence embeddings:

```bash
python -m src.models
```

This will:

- Load `data/student_queries_labeled.csv`
- Compute sentence embeddings with a pre-trained transformer
- Train separate classifiers for `intent`, `topic`, and `difficulty`
- Save trained models under `models/`

### 4. Running inference

Use `main.py` to classify a single query from the command line:

```bash
python main.py --query "I don't understand backpropagation."
```

This returns a JSON object like:

```json
{
  "intent": "Explanation",
  "topic": "Backpropagation",
  "difficulty_level": "Intermediate"
}
```

To enable the optional **LLM refinement** step, set your OpenAI credentials (for example, `OPENAI_API_KEY`) and run:

```bash
python main.py --query "I don't understand backpropagation." --use-llm
```

This will call the refinement layer and return a JSON object of the form:

```json
{
  "ml_prediction": {
    "intent": "Explanation",
    "topic": "Backpropagation",
    "difficulty_level": "Intermediate",
    "raw_scores": { "..." : "..." }
  },
  "final_prediction": {
    "intent": "Explanation",
    "topic": "Backpropagation",
    "difficulty_level": "Intermediate"
  }
}
```

### 5. Notes

- Uses only **pre-trained models** (no large-scale training from scratch).
- Models and code are modular so that additional intents, topics, or difficulty levels can be added later.
