## Project Overview

MemeMantra is a Python-based CLI tool that leverages the Imgflip API to generate custom memes with top and bottom captions in English, Hindi, or any Unicode language you choose. It streamlines the meme-creation process with a clean, modular codebase and robust error handling. Whether you’re crafting memes for social media or just having fun, MemeMantra makes it effortless.

## Features

* **Unicode Caption Support:** Accepts Hindi (देवनागरी) or any other Unicode text without extra configuration.
* **Interactive CLI:** Presents a numbered list of available templates and prompts for caption inputs.
* **Automated Download:** Optionally saves the generated meme locally with sanitized filenames.
* **Modular Design:** Clean functions for fetching templates, choosing a meme, generating captions, and downloading images.
* **Robust Error Handling:** Graceful exits and informative messages on network or API failures.

## Prerequisites

* **Imgflip Account:** A valid Imgflip username and password, used for API authentication.
* **`requests` Library:** Installed inside a virtual environment or globally via APT/pipx (recommended).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Soumyaditya25/MemeMantra.git
   cd MemeMantra
   ```

2. **Set up a virtual environment (Recommended):**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install requests
   ```


## Configuration

1. Open `meme.py` (or your renamed script).
2. Replace the placeholders at the top with your Imgflip credentials:

   ```python
   USERNAME = 'your_imgflip_username'
   PASSWORD = 'your_imgflip_password'
   ```

## Usage

Run the script from your project directory:

```bash
python3 meme_generator.py
```

1. **Select a template:** Type the number corresponding to your desired meme.
2. **Enter captions:** Provide top and bottom text (supports Hindi/Unicode).
3. **Review links:** The script prints both the direct image URL and the Imgflip page URL.
4. **Download (optional):** Choose “y” when prompted to save the meme locally.

## Examples

```bash
$ python3 meme.py

Available Meme Templates:
  1. Drake Hotline Bling (id: 181913649)
  2. Distracted Boyfriend (id: 112126428)
  3. Expanding Brain (id: 93895088)
  ...

Enter template number: 1
Enter top text (Hindi/English/Unicode supported): Reading through 500 lines of merge-conflict markers
Enter bottom text (Hindi/English/Unicode supported): Deleting someone else's code and calling it 'fixed'

Meme URL: https://i.imgflip.com/5abcde.jpg
Page URL: https://imgflip.com/i/5abcde

Download image? [y/N]: y
[Success] Image saved as: Drake_Hotline_Bling.jpg
```

   ![Drake_Hotline_Bling](https://github.com/user-attachments/assets/55abf8aa-dce5-4251-bfb0-dd1cd3506adc)
