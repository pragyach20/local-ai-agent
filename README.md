# Local AI Agent

A terminal-based AI file assistant built with Python, LangChain, and Google's Gemini API. It uses natural-language instructions to manage text files within a dedicated workspace.

## Features

* Gemini-powered AI assistant
* List files and folders
* Read UTF-8 text files
* Create and edit text files
* Create directories
* Workspace-restricted file operations
* Path traversal protection
* 1 MB file-size limits for reading and writing
* Environment-based API key management
* Formatted terminal interface using Rich

## Technologies Used

* Python
* LangChain Agents
* Google Gemini API
* python-dotenv
* Rich

## Project Structure

```text
Local_AI_Agent/
├── local_ai_agent.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── workspace/
    ├── test.txt
    └── agent_test.txt
```

The `.env` file stores the API key and must never be committed to GitHub.

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Local_AI_Agent
```

### 2. Install dependencies

```bash
py -m pip install -r requirements.txt
```

### 3. Configure the API key

Create a `.env` file in the project root:

```text
GOOGLE_API_KEY=your_gemini_api_key
```

Keep your API key private.

### 4. Run the application

```bash
py local_ai_agent.py
```

The application creates a `workspace` directory if it does not exist.

## Example Prompts

* List all files and folders in the workspace.
* Read `test.txt` and summarize its contents.
* Create `notes.txt` containing my project notes.
* Create a folder named `reports`.

## Security

The application resolves file paths and rejects paths that escape the workspace. Reading and writing are limited to 1 MB per file or content operation.

These checks help prevent accidental access outside the workspace but are not a complete operating-system security sandbox.

## API Quotas

Gemini API requests may fail when the configured account or project reaches its usage quota. Availability and limits depend on the Google AI configuration.

## Testing

Manually verified:

* Listing workspace files
* Reading a text file
* Creating and writing a text file
* Rejecting a path that attempts to escape the workspace

## Author

Pragya Chaudhary

B.Tech CSE (IoT) | Aspiring Data Analyst
