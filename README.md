# Regular Show AI Scene Generator

This project uses the OpenAI API to generate short, funny scene scripts in the style of the TV show "Regular Show", featuring characters like Mordecai and Rigby.

## Prerequisites

*   [Node.js](https://nodejs.org/) (which includes npm) installed on your machine.
*   An [OpenAI API key](https://platform.openai.com/account/api-keys).

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**
    Run the following command in your terminal to install the necessary Node.js packages listed in `package.json`.
    ```bash
    npm install
    ```

3.  **Configure your API Key:**
    You need to provide your OpenAI API key to the script. You can do this in one of two ways:

    *   **(Recommended) Environment Variable:** Set an environment variable named `OPENAI_API_KEY`.
        *   On macOS/Linux: `export OPENAI_API_KEY='your-key-here'`
        *   On Windows (Command Prompt): `set OPENAI_API_KEY=your-key-here`
        *   On Windows (PowerShell): `$env:OPENAI_API_KEY='your-key-here'`

    *   **Directly in the code:** Open the `index.js` file and replace the placeholder `'YOUR_API_KEY'` with your actual key.
        ```javascript
        // In index.js
        const API_KEY = process.env.OPENAI_API_KEY || 'YOUR_API_KEY';
        ```

## How to Run

Once you have completed the setup, you can generate a new scene by running:

```bash
npm start
```

The script will then print a newly generated scene to your console.