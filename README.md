# **LLM-Based Research Assistant**  

An AI-powered research assistant that can **automatically read research papers** in a folder and **answer queries or summarize content**.  

This project **fine-tunes GPT-2** using **materials science text** to build **domain expertise** and implements a **Retrieval-Augmented Generation (RAG) pipeline** for processing research papers.  


## **Installation & Setup**  

### **1. Install Dependencies**  
Run the following command to install the required libraries:  
```bash
pip install -r requirements.txt
```  

### **2. Prepare Data**  
- **Training Data**:  
  - Create a file named `data.txt` containing text with which the model should be trained.  
- **Research Papers**:  
  - Place the research papers to be processed inside a folder.  

### **3. Fine-Tune the Model**  
- Open and run **`main.ipynb`** to start the fine-tuning process.  
- You can also **choose a different model** to fine-tune as needed.  

### **4. Upload Fine-Tuned Model to Hugging Face**  
- The notebook will prompt you to **connect to your Hugging Face Hub** to upload your fine-tuned model.  

### **5. Process Research Papers & Answer Queries**  
- Run **`rag.ipynb`** to process research papers and answer queries.  

---

## **Usage Example**  
Once the model is trained and the RAG pipeline is set up, you can query the system like this:  
```python
query = "Summarize the key findings of the paper on superconductivity."
response = model.answer(query)
print(response)
```



