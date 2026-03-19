from io import BytesIO
from pathlib import Path

from markitdown import MarkItDown, StreamInfo
from pydantic import Field


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    path: str = Field(description="Absolute or relative path to a PDF or DOCX file"),
) -> str:
    """Convert a PDF or DOCX file to markdown-formatted text.

    Reads the file at the given path and converts its contents to markdown.

    When to use:
    - When you have a local PDF or DOCX file and want its content as markdown
    - When you need to extract text from a document for further processing

    Examples:
    >>> document_path_to_markdown("/path/to/report.pdf")
    '# Report Title\\n...'
    >>> document_path_to_markdown("/path/to/notes.docx")
    '# Notes\\n...'
    """
    file_path = Path(path)
    file_type = file_path.suffix.lstrip(".")
    binary_data = file_path.read_bytes()
    return binary_document_to_markdown(binary_data, file_type)
