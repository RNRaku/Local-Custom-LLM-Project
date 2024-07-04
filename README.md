# Local Custom LLM Project

## Overview
This project aims to create a custom Large Language Model (LLM) tailored to specific question-answer datasets. The following guide will walk you through the necessary pre-requisites, data preprocessing steps, training, and deployment procedures. This project can also easily be edited to accept story-summary pairs for summirization tasks and lang-{A} to lang-{B} pairs for translation tasks and many many more.

## Prerequisites

### Libraries
- `pytorch`
- `unsloth`
- `AutoTokenizer`
- `Streamlit`
- `json`
- `random`
- `datasets`
- `os`
- `glob`
- `re`

- `ngrok`
- `pyngrok`
- `localtunnel`

### System Requirements
- **GPU:** NVIDIA 2000 series or higher
- **VRAM:** Minimum 8GB (required for Gemma 2b)
- **PyTorch:** Version 2.3.0+cu121
- **CUDA:** Version 7.5
- **CUDA Toolkit:** Version 12.1

## File Structure
VinBot/  <br />
├── docs/<br />
│   ├── QA.txt<br />
├── data/<br />
│   ├── Question-1<br />
│   ├── Answer-1<br />
│   └── ...<br />
├── Jsonls/<br />
│   ├── answers.jsonl<br />
│   ├── queries.jsonl<br />
│   ├── instruction.jsonl<br />
├── notebooks/<br />
│   ├── training_notebook.ipynb<br />
├── scripts/<br />
│   ├── __init__.py<br />
│   ├── create_QA.py<br />
│   ├── combine_QA.py<br />
├── lora_model/<br />
│   ├── adapter_config.json<br />
│   ├── special_tokens_map.json<br />
│   ├── tokenizer.json<br />
│   ├── tokenizer_config.json<br />
│   ├── tokenizer.model<br />
│   ├── adapter_model.safetensors<br />
│   ├── README.md<br />
├── LICENSE<br />
├── README.md<br />
├── requirements.txt<br />
└── main.py<br />

## Steps to Use the LLM Project

### 1. Data Preprocessing
1. **Add Your QAs**
   - create QA pairs for any topic that you want to train the LLM on
   - while a few hundred questions may work, it is prone to overfitting and atleast a few hundred pairs are reccomneded for even the smallest llms.
   - Place your QAs in a document within the `docs` folder.

2. **Ensure Correct Format**
   - Format your document as follows:
     - Questions must begin with `Q:` or `Question:` followed by the question text.
     - Answers must begin with `A:` or `Answer:` followed by the answer text.

3. **Convert Word Document to TXT Files**
   - Save the Word document as a `.txt` file in the `docs` folder.

4. **Run `create_QA` Script**
   - Execute the `create_QA` script to extract questions and answers. The output will be stored in the `data` folder with filenames `Question-{NUMBER}` and `Answer-{NUMBER}`. Or run main.py file. 
   - Please change the file paths to fit your device

5. **Run `combine_QA` Script**
   - Execute the `combine_QA` script to tokenize and combine the QAs into `.jsonl` files. The output will be stored in the `Jsonls` folder. Or run main.py file.
   - Please change the file paths to fit your device

### 2. Training
1. **Run the Notebook**
   - Ensure the instructions, questions, and answers are in the correct directories.
   - Open and run the provided Jupyter notebook for training.
   - Please change the file paths to fit your device

2. **Adjust Training Parameters**
   - Adjust the following parameters as needed to achieve the desired performance:
     - `epochs`
     - `adaptors`
     - `r`
     - `alpha`
     - `dropout`
     - `test-train`
     - `warmup`
     - `decay`
     -  etc

3. **Save the Trained Model**
   - Save the trained model to lora_model for deployment.
   - Please change the file paths to fit your device

### 3. Deployment
   **Load and Merge Models**
   - Load the trained model from lora_model and merge it with the base model.

   **Deploy Front End**
   - Deploy the front-end code to interact with the model using Streamlit or other preferred frameworks.

## Additional Notes
   - **Environment Setup:**
      - Ensure all libraries and dependencies are installed correctly before running any scripts.
  
   - **GPU Utilization:**
     - Ensure your system meets the GPU and VRAM requirements to avoid training interruptions.

   - **Customization:**
     - Feel free to tweak the scripts and parameters to better fit your dataset and requirements.

   - **Deployment Options:**
     - You can use `ngrok`, `pyngrok`, or `localtunnel` for exposing your local deployment for testing purposes.

## Contributing
Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For further inquiries or issues, please contact me at rinchennorbu441@gmail.com
