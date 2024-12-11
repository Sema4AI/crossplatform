from pathlib import Path
import platform
import subprocess

IS_MAC = platform.system() == "Darwin"


def _trigger_excel_on_mac(filepath: str):
    """Trigger Excel to open and save a file using AppleScript.

    Args:
        filepath: Path to the Excel file to save
    """
    if IS_MAC:
        print("Triggering Excel save on MacOS Excel app")
        # Convert to absolute path
        abs_path = str(Path(filepath).resolve())

        # AppleScript to handle Excel operations
        apple_script = f"""
        tell application "Microsoft Excel"
            set was_running to running
            activate
            set display alerts to false

            try
                open "{abs_path}"
                save active workbook
                close active workbook saving no

                if not was_running then
                    quit
                end if

                return true
            on error errMsg
                if not was_running then
                    quit
                end if
                return errMsg
            end try
        end tell
        """

        # Run the AppleScript
        try:
            result = subprocess.run(
                ["osascript", "-e", apple_script],
                capture_output=True,
                text=True,
                check=True,
            )
            if "error" in result.stderr.lower():
                raise RuntimeError(f"Excel automation failed: {result.stderr}")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to execute Excel automation: {e.stderr}")
