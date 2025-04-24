# Google Cloud Run용 디스코드 봇

## 사용 방법
1. .env 파일에 DISCORD_TOKEN을 설정하세요.
2. Dockerfile을 기반으로 Google Cloud Run에서 배포하세요.
3. 예시 CLI:
   gcloud builds submit --tag gcr.io/PROJECT_ID/discord-bot
   gcloud run deploy discord-bot \
     --image gcr.io/PROJECT_ID/discord-bot \
     --platform managed \
     --region asia-northeast3 \
     --allow-unauthenticated \
     --set-env-vars DISCORD_TOKEN=봇_토큰