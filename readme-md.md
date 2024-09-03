# lazypush

`lazypush` is a simple, customizable Git command-line utility that streamlines the process of committing and pushing changes to your Git repository. It offers flexibility in how you handle commit messages and allows you to optionally pull the latest changes from the remote before pushing.

## Features

- **Auto-Stage and Commit**: Automatically stages all modified files and commits them.
- **Custom or Default Commit Message**: Option to provide a custom commit message or use an auto-generated default message.
- **Branch Detection**: Automatically detects the current branch and pushes to it.
- **Optional Pull Before Push**: Ensures your branch is up to date by optionally pulling the latest changes before pushing.
- **Verbose Mode**: Provides detailed output of each operation for easier debugging and transparency.

## Installation

### 1. Download the Script

```bash
curl -o lazypush https://github.com/amanmehtacode/LazyPush
```

### 2. Make the Script Executable

```bash
chmod +x lazypush
```

### 3. Move the Script to a Directory in Your PATH

```bash
sudo mv lazypush /usr/local/bin/
```

### 4. Verify Installation

Run `lazypush` in your terminal to ensure it's working correctly:

```bash
lazypush
```

## Usage

Simply run the `lazypush` command in your terminal from within a Git repository:

```bash
lazypush
```

### Command Flow

1. **Check for Unstaged Changes**: If there are no changes to commit, the script exits with a message.
2. **Prompt for Commit Message**: The script prompts you for a commit message. If you don't provide one, a default message is generated.
3. **Optional Pull**: You can choose to pull the latest changes from the remote repository before committing.
4. **Auto-Stage Changes**: The script automatically stages all changes.
5. **Commit Changes**: The script commits the changes with the provided or default message.
6. **Push to Remote**: The script pushes the changes to the current branch.
7. **Verbose Output**: Displays detailed information about each operation.

### Options

You can enhance the functionality of `lazypush` by including the following options:

- **-p or --pull**: Automatically pulls the latest changes from the remote branch before pushing.
- **-v or --verbose**: Enables verbose mode for detailed output.

### Example Commands

- **Basic Usage**:

  ```bash
  lazypush
  ```

  - Prompts for a commit message.
  - Stages all changes.
  - Commits and pushes to the current branch.

- **With Auto-Pull**:

  ```bash
  lazypush -p
  ```

  - Pulls the latest changes from the remote branch.
  - Prompts for a commit message.
  - Stages all changes.
  - Commits and pushes to the current branch.

- **Verbose Mode**:

  ```bash
  lazypush -v
  ```

  - Provides detailed output of each step in the process.
  
- **Pull and Verbose**:

  ```bash
  lazypush -pv
  ```

  - Pulls latest changes, then commits and pushes with detailed output.

## Script Code

Here's the full code for `lazypush` with the additional features:

```bash
#!/bin/bash

# Function to display verbose messages
verbose() {
  if [ "$verbose_mode" = true ]; then
    echo "$@"
  fi
}

# Parse options
pull_before_push=false
verbose_mode=false

while [[ "$1" =~ ^- ]]; do
  case $1 in
    -p | --pull)
      pull_before_push=true
      ;;
    -v | --verbose)
      verbose_mode=true
      ;;
    *)
      echo "Invalid option: $1"
      exit 1
      ;;
  esac
  shift
done

# Check for unstaged changes
if [ -z "$(git status --porcelain)" ]; then
  echo "No changes to commit."
  exit 0
fi

# Pull the latest changes if the option is enabled
if [ "$pull_before_push" = true ]; then
  verbose "Pulling latest changes from the remote branch..."
  git pull origin $(git branch --show-current)
fi

# Ask for a commit message
read -p "Enter commit message (leave empty for default): " commit_message

# Default message if none is provided
if [ -z "$commit_message" ]; then
  commit_message="Auto commit on $(date)"
fi

# Add changes to the staging area
verbose "Staging changes..."
git add .

# Commit with the provided or default message
verbose "Committing changes..."
git commit -m "$commit_message"

# Push the changes to the current branch
verbose "Pushing changes to the remote branch..."
git push origin $(git branch --show-current)

echo "Changes have been committed and pushed successfully."
```

## Troubleshooting

- **No Changes Detected**: If the script exits without committing, ensure you have unstaged changes in your working directory.
- **Invalid Options**: If you pass an unrecognized option, the script will display an error message and exit.

## Contributing

If you have ideas for improvements or find bugs, feel free to submit an issue or pull request.

## License

This script is licensed under the MIT License. Feel free to use and modify it as you see fit.
