# search-engine


Deployment Instructions:
1. Pull docker file: docker pull uderani/search-engine:latest
2. Make sure nothing is running on port 8000
3. Run docker image: docker run --network host -i uderani/search-engine:latest

Test:
1. Web Page: http://127.0.0.1:8000/dashboard/
2. API: http://127.0.0.1:8000/search/?keyword=Jerry
