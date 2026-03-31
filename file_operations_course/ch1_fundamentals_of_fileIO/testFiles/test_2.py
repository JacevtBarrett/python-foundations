import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1])) # Add the parent directory to the system path

from l2_safe_file_access_with_context_managers import write_log_file

def test_write_log():
    file_path = write_log_file()
    assert file_path.exists()
