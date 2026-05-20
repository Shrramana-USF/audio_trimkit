# CLI entry point - separate file to avoid importing streamlit
def main():
    import subprocess
    import sys
    from importlib.resources import files
    app_path = files("b2ai_voice_trimkit").joinpath("app.py")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", str(app_path), "--server.address=localhost"])
    except KeyboardInterrupt:
        print("\nB2AI Voice Trimkit stopped.")
        sys.exit(0)
