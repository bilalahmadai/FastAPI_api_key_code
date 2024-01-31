from fastapi import FastAPI, HTTPException,Depends
from fastapi.responses import JSONResponse
from dependencies import verify_api_key_header, verify_api_key_query
app = FastAPI()



@app.get("/secure-endpoint", dependencies=[Depends(verify_api_key_header),Depends(verify_api_key_query)])
async def secure_endpoint():
    try:
        # Your logic for the secure endpoint here
        message = {"message": "This is a secure endpoint. API key is valid."}
        return JSONResponse(content=message, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/public-endpoint")
async def public_endpoint():
    # Using JSONResponse to create a custom JSON response
    content = {"message": "This is a public endpoint."}
    return JSONResponse(content=content, status_code=200)
