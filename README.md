# OpenVoice Batch Processing Tool

## Overview
A customized implementation of OpenVoice for batch processing text-to-speech conversion. This tool is designed to process multiple text files simultaneously while maintaining original filenames, making it particularly useful for educational content creation.

## Requirements
- CUDA-enabled GPU
- OpenVoice Checkpoint Version 2
- Python 3.9 #ONLY

## Installation
1. Extract the OpenVoice checkpoint files to the main directory
2. Install required dependencies: follow origin method https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md#openvoice-v2

## Features
### Current Implementation
- **Batch Processing**: Automatically processes all text files from the `input` folder
- **Filename Preservation**: Maintains original filenames in the `output` folder
- **Educational Content Friendly**: Optimized for lecture title compatibility

### Upcoming Features
- **Dynamic Speech Rate Adjustment**
  - Speech rate adaptation based on timestamp information
  - Automatic speed adjustment for natural-sounding output
  - Variable speed processing for different speech patterns

## Directory Structure
```
.
├── input/
│   └── *.txt files
├── output/
│   └── generated audio files
├── converter/
├── resources
│    └── clone target voice
├── core.py
└── read_tex.py
```

## Usage
1. Place your text files in the `input` folder
2. Run the script:
```bash
python read_tex.py
```
3. Generated audio files will be available in the `output` folder

## Note
This implementation currently supports CUDA-enabled devices only and requires OpenVoice checkpoint version 2.

## License
MIT 3.0

---
*For more information, please refer to the original OpenVoice repository.*
