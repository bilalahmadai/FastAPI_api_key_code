from fastapi import  HTTPException, Header,Query

async def verify_api_key_header(api_key: str = Header(..., convert_underscores=False, title='API KEY Header')):
    """
    Dependency function to verify API key from the header.

    Args:
        api_key (str): The API key received in the header.

    Returns:
        bool: True if the API key is valid, else raises HTTPException with 401 status code.
    """
    if api_key == 'bilal123':
        return True
    else:
        raise HTTPException(status_code=401, detail="Invalid API Key")

async def verify_api_key_query(api_key: str = Query(..., convert_underscores=False, title='API KEY Query')):
    """
    Dependency function to verify API key from the query parameter.

    Args:
        api_key (str): The API key received in the query parameter.

    Returns:
        bool: True if the API key is valid, else raises HTTPException with 401 status code.
    """
    if api_key == '123bilal':
        return True
    else:
        raise HTTPException(status_code=401, detail="Invalid API Key")