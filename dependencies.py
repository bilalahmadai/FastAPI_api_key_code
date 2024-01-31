from fastapi import  HTTPException, Header,Query

async def verify_api_key_header(api_key: str = Header(..., convert_underscores=False, title='API KEY Header')):
    if api_key == 'bilal123':
        return True
    else:
        raise HTTPException(status_code=401, detail="Invalid API Key")
async def verify_api_key_query(api_key: str = Query(..., convert_underscores=False, title='API KEY Query')):
    if api_key == '123bilal':
        return True
    else:
        raise HTTPException(status_code=401, detail="Invalid API Key")