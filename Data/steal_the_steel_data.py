import requests
from pathlib import Path
from io import StringIO
from pathlib import Path
from typing import Optional, Union
import pandas as pd
from bs4 import BeautifulSoup
URL = "http://steeldata.ch/html/allproducts.html"
OUT = Path("steeldata/html/allproducts.html")
OUT.parent.mkdir(parents=True, exist_ok=True)  # ✅ create folders if missing
headers = {
    # Keep it simple: pretend to be a browser, but DO NOT set Accept-Encoding yourself
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/128.0.0.0 Safari/537.36",
    "Referer": "http://steeldata.ch/",
}


def html_to_csv(
    html: Union[str, bytes],
    out_csv: Union[str, Path],
    selector: Optional[str] = None,
    table_index: int = 0,
    encoding: str = "utf-8",
    include_header: bool = True
) -> pd.DataFrame:
    """
    Convert an HTML page (string) to CSV by extracting an HTML <table>.

    Parameters
    ----------
    html : str | bytes
        The HTML content. If bytes, will be decoded as UTF-8 with errors='replace'.
    out_csv : str | Path
        Output CSV path.
    selector : str | None
        Optional CSS selector to pinpoint a specific table (e.g., 'table#allproducts' or '.productTable').
        If None, falls back to pandas.read_html() to detect tables.
    table_index : int
        If multiple tables are found, which one to export (0-based index).
    encoding : str
        CSV output encoding (default 'utf-8').
    include_header : bool
        Whether to write the header row to CSV.

    Returns
    -------
    pd.DataFrame
        The DataFrame that was written to CSV.
    """
    # Normalize HTML to text
    if isinstance(html, bytes):
        html = html.decode("utf-8", errors="replace")

    # Try CSS selector first (if provided)
    if selector:
        soup = BeautifulSoup(html, "lxml")
        tables = soup.select(selector)
        if not tables:
            raise ValueError(f"No tables matched selector: {selector}")
        # Convert the selected table to DataFrame
        # Let pandas parse just that table's HTML
        html_fragment = str(tables[table_index])
        dfs = pd.read_html(StringIO(html_fragment), flavor="lxml")
        if not dfs:
            raise ValueError("Selector matched a table, but pandas could not parse it.")
        df = dfs[0]
    else:
        # Auto-detect tables with pandas
        dfs = pd.read_html(StringIO(html), flavor="lxml")
        if not dfs:
            raise ValueError("No HTML tables found in the provided HTML.")
        if table_index >= len(dfs):
            raise IndexError(f"table_index {table_index} out of range (found {len(dfs)} tables).")
        df = dfs[table_index]

    # Clean up whitespace and non-breaking spaces
    df = df.map(
        lambda x: (
            str(x).replace("\xa0", " ").strip()
            if isinstance(x, (str, bytes)) else x
        )
    )

    # Drop fully-empty columns/rows (optional but handy)
    df = df.dropna(axis=1, how="all").dropna(axis=0, how="all")

    # Write CSV
    out_csv = Path(out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_csv, index=False, header=include_header, encoding=encoding)

    return df


try:
    r = requests.get(URL, headers=headers, timeout=15)
    r.raise_for_status()

    # If the server sends text/html, decode to proper text
    content_type = r.headers.get("Content-Type", "").lower()
    raw = r.content  # bytes (already decompressed by requests if server used gzip/deflate)

    if "text/html" not in content_type:
        # Save the raw response for inspection if it's not HTML
        Path("allproducts.raw").write_bytes(raw)
        raise RuntimeError(f"Unexpected Content-Type: {content_type}. Saved as allproducts.raw")

    # Choose an encoding (server hint or chardet fallback)
    encoding = r.encoding or getattr(r, "apparent_encoding", None) or "utf-8"
    text = raw.decode(encoding, errors="replace")

    # Save as UTF-8 so VS Code opens it reliably
    OUT.write_text(text, encoding="utf-8")
    print(f"✅ Saved HTML to {OUT} (detected encoding: {encoding})")

except Exception as e:
    print(f"❌ Error: {e}")

html = Path("steeldata/html/allproducts.html").read_text(encoding="utf-8")

# 2) Convert to CSV (auto-detect first table)
df = html_to_csv(html, "steeldata/csv/allproducts.csv")