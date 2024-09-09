# Flask Excel Processor

This is a simple Flask application that allows users to upload an Excel file (`.xls` or `.xlsx`), process the file by calculating formulas in the cells, and then automatically provide a download of the processed CSV file.

## Setup Instructions

### 1. Set Up a Virtual Environment

It is a good practice to use a virtual environment to isolate your project dependencies:

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Requirements

Once the virtual environment is activated, install the required Python packages by running:

```bash
pip install -r requirements.txt
```


### 3. Run the Flask Application

With the environment set up and dependencies installed, you can now run the Flask application:

```bash
python main.py
```

### 4. Usage

- Open your web browser and go to [http://localhost:5000](http://127.0.0.1:5000).
- You will see a simple form where you can upload an Excel file (`.xls` or `.xlsx`).
- Click the **Choose File** button, select your Excel file, and then click **Upload**.
- Once the file is uploaded and processed, you will be redirected to a page where the processed CSV file will automatically download.




