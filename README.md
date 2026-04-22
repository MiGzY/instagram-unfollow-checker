# instagram-unfollow-checker

A simple Python script that compares your Instagram following and followers lists to find accounts that don't follow you back.

---

## Requirements

- Python 3.x (no extra libraries needed)

---

## Getting your Instagram data

1. Open Instagram and go to **Settings > Account Centre > Your information and permissions > Download your information**
2. Request a download of your data in **JSON format**
3. Wait for the email from Instagram (can take a few minutes to a few hours)
4. Download and unzip the file
5. Navigate to the `followers_and_following` folder inside the export

You'll find files including:
- `followers_1.json` — accounts that follow you
- `following.json` — accounts you follow

---

## Setup

Clone or download this repo and place `compare_followers.py` in the same folder as your JSON files:

```
followers_and_following/
├── compare_followers.py
├── followers_1.json
└── following.json
```

Make the script executable (Mac/Linux):

```bash
chmod +x compare_followers.py
```

---

## Usage

```bash
./compare_followers.py --following following.json --followers followers_1.json --out not_following_back.csv --lower
```

Or with Python directly:

```bash
python3 compare_followers.py --following following.json --followers followers_1.json --out not_following_back.csv --lower
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--following` | Yes | Path to your following JSON file |
| `--followers` | Yes | Path to your followers JSON file |
| `--out` | No | Output filename (default: `not_following_back.csv`) |
| `--lower` | No | Case-insensitive comparison (recommended) |
| `--key` | No | Manually specify the key in the JSON object that holds the list |

---

## Output

The script generates a CSV file with two columns:

| username | instagram_url |
|----------|---------------|
| someuser | https://www.instagram.com/someuser |

It also prints a summary to the terminal:

```
Following: 3331
Followers: 1178
Not following back: 2487
Saved to: not_following_back.csv
```

---

## Viewing the results

**Google Sheets** — drag the CSV onto [sheets.google.com](https://sheets.google.com). URLs are automatically clickable.

**Excel** — open the CSV, then in an empty column use the formula:
```
=HYPERLINK(B2, B2)
```
Drag down to apply to all rows for clickable links.

**Any text editor or spreadsheet app** — the CSV is plain text and will open anywhere.

---

## Notes

- Instagram's export format has changed over time. The script handles both formats currently in use — `followers_1.json` uses a `value` field for usernames, while `following.json` stores them in a `title` field.
- If your export has a different structure, use the `--key` flag to point the script at the right field.
- The script does not interact with Instagram's API and requires no login or authentication.

---

## License

MIT — do whatever you like with it.
