# Multiple Choice Question (MCQ) Generator using T5  

This repository contains an implementation of a **Multiple Choice Question Generator** leveraging the **T5 (Text-to-Text Transfer Transformer)** model. The project aims to automate the generation of high-quality, contextually accurate multiple-choice questions from any given text input, making it a powerful tool for educators, e-learning platforms, and developers in the field of natural language processing (NLP).  

## Features  
- **Text-to-MCQ Transformation**: Converts input text into multiple-choice questions with one correct answer and multiple distractors.  
- **Pretrained Models**: Uses the Hugging Face T5 model fine-tuned for question generation tasks.  
- **API Support**: REST API endpoints for easy integration into existing systems.  

## How It Works  
1. **Input Text**: The user provides a paragraph or passage as input.  
2. **Question Generation**: The T5 model processes the input to create a relevant question.  
3. **Answer and Distractors**: The model identifies the correct answer and generates plausible distractors.  
4. **Output**: A formatted MCQ is returned, ready to use.  

## Example  
**Input Text**:  
*The process of photosynthesis occurs in the chloroplasts of plant cells. It involves the conversion of light energy into chemical energy stored in glucose molecules.*  

**Generated MCQ**:  
*What is the main site of photosynthesis in plant cells?*  
- A) Mitochondria  
- B) Chloroplasts *(Correct Answer)*  
- C) Nucleus  
- D) Vacuole  

## Installation  
Clone the repository and install the required dependencies:  
```bash  
git clone https://github.com/yourusername/mcq-generator-t5.git  
cd mcq-generator-t5  
pip install -r requirements.txt  
```  

## Usage  
### 1. Command Line Interface (CLI)  
```bash  
python generate_mcq.py --input "Your input text here" --num_choices 4  
```  

### 2. API Usage  
Start the API server:  
```bash  
python app.py  
```  
Send a POST request with the input text:  
```bash  
curl -X POST -H "Content-Type: application/json" -d '{"text": "Your input text here"}' http://localhost:5000/generate  
```  

### 3. Web Interface  
Run the app and access it at `http://localhost:5000`.  

## Fine-tuning  
To fine-tune the T5 model for specific domains:  
1. Prepare your dataset in a question-answer format.  
2. Use the provided `fine_tune.py` script to train the model.  
```bash  
python fine_tune.py --dataset_path your_dataset.json --epochs 3  
```  

## Dependencies  
- Python >= 3.8  
- Transformers >= 4.47.0
- Tensorflow >= 2.18.0
- Flask >= 3.1.0

## Future Enhancements  
- Customizable Options: Adjust the number of answer choices, difficulty level, or topic specificity.  
- Add multilingual support for generating MCQs in other languages.  
- Improve distractor generation for increased realism.  
- Integrate with popular LMS (Learning Management Systems) like Moodle.  

## Contributing  
Contributions are welcome! Please open an issue or submit a pull request for any bugs or feature suggestions.  

## License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---  

Let me know if you'd like additional sections or refinements!
