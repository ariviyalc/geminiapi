## 🤖 Gemini Endpoint
GET /gemini
Query Parameters

Name   Required       Description
key   ✅ Yes  Gemini    API key 
text  ✅ Yes  Prompt    text

## Example Request
Copy code
```
https://gemini-api-ashen-ten.vercel.app/gemini?key=YOUR_KEY&text=Hello%20Gemini
```
## Example Response
Copy code
```Json
{
  "status_code": 200,
  "message": "Hello! How can I help you today?"
}
```
## Error Response
Copy code
```Json
{
  "status_code": 400,
  "message": "The parameters key and text are required"
}
```
## 🧪 Test Gemini API Key
⚠️ For testing purposes only. Do NOT use in production.
Copy code
```
AIzaSyAaCU1F7_46fEaUcyeXq0XUiffdn9mkq0w
```