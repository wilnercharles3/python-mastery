import os, shutil
pdf_copies = os.path.join(os.getcwd(), 'pdf_copies')
os.makedirs(pdf_copies, exist_ok=True)

for foldername, subfolders, filenames in os.walk(r'C:\Users\Cportable\Downloads'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            file_path = os.path.join(foldername, filename)
            shutil.copy(file_path, pdf_copies)