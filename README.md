
# ASEFTI

This project is a Python-based tool for generating conjugations of **Tarifit verbs**, inspired by the linguistic research and work of **Abdelwahid Hennu** and **Jaafar Yahia**. The goal is to create a robust verb conjugation generator that accommodates all Tarifit verbs and outputs the results in a structured **JSON file**. These JSON files are intended to be used by the conjugation website [asefti.com](http://asefti.com). 

The project is currently under development as part of the **Open Rif Project** ([openrif.com](http://openrif.com)) and aims to digitize and preserve the verbs of the Tarifit language.

---

## Features
- **Verb Conjugation Generator:**  
  Generates conjugation data for Tarifit verbs based on predefined linguistic rules.  

- **JSON Output:**  
  Conjugated data is saved in JSON format for use in external applications or systems.

- **Command-Line Support:**  
  - Pass a verb as an argument to print its conjugation directly to the terminal.  
  - For testing, the generator processes an array of verbs and limits the output accordingly.

- **Future Improvements:**  
  - Add support for reading verbs from an external file.  
  - Extend the generator for broader applications and uses.

---

## Usage

1. **Install Python Requirements**  
   Ensure Python is installed on your system. The script has no additional dependencies at this stage.

2. **Running the Script**  
   - To generate conjugation data for a single verb and print it to the terminal:  
     ```bash
     python main.py <verb>
     ```

   - To generate and save data for multiple verbs to a JSON file:  
     Modify the script to include an array of test verbs. Currently, this is done directly in the code. Later updates will enable feeding verbs from an external file.

---

## Output

1. **JSON File:**  
   The primary output is a JSON file containing the conjugation data, structured for easy integration with external systems such as the conjugation website.

   Example JSON structure:
   ```json
    {
    "ecc": {
        "root": "",
        "translations": {},
        "conj": {
            "anad": [
                "ecc",
                "ccem",
                "eccet",
                "ccemt"
            ],
        ...
   }
   ```

2. **Terminal Output:**  
   For testing or debugging, the conjugation results can also be printed directly to the terminal.

---

## Development Status

This project is in active development and will undergo changes to:
- Improve its functionality.
- Expand its scope for broader applications beyond the current JSON file export.

---

## Contribution

This project is part of the collaborative efforts of the **Open Rif Project** ([openrif.com](http://openrif.com)), which focuses on digitizing and preserving the Tarifit language. Contributions are welcome to help expand the tool's capabilities and enhance its accuracy.

---

## Acknowledgments

Special thanks to:
- **Abdelwahid Hennu** and **Jaafar Yahia** for their foundational research on Tarifit verbs.
- **Majid Akalai** for his support and efforts to provide help.
- The **Open Rif Project** team for supporting the digitization of Tarifit language resources.

---

## License

This project is licensed under the **GNU General Public License (GPL)**. You are free to use, modify, and distribute this software under the terms of the GPL license. For more details, see the [LICENSE](LICENSE) file.
