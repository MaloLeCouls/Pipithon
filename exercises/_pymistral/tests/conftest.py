"""Place le parent (`_pymistral/`) sur sys.path pour les tests de fumée du framework."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
