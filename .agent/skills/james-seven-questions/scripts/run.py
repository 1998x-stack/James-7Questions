#!/usr/bin/env python3
"""James Seven Questions / Strategic Decision skill entrypoint. Use shared case schema and generator."""
from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[4]
runpy.run_path(str(root/'src'/'build.py'),run_name='__main__')
