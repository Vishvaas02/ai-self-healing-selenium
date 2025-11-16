from __future__ import annotations

import csv
import os
from datetime import datetime
from typing import Optional, Tuple


class HealingLogger:
    """
    Logs locator healing attempts to a CSV file for later analysis.
    """

    def __init__(self, path: str = "healing_log.csv"):
        self.path = path
        self._ensure_header()

    def _ensure_header(self):
        if not os.path.exists(self.path):
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(
                    [
                        "timestamp",
                        "old_by",
                        "old_value",
                        "new_by",
                        "new_value",
                        "success",
                        "confidence",
                        "reason",
                    ]
                )

    def log_healing(
        self,
        old_locator: Tuple[str, str],
        new_locator: Optional[Tuple[str, str]],
        success: bool,
        confidence: float,
        reason: str,
    ):
        new_by, new_val = (None, None)
        if new_locator:
            new_by, new_val = new_locator

        with open(self.path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    datetime.utcnow().isoformat(),
                    old_locator[0],
                    old_locator[1],
                    new_by,
                    new_val,
                    success,
                    f"{confidence:.2f}",
                    reason,
                ]
            )
