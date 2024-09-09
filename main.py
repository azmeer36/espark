from flask import Flask, request, redirect, url_for, render_template, jsonify, send_file
import os
from processing import process_excel_file


# Set up Flask application
app = Flask(__name__)

# Set the folder for file uploads
UPLOAD_FOLDER = 'uploads'
EXPORT_FOLDER = 'exports'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['EXPORT_FOLDER'] = EXPORT_FOLDER

# Allow only specific file extensions (Excel files)
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}

# Function to check if the file is allowed (Excel files only)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Route to render a simple HTML form for file upload
@app.route('/')
def upload_form():
    return render_template('upload_form.html')
    

# Route to handle the file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        # Save the file in the uploads folder
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Perform any processing on the file 
        csv_file_path = process_excel_file(file.filename)
        
        # Provide the link to download the processed CSV file
        return redirect(url_for('download_file', filename=os.path.basename(csv_file_path)))

    return jsonify({"error": "File type not allowed"}), 400


# Route to download the processed CSV file
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(app.config['EXPORT_FOLDER'], filename)
    
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({"error": "File not found"}), 404


if __name__ == '__main__':
        
    # Run the Flask application
    app.run(debug=True)
