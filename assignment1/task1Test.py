# task1.py
import task1

def test_helloWorld(capsys):
    task1.helloworld()
    out, _ = capsys.readouterr()
    assert "Hello World" in out