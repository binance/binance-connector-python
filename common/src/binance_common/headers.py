import logging

from typing import List, Optional, Union

def sanitize_header_value(value: Union[str, List[str]]) -> Union[str, List[str]]:
    """Sanitizes a header value by checking for and preventing carriage return and line feed characters.

    Args:
        value (Union[str, List[str]]): The header value or array of header values to sanitize.

    Raises:
        ValueError: If the header value contains CR or LF characters.

    Returns:
        Union[str, List[str]]: The sanitized header value(s).
    """

    if "\r" in value or "\n" in value:
        raise ValueError(f'Invalid header value (contains CR/LF): "{value}"')
    return value

def parse_custom_headers(custom_headers: Optional[dict[str, Union[str, List[str]]]]) -> dict[str, Union[str, List[str]]]:
    """Parses custom headers for the API client.

    Args:
        custom_headers (Optional[dict[str, Union[str, List[str]]]]): A dictionary of custom headers to parse.

    Returns:
        dict[str, Union[str, List[str]]]: A dictionary of parsed custom headers.
    """

    forbidden_headers = {"host", "authorization", "cookie", ":method", ":path"}
    parsed_headers = {}

    if not custom_headers:
        return {}

    for key, value in custom_headers.items():
        header_name = key.strip()
        if header_name.lower() in forbidden_headers:
            logging.warning(f"Header '{header_name}' is not allowed to be set.")
            continue

        try:
            if isinstance(value, list):
                parsed_headers[header_name] = [sanitize_header_value(v) for v in value]
            else:
                parsed_headers[header_name] = sanitize_header_value(value)
        except ValueError as e:
            logging.warning(f"Dropping header '{header_name}' due to invalid value.")
            continue

    return parsed_headers