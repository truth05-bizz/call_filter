📞 Call Filter Script

This project extracts specific call records from large telecom report files (100k+ rows).
It was built to solve a client’s request on Upwork: filtering calls between two numbers from a raw text file and returning the results in spreadsheet format.

🚀 Features

Reads large .txt telecom report files.

Normalizes phone numbers (removes leading 1 if present).

Filters rows where Number A called Number B, or vice versa.

Saves results as .csv and .xlsx.

Easy to adapt for other numbers.

📂 Project Structure

call_filter/
│── main.py                 # Main Python script
│── ReportAU_3945468001.txt # Sample raw input file
│── Filtered_calls.csv      # Example output (CSV)
│── Filtered_calls.xlsx     # Example output (Excel)
│── .gitignore
│── README.md



---

## ⚙️ Usage

### 1️⃣ Install dependencies
```bash
pip install pandas openpyxl


python main.py


3️⃣ Outputs

The script will generate:

Filtered_calls.csv

Filtered_calls.xlsx

Both files contain only the calls between the two numbers you define in the script.

📝 Configuration

Inside main.py, change these lines to your target numbers:
num_a = "2168678299"
num_b = "2164085717"


📊 Example

Input (raw snippet):
OriginatingNumber, TerminatingNumber
12168678299, 12164085717
12164085717, 12168678299
12342740646, 12164085717

Output:
OriginatingNumber, TerminatingNumber
2168678299, 2164085717
2164085717, 2168678299


💡 Notes

Works with large files (~100k rows).

Built for Upwork freelance project.

Easy to extend (filter more numbers, export more formats).