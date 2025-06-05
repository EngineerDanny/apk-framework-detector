import zipfile
from pathlib import Path

from main import detect_framework, FrameWork


def test_flutter_detection(tmp_path: Path):
    zip_path = tmp_path / "test.apk"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("libflutter.so", "")

    frameworks = detect_framework(str(zip_path))
    assert FrameWork.FLUTTER in frameworks


def test_react_native_detection(tmp_path: Path):
    zip_path = tmp_path / "react.apk"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("libreactnativejni.so", "")

    frameworks = detect_framework(str(zip_path))
    assert FrameWork.REACT_NATIVE in frameworks
