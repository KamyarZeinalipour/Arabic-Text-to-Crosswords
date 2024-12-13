from transformers import AutoModelForCausalLM, AutoTokenizer
import argparse
import pandas as pd
import re

# Define the prompt
simple_prompt = (
    'Create Arabic crossword clues for a specified keyword in Arabic, '
    'using the provided text and focusing on the indicated category.'
)

def format_row(row):
    """Format the input row into the prompt format required by the model."""
    user_message = (
        f"{simple_prompt}\n\n"
        f"TEXT: {row['text']}\n\n"
        f"KEYWORD: {row['keyword']}\n\n"
        f"CATEGORY: {row['category']}"
    )

    formatted_prompt = (
        f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
        f"You are an invaluable assistant who creates Arabic crossword clues based on the "
        f"provided Arabic text, keyword, and specific category.\n"
        f"<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
        f"{user_message} <|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    )
    return formatted_prompt

def extract_text(text):
    """Extract the assistant's response from the generated text."""
    try:
        if text.count('<|end_header_id|>\n\n') > 1:
            response_part = text.split('<|end_header_id|>\n\n')[2]
            assistant_response = response_part.split('<|end_of_text|>')[0]
            assistant_response = assistant_response.replace('<|eot_id|><|start_header_id|>assistant', '')
            return assistant_response.strip()
    except IndexError:
        pass  # If the expected format isn't found
    return None

def get_code_completion(prompt, model, tokenizer, temperature):
    """Generates completion for the given prompt using the model."""
    model.eval()
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()
    outputs = model.generate(
        input_ids=input_ids,
        max_new_tokens=256,
        temperature=temperature,
        top_k=50,
        top_p=0.95,
        do_sample=True,
        repetition_penalty=1.1,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id = tokenizer.eos_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=False)


def get_first_three_clues(generated_text):
    """
    Extracts up to the first three clues from the generated_text string.

    Parameters:
    generated_text (str): The string containing all the clues.

    Returns:
    str: A string containing up to the first three clues separated by new lines.
    """
    # Use regular expression to find all clues starting with 'CLUE' followed by a number
    clues = re.findall(r'(CLUE\d+:.*)', generated_text)
    
    # Get up to the first three clues
    first_three_clues = clues[:3]
    
    # Join the clues into a single string separated by newlines
    return '\n'.join(first_three_clues)

def main(args):
    # Load the model and tokenizer
    model_name = "Kamyar-zeinalipour/Llama3-8B-Ar-Text-to-Cross"
    print(f"Loading the model {model_name}...")
    model = AutoModelForCausalLM.from_pretrained(model_name).cuda()
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print(f"Model {model_name} loaded successfully.")

    # Read the input CSV
    df = pd.read_csv(args.input_file)

    # List to store the outputs
    outputs = []

    for index, row in df.iterrows():
        # Create the prompt using the formatting function
        prompt = format_row(row)

        try:
            # Generate the response
            response = get_code_completion(prompt, model, tokenizer, args.temperature)
            generated_text = extract_text(response)
            generated_text = get_first_three_clues(generated_text)

            # Display progress
            print(f"Processing index {index}:")
            print(f"Input Text: \n{row['text']}")
            print(f"Input Keyword: {row['keyword']}")
            print(f"Input Category: s{row['category']}")
            print(f"Generated Clue: \n{generated_text}\n")

            # Append the result
            outputs.append({
                'text': row['text'],
                'keyword': row['keyword'],
                'category': row['category'],
                'Generated Arabic Crossword Clue': generated_text
            })

        except Exception as e:
            print(f"Error processing index {index}: {e}")
            outputs.append({
                'text': row['text'],
                'keyword': row['keyword'],
                'category': row['category'],
                'Generated Arabic Crossword Clue': None,
                'Error': str(e)
            })

    # Save the outputs to a CSV file
    output_df = pd.DataFrame(outputs)
    output_df.to_csv(args.output_file, index=False, encoding='utf-8-sig')
    print(f"Output saved to {args.output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Arabic crossword clues using a language model.')
    parser.add_argument('--input-file', type=str, required=True, help='Path to the input CSV file.')
    parser.add_argument('--output-file', type=str, default='output.csv', help='Path to save the output CSV file.')
    parser.add_argument('--temperature', type=float, default=0.1, help='Temperature for text generation.')

    args = parser.parse_args()
    main(args)
