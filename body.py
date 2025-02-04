# Request body & Response body
# most of the time server will return the response body
# but client don't have to send the request body
# to send the request body, use POST, PUT, DELETE, PATCH methods
# send the request body with GET method has undefined behavior, but is supported by FastAPI in extreme use cases
from pydantic import BaseModel # pydantic is a data validation library
