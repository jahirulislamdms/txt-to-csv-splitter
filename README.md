# 📄 TXT to CSV Splitter

A simple Python script to split a large `.txt` file into multiple `.csv` files based on a specified number of lines.

## 🚀 Features
- Splits a `.txt` file into multiple `.csv` files.
- Allows users to specify the maximum number of lines per CSV file.
- Ensures each line is written as a separate row in the CSV.

## 📌 Prerequisites
Make sure you have Python installed (version 3.x recommended).

## 🔧 Installation
Clone the repository:
```sh
git clone https://github.com/jahirulislamdms/txt-to-csv-splitter.git
cd txt-to-csv-splitter
```

## ▶️ Usage
Run the script using:
```sh
python split_txt_to_csv.py
```
You'll be prompted to enter the path of the `.txt` file and the maximum number of lines per CSV file.

### Example:
```
Enter the path of the .txt file: example.txt
Enter max lines per CSV file: 100
```
This will generate multiple CSV files, such as:
```
example_part1.csv
example_part2.csv
...
```

## 🛠 How It Works
1. Reads the `.txt` file.
2. Splits the content into chunks based on the user-defined line limit.
3. Writes each chunk to a new `.csv` file.
4. Saves the CSV files in the same directory as the original `.txt` file.

## 📜 License
This project is licensed under the MIT License.

## 💡 Future Enhancements
- Add support for different delimiters.
- Provide a GUI version for easier usage.
- Support for handling large files efficiently using streaming.

## 🤝 Contributing
Pull requests are welcome! Feel free to fork the project and submit improvements.

---
Made with ❤️ by [jahirulislamdms](https://github.com/jahirulislamdms)

