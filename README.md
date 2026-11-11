# From Arabic Text to Puzzles: Arabic Educational Crosswords

**Generate Arabic crossword clues from any text, keyword and category**

[![Paper](https://img.shields.io/badge/arXiv-2501.11035-b31b1b)](https://arxiv.org/abs/2501.11035)
[![Model](https://img.shields.io/badge/%F0%9F%A4%97_Model-Llama3--8B--Ar--Text--to--Cross-orange)](https://huggingface.co/Kamyar-zeinalipour/Llama3-8B-Ar-Text-to-Cross)
[![Dataset](https://img.shields.io/badge/%F0%9F%A4%97_Dataset-Arabic--Clue--Instruct-yellow)](https://huggingface.co/datasets/Kamyar-zeinalipour/Arabic-Clue-Instruct)
[![Collection](https://img.shields.io/badge/%F0%9F%A4%97_Collection-Arabic_Crosswords-orange)](https://huggingface.co/collections/Kamyar-zeinalipour/arabic-educational-crosswords-6af46e6797758d5046eb4f39)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE.txt)

This repository accompanies the paper
[*From Arabic Text to Puzzles: LLM-Driven Development of Arabic Educational Crosswords*](https://arxiv.org/abs/2501.11035).
It turns educational Arabic text into crossword clues: give it a passage, the answer word and a
topic category, and a fine-tuned Llama-3-8B-Instruct writes clues for that word grounded in the
passage. Teachers can then pick the best clues and build a crossword.

| Resource | |
|---|---|
| [Llama3-8B-Ar-Text-to-Cross](https://huggingface.co/Kamyar-zeinalipour/Llama3-8B-Ar-Text-to-Cross) | Llama-3-8B-Instruct fine-tuned with LoRA on Arabic-Clue-Instruct |
| [Arabic-Clue-Instruct](https://huggingface.co/datasets/Kamyar-zeinalipour/Arabic-Clue-Instruct) | 14,497 Arabic Wikipedia passages with keywords, categories and 54,196 clues |
| [HumanAnnotation-UI-Ar-Text-To-Cross](https://github.com/KamyarZeinalipour/HumanAnnotation-UI-Ar-Text-To-Cross) | Annotation tool and the expert ratings used in the paper |
| [AR_CW](https://huggingface.co/datasets/Kamyar-zeinalipour/AR_CW) | 57,706 clue–answer pairs from our earlier [ArabIcros](https://aclanthology.org/2023.arabicnlp-1.23/) generator |

## Results

Arabic-speaking experts rated the clues generated for 200 test passages (up to three clues each)
from A (best) to E. Share of clues per rating, in %:

| Model | A | B | C | D | E |
|---|---:|---:|---:|---:|---:|
| GPT-3.5-Turbo | 28.47 | 23.22 | 0 | 35.08 | 13.22 |
| GPT-3.5-Turbo, fine-tuned | 54.33 | 22.33 | 15.00 | 8.33 | 0 |
| Llama-3-8B-Instruct | 36.02 | 12.79 | 0.34 | 37.54 | 13.29 |
| **Llama3-8B-Ar-Text-to-Cross** | **78.86** | 2.66 | 0 | 18.13 | 0.33 |

## Installation

Python 3.9+ and a CUDA GPU with at least 24 GB of memory.

```bash
git clone https://github.com/KamyarZeinalipour/Arabic-Text-to-Crosswords.git
cd Arabic-Text-to-Crosswords
pip install -r requirements.txt
huggingface-cli login   # the Llama 3 base model is gated: accept its license on Hugging Face first
```

## Usage

```bash
python crossword_clue_generator.py --input-file input.csv --output-file output.csv --temperature 0.1
```

| Argument | Description |
|---|---|
| `--input-file` | CSV with the columns `text` (Arabic passage), `keyword` (Arabic answer word) and `category` (English topic, e.g. `Geography`) |
| `--output-file` | Where to write the results (default `output.csv`) |
| `--temperature` | Sampling temperature (default `0.1`) |

**Example (`input.csv`):**

| text                                                                                                                                                                                                                                                                       | keyword      | category   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|------------|
| هذه فقرة نصية عربية تستخدم للاختبار.                                                                                                                                                                                                                                         | اختبار       | Education  |
| يعتبر النيل أطول نهر في العالم.                                                                                                                                                                                                                                              | نيل          | Geography  |
| جزيرة لانتاو وتعني حرفيا الرأس الخشن، هي أكبر جزيرة في هونغ كونغ تقع في مصب نهر اللؤلؤ. إداريًا، تتبع لمقاطعة الجزر، إلا أن جزءًا صغيرًا في شمال شرق الجزيرة يتبع إلى مقاطعة تسوين وان. تبلغ مساحتها 146.38 كيلومتر مربع. كانت الجزيرة سابقًا موقعًا لبعض قرى الصيد الهادئة، إلا أنها تحولت في السنوات الأخيرة بشكل كبير مع تطور عدة مشاريع للبنى التحتية، بما في ذلك مطار هونغ كونغ الدولي الجديد، نغونغ بينغ 360 وديزني لاند هونغ كونغ. | جزيرة لانتاو | Geography  |

The output CSV keeps the input columns and adds `Generated Arabic Crossword Clue` with up to three
clues (`CLUE1: …`, `CLUE2: …`, `CLUE3: …`).

**Example (`output.csv`):**

| text                                                                                                                                                                                                                                                                       | keyword      | category   | Generated Arabic Crossword Clue                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|------------|---------------------------------------------------|
| هذه فقرة نصية عربية تستخدم للاختبار.                                                                                                                                                                                                                                         | اختبار       | Education  | CLUE1: ...                                        |
| يعتبر النيل أطول نهر في العالم.                                                                                                                                                                                                                                              | نيل          | Geography  | CLUE1: ...                                        |
| جزيرة لانتاو وتعني حرفيا الرأس الخشن، هي أكبر جزيرة في هونغ كونغ تقع في مصب نهر اللؤلؤ. إداريًا، تتبع لمقاطعة الجزر، إلا أن جزءًا صغيرًا في شمال شرق الجزيرة يتبع إلى مقاطعة تسوين وان. تبلغ مساحتها 146.38 كيلومتر مربع. كانت الجزيرة سابقًا موقعًا لبعض قرى الصيد الهادئة، إلا أنها تحولت في السنوات الأخيرة بشكل كبير مع تطور عدة مشاريع للبنى التحتية، بما في ذلك مطار هونغ كونغ الدولي الجديد، نغونغ بينغ 360 وديزني لاند هونغ كونغ. | جزيرة لانتاو | Geography  | CLUE1: ...                                        |

## How it works

1. **Passages.** Popular, quality-assessed Arabic Wikipedia articles were selected and filtered to
   14,497 passages, each with a keyword (the answer) and a topic category.
2. **Clues.** GPT-4-Turbo wrote at least three clues per passage for its keyword, following a prompt
   that asks for short, accurate clues grounded in the text (Arabic-Clue-Instruct, 54,196 clues).
3. **Fine-tuning.** Llama-3-8B-Instruct was fine-tuned with LoRA on this data (r = 32, α = 64,
   dropout 0.1, applied to all attention and MLP projections plus `embed_tokens` and `lm_head`;
   3 epochs, learning rate 1e-4 with cosine decay, 4 sequences per GPU × 8 accumulation steps on
   4 GPUs, bf16, seed 100).
4. **Evaluation.** Clues from the base and fine-tuned models were rated by Arabic-speaking experts
   (table above).

## Citation

```bibtex
@misc{zeinalipour2025arabictextpuzzles,
  title         = {From Arabic Text to Puzzles: LLM-Driven Development of Arabic Educational Crosswords},
  author        = {Kamyar Zeinalipour and Mohamed Zaky Saad and Marco Maggini and Marco Gori},
  year          = {2025},
  eprint        = {2501.11035},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2501.11035}
}
```

Earlier work on Arabic crossword generation:

```bibtex
@inproceedings{zeinalipour-etal-2023-arabicros,
    title = "{A}rab{I}cros: {AI}-Powered {A}rabic Crossword Puzzle Generation for Educational Applications",
    author = "Zeinalipour, Kamyar  and Saad, Mohamed  and Maggini, Marco  and Gori, Marco",
    booktitle = "Proceedings of {A}rabic{NLP} 2023",
    year = "2023",
    address = "Singapore (Hybrid)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.arabicnlp-1.23/",
    doi = "10.18653/v1/2023.arabicnlp-1.23",
    pages = "288--301"
}
```

## License

Code: [MIT](LICENSE.txt). The model follows the Meta Llama 3 Community License; Arabic-Clue-Instruct
is CC BY-SA 4.0.
