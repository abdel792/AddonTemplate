# Copyright (C) 2026 NV Access Limited, Abdel
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""CLI entry point for the NVDA Add-on Template synchronization tool."""

from pathlib import Path
import sys

# Insert the script's parent directory at the beginning of sys.path.
# This ensures syncAddonTool package resolution regardless of the current working directory.
SCRIPT_DIR: Path = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
	sys.path.insert(0, str(SCRIPT_DIR))

from syncAddonTool.cli import main

if __name__ == "__main__":
	main()