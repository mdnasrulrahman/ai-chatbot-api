cat > README.md << 'EOF'
# AI Chatbot API

FastAPI + Claude API se bana chatbot backend. Conversation history yaad rakhta hai.

## Tech Stack
- Python, FastAPI, Uvicorn
- Anthropic API

## Run karne ke steps
```bash
pip install fastapi uvicorn anthropic
export ANTHROPIC_API_KEY="your_key"
uvicorn main:app --reload
```
Phir http://127.0.0.1:8000/docs kholo.

## Future improvements
- Database mein history save karna
- PDF upload + RAG
EOF

git add README.md
git commit -m "Add README"
git push
