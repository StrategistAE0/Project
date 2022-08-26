# Import Module 
import tabula
  
# Read PDF File
# this contain a list
df = tabula.read_pdf(r"C:\Users\r14ale\Desktop\PDF_Reader\Doc1.pdf", pages = 1)[0]
  
# Convert into Excel File
df.to_excel(r'C:\Users\r14ale\Desktop\PDF_Reader\Doc1.csv')