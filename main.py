import uvicorn

import settings


if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=settings.APP_PORT, reload=True)

