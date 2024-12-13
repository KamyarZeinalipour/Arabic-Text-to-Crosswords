# Arabic Crossword Clue Generator

## Abstract

*We present an Arabic crossword puzzle generator from a given text that utilizes advanced language models such as **GPT-4-Turbo**, **GPT-3.5-Turbo**, and **Llama3-8B-Instruct**. Specifically developed for educational purposes, this innovative generator leverages a meticulously compiled dataset named **Arabic-Clue-Instruct** with over 50,000 entries encompassing text, answers, clues, and categories. This dataset is intricately designed to aid in the generation of pertinent clues linked to specific texts and keywords within defined categories.*

*This project addresses the scarcity of advanced educational tools tailored for the Arabic language, promoting enhanced language learning and cognitive development. By providing a culturally and linguistically relevant tool, our objective is to make learning more engaging and effective through gamification and interactivity. Integrating state-of-the-art artificial intelligence with contemporary learning methodologies, this tool can generate crossword puzzles from any given educational text, thereby facilitating an interactive and enjoyable learning experience. This tool not only advances educational paradigms but also sets a new standard in interactive and cognitive learning technologies. The model and dataset are publicly available.*

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Model and Dataset](#model-and-dataset)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Usage](#usage)
  - [Command-line Arguments](#command-line-arguments)
  - [Input File Format](#input-file-format)
  - [Output File Format](#output-file-format)
  - [Examples](#examples)
- [Code Overview](#code-overview)
  - [Main Functions](#main-functions)
  - [Workflow](#workflow)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

The Arabic Crossword Clue Generator is a tool designed to create Arabic crossword clues based on provided text, keywords, and specific categories. Leveraging advanced language models and a comprehensive dataset, this project aims to enhance Arabic language learning through gamification and interactive learning experiences.

By focusing on educational applications, this generator addresses the need for advanced tools tailored specifically for the Arabic language, supporting both educators and learners in the process of cognitive development and language proficiency.

## Features

- **Arabic Language Support:** Generates crossword clues in Arabic, catering to native speakers and learners.
- **English Categories:** Accepts categories specified in English to categorize the clues appropriately.
- **Education-Focused:** Designed to aid in language learning and cognitive development.
- **Advanced AI Models:** Utilizes models like **Llama3-8B-Instruct** for high-quality clue generation.
- **Customizable Inputs:** Accepts custom text, keywords, and categories for flexible clue generation.
- **Publicly Available Models and Datasets:** Open access to the underlying models and datasets for transparency and further development.

## Model and Dataset

- **Model:** [Kamyar-zeinalipour/Llama3-8B-Ar-Text-to-Cross](https://huggingface.co/Kamyar-zeinalipour/Llama3-8B-Ar-Text-to-Cross)
- **Dataset:** **Arabic-Clue-Instruct** with over 50,000 entries, including text, answers, clues, and categories.

Both the model and the dataset are publicly available, encouraging community engagement and contributions to the project's growth.

## Installation

### Prerequisites

- **Python 3.7** or higher
- **CUDA-enabled GPU:** Required for running the language model efficiently.
- **Python Packages:**
  - `transformers`
  - `torch` (with CUDA support)
  - `pandas`
  - `argparse`
  - `re`

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Arabic-Text-to-Crosswords.git
   cd Arabic-Text-to-Crosswords
   ```

2. **Set Up Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

   *If `requirements.txt` is not provided, install packages manually:*

   ```bash
   pip install transformers torch pandas argparse re
   ```

4. **Verify CUDA Installation:** Ensure that PyTorch recognizes your GPU.

   ```python
   import torch
   torch.cuda.is_available()
   ```

   If `True`, you're ready to proceed.

## Usage

The script `crossword_clue_generator.py` processes an input CSV file containing texts, keywords, and categories to generate Arabic crossword clues.

### Command-line Arguments

- `--input-file`: **(Required)** Path to the input CSV file.
- `--output-file`: Path to save the output CSV file. *(Default: `output.csv`)*
- `--temperature`: Temperature setting for text generation. *(Default: `0.1`)*

### Input File Format

The input CSV file should have the following columns:

- `text`: The Arabic text from which clues will be generated.
- `keyword`: The specific keyword for the crossword clue.
- `category`: The category related to the keyword, provided in **English**.

**Example (`input.csv`):**

| text                                                                                                                                                                                                                                                                       | keyword      | category   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|------------|
| هذه فقرة نصية عربية تستخدم للاختبار.                                                                                                                                                                                                                                         | اختبار       | Education  |
| يعتبر النيل أطول نهر في العالم.                                                                                                                                                                                                                                              | نيل          | Geography  |
| جزيرة لانتاو وتعني حرفيا الرأس الخشن، هي أكبر جزيرة في هونغ كونغ تقع في مصب نهر اللؤلؤ. إداريًا، تتبع لمقاطعة الجزر، إلا أن جزءًا صغيرًا في شمال شرق الجزيرة يتبع إلى مقاطعة تسوين وان. تبلغ مساحتها 146.38 كيلومتر مربع. كانت الجزيرة سابقًا موقعًا لبعض قرى الصيد الهادئة، إلا أنها تحولت في السنوات الأخيرة بشكل كبير مع تطور عدة مشاريع للبنى التحتية، بما في ذلك مطار هونغ كونغ الدولي الجديد، نغونغ بينغ 360 وديزني لاند هونغ كونغ. | جزيرة لانتاو | Geography  |

**Note:** Categories should be specified in English to maintain consistency with the model expectations.

### Output File Format

The output CSV will include the original columns plus:

- `Generated Arabic Crossword Clue`: The clues generated by the model.

**Example (`output.csv`):**

| text                                                                                                                                                                                                                                                                       | keyword      | category   | Generated Arabic Crossword Clue                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|------------|---------------------------------------------------|
| هذه فقرة نصية عربية تستخدم للاختبار.                                                                                                                                                                                                                                         | اختبار       | Education  | CLUE1: ...                                        |
| يعتبر النيل أطول نهر في العالم.                                                                                                                                                                                                                                              | نيل          | Geography  | CLUE1: ...                                        |
| جزيرة لانتاو وتعني حرفيا الرأس الخشن، هي أكبر جزيرة في هونغ كونغ تقع في مصب نهر اللؤلؤ. إداريًا، تتبع لمقاطعة الجزر، إلا أن جزءًا صغيرًا في شمال شرق الجزيرة يتبع إلى مقاطعة تسوين وان. تبلغ مساحتها 146.38 كيلومتر مربع. كانت الجزيرة سابقًا موقعًا لبعض قرى الصيد الهادئة، إلا أنها تحولت في السنوات الأخيرة بشكل كبير مع تطور عدة مشاريع للبنى التحتية، بما في ذلك مطار هونغ كونغ الدولي الجديد، نغونغ بينغ 360 وديزني لاند هونغ كونغ. | جزيرة لانتاو | Geography  | CLUE1: ...                                        |

### Examples

**Basic Command:**

```bash
python crossword_clue_generator.py --input-file input.csv
```

**Custom Output File and Temperature:**

```bash
python crossword_clue_generator.py --input-file input.csv --output-file clues.csv --temperature 0.1
```

### Sample Input and Output

**Sample Input (`input.csv`):**

```csv
text,keyword,category
"هذه فقرة نصية عربية تستخدم للاختبار.","اختبار","Education"
"يعتبر النيل أطول نهر في العالم.","نيل","Geography"
"جزيرة لانتاو وتعني حرفيا الرأس الخشن، هي أكبر جزيرة في هونغ كونغ تقع في مصب نهر اللؤلؤ. إداريا، تتبع لمقاطعة الجزر، إلا أن جزء صغير في شمال شرق الجزيرة يتبع إلى مقاطعة تسوين وان. تبلغ مساحتها 146.38 كيلومتر مربع. كانت الجزيرة سابقا موقع لبعض قرى الصيد الهادئة، إلا أنها تحولت في السنوات الأخيرة بشكل كبير مع تطور عدة مشاريع للبنى التحتية، بما في ذلك مطار هونغ كونغ الدولي الجديد، نغونغ بينغ 360 وديزني لاند هونغ كونغ.","جزيرة لانتاو","Geography"
```

**Sample Output (Console):**

```
Loading the model Kamyar-zeinalipour/Llama3-8B-Ar-Text-to-Cross...
Model Kamyar-zeinalipour/Llama3-8B-Ar-Text-to-Cross loaded successfully.
Processing index 0:
Input Text: 
هذه فقرة نصية عربية تستخدم للاختبار.
Input Keyword: اختبار
Input Category: Education
Generated Clue: 
CLUE1: أداة تقويم تستخدم لقياس قدرات الطلاب ومعرفتهم.

Processing index 1:
Input Text: 
يعتبر النيل أطول نهر في العالم.
Input Keyword: نيل
Input Category: Geography
Generated Clue: 
CLUE1: نهر يمر في مصر ويعد الأطول في العالم.

Processing index 2:
Input Text:
جزيرة لانتاو وتعني حرفيا الرأس الخشن، هي أكبر جزيرة في هونغ كونغ تقع في مصب نهر اللؤلؤ. إداريا، تتبع لمقاطعة الجزر، إلا أن جزء صغير في شمال شرق الجزيرة يتبع إلى مقاطعة تسوين وان. تبلغ مساحتها 146.38 كيلومتر مربع. كانت الجزيرة سابقا موقع لبعض قرى الصيد الهادئة، إلا أنها تحولت في السنوات الأخيرة بشكل كبير مع تطور عدة مشاريع للبنى التحتية، بما في ذلك مطار هونغ كونغ الدولي الجديد، نغونغ بينغ 360 وديزني لاند هونغ كونغ.
Input Keyword:
جزيرة لانتاو
Input Category:
Geography
Generated Clue:
CLUE1: أكبر جزيرة في هونغ كونغ تقع عند مصب نهر اللؤلؤ.

Output saved to output.csv
```

### Note on Categories

Ensure that the `category` field in your input CSV is in English, as the model expects English category labels. This helps the model in generating appropriate clues based on the specified category.

## Code Overview

The script consists of several functions designed to process input data, interact with the language model, and extract the generated clues.

### Main Functions

- **`format_row(row)`:**

  Formats an input row into a prompt suitable for the language model, incorporating the text, keyword, and category.

- **`extract_text(text)`:**

  Extracts the assistant's response from the raw output generated by the model.

- **`get_code_completion(prompt, model, tokenizer, temperature)`:**

  Generates model outputs based on the provided prompt and temperature settings.

- **`get_first_three_clues(generated_text)`:**

  Extracts up to the first three clues from the generated text using regular expressions.

- **`main(args)`:**

  The main function that orchestrates the loading of the model, reading input data, processing, and writing output data.

### Workflow

1. **Model Loading:**

   Loads the pretrained model and tokenizer from Hugging Face.

2. **Input Reading:**

   Reads the input CSV file specified by the user.

3. **Processing Loop:**

   Iterates over each row in the input data:

   - Formats the prompt, ensuring that categories are in English.
   - Generates model outputs.
   - Extracts clues from the outputs.
   - Logs progress to the console.

4. **Output Writing:**

   Writes the processed data, including the generated clues, to an output CSV file.

## Limitations

- **Resource Intensive:** Requires a CUDA-enabled GPU with sufficient VRAM to run the language model.
- **Model Variability:** The quality of generated clues can vary based on the input and model parameters.
- **Language Limitations:** While optimized for Arabic clue generation, nuances in dialects and expressions may affect output quality.
- **Category Language:** Categories must be provided in English to align with model expectations.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Acknowledgements


- **Libraries:** This project utilizes the following libraries:
  - [Transformers](https://github.com/huggingface/transformers)
  - [PyTorch](https://pytorch.org/)
  - [Pandas](https://pandas.pydata.org/)
  - [Argparse](https://docs.python.org/3/library/argparse.html)
  - [Regular Expressions (re module)](https://docs.python.org/3/library/re.html)
- **Community:** Appreciation for the open-source community and contributors who make such projects possible.

---

Feel free to reach out if you have any questions or need assistance with the setup. Happy clue generating!
