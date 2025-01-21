# RAG Chatbot

This is a simple rag chatbot.

> **Warning:** 
> 
> Please do not expose sensitive information such as passwords, API keys, or any other confidential data in your code. 
> 
> Always use environment variables or secure vaults to manage sensitive information. 
> 
> Exposing such data can lead to security vulnerabilities and unauthorized access to your systems.

## Prerequisites

- Basic knowledge of Git & Github
- FastAPI
- Python
- Pipenv
- Langchain
- Langsmith

## Imp Git commands

- **Initialize a empty git repo**:

    ```bash
    git init
    ```

- **Create and checkout to a new branch**:

    ```bash
    git checkout -b feature/your-feature-name
    ```
- **Stage changes**:

    ```bash
    git add .
    ```
- **Create and checkout to a new branch**:

    ```bash
    git commit -m "Your message"
    ```
- **Push to branch**:

    ```bash
    git push origin feature/your-feature-name
    ```

- **Add the upstream repository (the original repository you forked from) as a remote. Replace URL_OF_UPSTREAM_REPO with the actual URL of the upstream repository**:

    ```bash
    git remote add upstream URL_OF_UPSTREAM_REPO
    ```

- **Fetch the changes from the upstream repository**:

    ```bash
    git fetch upstream
    ```

- **Merge the changes into your local branch. If you are on the main branch (or master, depending on the repository), you can do**:

    ```bash
    git checkout main  # or master
    git merge upstream/main  # or upstream/master
    ```

- **Push the updated branch to your forked repository on GitHub**:

    ```bash
    git push origin main  # or master
    ```
    
## Imp Pipenv commands
- **Install pipenv package**:

    ```bash
    pip install pipenv
    ```


- **Initialize a virtual environment**:

    ```bash
    pipenv install
    ```

- **Start the pipenv terminal**:

    ```bash
    pipenv shell
    ```
- **Install required in your venv**:

    ```bash
    pipenv install -r requirements.txt
    ```
## Imp FastAPI commands

- **Run FastAPI app with Uvicorn**

    ```bash
    uvicorn main:app --reload
    ```
- **Run FastAPI app without Uvicorn**

    ```bash
    fastapi dev main.py
    ```
