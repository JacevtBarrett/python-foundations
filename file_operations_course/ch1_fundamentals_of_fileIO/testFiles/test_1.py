import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from l1_reading_writing_text_files import write_txt_file

def test_write_txt_file():
    file_path = write_txt_file()
    assert file_path.exists()
