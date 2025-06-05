import os
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import detect_frameworks, FrameWork


def create_test_apk(entries):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.apk')
    with zipfile.ZipFile(tmp.name, 'w') as zf:
        for entry in entries:
            zf.writestr(entry, b'')
    tmp.close()
    return tmp.name


def test_flutter_detection():
    apk = create_test_apk(['libflutter.so'])
    try:
        result = detect_frameworks(apk)
        assert result == [FrameWork.FLUTTER]
    finally:
        os.remove(apk)


def test_react_native_detection():
    apk = create_test_apk(['libreactnativejni.so'])
    try:
        result = detect_frameworks(apk)
        assert result == [FrameWork.REACT_NATIVE]
    finally:
        os.remove(apk)


def test_multiple_detection():
    apk = create_test_apk(['libflutter.so', 'libreactnativejni.so'])
    try:
        result = detect_frameworks(apk)
        assert FrameWork.FLUTTER in result
        assert FrameWork.REACT_NATIVE in result
        assert len(result) == 2
    finally:
        os.remove(apk)


def test_native_fallback():
    apk = create_test_apk(['somefile.txt'])
    try:
        result = detect_frameworks(apk)
        assert result == [FrameWork.NATIVE]
    finally:
        os.remove(apk)
