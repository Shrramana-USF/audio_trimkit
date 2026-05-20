# B2AI Voice Trimkit

A Streamlit-based audio trimming tool for acoustic researchers with Praat-Parselmouth integration.

## Features

- **Multiple Task Types:**
  - **Sustained Vowel** - Single segment extraction per file
  - **Cough** - Detect and isolate cough segments
  - **Speech** - Praat-based trimming to isolate voiced region
  - **Breathing** - Trim leading and trailing silence
  - **Everything Fused** - Multi-segment detection (cough, breathing, speech, vowel)
  - **General-manual** - Manual region selection and trimming

- **Supported Formats:** `.wav` and `.mp3` (auto-converted to WAV)
- **Interactive Waveform:** Visual selection with Plotly
- **Batch Processing:** Process multiple files via CSV upload


## Installation

```bash
pip install b2ai-voice-trimkit
```

## Usage

Launch the dashboard:

```bash
b2ai_voice_trimkit
```

### CSV Format

Upload a CSV file with a column named `audio_file_path`:

```csv
audio_file_path
/path/to/audio1.wav
/path/to/audio2.mp3
```

## Quitting

- Click **Quit Application** in the sidebar or
- Press `Ctrl+C` in the terminal

## Dependencies

- numpy, pandas, streamlit
- praat-parselmouth
- plotly, soundfile, librosa, pydub

## License

MIT