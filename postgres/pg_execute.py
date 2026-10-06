"""Run PostgreSQL statements against the broadway postgres container.

Usage:
    python pg_execute.py "SELECT * FROM students"   # run one statement
    python pg_execute.py -f script.sql              # run a .sql file
    python pg_execute.py                            # interactive mode
"""

import argparse
import os
import sys
from pathlib import Path

import psycopg

ENV_FILE = Path(__file__).with_name(".env")


def load_env(path: Path) -> None:
    """Load KEY=VALUE lines from .env into os.environ (existing vars win)."""
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def get_connection() -> psycopg.Connection:
    load_env(ENV_FILE)
    return psycopg.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=int(os.getenv("POSTGRES_HOST_PORT", "5433")),
        user=os.getenv("POSTGRES_USER", "broadway"),
        password=os.getenv("POSTGRES_PASSWORD", ""),
        dbname=os.getenv("POSTGRES_DB", "broadway"),
        autocommit=True,
    )


def print_result(cursor: psycopg.Cursor) -> None:
    """Print rows as a simple table, or the status for non-SELECT statements."""
    if cursor.description is None:
        print(cursor.statusmessage)
        return

    headers = [col.name for col in cursor.description]
    rows = cursor.fetchall()
    widths = [
        max(len(str(h)), *(len(str(r[i])) for r in rows)) if rows else len(h)
        for i, h in enumerate(headers)
    ]
    print(" | ".join(h.ljust(w) for h, w in zip(headers, widths)))
    print("-+-".join("-" * w for w in widths))
    for row in rows:
        print(" | ".join(str(v).ljust(w) for v, w in zip(row, widths)))
    print(f"({len(rows)} row{'s' if len(rows) != 1 else ''})")


def execute(conn: psycopg.Connection, sql: str) -> None:
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            print_result(cur)
    except psycopg.Error as exc:
        print(f"ERROR: {exc}", file=sys.stderr)


def interactive(conn: psycopg.Connection) -> None:
    print("Enter SQL ending with ';'. Type 'exit' to quit.")
    buffer: list[str] = []
    while True:
        try:
            line = input("pg> " if not buffer else "... ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not buffer and line.strip().lower() in {"exit", "quit", r"\q"}:
            break
        buffer.append(line)
        if line.rstrip().endswith(";"):
            execute(conn, "\n".join(buffer))
            buffer.clear()


def main() -> None:
    parser = argparse.ArgumentParser(description="Execute PostgreSQL statements.")
    parser.add_argument("sql", nargs="?", help="SQL statement to run")
    parser.add_argument("-f", "--file", type=Path, help="Path to a .sql file")
    args = parser.parse_args()

    with get_connection() as conn:
        if args.file:
            execute(conn, args.file.read_text())
        elif args.sql:
            execute(conn, args.sql)
        else:
            interactive(conn)


if __name__ == "__main__":
    main()
