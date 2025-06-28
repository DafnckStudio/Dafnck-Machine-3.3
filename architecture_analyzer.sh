#!/bin/bash

# Architecture Analyzer Wrapper Script
# Makes it easy to analyze folder architecture without manually activating virtual environment

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_PATH="$PROJECT_ROOT/venv"
ANALYZER_SCRIPT="$SCRIPT_DIR/architecture_analyzer.py"

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if folder path is provided
if [ $# -eq 0 ]; then
    echo -e "${BLUE}Architecture Analyzer${NC}"
    echo "Usage: $0 <folder_path> [options]"
    echo ""
    echo "Examples:"
    echo "  $0 \"dafnck-machine-3.3/01_Machine/01_Workflow/Phase 1: Initial User Input & Project Inception\""
    echo "  $0 \"path/to/your/folder\" --verbose"
    echo "  $0 \"dafnck-machine-3.3/01_Machine/01_Workflow\" --recursive"
    echo "  $0 \"dafnck-machine-3.3/01_Machine/01_Workflow\" --show-structure"
    echo "  $0 \"path/to/folder\" --export json"
    echo "  $0 \"path/to/folder\" --export-html"
    echo ""
    echo "Options:"
    echo "  --verbose, -v         Enable verbose output"
    echo "  --recursive, -r       Recursively analyze all subfolders"
    echo "  --show-structure, -s  Show folder structure even when no markdown files found"
    echo "  --export, -e          Export results (json|csv|html|all)"
    echo "  --output-dir, -o      Output directory for exported files"
    echo "  --export-html         Interactive HTML export (keeps running, auto-cleanup on Ctrl+C)"
    echo "  --help, -h            Show this help message"
    exit 1
fi

# Check if help is requested
if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
    echo -e "${BLUE}Architecture Analyzer Help${NC}"
    echo ""
    echo "This script analyzes folder architecture and validates YAML front matter in markdown files."
    echo ""
    echo "Features:"
    echo "  ✅ Displays folder structure in tree format"
    echo "  ✅ Extracts and shows all ## headers"
    echo "  ✅ Validates YAML front matter format"
    echo "  ✅ Shows missing required fields"
    echo "  ✅ Provides comprehensive analysis summary"
    echo ""
    echo "Required YAML fields:"
    echo "  - phase, step, task, task_id, title"
    echo "  - previous_task, next_task, version"
    echo "  - agent, orchestrator"
    echo ""
    echo "Usage: $0 <folder_path> [options]"
    exit 0
fi

# Check if virtual environment exists
if [ ! -d "$VENV_PATH" ]; then
    print_error "Virtual environment not found at $VENV_PATH"
    print_status "Creating virtual environment..."
    python3 -m venv "$VENV_PATH"
    
    if [ $? -ne 0 ]; then
        print_error "Failed to create virtual environment"
        exit 1
    fi
    
    print_status "Installing dependencies..."
    source "$VENV_PATH/bin/activate"
    pip install -r "$SCRIPT_DIR/requirements.txt"
    
    if [ $? -ne 0 ]; then
        print_error "Failed to install dependencies"
        exit 1
    fi
fi

# Check if analyzer script exists
if [ ! -f "$ANALYZER_SCRIPT" ]; then
    print_error "Analyzer script not found at $ANALYZER_SCRIPT"
    exit 1
fi

# Check if folder exists
FOLDER_PATH="$1"
if [ ! -d "$FOLDER_PATH" ]; then
    print_error "Folder not found: $FOLDER_PATH"
    exit 1
fi

# Activate virtual environment and run analyzer
print_status "Activating virtual environment..."
source "$VENV_PATH/bin/activate"

print_status "Running architecture analysis..."
echo ""

# Pass all arguments to the Python script
python "$ANALYZER_SCRIPT" "$@"

# Check if analysis was successful
if [ $? -eq 0 ]; then
    echo ""
    print_status "Analysis completed successfully!"
else
    echo ""
    print_error "Analysis failed!"
    exit 1
fi 